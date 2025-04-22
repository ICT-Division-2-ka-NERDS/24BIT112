import random
L = [0]*50
for i in range(50):
    L[i] = random.randint(1,30)
print(L)
for i in range(len(L)):
    if (L.count(l[i]) > 1):
        L.remove()