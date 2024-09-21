
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden in the subclass

# Subclass or Derived class
class sir():
    def speak(self):
        return f"{self.name} beats student"

class student():
    def speak(self):
        return f"{self.name} says why are u beating"

# Creating instances of the subclasses
dog = sir("sir")
cat = student("student")

# Calling the speak method for the instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
