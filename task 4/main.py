import math
x=int(input("Введите значение x:"))
y=int(input("Введите значение y:"))
z=int(input("Введите значение z:"))
b= (math.sqrt(10*(math.pow(x,1/3)+math.pow(x,y+2))))*(pow(math.asin(z),2)-abs(x-y))
print(b)