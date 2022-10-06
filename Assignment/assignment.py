class Assignment:

    def __init__(self, full_name, age):
        self.full_name = full_name
        if age > 0:
            self.age = age

    def set_name(self, full_name):
        self.full_name = full_name

    def get_name(self):
        return self.full_name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def max_heart_rate(self):
        heart_rate = 220 - self.age
        print(f"Your Max heart rate is:{heart_rate} ")

    def target_heart_rate(self):
        target = 0.50 * (220 - self.age)
        target2 = 0.85 * (220 - self.age)
        print(f"Your heart rate target should be between {target:.2f}bpm - {target2:,.2f} bpm")

    @staticmethod
    def heart_rate():
        p1 = Assignment("", 0)
        name = input("Enter full name :")
        Assignment.set_name(p1, name)
        age = int(input("Enter your age :"))
        Assignment.set_age(p1, age)
        if age < 0:
            try:
                age = int(input("Enter valid  age"))
                Assignment.set_age(p1, age)
            except ValueError:
                print("Enter a valid age")

        print("Heart Record File")
        print(f"Name :{Assignment.get_name(p1)}".upper())
        print(f"Age :{Assignment.get_age(p1)}")
        Assignment.max_heart_rate(p1)
        Assignment.target_heart_rate(p1)

    @staticmethod
    def fibonacci():
        position = int(input("Enter a number"))
        first_no = 0
        second_no = 1
        count = 0
        while count < position - 2:
            total = first_no + second_no
            first_no = second_no
            second_no = total
            print(f"{total:,}")
            count = count + 1

    @staticmethod
    def palindrome():
        num = int(input("Enter number"))
        total = 0
        temp = num
        while num > 0:
            rem = num % 10
            total = (total * 10) + rem
            num = num // 10
        if temp == total:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")

    @staticmethod
    def reverse():
        rev = 0
        num = int(input("Enter number"))
        while num > 0:
            rem = num % 10
            rev = (rev * 10) + rem
            num = num // 10
        print(f"The reverse is {rev}")

    @staticmethod
    def triangle():
        a = int(input("Enter for side 'A'"))
        b = int(input("Enter for side 'b'"))
        c = int(input("Enter for side 'C'"))
        if a == b and a == c and c == b:
            print("It is a equilateral")
        else:
            print("It is not an equilateral triangle")

    @staticmethod
    def turing_test():
        problem = input("What is your problem ?")
        print("Have you had this problem before")

        prob = int(input(print("If YES press 1" + " \nIf NO press 2")))
        if prob == 1:
            print("Well you have it again.Solve it")
        elif prob == 2:
            print("Well you have now. Solve it")
        while prob != 1 or prob != 2:
            print("Enter 1 or 2")
            prob = prob + 1
            problem = input("What is your problem ?")

    @staticmethod
    def bacteria():
        virus = 200
        hours = 0
        print(f" hours\t\t\tNumber of bacteria")
        while hours < 20:
            b = virus * (2 * hours)
            print(f"{hours}          {b}")
            hours += 5

    @staticmethod
    def eggs_per_box():
        box1 = 6
        x = 28
        each = (28 * 1) // 6
        print(f"The farmer will need {each} boxes to store 24 eggs")
        box4 = 24
        remaining = x - box4
        print(f"{remaining} eggs will be remaining in the uncompleted box")
        fill = box1 - remaining
        print(f"{fill} eggs will be needed to fill the uncompleted box ")

    @staticmethod
    def hourly_wage():
        o = 10 * 24 * 365

        p = 0.03
        print("Years        Wages_After_5_Years")
        n = 5
        w = o * ((1 + p) ** n)
        print(f"{n}         ${w:,.2f}")

        print("After two years of bad review")
        print()
        print("Years        Wages")
        n2 = 2

        w2 = o * ((1 - p) ** n2)

        print(f"{n2}         ${w2:,.2f}")

    @staticmethod
    def missing_code():
        try:
            grade = int(input("Enter grade :"))
            if grade >= 90:
                print("Congratulations")
                print(f" {grade} : ***")
            else:
                print("You tried")
        except ValueError:
            print("Enter an integer")

    @staticmethod
    def flu_patients():
        smallest = 99999999999
        largest = 0
        total = 0
        average = 0
        for day in range(1, 8):
            flu = int(input(f"Enter number of affected patients:day{day}:"))
            total += flu
            average = total / 7

            if flu > largest:
                largest = flu
            if flu < smallest:
                smallest = flu

        print(f"Total :{total} \n Average:{average}\n largest case:{largest}\n smallest case:{smallest}")

    @staticmethod
    def multiply():
        for number1 in range(1, 21):
            for number2 in range(1, 13):
                print(number1 * number2, end=' ')
            print("\n")


if __name__ == '__main__':
    # Assignment.palindrome()
    # Assignment.reverse()
    # Assignment.heart_rate()
    # Assignment.triangle()
    # Assignment.fibonacci()
    # Assignment.turing_test()
    Assignment.bacteria()
    # Assignment.eggs_per_box()
    # Assignment.hourly_wage()
    # Assignment.missing_code()
    # Assignment.flu_patients()
    # Assignment.multiply()
