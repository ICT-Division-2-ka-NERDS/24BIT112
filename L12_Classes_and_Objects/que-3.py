class Solid:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)
    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

s = Solid(3, 7)
print(s.surface_area())
print(s.volume())