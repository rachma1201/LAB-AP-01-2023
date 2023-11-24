class Human: #ini adalah kelas kakek dari bapaknya yaitu hero, dan cucunya yaitu warrior, support, assasin
    def __init__(self, name, position, speed=1): #Constructor, langsung dijalankan tanpa di panggil seperti method
        self.__name = name #ini adalah atribut
        self.__position = position #ini adalah atribut
        self._speed = speed #ini adalah atribut
        
    def Movement(self, arah): #ini adalah method
        if arah == "RRR":
            self.__position += self._speed
        elif arah == "L":
            self.__position += self._speed;
            
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
        
    def getPosition(self): #ini juga method
        return self.__position
    def setPosition(self, position):
        self.__position = position
        
    def getSpeed(self):
        return self._speed
    def setSpeed(self, speed):
        self._speed = speed
        
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def Attack(self, target):
        target._health -= self._power
        
    
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def setPower(self, power):
        self._power = power
    def setHealth(self, health):
        self._health = health
    def setArmor(self, armor):
        self._armor = armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power


class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self._speed = 4
        
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health = self._power

        
class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4
    def special(self, target):
        self._speed = 6
        target._health += 150
    
    
warrior = Warrior("bambang", 10)
assassin = Assassin("joko", 25)
support = Support("udin", 30)

print(warrior.getName())
#Sebelum
print("health (before)", warrior.getHealth())
assassin.Attack(warrior)
#Sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
#Sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())

support.special(warrior)
#Sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())

print(warrior.__dict__)
warrior.Movement("RRR")
print(warrior.__dict__)