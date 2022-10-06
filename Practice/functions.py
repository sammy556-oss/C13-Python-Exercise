def cube(a, b):
    square = pow(a, b)
    return square


def name():
    my_name = input("enter your name")
    print(f"Hello{my_name}")


name()

base = int(input("Enter the base :"))
exponent = int(input("Enter the exponent :"))
power = cube(base, exponent)
print(f"{base} raised to the power {exponent} is : {power}")


def celsius(c):
    f = c * 9 / 5 + 32
    return f


def fahrenheit(f):
    c = (f - 32) * 5 / 9
    return c


degree = float(input("Enter celsius to covert :"))
result = celsius(degree)
print(f"{degree} degree C = {result} degree F")

degree = float(input("Enter fahrenheit to covert :"))
result = fahrenheit(degree)
print(f"{degree} degree F = {result:.2f} degree C")
