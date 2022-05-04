print("hello")
from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hy")
            sleep(1)
t1=hello()
t2=hi()
t1.start()   #have to use start instead of run,because run method is already used in Thread class
sleep(.2)     #for avoiding collition
t2.start()
t1.join()
t2.join()
print("bye")

