"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

time_1 = timeit('func_1(range(50))', globals=globals())
print(f'время выполнения функции: {time_1}')


def func_2(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]


time_2 = timeit('func_2(range(50))', globals=globals())
print(f'время выполнения оптимизированной функции: {time_2}')


'''
время выполнения функции: 5.3306213999167085
время выполнения оптимизированной функции: 2.721817099954933

list comprehension гораздо быстрее заполняет список и выглядит более лаконично!
'''