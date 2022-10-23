# Напишите функцию, которая будет принимать координаты
# двух точек (в двумерной декартовой системе координат)
# возвращать расстояние между этими точками.
import math
def distance(coordinates):
    l = coordinates.split(',')
    return round(math.hypot(int(l[2])-int(l[0]), int(l[3])-int(l[1])),2)

print(distance("1,1,2,1"))
print(distance("1,1,3,1"))
print(distance("-5,1,3,1"))
print(distance("-5,2,3,1"))

def shortestDistance(txt):
    a, b, c, d = map(int, txt.split(","))
    return round(((c - a) ** 2 + (d - b) ** 2) ** 0.5, 2)


import math
def shortestDistance(txt):
    x1, y1, x2, y2 = (int(num) for num in txt.split(','))
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)