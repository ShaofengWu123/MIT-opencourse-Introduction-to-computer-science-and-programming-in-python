import threading
import time
#线程模块的方法
print(threading.active_count())#返回已激活的线程数量
print(threading.enumerate())#返回所有线程信息
print(threading.current_thread())#查看正在运行的线程

#线程的建立
#1.threading.Tread(target)方法
def thread_job_1():
    print('Current thread: %s!' % threading.current_thread())

def main():
  thread_1 = threading.Thread(target= thread_job_1)#添加一个线程
  thread_1.start()#让线程开始工作
  print(threading.active_count())
  thread_1.join()
  print(threading.active_count())

if __name__ == '__main__':
    main()
#关于__name__ == '__main__'的意义：__name__是每个python文件都包含的内置变量，当该模块被直接执行的时候，__name__ 等于文件名（包含后缀 .py ）；
#如果该模块 import 到其他模块中，则该模块的 __name__ 等于模块名称（不包含后缀.py）。
#而 “__main__” 始终指当前执行模块的名称（包含后缀.py）。进而当模块被直接执行时，__name__ == 'main' 结果为真。
#因此此if语句表示：表示如果此python文件被直接运行，那么执行if包含的语句；如果此python文件被作为模块导入，那么不会执行if包含的语句

#2.用类包装线程
class mythread(threading.Thread):
    def __init__(self,name,counter,delay):
        super().__init__()
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self): #类的方法传入的参数是self，因此如果引用counter会报错not defined，而引用self.counter就没问题
       while self.counter:
           time.sleep(self.delay)
           print(time.asctime(time.localtime()))
           print(threading.current_thread())
           print(threading.enumerate(),'\n')
           self.counter -= 1

mythread1 = mythread('thread1',5,1)
mythread1.start()
mythread1.join()

print('End of thread A')#Mainthread等待新建的thread1结束，在thread1结束后才执行这一行语句并结束。因此会最后看到输出'End of thread A'，thread1运行
                       #过程中enumerate()的结果也可以看到Mainthread并没有结束。

#线程的等待中止join():等待至线程中止。
#与上一段代码对比
mythread2 = mythread('thread2',5,2)
mythread2.start()
print('End of thread B')#Mainthread没有等待新建的thread1结束，直接执行了这一行语句并结束。因此会先看到输出'End of thread B'，thread1运行
                       #过程中enumerate()的结果也可以看到Mainthread已经结束。

#线程数据存储、数据处理与线程优先级队列
#数据处理，并通过queue.empty实现线程同步
import queue

exitflag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = queue
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(n,q):
    while not exitflag:
        if not q.empty():
           print('%s is processing %s' % (n,q.get()))
        else:
           pass
        time.sleep(1)#作用是暂时挂起线程让其他线程来访问数据并运算。
    #time.sleep(1)放在这里能起到上一行的作用么？ 不能，因为while循环一直在进行，Thread-1没有被挂起，只有其在处理数据

datalist = ['a','b','c','d','e']
threadlist = []
dataqueue = queue.Queue()
for i in datalist:
    dataqueue.put(i)
threadname = ['Thread-1','Thread-2','Thread-3']
ID = 1
for j in threadname:
    t = myThread(ID,j,dataqueue)
    t.start()#三个进程对数据进行自由访问并处理
    threadlist.append(t)
    ID += 1

while not dataqueue.empty():#当三个进程自由处理数据，使得队列数据全部运算完成时，提示可以进入下一步
    pass

exitflag = 1#提示所有进程可以退出

for thread in threadlist:
    thread.join()#join() 方法的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源。
                 #依次检查线程池中的线程是否结束，没有结束那么继续阻塞调用线程，结束则转向下一个join()方法。

print('进程结束')



#数据存储(此功能可以由列表代替)
dataQ = queue.Queue()
Tlock = threading.Lock()
def calculation(l):
    Tlock.acquire()
    for i in range(len(l)):
        l[i] = l[i] ** 2
    dataQ.put(l)
    Tlock.release()

def main():
    Tl = []
    datal = [[1,2,3],[2,2,2],[4,5,6],[9,8,7]]
    for i in range(4):
        t = threading.Thread(target = calculation, args = (datal[i],))#这里可以把Queue作为参数传入线程的target中，当然也可以像本例
                                                                      #中这样把Queue作为全局变量存储数据，不需要把其作为参数
        Tl.append(t)
    for T in Tl:
        T.start()
        T.join()
    result = []
    while not dataQ.empty():
        result.append(dataQ.get())
    print(result)

if __name__ == '__main__':
    main()



#线程同步：锁定与未锁定
#对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。
lock = threading.Lock()
class mythread(threading.Thread):
    def __init__(self,name,counter,delay):
        super().__init__()
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self): #类的方法传入的参数是self，因此如果引用counter会报错not defined，而引用self.counter就没问题
       lock.acquire()#把acquire和release放到while内也可以，只不过没有必要反复获得和释放锁
       while self.counter:
           time.sleep(self.delay)
           print(time.asctime(time.localtime()))
           print(threading.current_thread())
           print(threading.enumerate(),'\n')
           self.counter -= 1
       lock.release()

def test_fun(t1,t2):
   thread1 = mythread('thread1',5,1)
   thread2 = mythread('thread2',5,2)
   threadl = []
   threadl.append(thread1)
   threadl.append(thread2)

   for i in range(2):
       threadl[i].start()
   for i in range(2):
       threadl[i].join()

   print('线程结束')




