#time模块
import time
#时间戳:time.time()返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
print('当前时间戳为',time.time())
#时间元组：很多Python函数用一个元组装起来的9组数字处理时间。
#当前时间获取:
# 1.time.localtime([sec]):时间戳转换成时间元组。接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（时间元组中的t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。如果sec参数未输入，则以当前时间为转换标准。
localtime = time.localtime(time.time())
print('当前时间：',localtime)
print("返回类型 :", type(localtime))
#特定字段的获取。即只获取时间元组中的某一项(例如年等)。

print('当前年份',localtime[0],localtime.tm_year)
#2.time.gmtime([sec]):接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0。如果sec参数未输入，则以当前时间为转换标准。
print('当地格林威治天文时间',time.gmtime())
#逆操作:time.mktime(t)接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError。
#t -- 结构化的时间或者完整的9位元组元素。
print('mktime()方法返回的时间戳 %.6f' % time.mktime(time.localtime()))
print('某日期时间戳%.6f' % time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0)))
print('将格式化时间转化为时间戳%.6f' % time.mktime(time.strptime('2020年08月07日 Friday 10:15:24','%Y年%m月%d日 %A %H:%M:%S')))#time.strptime(str,format)将格式化时间转换为时间元组，参数为格式化时间和格式

#3.获取格式化的时间
#最简单的方法:time.asctime(time_struct)
localtime1 = time.asctime(time.localtime(time.time()))
print(localtime1)
#生成自定义的格式化时间:time.strftime(format[,t])
localtime2 = time.strftime('%Y年%m月%d日 %A %H:%M:%S',time.localtime())
print(localtime2)

#日期模块
import calendar
#calendar.month(year,month,w,l)返回某年某月的月历
#其中w代表日之间的间隔，l表示每周占的行数(高度)
calendar1 = calendar.month(2020,8,w=3,l=2)
print(calendar1)
#calendar.calendar(year,w,l,)返回某年的年历
calendar2 = calendar.calendar(2020,w=2,l=1,c=6)
#其中w代表日之间的间隔，l表示每周占的行数(高度)，c表示每个月之间相隔的距离
print(calendar2)

#tips
#time.sleep(t)函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
time.sleep(2)
print('暂停2s后输出')
#判断闰年平年:calendar.isleap()
print(calendar.isleap(1900))

#测试程序运行时间
def procedure():
    time.sleep(2)
#1.time.perf_counter()返回性能计数器的值（以小数秒为单位）作为浮点数，即具有最高可用分辨率的时钟，以测量短持续时间。 它确实包括睡眠期间经过的时间，并且是系统范围的。
t0 = time.perf_counter()
procedure()
print (time.perf_counter() - t0)
#2.time.process_time()返回当前进程的系统和用户CPU时间总和的值（以小数秒为单位）作为浮点数。不包括sleep()休眠时间期间经过的时间。
t0 = time.process_time()
procedure()
print (time.process_time() - t0)