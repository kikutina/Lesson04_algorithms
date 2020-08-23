# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
import timeit
import cProfile

#Первый — без использования «Решета Эратосфена».
def prime_num(x):
    lis= []
    lis.append(1)

    idx=1
    i=2
    while True:
        if idx > x:
            #print(lis)
            return lis[idx - 1]
        v=False
        for z in range(2, i):
            if i % z == 0:
                v=True
                break
        if not v:
          lis.append(i)
          idx+=1
        i+=1
print(prime_num(4))
#Второй — с помощью алгоритма «Решето Эратосфена».
def prime_num_eras(x):
    lis= []
    lis.append(1)

    idx=1
    i=2
    while True:
        if idx > x:
            #print(lis)
            return lis[idx - 1]
        v=False
        for z in range(1, idx):
            if i % lis[z] == 0:
                v=True
                break
        if not v:
          lis.append(i)
          idx+=1

        i+=1

print(prime_num_eras(4))

#print('For i=10 NoErastofen ', timeit.timeit('prime_num(10)', number=1000, globals=globals())) #0.03088727599999999
#print('For i=10 Erastofen ', timeit.timeit('prime_num_eras(10)', number=1000, globals=globals())) #0.028124178999999985
#print('For i=100 NoErastofen ', timeit.timeit('prime_num(100)', number=1000, globals=globals())) #3.325155987
#print('For i=100 Erastofen ', timeit.timeit('prime_num_eras(100)', number=1000, globals=globals())) #1.4483760959999996
#print('For i=1000 NoErastofen ', timeit.timeit('prime_num(1000)', number=1000, globals=globals())) #559.915193556
#print('For i=1000 Erastofen ', timeit.timeit('prime_num_eras(1000)', number=1000, globals=globals())) #114.53128896800001

#cProfile.run('prime_num(200)')
#204 function calls in 0.016 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.016    0.016 <string>:1(<module>)
    #    1    0.016    0.016    0.016    0.016 task_2.py:8(prime_num)
    #    1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
    #  200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('prime_num_eras(200)')
#204 function calls in 0.005 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.005    0.005 <string>:1(<module>)
    #    1    0.005    0.005    0.005    0.005 task_2.py:27(prime_num_eras)
    #    1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
    #  200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# алгоритм с переменением "Решета Эратосфена" работает эвффективнее.