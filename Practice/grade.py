# score = int(input("Enter grade :"))
# for grade in range(1, 100):
#     if 90 <= score < 100:
#         print("A")
#
#     elif 70 <= score < 89:
#         print("B")
#         break
#     elif 50 <= score < 69:
#         print("C")
#         break
#     elif 40 <= score < 49:
#         print("D")
#         break
#     elif 30 <= score < 39:
#         print("E")
#         break
#     else:
#         print("Zero Talent")
#         break
from Practice.grades import grade

# class classname
# to differentiate between method and static method . annotate @class method and @ static method for static method

# def __init__(self, name,age)
# self refers to the reference
# self.name,self.age
if __name__ == '__main__':
    grade()

# to setname def set_name_age(self,name,age):
# self.name = name
# self.age = age
# def get_name(self)
# return self.name
# def get_age()
# return self.age
# for private function def__set_name()
