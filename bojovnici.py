# import random 

# class Kostka:
#     def __init__(self, pocet_sten):
#         self._pocet_sten = pocet_sten
        
#     def hod(self):
#         return random.randint(1, self._pocet_sten)

# kostka1 = Kostka(12)
# kostka2 = Kostka(6)
# kostka3 = Kostka(4)

# print(kostka1.hod())

class Bojovnik:
    def __init__(self, name, max_hp, current_hp, attack, defend):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = current_hp
        self._attack = attack
        self._defend = defend

    def is_alive(self):
        if self._current_hp > 0:
            return True
        else:
            return False

bojovnik1 = Bojovnik("Soldier", 50, 50, 10, 15)
bojovnik2 = Bojovnik("Enemy", 50, 45, 5, 10)
