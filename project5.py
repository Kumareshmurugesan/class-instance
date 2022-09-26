#class method
class student():
    name = "ram"
    age = 25
    def printall():
        print("Name :", student.name)
        print("age: ", student.age)
student.printall()
print(getattr(student,'printall'))
(getattr(student,'printall'))()

print("___________________________________")

#instance method
class student():
    name = "ram"
    age = 25

    def printall(self,gender, city):
        print("Name :", student.name)
        print("age: ", student.age)
        print("Gender: ", gender)
        print("City: ", city)


o = student()
print(o.printall( 'cbe','male'))
o.printall('male','cbe')
o.printall()
print("---------------------------------------")

#__init__ method
class student():
    def __init__(self,name):
        self.name = name
    def printall(self):
        print("name: ", self.name)

o1 = student('Yashu')
o1.printall()
o2 = student('Ram')
o2.printall()

print("--------------------------")

#static method

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ", self.name, "  Age : ", self.age)

    @staticmethod
    def welcome():
        print("welcome")

o1 = student('ram', 25)
o1.printDetail()
o1.welcome()
o2 = student('sam', 20)
o2.printDetail()
o2.welcome()