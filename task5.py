#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Введите Х координату первой точки:'))
y1 = float(input('Введите У координату первой точки:'))
x2 = float(input('Введите Х координату второй точки:'))
y2 = float(input('Введите У координату второй точки:'))
d = ((((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5)
print(f'Расстояние между точками: {d:.2f}')   
  