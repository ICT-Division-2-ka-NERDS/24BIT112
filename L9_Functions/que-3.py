def creat_array(a,b,c,n):
    ele = 1
    l1 = []
    for i in range(a):
        l2 = []
        for j in range(b):
            l3 = []
            for i in range(c):
                l3.append(ele)
                ele += 1
            l2.append(l3)
        l1.append(l2)
    return(l1)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
n = int(input("Enter n : "))
print(creat_array(a,b,c,n))