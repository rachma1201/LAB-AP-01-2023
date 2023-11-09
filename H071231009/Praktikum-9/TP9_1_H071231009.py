class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self._speed = 0
    def movement(self, arah):
        for i in arah:
            if i == "L":  #kiri
                self.__position -= self._speed
            elif i == "R":
                self.__position += self._speed
            else:
                pass
    def get_position(self):
        return self.__position
    def set_position(self, position):
        self.__position = position
    def get_speed(self):
        return self._speed
    def set_speed(self, speed):
        self._speed = speed

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    def attack(self, target):
        target.set_health(target.get_health() - self._power)
    
    def get_power(self):
        return self._power
    def set_power(self, power):
        self._power = power
    def get_health(self):
        return self._health
    def set_health(self, health):
        self._health = health
    def get_armor(self):
        return self._armor
    def set_armor(self, armor):
        self._armor = armor

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self.set_armor(45)
        self.set_power(32)
        target.set_health(target.get_health() - self._power)

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self.speed = 4
    def special(self, target):
        self.set_power(42)
        self.speed = 7
        target.set_health(target.get_health() - self._power)

class Support(Hero):
    def __init__(self, nama, position):
        super().__init__(nama, position)
        self._health = 500
        self._armor = 8
        self.speed = 4
    def special(self, target):
        self.speed = 6
        target.set_health(target.get_health() + 150)


 
warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin",position=30)

# Memanggil method class human
print("Before position: ", warrior.get_position())
warrior.set_speed(5)
warrior.movement("RRL")
print("After position: ", warrior.get_position())

# memanggil method class hero
# sebelum
print("health (before):", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after):", warrior.get_health())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.get_health())
# print("Assassin (health)", assassin.get_health())
print("Support (speed) : ",support.speed)
support.special(warrior)
support.special(assassin)
# sesudah
print("Warrior (health)", warrior.get_health())
# print("Assassin (health)", assassin.get_health())

print("Support (speed): ",support.speed)