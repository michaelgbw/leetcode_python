# -*- coding:utf-8 -*-
import threading
import time


num = 0
con = threading.Condition()


class producter(threading.Thread):
    """生产者"""
    def run(self):
        global num
        # 获取锁
        if con.acquire():
            while True:
                num += 1
                print('生产了1个，现在有{0}个'.format(num))
                time.sleep(0.1)
                if num >= 5:
                    print('已达到5个，不再生产')
                    # 唤醒消费者
                    con.notify()
                    # 等待-释放锁；被唤醒-获取锁
                    con.wait()


class consumer(threading.Thread):
    def __init__(self,money,name):
        super().__init__()
        self.money = money
        self.name = name

    def run(self):
        global num
        while self.money > 0:
            if con.acquire():
                if num <= 0:
                    print('没货了，{0}通知生产者'.format(
                        self.name))
                    con.notify()
                    con.wait()
                self.money -= 1
                num -= 1
                print('{0}消费了1个, 剩余{1}个'.format(
                    self.name, num))
                con.release()
                # time.sleep(0.01)
        print('{0}没钱了-回老家'.format(self.name))


if __name__ == '__main__':
    p = producter(daemon=True)
    p.start()

    consumer_threads = []
    for i in range(5):
        c = consumer(3,name='Customer-' + str(i))
        consumer_threads.append(c)

    for one in consumer_threads:
        one.start()