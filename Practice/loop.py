# n = 0
# while n <= 10:
#     print(n)
#     n = n+2
#
# num = int(input("Enter a even number"))
# while num % 2 != 0:
#     print("Not correct")
#     user_input = input("Enter an even number")
# user_input = input("Enter")
#
# for letters in user_input:
#     print(letters, " ")
#
#
# for numbers in range(2, 10):
#     print()
#     print(numbers)
#
#
# num = "twenty"
# index = 2
#
# while index < len(num):
#     print(num[index])
#     index = index + 1
#
#
# word = "python"
# index = 0
# while index < len(word):
#     print(word[index])
#     index = index + 1

def invest(amount, rate, years):
    for years in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year{years} :${amount:,.2f}")


amount = float(input("Enter your amount :"))
rate = float(input("Enter your rate :"))
years = int(input("Enter years"))
invest(amount, rate, years)

