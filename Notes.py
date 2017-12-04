import random
# # # this is working
# # car_name = "Wiebe mobile"
# # car_type = "Tesla"
# # car_cylinders = 8
# # car_mpg = 9000.1
# #
# # # inline printing
# # print("i have a car called the %s" % car_name)
# # print("i have a car called the %s. it's a %s." % (car_name, car_type))
# #
# # # asking for input
# # name = input("what is your name? ")  # in python 3, it is just called input()
# # print("Hello %s." % name)
# #
# # age = input("how old are you? ")
# # print("%s That's really old." % age)
#
#
# # Functions
#
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
# print_hw()
# print_hw()
#
#
# def say_hi(name):  # name is a parameter
#     print("Hello %s." % name)
#     print("Enjoy your day.")
#
#
# say_hi("John")
#
#
# def print_age(name,age):
#     print("%s is %d years old" % (name,age))
#     age += 1  # this means the sae thign (age = age + 1)
#     print("Next year, they will be %d" % age)
#
#
# print_age("John", 15)
#
#
# # If statements
#
#
# def f(x):
#     return x**3 + 4 * x**2 + 7 * x - 4
#
#
# print(f(3))
# print(f(4))
# print(f(5))
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage <= 60:
#         return "F"
#
#
# def happy_bday(name):
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to " + name + ",")
#     print("Happy birthday to you" + ".")
#
#
# happy_bday("Mr. Feyma")
#
#
# # Loops
#
# for num in range(10):
#     print(num + 1)
#
#     # DO NOT RUN!!!
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#
#
# # Random Numbers

# import random   # This should be on Line 1
print(random.randint(0, 100))

# Comparisons
print(1 == 1)  # Is 1 equal to 1?
print(1 != 2)  # Is 1 equal to 2?
print(10 <= 15)
print(not False)

# Recasting

c = '1'
print(c == 1)
print(int(c) == 1)  # Both are ints
print(c == str(1))  # Both are strings

# The input command ALWAYS gives a string
