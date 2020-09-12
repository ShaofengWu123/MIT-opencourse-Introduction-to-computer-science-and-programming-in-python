import 排序算法
import random

list = []
for i in range(0,5):
    list.append(random.randint(0,30))
print('Original list',list)

排序算法.bubble_sort(list)
print('Sorted list:',list,'\n')

#1.O(logn):logarithmic complexity
#e.g. Bisection search/binary search/二分法查找
def binary_search(list_sorted,num):
    """二分法在有序列表里查找元素"""
    if len(list_sorted) == 1:
       if num == list_sorted[0]:
           return True
       else:
           return False
    if len(list_sorted) == 2:
       if num == list_sorted[0]:
           return True
       elif num == list_sorted[1]:
           return True
       else:
           return False
    else :
       mid = len(list_sorted)//2
       if num < list_sorted[mid]:
           return binary_search(list_sorted[0:mid+1],num)#二分法要注意这里递归传递的列表的长度，包不包含中间元素要自己斟酌，否则可能无限递归
       elif num > list_sorted[mid]:
           return binary_search(list_sorted[mid:],num)
       else:
           return True
#思考：上面这种算法复杂度是0(logn)吗？ 不是！因为总共要进行logn次递归，而每次递归要对列表进行复制所以是O(nlogn)（实际上考虑到每次复制的下次复制
#列表的长度减半，所以复杂度应该是(1+1/2+...+1/2^k)n，其中k=logn，计算结果为n-1 = O(n)）

num = random.randint(0,30)
print('{0} in list?: {1}'.format(num,binary_search(list[::],num)),'\n')

#复杂度为O(logn)的二分法查找
def binary_search2(list_sorted,start,end,num):
    """二分法在有序列表里查找元素"""
    #Base cases
    if start == end:
        if list_sorted[start] == num:
            return True
        else:
            return False
    if end - start == 1:
       if num == list_sorted[start] or num == list_sorted[end]:
            return True
       else:
            return False
    else:
        mid = (start + end)//2
        print('三个索引分别是',start,mid,end)
        if num > list_sorted[mid]:
            return binary_search2(list_sorted,mid,end,num)
        elif num < list_sorted[mid]:
            return binary_search2(list_sorted,start,mid,num)
        else:
            return True

print('{0} in list?: {1}'.format(num,binary_search2(list[::],0,len(list)-1,num)))

#2.O(n):linear complexity
#e.g.iteration
def iteration_sum(num):
    """对1到num的数字求和"""
    if num == 1:
        return num
    return num+iteration_sum(num-1)

print('Iteration result:',iteration_sum(10))

#3.O(nlogn),log-linear complexity
print('Merge sort:',排序算法.merge_sort(list[::]))

#4.O(n^x),polynnominal complexity,二次方叫做quadratic complexity
#Typical cases:nested loop or recursive function calls
def intersect(l1,l2):
    tmp = []
    for i in l1:
        for j in l2:
            if (i == j) and (i not in tmp):
                tmp.append(i)
            else:
                pass
    return tmp

#初始化两个用于交集运算的列表
l1 = []
l2 = []
for i in range(0, random.randint(0, 10)):
    l1.append(random.randint(0, 30))
for i in range(0, random.randint(0, 10)):
    l2.append(random.randint(0, 30))

print('Intersection of {0} and {1}:'.format(l1,l2))
print(intersect(l1,l2))

#5.O(e^x),expoential complexity
#Typical cases:multiple recursive calls(Towers of Hanoi,find subset)，分析复杂度的方法，递推公式tn = constant*tn-1+Sn
#Quesition 1.Find all subset:用递归的方法找一个集合的所有子集，只需要考虑已知去掉一个元素的集合所有子集，在这些子集的基础上加上这些子集加一个
# 元素的所有集合就解决了问题
def find_subset(list):
    """找到一个集合（用列表表示）所有子集的数量，为了方便不输出所有子集"""
    list_length = len(set(list))
    def subset_amount(n):
        if n == 0:
            return 1
        else:
            return 2*subset_amount(n-1)
    return subset_amount(list_length)

print('{0}的子集数量：{1}'.format(list,find_subset(list)))

#Question 2.Hanoi Tower:用递归方法解决这个问题，要把n从left移到right，那么就要先把n-1从left移到mid，然后把1从left移到right，然后把n-1
# 从mid移到right。tn = 2tn-1 + 1
def Tower(n,l,m,r):
    """计算Hanoi塔移动次数（primitive operation），其中l,m,r参数用于表明正在从哪个底座转移到哪个底座，可以加入输出功能将其输出"""
    if n == 1:
        return 1
    else:
        return Tower(n-1,l,r,m)+Tower(1,l,m,r)+Tower(n-1,m,l,r)

n = random.randint(1,20)
print('{0}层Hanoi塔需要移动{1}次'.format(n,Tower(n,'left','middle','right')))


