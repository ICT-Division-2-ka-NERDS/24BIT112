class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

d1 = Date(15, 4, 2025)
d2 = Date(15, 4, 2025)
print(d1 == d2)