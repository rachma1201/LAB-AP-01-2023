class Animal():
    def __init__(self, name):
        self._name = name
        self._health = 10

    def make_sound(self):
        pass

    def get_name(self):
        return self._name
    
    def setHealth(self, health):
        self._health = health
    
    def getHealth(self):
        return self._health

    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "gukguk!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    return animal.make_sound()


dog = Dog("mochi")
print(f"Dog   : {dog.get_name()}")  
print(f"Sound : {animal_sound(dog)}\n")  

cat = Cat("adam")
cat.setHealth(20)
print(f"Cat   :{cat.get_name()}")
#after
print(f"Health:{cat.getHealth()}")
print(f"Sound :{animal_sound(cat)}") 


