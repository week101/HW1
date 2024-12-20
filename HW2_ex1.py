def proverka(s):
    skoba = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for char in s:
        if char in skoba:
            top_element = stack.pop() if stack else None

            if skoba[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(proverka("(({[]}))"))
print(proverka("{(})"))       
print(proverka("([])[[]]"))   
print(proverka(")())[[]]"))    
print(proverka("(())[[]]"))    
print(proverka("([])"))        