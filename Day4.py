class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.Age=0
        else:
            self.Age = initialAge  # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.Age<13:
            print("You are young.")
        elif self.Age>=13 and self.Age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.Age= self.Age+ 1 # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
