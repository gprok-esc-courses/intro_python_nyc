# 2. Integer Info
# Ask user to give a positive integer.
# Find and print
# a) The biggest digit in the integer. b) The sum of all digits. c) The number of digits. d) The average of digits.
# NOTE: Do not convert the integer to string.
# Example:
# Give a positive integer: 4728 
# Max digit: 8
# Sum: 21
# Digits: 4
# Average: 5.25

num = int(input("Give a positive number: "))

if num < 0:
    print("Number must be positive")
else:
    max = 0
    total = 0
    size = 0
    while num > 0:
        d = num % 10
        total = total + d 
        size = size + 1
        if max < d:
            max = d
        num = num // 10
    
    print(f"MAX: {max}")
    print(f"TOTAL: {total}")
    print(f"SIZE: {size}")
    print(f"AVERAGE: {total/size}")
          
