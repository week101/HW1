def print_reverse():
    number = int(input("Vvedite chislo (ne 0)"))
    if number == 0:
        return
    print_reverse()
    print(number)
print_reverse()