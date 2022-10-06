
# Calculate the area and circumference of a circle from its radius
# Step 1: Prompt for a radius
# Step 2: Apply the area formula
# Step 3: Print out the result

import math

if __name__ == '__main__':
    print(10, 20, 30, sep=', ')  # prints 10, 20, 30

    radius = int(input("Enter the radius of your circle: "))
    '''
    radius_int = int(radius_str)
    
    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)
    print ("The circumference is:", circumference, \
    ", and the area is:", area)
    '''

    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    print("The circumference is", circumference, "\nThe area is", area)
    print(ord("A"))
    print(ord("B"))

    grade = int(input("Enter grade: "))
    print("Passed" if grade >= 80 else "Failed")
    result = "Passed" if grade >= 80 else "Failed"
    print(result)

    while grade < 100:
        grade *= 2
        print("grade is", grade)

    for character in "ProgrammingClass":
        print(character, end=",  ")

    for name in "Paragons Cohort 13":
        print(name, name, sep=", ")

    # character = "m"
    # while character in "Programming":
    #     print(letter, end="  ")
