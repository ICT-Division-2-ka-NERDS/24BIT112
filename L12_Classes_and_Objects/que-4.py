class Shape:
    def __init__(self, side):
        self.side = side
    def perimeter(self, sides):
        return self.side * sides
    def area(self):
        return self.side ** 2

s = Shape(7)
print(s.perimeter(4))
print(s.area())