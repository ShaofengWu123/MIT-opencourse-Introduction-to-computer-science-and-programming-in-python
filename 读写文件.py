text = 'Name:\tShaofeng Wu\nAge:\t22\nHeight:\t180cm'
my_file = open('Information.txt','w')
my_file.write(text)
my_file.close()
append_text = '\nWeight:\t80kg'
my_file = open('Information.txt','a')
my_file.write(append_text)
my_file.close()

my_file = open('Information.txt','r')
content = my_file.read()#读取文件内容
print(content)
my_file.close()

my_file = open('Information.txt','r')
content2 = my_file.readline()#逐行读文件
print(content2)
content2 = my_file.readline()#自动按顺序逐行读取
print(content2)
my_file.close()

my_file = open('Information.txt','r')
content3 = my_file.readlines()#把文件的每一行作为list的一个元素存储进list中
print(content3)
my_file.close()

#其他格式文件
my_file = open('Grade-class.xls','w')
my_file.write(text)
my_file.close()

my_file = open('Information1.doc','r')
content4 = my_file.read()
print(content4)
my_file.close()