def tpl(num):
    l = [(i,i**2,i**3) for i in range(1,num+1)]
    return l
print(tpl(5))