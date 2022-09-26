
#classmethod
'''
class vehicel():
    name="m.k.s"
    no="TN34B6427"
    def printall():
        print("Name=", vehicel.name)
        print("No=",  vehicel.no)
vehicel.printall()
print(getattr(vehicel,'printall'))
getattr(vehicel,"printall")()

print("------------------------------")
#--instance method
class truck():
     name="M.K.S"
     no="TN34B6427"
     
     def printall(self,owner,route):
         print("Name=", truck.name)
         print("No=", truck.no)
         print("Owner=", owner)
         print("Route=", route)
o=truck()
print(o.printall('murugesan','chennai'))
o.printall('murugesan','chennai')
print("----------------------------------")
'''
#inisilition method
class Truck():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printall(self):
      print("Name=",self.name,"\nage=",self.age)
p=Truck("M.K.S","20")
p.printall()
#static Method
class Truck():
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def printall(self):
        print("name=",self.name,"\nnumber=",self.number)
    @staticmethod
    def Welcome():
        print("Welcome")
p2=Truck("M.K.S","1318")
p2.printall()
p2=Truck("welcome")
p2.Welcome()

