def count_lower_upper(s):
    count = {"Lower":0,"Upper":0}
    for ele in s:
        if ele.islower():
            count["Lower"] += 1
        elif ele.isupper():
            count["Upper"] += 1
    print(count)
st = input("Enter a string : ")
count_lower_upper(st)