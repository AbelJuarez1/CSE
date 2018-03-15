class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def get_payed(self):
        print("%s got payed" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, job, computer):
        super(Programmer, self).__init__(name, age, job)
        self.computer = computer

    def code(self):
        print("The employee's name is %s" % self.name)
        print("He is a %s" % self.job)
        print("He is %s years old" % self.age)


employee = Programmer("Bob", "21", "programmer", "Asus")
employee.work()
employee.get_payed()
employee.code()
