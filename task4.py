#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
#они сделали S журавликов. Сколько журавликов сделал каждый
#ребенок, если известно, что Петя и Сережа сделали одинаковое
#количество журавликов, а Катя сделала в два раза больше журавликов,
#чем Петя и Сережа вместе?
col=int(input("Сколько журавликов сделали дети вместе?: "))
x= col / 6
y = 2 * (x + x)
z=x
print(int(x),int(y),int(z))