# this is working
car_name = "Wiebe mobile"
car_type = "Tesla"
car_cylinders = 8
car_mpg = 9000.1

# inline printing
print("i have a car called the %s" % car_name)
print("i have a car called the %s. it's a %s." % (car_name, car_type))

# asking for input
name = input("what is your name? ")  # in python 3, it is just called input()
print("Hello %s." % name)

age = input("how old are you? ")
print("%s That's really old." % age)
