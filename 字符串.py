#字符串创建方式
str1 = 'Hello!'
str2 = 'I'
str3 = 'You'
str4 = 'and'
#字符串的子字符串访问与截取
str1_1 = str1[1]
str1_2 = str1[1:3]
str1_3 = str1[1:-2]
print(str1,'\n'+str1_1,'\n'+str1_2,'\n'+str1_3)
#多行字符串
print("""I
\tam\n
fine""")
#字符串运算符
print(str2 + 'love' + str3[0:3])
print(str3*2)
print('e' in str1)
print('a' not in str1)
print(r'\n',R'\n')
#格式化字符串
name = 'David'
b = 1
a = f'ABCDEFG'
print(f'Hello {name} {b}')
print(f'{b+1=}')
age = 10
print('{0} is {1}'.format('David',age) + ('year old' if age <= 1 else 'years old'))#可以用推导式封装一定的逻辑
#字符串内建函数
#str.capitalize()返回一个首字母大写，其他字母小写的字符串
str1 = 'hello WORLD!'
str2 = '@Hello World!'
print('首字母大写，其他小写',str1.capitalize())
print('首字母大写，其他小写',str2.capitalize())
#str.center(width[,fillchar])返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。fillchar默认为空格
print('居中字符串',str1.center(40,'*'))
#str.count(sub[,start= 0[,end=len(string)]])返回子字符串在字符串中出现的次数。
print('str2中l固定范围出现次数',str2.count('l',4,-3))
#bytes.decode(encoding="utf-8", errors="strict")方法以指定的编码格式解码 bytes 对象,返回解码后的字符串
#str.encode(encoding='UTF-8',errors='strict')方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。该方法返回编码后的字符串，它是一个 bytes 对象。
str1 = '伍少枫'
str1_utf8 = str1.encode('UTF-8','strict')
print('伍少枫的UTF-8编码',str1.encode('UTF-8','strict'))
print('UTF-8编码解码',str1_utf8.decode('UTF8'))
#str.lendswith(suffix[,beg=0[,end=len(string)]])用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='Run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 3))
#str.join(sequence)将序列中的元素以指定的字符连接生成一个新的字符串并返回。
s1 = '-'
David = ('D','a','v','i','d')
print('组合后字符串',s1.join(David))
#str.translate(table),bytes.translate(table[,delete]),bytearray.translate(table[,delete]) 根据参数table给出的表返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，
#剩下的字符要按照table中给出的映射来进行映射。
#str.maketrans(x[,y[,z]]),bytearray.maketrans(x,y),bytes.maketrans(x,y) 创建字符映射的转换表
#1.一个参数，该参数必须为字典
#2.两个参数 x 和 y，x、y 必须是长度相等的字符串，并且 x 中每个字符映射到 y 中相同位置的字符
#3.三个参数 x、y、z，第三个参数 z 必须是字符串，其字符将被映射为 None，即删除该字符；如果 z 中字符与 x 中字符重复，该重复的字符在最终结果中还是会被删除。也就是无论是否重复，只要有第三个参数 z，z 中的字符都会被删除。
str_tabtrans = str.maketrans({'e':'E','o':'O'})
print('Hello!转换后'.translate(str_tabtrans))
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('David转换后',b'David'.translate(bytes_tabtrans,b'D'))
str_tabtrans2 = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','a')
print('David转换后','David'.translate(str_tabtrans2))
print('映射表实质上为ASCII编码字典',str_tabtrans2,'\n',type(str_tabtrans2))

#修改字符串
empty = ''
name_me = 'shaofeng wu'
name_list = []
name_list.extend(name_me)
name_list[0] = 'S'
print('修改后字符串',empty.join(name_list))
#str.split(str1='',num=str.count(str1))通过指定分隔符对字符串进行切片并返回分割后的字符串列表。
url = 'http://www/baidu/pictures/a12345.jpg'
print(url.split('/')[-1])#python爬虫获取图片名称

#查找子串
str1 = 'exam exam exam'
beg = 0
while str1.find('exam',beg) != -1:
    print(str1.find('exam',beg))
    beg = str1.find('exam',beg) + len('exam')-1


str1 = "this is\tstring example....wow!!!"
str2 = "athis is\tstring example....wow!!!"
str3 = "athis is    string example....wow!!!"  # is 和 string 中间输入 8 个空格
print(str1)
print(str1.expandtabs(8))
print("a"+str1)
print(str2)
print(str3)

print('\n')

#判断字符串是否由数字组成
print('s.isdigit、isdecimal 和 s.isnumeric 区别\n\
isdigit()-狭义上的数字，只包括byte数字，十进制数和Unicode数字\n\
True: Unicode数字，byte数字（单字节），全角数字（双字节）\n\
False: 汉字数字，罗马数字，小数\n\
Error: 无\n\
\n\
isdecimal()-狭义上的数字，只包括十进制数和Unicode数字\n\
True: Unicode数字，全角数字（双字节）\n\
False: 罗马数字，汉字数字，小数\n\
Error: byte数字（单字节）\n\
\n\
isnumeric()-最广泛意义上的数字\n\
True: Unicode 数字，全角数字（双字节），汉字数字，罗马数字\n\
False: 小数\n\
Error: byte数字（单字节）')

#tricks
#1.用表达式封装简单逻辑
age = eval(input('age?'))
print('{0} is {1} '.format('David',age) + ('year old' if age <= 1 else 'years old'))
#2.eval()方法：用来执行一个字符串表达式，并返回表达式的值。注意这里表达式不一定是一个算术式，可以是其他的形式。
print(eval('1+1'))
try:
  print(type(eval(input('please input'))))#将输入的内容从字符串转换成本来的类型
except Exception as error:
  print(error)

print(type('[1,2,3,4]'))
print(type(eval('[1,2,3,4]')))
#unicodedata包