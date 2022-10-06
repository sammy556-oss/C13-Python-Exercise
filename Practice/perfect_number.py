number = int(input("Enter a number"))
total = 0
for num in range(1, number):
    if num % number == 0:
        total += num
