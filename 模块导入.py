import time #导入模块
print(time.localtime())
import time as t #导入模块并简写
print(t.localtime())
from time import localtime #导入模块中部分方法
print(localtime())#只导入了localtime()方法，使用from import后time.可省略
from time import *
print(time())#*代表所有方法，此时可省略time.