if __name__ == '__main__':
    user_input = 0
    number = 70
    count = 0
    while user_input != -1:
        user_input = int(input("Guess the number :"))
        if user_input > number:
            print("Too high")
        elif user_input < number:
            print("Too low")
        elif user_input == number:
            print(f"Wow you got it right the number is {number}")
            break
        count = count + 1
        if count == 3:
            user_input = int(input("Enter 1 to continue or -1 to quit"))
            if user_input == 1:
                continue
            elif user_input == -1:
                break
            else:
                print("Enter a valid integer")

