def ispangram(s):
    alpha = set(chr(i) for i in range(65,123) if chr(i).isalpha())
    if (set(s) <= alpha):
        print("Entered string is pangram.")
    else :
        print("Entered string is not pangram.")
st = input("Enter a string : ")
ispangram(st)