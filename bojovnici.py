import random 

class Kostka:
    def __init__(self, pocet_sten):
        self._pocet_sten = pocet_sten
        
    def hod(self):
        return random.randint(1, self._pocet_sten)

class Bojovnik:
    def __init__(self, name, hp, attack, defend, kostka):
        self._name = name
        self._max_hp = hp
        self._current_hp = hp
        self._attack = attack
        self._defend = defend
        self._kostka = kostka
        self._message = ""

    def is_alive(self):
        if self._current_hp > 0:
            return True
        else:
            return False
    
    def remaining_life(self):
        return "{0} has {1}hp ".format(self._name, self._current_hp)
    
    def defend_youself(self, strike):
        damage = strike - (self._defend + self._kostka.hod())
        if damage > 0:
            self._current_hp = self._current_hp - damage
            message = f"{self._name} has suffered {damage} damage."
            if not self.is_alive():
                message = f"{self._name} has died"
        else:
            message = f"{self._name} has defended himself."
        self._message(message)
        
    def attack(self, bojovnik1):
        strike = self._attack + self._kostka.hod()
        message = f"{self._name} is attacking with {strike} damage."
        bojovnik1.defend_youself(strike)
        self._message(message)

    def message(self, message):
        self._message = message

    def return_message(self):
        return self._message

class Area:
    def __init__(self, bojovnik1, bojovnik2):
        self._bojovnik1 = bojovnik1
        self._bojovnik2 = bojovnik2

    def fight():
        print("Let the fight begin!")
        while bojovnik1.is_alive() and bojovnik2.is_alive():
            bojovnik2.attack(bojovnik1)
            print(bojovnik2.return_message())
            print(bojovnik1.return_message())
            bojovnik1.attack(bojovnik2)
            print(bojovnik1.return_message())
            print(bojovnik2.return_message())

kostka = Kostka(10)
print(kostka.hod())

bojovnik1 = Bojovnik("Soldier", 100, 15, 20, kostka)
bojovnik2 = Bojovnik("Enemy", 80, 10, 10, kostka)
area = Area(bojovnik1, bojovnik2)
area.fight()
