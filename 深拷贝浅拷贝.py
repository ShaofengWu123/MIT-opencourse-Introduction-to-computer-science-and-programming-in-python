import copy
#将一个列表的数据复制到另一个列表中。
list1 = [1,2,3,['a','b','c']]

#直接赋值:list1和list2都指向同一个对象（即列表[1,2,3,['a','b','c']]），他们都是这个列表的引用别名
list2 = list1

#浅拷贝：浅拷贝, list1 和 list3 是一个独立的对象，但他们的子对象还是指向统一对象（是这一对象的引用）,但是对于不可变对象改变其值相当于新分配一个地址存放，因此改变list1中的不可变对象（例如数字）怒会改变list3中对应索引的元素；但是改变
list3 = copy.copy(list1)
print(id(list1) == id(list3))#list1和list3独立
print(id(list1[0]) == id(list3[0]))
print(id(list1[3]) == id(list3[3]))
#或者list3 = list1.copy()
print('改变list1第0项')
list1[0] = 0#list3第0项不改变
print(id(list1[0]) == id(list3[0]))
print(id(list1) == id(list3))
print(list1,list3)

print('改变list1第3项的内容')
list1[3][0] = 'A'#list3第3项内容变化
print(id(list1[3]) == id(list3[3]))
print(id(list1) == id(list3))
print(list1,list3)

print('改变list1第3项')
list1 = [1,2,3,['a','b','c']]
list3 = copy.copy(list1)
list1[3] = [11,22,33]#list3第3项不变化，因为直接给list1的第3项了一个新的地址
print(id(list1[3]) == id(list3[3]))
print(id(list1) == id(list3))
print(list1,list3)

print('\n')

#列表切片:相当于浅拷贝
print('列表切片')
list1 = [1,2,3,['a','b','c']]
list3 = list1[::]
print(list3)
print(id(list1) == id(list3))#list1和list3独立
print(id(list1[0]) == id(list3[0]))
print(id(list1[3]) == id(list3[3]))
#或者list3 = list1.copy()
print('改变list1第0项')
list1[0] = 0#list3第0项不改变
print(id(list1[0]) == id(list3[0]))
print(id(list1) == id(list3))
print(list1,list3)

print('改变list1第3项的内容')
list1[3][0] = 'A'#list3第3项内容变化
print(id(list1[3]) == id(list3[3]))
print(id(list1) == id(list3))
print(list1,list3)

print('改变list1第3项')
list1 = [1,2,3,['a','b','c']]
list3 = copy.copy(list1)
list1[3] = [11,22,33]#list3第3项不变化，因为直接给list1的第3项了一个新的地址
print(id(list1[3]) == id(list3[3]))
print(id(list1) == id(list3))
print(list1,list3)


#深拷贝:深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
print('深度拷贝')
list1 = [1,2,3,['a','b','c']]
list3 = copy.deepcopy(list1)
print(id(list1) == id(list3))
print(id(list1[0]) == id(list3[0]))#不可变对象地址是一样的，但是这不影响两个list完全独立的事实，因为无论深浅拷贝，改变不可变对象相当于重新给了存储地址
print(id(list1[3]) == id(list3[3]))#深拷贝子对象也是独立的

list1[0] = 0
list1[3][0] = 'A'
print(list1,list3)


