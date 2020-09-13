import math
#列表嵌套实现3*4矩阵
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#将上述矩阵转换成4*3矩阵
#方法1：列表推导式
matrix2 = [ [x[i] for x in matrix] for i in range(4) ]
print(matrix2)
#方法2:循环语句和append()方法
matrix2 = []
for i in range(4):
    matrix_tempo = []
    for x in matrix:
        matrix_tempo.append(x[i])
    matrix2.append(matrix_tempo)
print(matrix2)