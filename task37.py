# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def funk(num):
    number = input()
    if num == 1:
        return number
    return funk(num - 1) + ' ' + number


n = int(input('Введите число: '))
print(funk(n))