#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :LiveRobot.py
@说明        :给录播视频加入进出机器人功能 #https://quningmeng.coding.net/p/lemon-live-server/wiki/36
@时间        :2020/04/28 11:37:06
@作者        :gbw
@版本        :1.0
'''
import os
import json
import time
import random
from model.redis.RedisLiveModel import RedisLiveModel
from config.UserScoreConfig import UserScoreConfig
from tool.Log import Loger
import tool.Util as util
from config.RedisKeys import RedisKeys
import multiprocessing
from config.Const import Const
import psutil

#q1.在类中把进程池设为成员变量，同时把self作为参数传给线程池中的函数的时候会报错:
#pool objects cannot be passed between processes or pickled
#q2. apply_async().get()是阻塞的，生产环境不能用get，调试用get查看子进程错误
#q3. psutil 要在子进程中获取，并不能通过主进程传入

class LiveRobot:
    def __init__(self):
        self.is_test = util.get_is_test_env()
        self._redis = RedisLiveModel()
        self.inner_host = Const.INNER_TEST_LIVE_HOST if self.is_test else Const.INNER_LIVE_HOST

    def worker_run(self,room_id='',pid=''):
        robot_list = []
        pps = psutil.Process(pid=pid)
        Loger("live_robot").info("===pid=%d==="%os.getpid())
        Loger("live_robot").info('room_id:' + str(room_id) + ' start~')
        robot_add_limit = random.randint(20,40)
        for _ in range(robot_add_limit):

            try:
                if pps.status() in [psutil.STATUS_DEAD, psutil.STATUS_STOPPED]:
                    Loger("live_robot").info('主进程主动死亡,子进程' + str(os.getpid()) + '退出')
                    break
            except:
                Loger("live_robot").info('主进程被杀了,子进程' + str(os.getpid()) + '退出')
                break
            time.sleep(random.randint(10,30))
            #请求加机器人接口并获取uid
            url = self.inner_host + '/live/inner/robot/liveInteractionRobot'
            payload = {
                'type':'join_room',
                'room_id':str(room_id),
                'stream':1,
            }
            res = util.myPost(url, payload)
            if int(res.get('code',-1)) == 0:
                robot_id = res['data']['robot_info']['id']
                robot_list.append(str(robot_id))
                Loger("live_robot").info('room_id:' + str(room_id) + '-> ' +  ','.join(robot_list))
            
            elif int(res.get('code',-1)) == 1003:
                #直播下线了
                Loger("live_robot").info('room_id:' + str(room_id) + ' has offline~')
                return 1
            
            else:
                # 网络波动,本次请求失败
                continue
        
        if len(robot_list) == 0 :
            return 1

        # #随机停止时间
        # time.sleep(random.randint(60,600))

        # #开始减少人
        # uid_reduce_list = random.sample(robot_list, robot_reduce_limit)
        # for uid in uid_reduce_list:
        #     time.sleep(random.randint(2,4))
        #     #请求减少机器人接口并获取uid
        #     url = self.inner_host + '/live/inner/robot/liveInteractionRobot'
        #     payload = {
        #         'type':'join_room',
        #         'room_id':str(room_id),
        #         'stream':1,
        #         'uid':uid,
        #     }
        #     res = util.myPost(url, payload)
        #     Loger("live_robot").info(res)

        # Loger("live_robot").info('room_id:' + str(room_id) + ' end~')
        return 1

    def master_run(self):
        #初始化进程池
        p_num = multiprocessing.cpu_count()*10
        pid = os.getpid()
        Loger("live_robot").info('主进程开始于:' + str(pid))
        Loger("live_robot").info('初始进程池：' + str(p_num))
        Loger("live_robot").info('机器cpu：' + str(multiprocessing.cpu_count()))
        pool = multiprocessing.Pool(p_num)
        

        while 1:
            #接受room_id开播通知
            feed_json = self._redis.brpop(RedisKeys.LIVE_ROOM_QUEUE)
            if feed_json is None:
                continue
            room_id = feed_json[1].decode()
            result = pool.apply_async(self.worker_run, args=(room_id,pid))
            # result.get()

    def run(self):
        self.master_run()


        

