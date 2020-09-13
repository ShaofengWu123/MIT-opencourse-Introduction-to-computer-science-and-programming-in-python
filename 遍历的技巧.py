import math
#序列遍历：enumerate()函数同时得到索引值和对应值。
for i,j in enumerate(['David','John','Harry']):
    print('排名1：%s 同学的排名是 %s' %(j,i+1))
#反向遍历:reversed()函数
for i,j in enumerate(reversed(['David','John','Harry'])):
    print('排名2：%s 同学的排名是 %s' %(j,i+1))
#顺序遍历:sorted()返回一个已经排序的序列，并且不改变原来的序列
for i,j in enumerate(sorted(['David','John','Harry'])):
    print('排名3：%s 同学的排名是 %s' %(j,i+1))
for i,j in enumerate('ABCDEFG'):
    print('字母 %s 的顺序是 %s' %(j,i+1))

#多序列遍历:zip()函数组合不同序列。
for i,j in zip(['David','John','Marry'],['Shaofeng','Jianzhi','Xueya']):
    print('English name:{0}\t  Chinese name:{1}'.format(i,j))
#更多例子
l1 = [1,2,3]
l2 = ['a','b','c']
l3 = ['A','B','C']
for i,j,k in zip(l1,l2,l3):
    print(i,j,k)

print(zip(l1,l2,l3))#type返回的是zip object
print(type(zip(l1,l2,l3)))#type返回的是zip object
print(list(zip(l1,l2,l3)))

#字典的键值遍历:dict.items()返回键值对序列
dict1 = dict([('Apple',1),('Orange',2),('Pear',3)])
for i,j in dict1.items():
    print('销量排名:{0}  水果种类:{1}'.format(j,i))
#对比输出结果
for i in dict1.items():
    print('水果种类和销量排名',i)#i为键值对