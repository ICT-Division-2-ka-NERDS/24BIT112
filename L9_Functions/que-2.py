def compute(num):
    num = str(num)
    return int(num) + int(num*2) + int(num*3) + int(num*4)
n = int(input("Enter a number : "))
print(compute(n))