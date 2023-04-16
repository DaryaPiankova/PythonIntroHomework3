n = int(input('Введите кол-во элементов в массиве: '))
lst = []
for i in range(n):
    number = lst.append(int(input(f"Введите {i+1}-е число в массив: ")))
x = int(input('Введите число, кол-во которого надо посчитать в массиве: '))
print(lst.count(x))
