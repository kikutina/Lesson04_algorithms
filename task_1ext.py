# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

#1 Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков

import random
import timeit
import cProfile

#вар1
def variant1(SIZE):
 MIN_ITEM = -100
 MAX_ITEM = 100
 array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(array)
 index_num = -1
 i=0
 while i < len(array):
     if array[i] < 0 and index_num == -1:
        index_num = i
     elif array[i] < 0 and array[i] > array[index_num]:
        index_num = i
     i += 1
 #print(f'1. Максимальный отрицательный элемент {array[index_num]} : позиция {index_num}')
 return index_num

#вар2
def variant2(SIZE):
 MIN_ITEM = -100
 MAX_ITEM = 100
 array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
 #print(array)
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
 #print(f'2. Максимальный отрицательный элемент {array[max_value_index]} : позиция {max_value_index}')
 return max_value_index

#вар3
def variant3(SIZE):
 MIN_ITEM = -100
 MAX_ITEM = 100
 array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
 #print(array)
 def max_value(index_n, current_index):
     if current_index==len(array):
         return index_n
     if array[current_index] < 0 and index_n == -1:
         return max_value(current_index,current_index+1)
     elif array[current_index] < 0 and array[current_index] > array[index_n]:
         return max_value(current_index, current_index+1)
     return max_value(index_n, current_index+1)

 idx=max_value(-1,0)
 #print(f'3. Максимальный отрицательный элемент {array[idx]} : позиция {idx}')
 return idx

#variant1(20)
#variant2(20)
#variant3(20)
print(timeit.timeit('variant1(100)', number=1000, globals=globals())) #0.299326787
print(timeit.timeit('variant2(100)', number=1000, globals=globals())) #0.31771341500000005
print(timeit.timeit('variant3(100)', number=1000, globals=globals())) #0.33802098199999997
print(timeit.timeit('variant1(200)', number=1000, globals=globals())) #0.567291338
print(timeit.timeit('variant2(200)', number=1000, globals=globals())) #0.6191470210000001
print(timeit.timeit('variant3(200)', number=1000, globals=globals())) #0.6030091870000001
print(timeit.timeit('variant1(400)', number=1000, globals=globals())) #1.15661447
print(timeit.timeit('variant2(400)', number=1000, globals=globals())) #1.2713514260000003
print(timeit.timeit('variant3(400)', number=1000, globals=globals())) #1.309700661
print(timeit.timeit('variant1(800)', number=1000, globals=globals())) #2.3265352549999996
print(timeit.timeit('variant2(800)', number=1000, globals=globals())) #2.5165081659999995
print(timeit.timeit('variant3(800)', number=1000, globals=globals())) #2.6680206559999995

cProfile.run('variant1(800)')
#5037 function calls in 0.004 seconds

   #Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
  #    800    0.001    0.000    0.002    0.000 random.py:200(randrange)
  #    800    0.001    0.000    0.003    0.000 random.py:244(randint)
  #    800    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
  #      1    0.001    0.001    0.004    0.004 task_1ext.py:14(variant1)
  #      1    0.001    0.001    0.003    0.003 task_1ext.py:17(<listcomp>)
  #      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
  #    801    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  #    800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #   1031    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('variant2(800)')
#         5834 function calls in 0.005 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #     1    0.000    0.000    0.005    0.005 <string>:1(<module>)
   #   800    0.001    0.000    0.002    0.000 random.py:200(randrange)
   #   800    0.001    0.000    0.003    0.000 random.py:244(randint)
   #   800    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
   #     1    0.001    0.001    0.005    0.005 task_1ext.py:31(variant2)
   #     1    0.001    0.001    0.003    0.003 task_1ext.py:34(<listcomp>)
   #     1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
   #  1602    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #   800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
   #     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #  1027    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



cProfile.run('variant3(800)')
#         5829 function calls (5029 primitive calls) in 0.006 seconds

 #  Ordered by: standard name

 #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #       1    0.000    0.000    0.006    0.006 <string>:1(<module>)
 #     800    0.001    0.000    0.002    0.000 random.py:200(randrange)
 #     800    0.001    0.000    0.003    0.000 random.py:244(randint)
 #     800    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
 #       1    0.000    0.000    0.006    0.006 task_1ext.py:54(variant3)
 #       1    0.001    0.001    0.004    0.004 task_1ext.py:57(<listcomp>)
 #   801/1    0.002    0.000    0.002    0.002 task_1ext.py:59(max_value)
 #       1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
 #     801    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 #     800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
 #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 #    1022    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



# вар 1, вар 2 и вар 3 по времени обработки не сильно разняться, но при использавание вар 3, при увеличении
# колличества иттераций, может привести к переполнению стека. Вар 1 и Вар2 имеют схожие "кривые
# на графике" при увеличении иттераций, но вар 1 чуть быстрее проводит обработку.
