class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self.__position = pos_x
        self._speed = 0

    def movement(self, direction):
        for i in direction:
            if i == "L":
                self.__position -= self._speed
            elif i == "R":
                self.__position += self._speed
            else:
                pass
    
    def setPosition(self, position):
        self.__position = position
    
    def setSpeed(self, speed):
        self._speed = speed

    def getPosition(self):
        return(self.__position)
    
    def getSpeed(self):
        return self._speed
    
class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power
    
    def setHealth(self, health):
        self._health =  health 
    
    def setPower(self, power):
        self._power = power

    def setArmor(self, armor):
        self._=armor
    
    def setSpeed(self, speed):
        self._speed = speed

    def getHealth(self):
        return self._health
    
    def getPower(self):
        return self._power
    
    def getArmor(self):
        return self._armor
    
    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x ):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self.setPower(32)
        self.setArmor(45)
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4
    
    def special(self, target):
        self._speed = 7
        self.set_power(42)
        target._health -= self._power
    
class Support(Hero):
    def __init__(self, name, pos_x ):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        target._health += 150
        self._speed = 6

warrior = Warrior("bambang", pos_x=20)
assassin = Assassin("joko", pos_x=25)
support = Support("udin", pos_x=30) 

print("Position warrior (before movement)", warrior.getPosition())
warrior.setSpeed(10)

warrior.movement("LLUR")
print("Position warrior (after movement)", warrior.getPosition())

print("-"*10)

print("health (after)", warrior.getHealth())
assassin.attack(warrior)
print("health (before)", warrior.getHealth())

print("-"*10)

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())
support.special(warrior)

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())