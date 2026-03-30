# cau 1
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p1):
        return math.sqrt((self.x - p1.x) ** 2 + (self.y - p1.y) ** 2)
A=Point(3, 4)
x=int(input("Enter Bx: "))
y=int(input("Enter By: "))
B=Point(x, y)
C=Point(-1*x, -1*y)
O=Point(0, 0)
print("Distance from A to B: ", A.distance(B))
print("Distance from B to O: ", B.distance(O))