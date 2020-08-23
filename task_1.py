# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

#1 Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков

import random
import timeit

SIZE = 200
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
#вар1
def variant1():
 index_num = -1
 i=0
 while i < len(array):
     if array[i] < 0 and index_num == -1:
        index_num = i
     elif array[i] < 0 and array[i] > array[index_num]:
        index_num = i
     i += 1
 return index_num
idx1=variant1()
print(f'1. Максимальный отрицательный элемент {array[idx1]} : позиция {idx1}')

#вар2
def variant2():
 i = 0
 min_value = 1
 while i < len(array):
     if array[i] < 0 and min_value>array[i]:
         min_value = array[i]
     i += 1
 max_value=min_value
 max_value_index=0
 i=0
 while i<len(array):
     if array[i]<0 and array[i]>max_value:
         max_value=array[i]
         max_value_index=i
     i+=1
 return max_value_index
idx2=variant2()
print(f'2. Максимальный отрицательный элемент {array[idx2]} : позиция {idx2}')

#вар3
def variant3():
 def max_value(index_n, current_index):
     if current_index==len(array):
         return index_n
     if array[current_index] < 0 and index_n == -1:
         return max_value(current_index,current_index+1)
     elif array[current_index] < 0 and array[current_index] > array[index_n]:
         return max_value(current_index, current_index+1)
     return max_value(index_n, current_index+1)

 idx=max_value(-1,0)
 return idx
idx3=variant3()
print(f'3. Максимальный отрицательный элемент {array[idx3]} : позиция {idx3}')

print(timeit.timeit('variant1()', number=1000, globals=globals())) #0.155975297
print(timeit.timeit('variant2()', number=1000, globals=globals())) #0.22324582399999998
print(timeit.timeit('variant3()', number=1000, globals=globals())) #0.17464302399999998