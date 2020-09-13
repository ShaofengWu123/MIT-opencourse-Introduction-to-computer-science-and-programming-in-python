import math
import random
#数字:不可变数据类型之一，若改变数字数据类型的值，那么将重新分配存储空间
num1 = 1
num1_1 = int(num1)
num1_2 = float(num1)
num1_3 = complex(num1)
num1_4 = complex(num1,num1)
print('四种种数字类型\n',
      num1_1,'\n',
      num1_2,'\n',
      num1_3,num1_4,'\n',
      True)
#数学函数
#abs(x)的绝对值或者模
print('-1的绝对值',abs(-1))
print('1+1j的模',abs(1+1j))
#math.ceil(x)返回x的上整数,math.floor(x)返回x的下整数
print('-4.7的上整数',math.ceil(-4.7))
print('-4.7的下整数',math.floor(-4.7))
#math.fabs(x)返回x的绝对值(浮点型)
print('-1的绝对值',math.fabs(-1))
#math.exp(x)返回e的x次幂
print('e^1=',math.exp(1))
print(f'{math.pi**1=}')
#round(x,[n])返回浮点数x保留小数点后n位四舍五入后的值，精度较低
print('四舍五入',round(5.225000001,2))
#math.log(x)和math.log10(x)分别返回x的自然对数和以10为底的对数
print('e的自然对数和以10为底的对数',math.log(math.e),math.log10(math.e))
#max()和min()函数，参数可以是序列，返回给定参数的最大值和最小值
print('最大值',max(1,2,3,4,5))
print('最大值',max([1,2,3,4,5]))
print('最大值',max([(4,1,1),(3,6),(2,10)]))#按每个元素的第一个元素排序
print('最小值',min('123456'))
print('最小值',min({1,2,3,4}))
print('最小值',min({2:1,3:8,4:5}))#按照键排序
#math.modf(x)返回x的小数部分和整数部分(浮点型)
print('pi的小数部分和整数部分',math.modf(math.pi))
#math.pow(x,y) math模块pow方法，计算x**y%z。pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。
print('pow(2,10)和math.pow(2,10)',pow(2,10),math.pow(2,10))
print('pow(2,4,5)',pow(2,4,5)) #math.pow()只有两个参数，没有取模的参数
#math.sqrt(x)返回x的平方根(浮点型)
print('100的平方根',math.sqrt(100))
#随机数函数
#random.choice(seq)从序列(字符串、列表、元组、集合、字典，对于字典而言，选出的是value)中返回随机项
print('随机选择1-10以内的数字',random.choice(range(1,11)))
#random.randrange([start],stop[,step])返回指定递增基数集合中的一个随机数，基数默认值为1。
print('随机生成除三余一的数字',random.randrange(1,10,3))
#random.random()返回随机生成的一个实数，它在[0,1)范围内。
print('随机生成0-1内的实数',random.random())
#random.randint(start,end)返回随机生成的一个整数，它在[start,end)内
print('随机生成1-10内的整数',random.randint(1,10))
#random.uniform(start,end)返回随机生成的一个浮点数，它在[start,end)内
print('随机生成1-3内的整数',random.uniform(1,3))
#random.seed(x)改变随机数生成器的种子，无返回值
random.seed(100)
print('种子为100',random.randrange(1,10))
random.seed()
#random.shuffle(list)将list所有元素随机排序，无返回值
a = [1,2,3,4,5]
print('a序列随机排序',a)

print('\n')