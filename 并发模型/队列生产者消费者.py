import threading,queue,time
 
q = queue.Queue(maxsize=10)
 
def Producer(name):
    count = 0
    while True:
        q.put("小鱼干%s" % count)
        print("[%s]生产了骨头"%name,count)
        count += 1
        time.sleep(0.5)
         
def Consumer(name):
    while True:
        print("[%s] 取到[%s]并且吃了它..." %(name,q.get()))
        time.sleep(1)
 
for i in range(2):
    p = threading.Thread(target=Producer, args=("主人%s"%i,))
    p.start()
 
for i in range(3):
    c = threading.Thread(target=Consumer,args=("大猫%s"%i,))
    c.start()