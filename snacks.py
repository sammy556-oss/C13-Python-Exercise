class Assignment:
    @staticmethod
    def grade_printing(grade):
        grade = int(input('Enter grade: '))
        if grade >= 90:
            print('Congratulations!, your grade of ' + str(grade) + ' earns you an A in this course.')
        else:
            print('Passed!')

    @staticmethod
    def multiplication_table():
        for one in range(1, 11, 1):
            two = one * 2
            three = one * 3
            four = one * 4
            five = one * 5
            six = one * 6
            seven = one * 7
            eight = one * 8
            nine = one * 9
            ten = one * 10
            print(one, ' ', two, ' ', three, ' ', four, ' ', five, ' ', six, ' ', seven, ' ', eight, ' ', nine, ' ',
                  ten,
                  ' ')

    @staticmethod
    def turing_test():
        question = input('What is your problem? ')
        respond = input('Have you had this problem before(yes or no)? ')
        if respond == "yes":
            print('Well, you have it again.')
        else:
            print('Well, you have it now.')

    @staticmethod
    def equilateral_triangle(side_a, side_b, side_c):
        print('Enter lengths of triangle: ')
        side_a = int(input('Enter the first side: '))
        side_b = int(input('Enter the second side: '))
        side_c = int(input('Enter the third side: '))

        if side_a == side_b and side_b == side_c:
            print('It is an equilateral triangle.')
        else:
            print('it is not.')

    @staticmethod
    def palindrome_number(num):
        num = int(input('Enter a number: '))
        temp_num = num
        reverse_num = 0
        while num > 0:
            number = num % 10
            reverse_num = reverse_num * 10 + number
            num = num // 10
        if temp_num == reverse_num:
            print('It is a palindrome! ')
        else:
            print("It isn't")

    @staticmethod
    def flu():
        total_cases = 0
        smallest_case = 9999999
        largest_case = 0
        for i in range(0, 7):
            cases = int(input('Enter the number of cases for the day: '))
            if cases < smallest_case:
                smallest_case = cases
            elif cases > largest_case:
                largest_case = cases
            total_cases += cases
        average_of_all_cases = total_cases / 7
        print(f'Total cases for week is {total_cases}')
        print(f'Average cases for week is {average_of_all_cases}')
        print(f'Smallest case is {smallest_case}')
        print(f'Largest case is {largest_case}')

    @staticmethod
    def box_of(egg):
        box = egg // 6
        rem = egg % 6
        new_box = 6 - rem
        if rem == 0:
            print(f'{box} boxes are needed.')
        else:
            print(f'{box} boxes are needed with a remainder of {rem} eggs.')
            print(f'{new_box} eggs are needed to complete the box.')

    @staticmethod
    def bacteria_start_with(bacteria):
        print(f'Hour\t\tNumber of Bacteria')
        for hours in range(0, 20, 5):
            output = bacteria * 2 * hours
            print(f'{hours}\t\t\t{output}')

    @staticmethod
    def hourly_wage(good, bad, principal):
        good_new_hourly_wage = principal * ((1 + 0.03) ** good)
        print(f'After {good} years of good reviews, new hourly wage is ${good_new_hourly_wage : .2f}')
        bad_new_hourly_wage = principal * ((1 - 0.03) ** bad)
        print(f'After {bad} years of bad reviews, new hourly wage is ${bad_new_hourly_wage : .2f}')

    @staticmethod
    def heart_rate():
        age = int(input('Enter your age: '))
        maximum_heart_rate = 220 - age
        target_heart_rate = maximum_heart_rate / 2
        target_heart_rate_2 = 85 * maximum_heart_rate / 100
        print(f'Maximum heart rate: {maximum_heart_rate}bpm')
        print(f'Target heart rate is {target_heart_rate}bpm to {target_heart_rate_2}bpm.')

    @staticmethod
    def fibonacci(position):
        total = 0
        count = 0
        number_before_1 = 0
        number_before_2 = 1
        if position == 1:
            print(f'The number in position {position} is 0')
        elif position == 2:
            print(f'The number in position {position} is 1')
        elif position >= 3:
            while count < position - 2:
                total = number_before_1 + number_before_2
                number_before_1 = number_before_2
                number_before_2 = total
                count += 1
        print(f'The number in position {position} is {total}')

    @staticmethod
    def extract(number):
        while number != 0:
            rem = number % 10
            number //= 10
            print(rem, end=' ')


