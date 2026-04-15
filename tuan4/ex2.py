import math

class Point:
    """Lớp Point biểu diễn một điểm trong mặt phẳng tọa độ."""
    def __init__(self, x=2, y=-3):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"P({self.x}; {self.y})"

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(6, -2)
            self.__d2 = Point(-4, 3)

        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            src = args[0]
            self.__d1 = Point(src.getD1().x, src.getD1().y)
            self.__d2 = Point(src.getD2().x, src.getD2().y)

        else:
            raise ValueError("Sai tham số đầu vào!")

    # Getter / Setter
    def getD1(self):
        return self.__d1

    def getD2(self):
        return self.__d2

    def setD1(self, d1):
        self.__d1 = d1

    def setD2(self, d2):
        self.__d2 = d2

    # Phương thức tiện ích
    def length(self):
        dx = self.__d1.x - self.__d2.x
        dy = self.__d1.y - self.__d2.y
        return math.sqrt(dx**2 + dy**2)

    def hienThi(self):
        print(f"Doan thang: {self.__d1} --> {self.__d2}")