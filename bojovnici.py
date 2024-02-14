import random 

class Kostka:
    def __init__(self, pocet_sten):
        self._pocet_sten = pocet_sten
    
    def return_pocet_stran(self):
        return self._pocet_sten

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
            message = f"{self._name} has suffered {damage} damage."
            self._current_hp = self._current_hp - damage
            if not self.is_alive():
                message = f"{self._name} has died"
        else:
            message = f"{self._name} has defended himself."
        self.Message(message)
        
    def attack(self, bojovnik1):
        strike = self._attack + self._kostka.hod()
        message = f"{self._name} is attacking with {strike} damage."
        self.Message(message)
        bojovnik1.defend_youself(strike)

    def Message(self, message):
        self._message = message

    def return_message(self):
        return self._message

class Mag(Bojovnik):
    def __init__(self, name, hp, attack, defend, kostka, mana, magic_attack):
        super().__init__(name, hp, attack, defend, kostka)
        self._max_mana = mana
        self._current_mana = mana
        self._magic_attack = magic_attack
    
    def attack(self, bojovnik1):
        if  self._current_mana < self._max_mana:
            self._current_mana = self._current_mana + 15
            strike = self._attack + self._kostka.hod()
            message = f"{self._name} is attacking with {strike} damage."
            self.Message(message)
        else:
            strike = self._magic_attack + self._kostka.hod()
            message = f"{self._name} has used {strike} magic attack"
            self.Message(message)
            self._current_mana = 0
        bojovnik1.defend_youself(strike)

class Area:
    def __init__(self, bojovnik1, bojovnik2):
        self._bojovnik1 = bojovnik1
        self._bojovnik2 = bojovnik2

    def fight(self):
        print("Let the fight begin!")
        while self._bojovnik1.is_alive() and self._bojovnik2.is_alive():
            self._bojovnik2.attack(self._bojovnik1)
            print(self._bojovnik2.return_message())
            print(self._bojovnik1.return_message())
            self._bojovnik1.attack(bojovnik2)
            print(self._bojovnik1.return_message())
            print(self._bojovnik2.return_message())

kostka = Kostka(10)
print(kostka.hod())

bojovnik1 = Bojovnik("Soldier", 100, 15, 20, kostka)
bojovnik2 = Mag("Mág", 120, 20, 8, kostka, 30, 25)

area = Area(bojovnik1, bojovnik2)
area.fight()
