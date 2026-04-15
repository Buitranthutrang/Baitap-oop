import math
class Point:
    def __init__(self, a=0.0, b=0.0):
        self.a = a
        self.b = b

class Rectangle:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner   
        self.width  = width
        self.height = height

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.a - p2.a)**2 + (p1.b - p2.b**2))

def point_in_circle(circle: Circle, point: Point) -> bool:
    """True nếu điểm nằm trong hoặc trên vòng tròn."""
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    """True nếu HCN nằm hoàn toàn trong/trên vòng tròn."""
    c = rect.corner
    corners = [
        Point(c.a,              c.b),
        Point(c.a + rect.width, c.b),
        Point(c.a,              c.b + rect.height),
        Point(c.a + rect.width, c.b + rect.height),
    ]
    return all(point_in_circle(circle, p) for p in corners)

def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    """True nếu bất kỳ góc nào của HCN nằm trong vòng tròn."""
    c = rect.corner
    corners = [
        Point(c.a,              c.b),
        Point(c.a + rect.width, c.b),
        Point(c.a,              c.b + rect.height),
        Point(c.a + rect.width, c.b + rect.height),
    ]
    return any(point_in_circle(circle, p) for p in corners)