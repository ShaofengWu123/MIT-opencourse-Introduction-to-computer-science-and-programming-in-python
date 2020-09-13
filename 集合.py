import math
import random
#集合（无序的不重复元素序列）的创建
#集合元素不能是不可哈希对象，即列表，集合，字典，原因如下：
#An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method),
#and can be compared to other objects (it needs an __ eq__() or __cmp__(). Hashable objects which compare equal must
#have the same hash value.
#对于列表、字典、集合，他们在改变值的同时却没有改变id,无法由地址定位值的唯一性,因而不可哈希。我们自定义的类的实例对象默认也是可哈希的（hashable）
# ，而hash值也就是它们的id()。

a = [1,2,3,4,5,6,7,8,9,123,543,756,312]
s1 = {1,2,3,4,5,6,'a','b','c'}
s2 = {2,4,6,8,'b'}
s_single = set(('apple',))#其他形式会导致字符串被拆分
empty = set()#不能用{}，这表示空字典
s3 = {x**2 for x in range(4)}
print('集合推导式(set comprehension)创建得到s3',s3)
print(s_single)
#集合的运算
print('属于s1但不属于s2',s1 - s2,s1.difference(s2))
print('属于s2但不属于s1',s2 - s1,s2.difference(s1))
print('&为按位与运算符，这里表示交集',s1 & s2,s1.intersection(s2))#按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0。
print('|为按位或运算符，这里表示并集',s1 | s2)#按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print('^为按位异或运算符，这里表示并集和交集的差集',s1 ^ s2)#按位异或运算符：当两对应的二进位相异时，结果为1。
print('(s1 - s2) | (s2 - s1) == s1 ^ s2是否成立？',(s1 - s2) | (s2 - s1) == s1 ^ s2)
#其他的位运算符
#1. ~ 按位取反运算符 ~x = -x-1
print(~5)
#2.<</>>左移、右移运算符
a = 60
print(a << 2)

#集合内置方法
#添加元素
#s.add(elements)给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。无返回值。
#s.update(elements/sequence)修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。无返回值。
s3.update('56789')
print('更新后的s3',s3)
s1.update(s2)
print('s1,s2的并集',s1)
#删除元素
#s.remove(element)移除集合中的指定元素。无返回值。remove()方法移除一个不存在的元素时会发生错误。
#s.discard(element)移除指定的集合元素。无返回值。discard()方法移除一个不存在的元素时不会发生错误。
#s.pop()随机移除一个元素并返回该元素。set 集合的 pop 方法会对集合进行无序的排列(对于纯数字集合不是无序的)，然后将这个无序排列集合的左面第一个元素进行删除。
s4 = {1,2,3,4,5,6,7,8,9,0}
print(s4.remove(1))
print(s4.discard(2))
print(s4.pop())
print(s4.pop())
print('更新后的s4',s4)
#清空集合
#s.clear()


