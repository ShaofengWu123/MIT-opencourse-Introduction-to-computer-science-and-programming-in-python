#list创建方法
a1 = [1,2,3]
a2 = ['a','b','c']
a3 = ['A','B','C']
a4 = list(range(10))
print('用range()函数创建list',a4)
#嵌套list(nested list)
x = [a1,a2]
print('嵌套list',x, end="")
print('\n')
#访问list中的元素，并修改或删除其中元素
x[1] = a3
print('a1 a2列表嵌套列表x',x)
print('列表x第一个元素的第一个元素',x[0][0])
del(x[1])
print('修改后x',x)
#list函数
print('a1列表长度是',len(a1)) #len(list)返回列表元素个数
print('a1列表最大值最小值分别是',max(a1),max(a2)) #max(list),min(list)分别返回列表最大值最小值
print('字符串和元组转换为列表',list('hello'),list(('abc','ABC',1))) #list(seq)将字符串和元组转换为列表并返回
#list方法
# list.append(obj)在list末尾添加obj,obj可以是任意数据类型。无返回值但修改列表。
tuple1 = ('d','e')
a2.append(tuple1)
print('改变后的a2列表',a2)
#list.extend(seq)在列表末尾一次性追加一个序列（列表、元组、集合、字典）的多个值，其中字典的key作为元素依次添加到列表末尾。无返回值但修改列表。
a3.extend(['D','E','F'])
a3.extend(('D','E','F'))
a3.extend({'D','E','F'})
a3.extend({'D':'d','E':'d','F':'d'})
print('改变后的a3列表',a3)
#list.count(obj)返回obj在list中出现的次数
print('列表a1中出现1的次数',a1.count(1))
#list.index(obj[,start[,end]])返回列表中某个值第一个匹配项的索引位置
print ('D 索引值为', a3.index('D',1))
print ('D 索引值为', a3.index('D',4,8))
#list.pop([index=-1])从list中移除某一索引值的元素并返回该元素的值，每进行一次移除list各元素的索引发生变化
print('移除的元素是',a3.pop(0),a3.pop(0),a3.pop())
#list.remove(obj)移除列表中obj的第一个匹配项，没有返回值
print('a3',a3)
a3.remove('E')
print('变化后a3',a3)
#list.reverse()将list反向排序，无返回值
a3.reverse()
print('反转后的a3',a3)
#list.sort(key=None,reverse=False)对list的对象进行排序，key用于指定用于排序比较的元素，reverse为排序规则，默认为False。无返回值。
a3.sort()
print('排序后的a3',a3)
list1 = [(1,2,4),(3,5,1),(4,7,1),(3,4,0)]
def takesecond(elem):
        return elem[2]
print('返回list1中的元素',takesecond(list1[0]))
list1.sort(key=takesecond,reverse=True)# 指定第二个元素排序
print('排序后的list1',list1)
#list.clear()清空列表，无返回值
a3.clear()
print('清空后的a3',a3)
#list.copy()复制列表，返回复制得到的列表
print('复制得到的a1',a1.copy())

#列表当做堆栈(stack)使用。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
list_stack = ['a','b','c']
list_stack.append('d')
list_stack.append('e')
print(list_stack)
print(list_stack.pop())
print(list_stack.pop())

#列表当做队列使用。
#在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
from collections import deque #标准库collections中的deque模块
list_queue = deque(['a','b','c'])
list_queue.append('d')
list_queue.append('e')
print(list_queue)
print(list_queue.popleft())
print(list_queue.popleft())
print(list_queue.pop())
#deque长度限制
list_queue2 = deque(maxlen = 10)
for i in range(20):
    list_queue2.append(i)
print(list_queue2)#超过长度，尾端会自动删除元素

#列表推导式
#每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
from math import  pi
import math
vec1 = [1,3,5,7,9]
vec2 = [2,4,6,8,10]
vec3 = [['a','b','c'],['d','e','f'],['g','h','i']]
vec_g1 = [x*y for x in vec1 if x<6 for y in vec2 if y>6]
print('生成的列表vec_g1:',vec_g1)
vec_g2 = [[x[i] for x in vec3] for i in range(3)]
print('生成的列表vec_g2:',vec_g2)
vec_g3 = [round(pi,i) for i in range(5)]
print('生成的列表vec_g3:',vec_g3)#列表推导式可以使用复杂表达式或嵌套函数：
#上述推导式可以运用于元组、字典、集合的创建。要注意的是元组用推导式创建时要使用tuple()函数，用括号得到的是生成器对象。

#del语句删除列表元素和切割
del vec[0]
del vec[0:2]#等同于vec[0:2] = []
del vec[:]

#迭代的时候避免改变列表，否则可能漏掉某些元素(因为python在遍历时不会更新counter，列表长度改变会导致漏掉一些元素)

