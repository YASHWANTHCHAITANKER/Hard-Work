class student:
    uniform="Red"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def details(self):
        print(f"My name is {self.name} and age is {self.age}")
std1=student("PrabhusriRam",3000000)
std2=student("prabhusrihanuman",290000)
#std1.name="sriram"
#std1.age=30909098
#std2.name="srihanuman"
#std2.age=23846594
std1.details()
std1.uniform="orange"
print(std1.uniform)
std2.details()
print(std2.uniform)