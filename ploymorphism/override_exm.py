class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!!!!")


animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()





