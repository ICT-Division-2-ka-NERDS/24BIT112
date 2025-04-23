class String:
    def __init__(self, text):
        self.text = text
    def __iadd__(self, other):
        self.text += other.text
        return self
    def toLower(self):
        self.text = self.text.lower()
    def toUpper(self):
        self.text = self.text.upper()
    def __str__(self):
        return self.text

s1 = String("Hello")
s2 = String("World")
s1 += s2
print(s1)
s1.toLower()
print(s1)
s1.toUpper()
print(s1)