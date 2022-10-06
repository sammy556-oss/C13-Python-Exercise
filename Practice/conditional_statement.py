# print(("good" != "bad") and not (1 == 1))
# if 2 + 2 != 5:
#     print("This is normal")

character = input("Enter any character :")
if len(character) > 5:
    print(f"{character} is greater than 5")
elif len(character) == 5:
    print(f"{character}  is equal to 5")
else:
    print("Your character is less than 5")

integer = int(input('Enter a positive integer:'))
num = 1
for num in range(1, integer):
    if integer % num == 0:
        print(f"{num} is a factor of {integer}")
        num = num + 1
print(f"{integer} is a factor of {integer}")

letter = " "

while letter != "q" and letter != 'Q':
    letter = input("Enter a character or enter 'q' or 'Q' : ")
    if letter == "q" or letter == 'Q':
        break
    else:
        print("Try again")


for numbers in range(1,50):
    if numbers % 3 == 0:
        continue
    print(numbers)



