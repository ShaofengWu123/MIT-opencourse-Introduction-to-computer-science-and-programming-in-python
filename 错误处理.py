try:
 file = open('TestFile','r+')
except Exception as error:#如果发生错误，错误信息存在一个变量中，可以打印
  print(error)
  choice = input('Create \'TestFile\' ?')
  if choice == 'y':
      file = open('TestFile','w')
  else:
      pass
else:#如果没发生错误，执行以下的语句
    pass

#tips
#1.try...except...无法捕捉SyntaxError（语法错误）和IndentationError（缩进错误）
#原因是只能捕捉程序运行时发生的错误，而这两种错误发生在程序运行之前
#捕捉SyntaxError的方法:使用exec('python code')，让错误发生在程序运行时
try:
    exec('print a')#exec(str)执行字符串str中的python代码
except Exception as errorinfo:
    print(errorinfo)

try:
    exec("print('%d' % a = 1 )")#use " to pari with " and ' to pair with ' so that no misunderstanding is occurred
                                #By the way, in C, code string inside exec() function is allowed.
except Exception as errorinfo:
    print(errorinfo)
