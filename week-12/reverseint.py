# 1. Reverse Integer 
# Ask user to give a positive integer. Find and print the reverse integer. 
# Example:
# Give a positive integer: 4728
# Reverse integer: 8274
# Exceptions: If the integer is negative display an error. 
# NOTE: Do not convert the integer to string.

num = int(input("Give a positive number: "))

if num < 0:
    print("Number must be positive")
else:
    digits = []
    mult = 1
    rev = 0
    while num > 0:
        d = num % 10
        digits.append(d)
        num = num // 10
    for i in range(len(digits)-1, -1, -1):
        d = digits[i]
        rev = rev + (d * mult)
        mult = mult * 10
    print(digits)
    print(rev)
