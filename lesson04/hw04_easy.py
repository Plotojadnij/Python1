# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

try:
    list1 = list(map(int,input("Введите числа через пробел: ").split()))
    list2 = [i ** 2 for i in list1]
    print(list2)
except ValueError:
    print("В исходном списке должны быть числа!")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = input("Введите фрукты через пробел: ").split()
fruits2 = input("Введите фрукты через пробел: ").split()

fruits3 = [i for i in fruits1 if i in fruits2]
print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

try:
    list1 = list(map(int,input("Введите числа через пробел: ").split()))
    list2 = [i for i in list1 if (i%3 == 0) and (i >= 0) and (i%4 != 0)]
    print(list2)
except ValueError:
    print("В исходном списке должны быть числа!")