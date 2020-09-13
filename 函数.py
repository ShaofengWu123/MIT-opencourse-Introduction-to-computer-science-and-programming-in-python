#基本语法
def function1():
    print(1)
def function2(x):
    print(x)
def function3(x):
    print(x)
    return True
#对象、变量与类型
#对象有类型，而变量没有类型，变量只是指向对象的一个指针或者说是对象的一个引用
a = 'David'
a = [1,2,3]#a是变量，其既可以指向'David'(string类型的对象)，也可以指向[1,2,3](list类型的对象)

#参数传递:引用传递(传可变对象)与值传递(传不可变对象)
def changeint(x):
    x = 10
x = 2
changeint(x)
print('x是否变化？-不变',x)

def changelist(l):
    l[0] = 'changed'
l = [1,2,3,4,5]
changelist(l)
print('l是否变化？-变化',l)
#更多例子
a = b = 10
a= 5
print(a,b)

list1 = list2 = [1,2,3,4]
list1[0] = 0
print(list1,list2)
list1 = [5,6,7,8]
print(list1,list2)#和下面这个例子道理一样。list1和list2都指向存放同一个列表的元素的一串地址，上一行让list1指向了一个新的列表的元素的一串地址
                  #因此l1的“改变”不会影响到l2
#更多例子
l2 = [1,2,3,4,5,6]
print(id(l2))
def changelist2(l2):#形参l2和实参指向同一个对象，这里值传递传递的是一组地址，这组地址指向的是列表[1,2,3,4,5,6]
    l2[0] = 0#访问列表中某个元素，改变了这个元素，但是没有改变实参（存放列表元素的一串地址）
    print(id(l2))#形参和实参指向同一个对象（存放列表元素的一串地址），因此形参id和实参一样
    l2 = ['changed','list']#形参指向一个新的对象
    print(id(l2))#形参指向新的对象，id变化
def printl2():
    l2 = ['local','defined','list']#l2这个时候是个局部变量，和全局变量l2没有关系
    print(l2)

changelist2(l2)


print('l2是否发生变化-不变',l2)#可变类型的对象变化的是其内部的内容，函数内可以访问全局变量，但不能更新(修改)其值！这里只是对函数内的对象分配了一个局部变量，不影响全局变量。

printl2()


#参数类型
#必需参数（位置参数）:必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
def printme():
    print('David')
printme()#可以无参数调用
def printme1(string):
    print(string)
printme1('David')
#关键字参数:关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printme2(str1,str2):
    print(str1,str2)
printme2(str2 = 'David',str1 = 'Hello')
printme2('Hello',str2 = 'David')
try:
   exec('printme2(str1 = \'Hello\',\'David\')')
   #exec()方法：执行存放在字符串中的python代码

except Exception as errorinfo:
    print(errorinfo)
#默认参数
def printme3(str1,str2 = 'Hello'):#默认参数必须放在最后
    print(str2,str1)
printme3('John')
printme3('John','Welcome')#修改默认值
printme3(str2 = 'Welcome',str1 = 'John')#关键字参数修改默认值
#不定长参数:可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printme4(str1,*str_tuple):
    print(str1)
    print(str_tuple)
printme4('David','John','Marry','Cathy')
printme4('Tony')#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。这里使用for遍历tuple中的元素可以避免输出空元组。
def printme5(*str_tuple):
    print(str_tuple)
printme5('David','John','Marry','Cathy')
#如果已经有一个字符串、列表、元组，想要以不定长参数的形式导入,在前面加*
list_name = ['David','John','Marry','Cathy']
printme5(*list_name)
printme5(list_name)#对比上一行结果

#加了两个星号 ** 的参数必须是关键字参数，以字典的形式导入。
def printme6(str,**str_dic):
    print(str)
    print(str_dic)
printme6('David',John=1,Marry=2,Cathy=3)#注意变量导入时候的格式
#如果单独出现星号 * 后的参数必须用关键字传入。
def printme7(str,*,a):
    for i in range(a):
        print(str,i)
printme7('David',a = 4)
#python3.8强制位置参数,不允许用关键词参数形式
def printme8(a,b,/):
    print(a+b)
printme8('Good','Morning')

#显示指定参数类型和返回值类型？？
def function_demo(param_A: int, param_B: float, param_C: list, param_D: tuple) -> dict:
    return {param_A:param_B}

print('返回值类型指定',function_demo('abcd',2,3,4))

#匿名函数
#python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
#1.lambda 只是一个表达式，函数体比 def 简单很多。
#2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#3.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#4.虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#语法:lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum(arg2=10, arg1=20))#关键字参数调用
print("相加后的值为 : ", sum(20, 20))#位置参数调用
#更多例子：
function_m = lambda x : x * x
print(function_m(5))

function_d = lambda x=10 : x**2#默认参数
print(function_d())

#Tricks
#函数与参数绑定:map()方法，与zip()用于遍历区分
print('函数与参数绑定-map()方法')
def fun_test(a,b,c):
    return(a+b+c)
d = map(fun_test,[1,10,6],[4,2,8],[11,6,20])
print(type(d))#类型为map object
print(d)#map object
print(list(d))#可生成list，和zip object相似
print(tuple(d))#空的元组




#函数用另一个函数作为参数
#例子1
def sum(a,b):
    return (a+b)
def test(a):
    print(a != 0)
    print('Test Over!')
test(sum(1,2))#思考：这里是不是函数作为了参数？ 不是，这里作为参数的是函数的返回值。
#例子2
def hello () :
  print ("Hello, world!")
def hello_follow1(a):
  "执行hello()函数"
  return a
print('例2')
print(type(hello()))
print(hello_follow1(hello()))#思考：hello_follow1函数此时的参数是什么？是函数还是函数的返回值？ 返回值，为None。 为什么此时会有hello world被输出？ 因为hello()函数每被引用一次就会输出一次。
#例3
def hello2(x):
    print("Hello, world!")
    return x
print('例3')
print(type(hello2(1)))
hello_follow1(hello2(1))
print(hello_follow1(hello2(1)))#和例2同理
#例子4
def hello_follow2(a):
    "执行hello()函数"
    a()#注意与例2的区别
print('例4')
hello_follow2(hello)
#例子5
def demo(*p):
    i=0
    for var in p:
        var(i)
        i+=1
def d1(i):
    print("这里是第一个子函数,输入的数是",i)
def d2(i):
    print("这里是第二个子函数,输入的数是",i)
def d3(i):
    print("这里是第三个子函数,输入的数是",i)
def d4(i):
    print("这里是第四个子函数,输入的数是",i)
demo(d1,d2,d3,d4)#思考：能不能将d1(0)作为demo()函数的参数？ 不能，因为此时p元组里必须是函数才能满足要求，如果用d1(0)作为参量，实际上就是用d1函数的返回值None作为参量。

#可以通过 函数名.__doc__ 的方式来显示函数的说明文档
print(hello_follow1.__doc__)



#全局变量与局部变量
#1.函数内可以访问全局变量，但是不能修改其值
#对比以下例子
#1.例1：
a = 10
def sum():
    n = 5
    #n += a
    a = 11
    print('例1函数内a的值', a, end=' , ')
    print('n = ', n)
sum()
print('例1函数外a的值',a)#不可变类型的值传递
#2.例2：
def sum():
    n = 5
    n += a
    #a = 11
    print('例2函数内a的值', a, end=' , ')
    print('n = ', n)
sum()
print('例2函数外a的值',a)#对全局变量进行了访问，未报错，与例3、例4对比
#3.例3：
def sum():
    n = 5
    a = 11
    n += a
    print('例3函数内a的值', a, end=' , ')
    print('n = ', n)
sum()
print('例3函数外a的值',a)#未报错，因为函数内a作为本地变量并没有引起歧义。

#4.例4
if input('跳过错误的例4？') == 'N' :
 def sum():
    n = 5
    n += a
    a = 11
    print('例4函数内a的值', a, end=' , ')
    print('n = ', n)
 sum()
 print('例4函数外a的值',a)#报错，因为先引用了全局变量，又有同名的本地变量，引起了歧义。






#5.例5
def sum():
    global a#在引用a之前，一定要先声明其为全局变量，这样就可以在函数中对其进行更新
    n = 5
    n += a
    a = 11
    print('例5函数内a的值', a, end=' , ')
    print('n = ', n)
sum()
print('例5函数外a的值',a)

#变量作用域
choice = int(input('选择你想要的作用域:\n\
1.局部作用域\n\
2.局部外的局部(闭包函数外的函数中)\n\
3.全局作用域\n\
4.内建作用域\n\
请输入：'))

if choice == 1:
#局部作用域
 x = int(3.3)

 x = 0
 def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()

 outer()

elif choice == 2:
#局部外的局部
 x = int(3.3)

 x = 0
 def outer():
    x = 1
    def inner():
        y = 2
        print(x)
    inner()

 outer()

elif choice == 3:
#全局作用域
 x = int(3.3)

 x = 0
 def outer():
    y = 1

    def inner():
        y = 2
        print(x)

    inner()

 outer()

elif choice ==4:
#内建作用域
 x = int(3.3)

 y = 0
 def outer():
    y = 1

    def inner():
        y = 2
        print(x)

    inner()

 outer()

#global关键字会跳过中间层直接将嵌套作用域内的局部变量变为全局变量:
num = 20
def outer():
    num = 10
    def inner():
        global num
        print (num)#global关键字使num跳过了中间层中局部变量num=10直接成为全局变量num = 20
        num = 100
        print (num)#由于这里的num是全局变量，因此对其的更新也是有效的
    inner()
    print(num)#根据变量作用域，这里的num是outer函数层的局部变量
outer()
print (num)#全局变量num已更新

