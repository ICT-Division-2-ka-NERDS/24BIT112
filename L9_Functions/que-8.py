def convert(s):
    s = set(s.split())
    return " ".join(sorted(s))
print(convert("apple mango pineapple banana cheery strawberry"))