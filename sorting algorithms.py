import random

if __name__ == '__main__':
#对数字list排序
    list = []
    for i in range(0,5):
        list.append(random.randint(0,500))
    print('Original list',list)

#1.Monkey sort/穷举法
def is_sorted(list1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            return False
        else:
            i += 1
    return True

def monkey_sort(list):
    """A stupid sorting method. Complexity worst case O(infinite)"""
    sort_flag = False
    while not sort_flag:
        random.shuffle(list)
        if is_sorted(list):
            sort_flag = True
        else:
            pass
    return list

if __name__ == '__main__':
    print('Monkey sort:',monkey_sort(list[::]),'\n')

#2.Bubble sort/冒泡排序
def bubble_sort(list):
  """冒泡排序法/Bubble sort：Complexity O(n^2)"""#Note: Docstring of the function should have same identation with
                                               #following function body.(May raise IdentationError if not)
  # 在列表没有排序好之前，flag为False，重复进行一次冒泡排序，并在排序后判断是否排序好
  sort_flag = False
  while not sort_flag:
     for i in range(len(list)-1):
         if list[i] > list[i+1]:
             list[i],list[i+1] = list[i+1],list[i]
         else:
             pass
         i +=1
    #判断列表是否已经排序好
     if is_sorted(list):
         sort_flag = True

  return list

if __name__ == '__main__':
    print('Original list',list)
    print('Bubble sort:',bubble_sort(list[::]),'\n')

#3.Selection sort/选择排序
def selection_sort(list):
    """选择排序/Selection sort: Complexity O(n^2)"""
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[j] < list[i]:
                list[j],list[i] = list[i],list[j]
            else:
                pass
    return list

if __name__ == '__main__':
    print('Original list',list)
    print('Selection sort:',selection_sort(list[::]),'\n')

#4.Merge sort/归并排序
#错误过的地方：列表切片list[i,j]不包括list[j]
def merge(l1,l2):
    i,j= 0,0
    l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            l3.append(l2[j])
            j += 1
        else:
            l3.append(l1[i])
            i += 1
    if i == len(l1):
        l3.extend(l2[j:len(l2)])
    else:
        l3.extend(l1[i:len(l1)])
    return l3

def merge_sort(list):
    """归并排序/Merge sort: Comlexity: O(nlogn) 即要进行logn次合并排序，每次排序复杂度为len(l1)+len(l2)=O(n)"""
    if len(list) == 0 or len(list) == 1:
        return list[::]
    else:
        middle = len(list)//2
        prelist = merge_sort(list[0:middle])
        sulist =  merge_sort(list[middle:len(list)])
        return merge(prelist,sulist)

if __name__ == '__main__':
    print('Original list',list)
    print('Merge sort:',merge_sort(list[::]))

