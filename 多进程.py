import multiprocessing as mp
import time

#提纲：
#1.进程创建与定义：Process()和用类包装
#2.数据沟通：Queue(),Pipe(),Manager(),shared memory (mp.value,mp.array...注意指明数据类型)
#3.进程控制：进程锁 Lock()
#4.进程自动创建与任务分配：进程池Pool()。相关方法:map(job,iterable item),apply_async(job,iterable item with single element)与
#  get()

def job1(a,b,q):
    sum = 0
    for i in range(a,b):
        sum = sum + i
    q.put(sum)
def job2(pipe):
    pipe.send('你好，主进程')#向管的另一端发送信息
    print('子进程接收消息: ',pipe.recv())#从管的另一端接收信息,在收到信息前会一直等待
    pipe.close()#关闭管道
def job3(dic,lis,i):
    dic[i] = i
    lis.append(i)
def job4(v,i):
    v.value += i
def job5(i,l,v):
    #time.sleep(0.1)
    l.acquire()
    print('线程{0}正在运行'.format(i))
    for k in range(i+1):
        v.value += k
        print(v.value)
    l.release()
def job6(x):
    return x**2
class my_process(mp.Process):
     def __init__(self,n,a,b,q):
         super().__init__()
         self.name = n
         self.min = a
         self.max = b
         self.q = q
     def run(self):
         job1(self.min,self.max,self.q)
if __name__ =='__main__':#子进程通过导入其所在的脚本模块来实现target函数的运行。python禁止了子进程再创建子进程，防止创建子进程的语句也被导入，
                         #要用改if语句保护子进程相关的代码；同理，函数的定义必须在该if语句之前，如果在if语句内，子进程导入其所在的脚本模块
                         #（即本文件）时，定义函数的语句没有被导入，就会发生not defined报错。
 #创建Queue存放结果
 q1 = mp.Queue()
 #新建一个进程(各种方法基本和多线程类似)
 p1 = mp.Process(target = job1, args = (1,100,q1))
 p2 = my_process('Process 2',1,100,q1)
 #开始进程
 p1.start()
 p2.start()
 #进程join()方法
 p1.join()
 p2.join()
 print('p1,p2进程结束')
 #从Queue中取出结果
 result = []
 while not q1.empty():
   result.append(q1.get())
 print(result)
 p1.close()
 p2.close()

#除了Queue的其他进程通信方法
#Pipe
 pipe1,pipe2 = mp.Pipe()#创建一个双向管
 p3 = mp.Process(target = job2, args = (pipe2,))
 p3.start()
 print('主进程接收消息: ',pipe1.recv())
 pipe1.send('你好，子进程')
 p3.join()
 p3.close()
#Manager：不同进程处理同一份数据
 dic = mp.Manager().dict()#创建字典的时候不能用{}创建
 lis = mp.Manager().list([1,2,3,4])
 plist = []
 for i in range(3):
     p = mp.Process(target = job3, args = (dic,lis,i))
     plist.append(p)
     p.start()
 for process in plist:
     process.join()
 print(dic)
 print(lis)
 for process in plist:
     process.close()
#共享内存shared memory:
 shared_value = mp.Value('i',-1)#i表示带符号的整型
 shared_array = mp.Array('I',[1,2,3,4,5])#I表示不带符号的整型
 plist = []
 for i in range(5):
     p = mp.Process(target = job4, args = (shared_value,i))
     plist.append(p)
     p.start()
 for process in plist:
     p.join()
 print(shared_value.value)
 for process in plist:
     p.close()

#进程锁
 lock = mp.Lock()#和线程锁使用方法一样
 plist = []
 v = mp.Value('i',0)
 for i in range(5):
     p = mp.Process(target = job5, args = (i,lock,v))
     p.start()
     plist.append(p)
 for process in plist:
     process.join()
 for process in plist:
     process.close()

#进程池：思想就是把任务和数据放入进程池中，让其自由运算。这样的话就不需要用mp.Process方法创建进程了。
 pool = mp.Pool(processes = 4)#processes参数指定了用几个核进行运算
#apply_async():异步方法。中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的。在获取值时使用get()方法。
 result = [pool.apply_async(job6,(i,)) for i in range(10)]#用迭代器来实现多个结果的输出
 print(result)#列表中的元素全部都是 multiprocessing.pool.ApplyResult 对象
 print([res.get() for res in result])#挨个获取result列表中multiprocessing.pool.ApplyResult对象的值
#map()方法，传入的参数是函数名和迭代参数，输出多个结果
 res = pool.map(job6,range(10))
 print(res)




