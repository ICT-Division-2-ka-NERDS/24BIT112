class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)
    def display(self):
        print(f"{self.hours}h {self.minutes}m")

t1 = Time(3, 56)
t2 = Time(1, 25)
t3 = t1.add(t2)
t3.display()