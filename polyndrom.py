# Палиндром — это строка, которая читается одинаково слева направо и справа налево.
# На вход программе подается строка.
# Программа должна работать за O(n/2) без выделения лишней памяти.
def is_palindrom(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True

input_word = input("Введите слово: ")
if is_palindrom(input_word):
    print(f"Слово '{input_word}' является палиндромом.")
else:
    print(f"Слово '{input_word}' не является палиндромом.")
