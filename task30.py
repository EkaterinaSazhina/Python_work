#Заполните массив элементами арифметической
#прогрессии. Её первый элемент, разность и количество
#элементов нужно ввести с клавиатуры. Формула для
#получения n-го члена прогрессии: a
#n= a1+ (n-1) * d.
a1 = 2
d = 3
n = 4
for i in range(n):
    print(a1 + i * d)