class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    def __add__(self, other):
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def __mul__(self, other):
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])
    def display(self):
        for row in self.data:
            print(row)

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m1.__add__(m2).display()
print()
m1.__mul__(m2).display()
print()
m1.transpose().display()