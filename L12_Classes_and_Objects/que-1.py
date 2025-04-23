class Mycomplex():
    def __init__(self,real,image):
        self.r = real
        self.i = image
    def addition(self,c2):
        ob3 = Mycomplex(0, 0)
        ob3.r = self.r + c2.r
        ob3.i = self.i + c2.i
        return ob3
    def substraction(self,c2):
        ob4 = Mycomplex(0, 0)
        ob4.r = self.r - c2.r
        ob4.i = self.i - c2.i
        return ob4
    def multiplication(self,c2):
        ob5 = Mycomplex(0, 0)
        ob5.r = (self.r * c2.r) - (self.i * c2.i)
        ob5.i = (self.r * c2.i) + (self.i * c2.r)
        return ob5
    def division(self,c2):
        ob6 = Mycomplex(0, 0)
        dem = (self.r * c2.r) + (self.i * c2.i)
        ob6.r = ((self.r * c2.r) - (self.i * c2.i)) / dem
        ob6.i = ((self.r * c2.i) + (self.i * c2.r)) / dem
        return ob6
    def printN(self):
        print(self.r,"+ j",self.i)
ob1 = Mycomplex(10, 20)
ob1.printN()
ob2 = Mycomplex(15, 12)
ob2.printN()
ob1.addition(ob2).printN()
ob1.substraction(ob2).printN()
ob1.multiplication(ob2).printN()
ob1.division(ob2).printN()