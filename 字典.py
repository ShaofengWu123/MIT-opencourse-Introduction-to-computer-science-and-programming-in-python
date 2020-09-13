import math
import random
#字典的创建方法
dic1 = {x: x**2 for x in range(1,4) }
dic2 = {'key1':1, 'key2': 'abc', 'key3': [1,2,3]}
dic3 = dict([('fruit','apple'),('vegetable','tomato'),('food','bread')]) #用键值对list直接以及dict函数创建字典，要注意list中键值对的写法(key,value)
dic_hubei = {'shiyan':{'shiyanzhan': 1,'shiyandong':2}
    ,'xiangyang':{'xiangyangzhan':1,'xiangyangdong':2}
    ,'wuhan':{'hankouzhan':1,'wuhanzhan':2,'wuchangzhan':1}}
print('湖北省某些城市铁路站',dic_hubei)#字典的嵌套
print(dic_hubei['shiyan']['shiyandong'])
#key必须是不可修改的数据类型，value可以是任何数据类型

#字典内置函数
print('元素个数',len(dic1))
print('输出字典，以可打印的字符串表示',str(dic1))
print('种类',type(dic1),type(str(dic1)))
#字典内置方法
#dic.clear()清空字典，无返回值
print('原字典',dic1)
dic1.clear()
print('清空后字典',dic1)
#dic.copy()返回一个字典的浅复制
dic4 = {'david':180,'john':200,'cathy':165}
dic5 = dic4
dic6 = dic4.copy()
dic4['david'] = 185
print(dic4)
print(dic5)
print(dic6)
#dict.fromkeys(seq[,value])返回一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值，默认为None。
names = ['david','mike','jonh']
ages = [18,19,20]
dic_names = dict.fromkeys(names,ages)
print('字典为：%s' % str(dic_names))

test = 'xiao jian zhi'
test1 = dict.fromkeys(test,10)
print('小健至',test1)
for i in test1.keys():
    print(i)
#dict.get(key,default=None)返回指定键的值，如果值不在字典中返回默认值。
#用key查找value
dic_names = {'wsf':100,'cjy':99,'aa':20,'bb':60}
print(dic_names.get(input('Name:'),'NA'))#可以代替if语句判断
#用value查找key
dic_names = {'wsf':100,'cjy':99,'aa':20,'bb':60}
score = input('please input score:')
index = list(dic_names.values()).index(float(score))
a = list(dic_names.keys())[list(dic_names.values()).index(float(score))]
print(a)
#dict.setdefault(key,default=None)如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None
print(dic_names.setdefault('ysn','NA'))
print('更新后dic_names',dic_names)
#dict.update(dict2)把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里，无返回值。
dic_names2 = {'wyc':100,'tjz':100,'yxy':100}
dic_names.update(dic_names2)
print('补充dic_names2数据后的dic_names',dic_names)
#dict.pop(key,default)删除字典给定键 key 所对应的值，返回值为被删除值。key值必须给出。 否则，返回default值。如果key不在dict中，必须设置default的值，否则会报错。
print('删除aa对应的值',dic_names.pop('aa'))
print('删除后字典',dic_names)
print(dic_names.pop('wdf','No key'))
#dict.popitem()返回一个键值对(key,value)形式(tuple)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对，并删除此键值对。如果字典已经为空，却调用了此方法，就报出KeyError异常。
print(dic_names2.popitem())
print(type(dic_names2.popitem()))
print('删除一次',dic_names2)
print(dic_names2.popitem())
print('删除两次',dic_names2)
#key in dict in操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
print('wsf' in dic_names)#无需'wsf' in dic_names.keys()
print(100 in dic_names)
print(100 in dic_names.values())
#dict.items()以列表返回可遍历的(键, 值) 元组数组。
print('返回的元组数组',dic_names.items())
#print('类型',type(dic_names.items()),'dict_items类型不能访问元素',type(dic_names.items()[0]))
for i,j in dic_names.items():
    print(i.center(6,' '),j)#遍历的方法
#dict.keys()/dict.values()方法返回一个可迭代对象，可以使用 list() 来转换为列表。
print('名字列表',list(dic_names.keys()))
