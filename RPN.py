def calculate_polish_notation(expression):
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }

    stack = []

    for token in expression.split():
        if token in operators:
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(int(token))

    return stack.pop()

expression = "5 8 + 3 2 + /"
result = calculate_polish_notation(expression)
print(f'Результат выражения "{expression}" равен {result}')