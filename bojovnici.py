import random 

class Kostka:
    def __init__(self, pocet_sten):
        self._pocet_sten = pocet_sten
        
    def hod(self):
        return random.randint(1, self._pocet_sten)

class Bojovnik:
    def __init__(self, name, max_hp, current_hp, attack, defend, kostka):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = current_hp
        self._attack = attack
        self._defend = defend
        self._kostka = kostka

    def is_alive(self):
        if self._current_hp > 0:
            return True
        else:
            return False
    
    def remaining_life(self):
        return "{0} has {1}hp ".format(self._name, self._current_hp)
    
    def defend_youself(self, punch):
        damage = punch - (self._defend + self._kostka.hod())
        if damage > 0:
            self._current_hp = self._current_hp - damage
        
    def attack(self, bojovnik1):
        punch = self._attack + self._kostka.hod()
        bojovnik1.defend_youself(punch)

kostka = Kostka(10)
print(kostka.hod())

bojovnik1 = Bojovnik("Soldier", 50, 50, 10, 15, kostka)
bojovnik2 = Bojovnik("Enemy", 50, 45, 5, 10, kostka)

bojovnik2.attack(bojovnik1)
print(bojovnik1.remaining_life())
bojovnik1.attack(bojovnik2)
print(bojovnik2.remaining_life())