class Person:
    def __init__(self, name):
       self.name = name  

    def greet(self):
        print(f"Hello, my name is {self.name}")


person1 = Person("Siri")
person1.greet()