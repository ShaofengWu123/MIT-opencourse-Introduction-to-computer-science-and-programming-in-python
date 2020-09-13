import math
import time
n = int(input('请输入数列项数:'))
#1.循环语句
start = time.time()
i = 0
a = 0
b = 1
while i < n-1:
    a , b = b , a+b
    i += 1
print('第 %s 项为：%s' % (n,a))
end = time.time()
print('时间为：%.5f' % (end - start))

#2.函数递归
start = time.time()
def F(n) :
    if n == 1:
       return 0
    else:
        if n == 2:
            return 1
        else:
            return F(n-1)+F(n-2)
print('第 %s 项为：%s' % (n,F(n)))
end = time.time()
print('时间为：%.5f' % (end - start))

#3.尾递归
start = time.time()
a = 0
b = 1
def F(n,a,b):
    if n == 1:
        return a
    else:
        return F(n-1,b,a+b)
print('第 %s 项为：%s' % (n,F(n,a,b)))
end = time.time()
print('时间为：%.5f' % (end - start))

print(isinstance(1,(float,str)))