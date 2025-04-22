def ispalindrome(s):
    for i in range(len(s) // 2):
        if (s[i] != s[len(s) - i - 1]):
            return 1
st = input("Enter a string : ")
if ispalindrome(st):
    print("Entered string is not palindrome.")
else :
    print("Entered string is palindrome.")