#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = ((number * -1) % 10)
    else:
        last = number % 10

    print(f"{last}", end="")
    return last


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
