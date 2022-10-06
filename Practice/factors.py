factor = int(input("Enter an integer"))
for num in range(1, factor):
    if factor % num == 0:
        print(f"{num} is a factor of {factor}")
print(f"{factor} is a factor of {factor}")
