# This is a sample Python script.
from random_test import FirstClass

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    myAccount = FirstClass('Adeola', 34)
    print(myAccount.get_name())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
x = "Adewunmi"
print(type(x))

a = "ADEKUNLE adeola EMMANUEL"


def myfunc():
    global a
    a = "Adewunmi"
    print(a.replace("A", "E"))  # prints Edewunmi


myfunc()
print(a)  # prints Adewunmi


def newfunc():
    x = "AdeolA"
    print(x.replace("A", "E"))  # prints EdeolE
    print(x.split("e"))  # prints ['Ad', 'olA']


newfunc()

name = "Emmanuel"
cohort = "cohort 13"
detail = "my name is {} and I am in {}"
print(detail.format(name, cohort))

a = 95
b = 25

c = "{} is greater than {}"

if a > b:
    print(c.format(a, b))
else:
    print(c.format(b, a))


class myclass():
    def __len__(self):
        return 0



__len__(self) is a function that determines the length of what the class is returning.


myobj = myclass()
print(bool(myobj))  # prints false

thislist = ["ADEOLA", 10, "6.2"]
name, age, height = thislist
print(name)  # prints ADEOLA
print(age)  # prints 10
print(height)  # prints 6.2

print(thislist)  # prints ['ADEOLA', 10, '6.2']
print(type(thislist))  # prints <class 'list'>

thisnewlist = list(("adeola", "adewunmi", "daniel"))
print(thisnewlist)  # prints ['adeola', 'adewunmi', 'daniel']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon", "mango"]
print(thislist)
'''

print(
    '''
this is a longer string, so we \
split it over two lines
'''
)
