n = int(input('Введите кол-во элементов в массиве: '))
lst = []
for i in range(n):
    number = lst.append(int(input(f"Введите {i+1}-е число в массив: ")))

x = int(input('Введите число X: '))
while(lst.count(x)!=0):
    x = int(input('Неверно! Число не должно содержаться в массиве! Введите число X: '))
smallestDiff=abs(lst[0]-x)
nearestElement=lst[0]
for j in lst:
    if abs(j-x)<smallestDiff:
        smallestDiff=abs(j-x)
        nearestElement=j
print(nearestElement)

    

