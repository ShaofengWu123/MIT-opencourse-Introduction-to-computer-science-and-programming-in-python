#类定义
class people:
    # 定义基本属性(公开变量)
    age = None
    name = 'Unknown'
    Marriage = 'Y'
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __sex = None
    # 定义构造方法
    def __init__(self,a,n = None,s = None,w = None):#类的方法与普通函数的区别，必须有self参数，self代表的是类的实例化而非类。注意构造方法
        #设置默认参数不能调用self或者people，原因是self事实上也是一个参数，而people是类，他们在这个时候都还没有完全定义，解释器无法识别self和people是什么
        self.age = a
        self.name = n
        self.__sex = s
        self.weight = w#构造方法的参数通过 __init__() 传递到类的实例化操作上
        self.mate = self.Marriage#self.Marriage是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
        self.mate = people.Marriage#在类定义内访问类的基本属性是合法的,即使这个时候people类还没有定义完全
        self.notice()#在构造方法中调用其他方法
    def __str__(self):
        return str('%s belongs to people class' % self.name)
    def __repr__(self):
        return repr('%s belongs to people class' % self.name)
    def notice(self):
        print('英文个人信息如下')
    def speak(self):
        #自我介绍
        print('My name is %s. I am %d years old and I am a %s. My weight is %d kg.' %(self.name,self.age,self.__sex,self.weight))
    def marriage_status(self):
        print(people.Marriage)#在类定义内访问类的基本属性是合法的
#类实例化与构造方法的自动调用
David  = people(22,'David','boy',75)
Cathy  = people(21,'Cathy','girl',50)
Unknown = people(a = 20)#构造方法在类实例化时自动调用
print('(实例化完成)')
print(id(David))
print(id(Cathy))
set_people = {David,Cathy,Unknown}
print(set_people)
#自定义的类的实例对象默认也是可哈希的（hashable），而hash值也就是它们的id()。可哈希对象才能用于创建集合。

#访问类的属性，其中私有属性不能在类的定义外访问
print('people类默认的名字',Unknown.name,people.name)#注意结果的不同，前者是类实例化对象Unknown的name属性，由于调用构造方法的默认参数n等
#于None，传递给self.name，所以Unknown.name = None；people.name是类的基本属性且不是私有的，外部访问其值，此时没有实例化，因此没有构造方法
#传递参数n的默认值，输出结果是'Unknown'

#类__str__()方法的作用：返回一个类的描述信息，在类的实例被打印时，打印内容为这个方法返回的描述信息，并且能够使得用户自定义类的实例能够被 str()调用。
# __repr__()方法类似，能够使得用户自定义类的实例能够被 repr()调用，但是没有重写了__str__()方法的类实例被print()调用时输出返回的描述信息的作用。
print('类实例化后的描述信息',David)
#str()与repr()方法的对比：
# 前者输出适合人阅读的信息，输出格式便于理解，适合用于输出内容到用户终端；
# 而后者输出适合解释器阅读的信息，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
# 对于自定义类的实例，要想实例能够被str()和repr()调用，必须在自定义类中重载 __str__ 和 __repr__ 方法。
print(str(David))
print(repr(David))

#print(people.weight) 报错，因为构造方法在类实例化时才会调用，没有实例化无法访问构造方法里的变量。
print('David名字是',David.name)
#访问类的方法
David.speak()

#self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

#类的继承
#单继承
class Student(people):
    grade = None
    def __init__(self,a,n,s,w,g):
    # 调用父类的构函(不是必须的,但是最好调用一下)
        people.__init__(self,a,n,s,w)
        self.grade = g#或者写self.grade
    # 覆写父类的方法
    def speak(self):
        print('My name is %s. I am %d years old. My weight is %d kg. My test grade is %s.' % (self.name, self.age, self.weight, self.grade))#不能调用self.__sex，因为其为people类的私有属性
David = Student(22,'David','boy',75,'A')
David.speak()
super(Student,David).speak()#用super(class,class_example).method()调用父类被覆写的方法

#多继承
#定义一个player的类用于多继承
class Player(people):
    average_score = None
    def __init__(self,a,n,s,w,AS):
        people.__init__(self,a,n,s,w)
        self.average_score = AS
    def speak(self):
        print('My name is %s. I am %d years old. My weight is %d kg. I can get %d points per game.' % (
        self.name, self.age, self.weight, self.average_score))
print('\n')
#多继承实例：菱形继承
class Student_Player(Student,Player):
    def __init__(self,a,n,s,w,g,AS):
        Student.__init__(self,a,n,s,w,g)
        Player.__init__(self,a,n,s,w,AS)

class Player_Student(Player,Student):
    def __init__(self,a,n,s,w,g,AS):
        Student.__init__(self,a,n,s,w,g)
        Player.__init__(self,a,n,s,w,AS)
David = Student_Player(22,'David','boy',75,'A',20)
David.speak()
David = Player_Student(22,'David','boy',75,'A',20)
David.speak() #方法名同，默认调用的是在括号中排前的父类的方法
print('\n')
#思考，如何避免重复调用构造函数？-使用super()方法
#原理：super()会查找所有的超类，以及超类的超类，直到找到所需的特性为止。
class Player_Student(Player,Student):
    def __init__(self,a1,n1,s1,w1,g1,AS1):
        super().__init__(a1,n1,s1,w1,AS1)
        self.grade = g1
        #super(Player_Student,self).__init__(a,n,s,w,AS)#参数只能是MRO中靠前的父类构造方法包含的参数。
David1 = Player_Student(22,'David','boy',75,'A',20)
David1.speak()
print(David1.grade)
print('\n')
#菱形继承的其他例子
class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


d = D()
print('\n')
#在调用到 B 时，首先输出 “Enter B”，但是运行到父类 A 的初始化方法时不立即调用，反而时转向广度优先级高的 C 类，因为 A 类对于 B 类来说是深度遍历。
#使用super()方法A类作为父类其构造函数只被调用了一次，对比以下代码输出结果
class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        A.__init__(self)
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        A.__init__(self)
        print('leave C')



class D(B,C):
    def __init__(self):
        print('enter D')
        B.__init__(self)
        C.__init__(self)
        print('leave D')

d = D()
print('\n')
#未使用super()方法，而是调用未绑定的超类构造方法
#原理：在调用了一个实例的方法时，该方法的self参数会自动绑定到实例上（称为绑定方法）；如果直接调用类的方法（比如Bird.__init__），那么就没有实例会被绑定，可以自由提供需要的self参数（未绑定方法）。

#再对比以下代码
class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()#super(B,D),D的MRO为 DBCA,在B之后的CA里寻找__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B,C):
    def __init__(self):
        print('enter D')
        B.__init__(self)#这里的self指的是？ D self传递给B的构造方法
        C.__init__(self)
        print('leave D')

d = D()
print(D.mro())
print(B.mro())
print('\n')

#理解self代表的对象
class A():
    def __init__(self):
        print('enter A')
        self.Dobject = 'A'
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        A.__init__(self)
        print('leave B')


class D(B):
    Dobject = None
    def __init__(self):
        print('enter D')
        print(self.Dobject)#self指的是？D
        B.__init__(self)#self指的是？ D,依次传递给B和A
        print(self.Dobject)#在执行A的构造方法时，self代表D，self.Dobject = 'A'语句改变了D.Dobejct的值
        print('leave D')

d = D()



