def capitalize(word):
    first_lower = word[0]
    return first_lower.upper() + word[1:]
word = input()
print(capitalize(word))
