class Dog:
    def _init_(self, name, breed):
        self.name = name
        self.breed = breed
def bark(self):
    print(f"{self.name} say Woof")
def fetch(self,item):
    print(f"{self.name} fetches the {item}"")
my_dog = Dog("Buddy","Golden Retriever")
print(my_dog.name)
my_dog.bark()
