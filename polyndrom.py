# Палиндром — это строка, которая читается одинаково слева направо и справа налево.
# На вход программе подается строка.
# Программа должна работать за O(n/2) без выделения лишней памяти.
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

input_word = input("Введите слово: ")

if is_palindrome(input_word):
    print(f"Слово '{input_word}' является палиндромом.")
else:
    print(f"Слово '{input_word}' не является палиндромом.")