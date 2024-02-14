class Rocket:
    def __init__(self, size, speed, smer, position, hp):
        self._size = size
        self._speed = speed
        self._smer = smer
        self._position = position
        self._max_hp = hp
        self._current_hp = hp

class Bonuses:
    def __init__(self, size, position, hodnota):
        self._size = size
        self._position = position
        self._hodnota = hodnota

class Asteroids:
    def __init__(self, size, speed, smer, position):
        self._size = size
        self._speed = speed
        self._smer = smer
        self._position = position
