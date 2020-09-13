#用copy()函数实现
my_foods = ['pizza', 'falafel', 'carrot cake']
myfriend_foods = my_foods.copy()
my_foods.append('beef')
print(my_foods)
print(myfriend_foods)

#用for循环实现
my_foods = ['pizza', 'falafel', 'carrot cake']
myfriend_foods = []
a = len(my_foods)
for i in range(a):
        myfriend_foods.append(my_foods[i])
my_foods.append('beef')
print(my_foods)
print(myfriend_foods)

#用列表切片实现(列表切片是浅复制)
my_foods = ['pizza', 'falafel', 'carrot cake']
myfriend_foods = my_foods[::]
my_foods.append('beef')
print(my_foods)
print(myfriend_foods)

#错误示范
my_foods = ['pizza', 'falafel', 'carrot cake']
myfriend_foods = my_foods
my_foods.append('beef')
print(my_foods)
print(myfriend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
myfather_foods = my_foods
print('myfather',myfather_foods)
print('me',my_foods)
my_foods.append('beef')
print('myfather',myfather_foods)
print('me',my_foods)
#通过 clear() 方法，remove() 方法，pop() 方法，append() 方法等改变列表的，相应的已经赋值给其它变量的列表也会发生相应改变。



import math
a = [3.4568,5.66987,546.25697,165464.65,20114.002,254638.00]
b = []
for i in range(len(a)) :
        c = math.modf(a[i])
        b.append(c)
d = b[::-1]
print(d)
print(b)
b.reverse()
print(d == b)

a = math.sqrt(100)
b = 10
print(a)