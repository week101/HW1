#1
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
#2
def resolve_collision(hash_table, key, value):
    if key not in hash_table:
        hash_table[key] = []
    hash_table[key].append(value)
#3
def count_strings():
    return 2 ** 6 - 2 ** 5  # 32 возможных строк
#4
matrix = [[j for j in range(6)] for i in range(4)]
#5
nums = list(range(1, 11))
squares = list(map(lambda x: x ** 2, nums))
#6
strings = [f"{num}!" for num in nums]
#7
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
#8
def long_strings(strings):
    for string in strings:
        if len(string) > 3:
            yield string
#9
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            if not isinstance(merged[key], list):
                merged[key] = [merged[key]]
            merged[key].append(value)
        else:
            merged[key] = value
    return merged
#10
def unique_letters(string):
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            yield char
#11
def square_roots():
    while True:
        num = yield
        if num >= 0:
            yield num ** 0.5