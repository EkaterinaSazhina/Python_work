'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.

10 -> 1 2 4 8
'''

number = int(input('Введите число: '))
k = 1
while k <= number:
        print(k, end=' ')
        k *= 2