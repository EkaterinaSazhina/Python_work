#Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input("Введите трехзначное число: "))
res = n % 10 + ((n - (n % 10)) //10) % 10 + n // 100
print(res)
