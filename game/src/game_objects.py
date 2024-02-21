class Rocket:
    def __init__(self, size, speed, direction, position, hp):
        self._size = size
        self._speed = speed
        self._direction = direction
        self._position = position
        self._max_hp = hp
        self._current_hp = hp
        self._skore = 0
    
    def return_skore(self):
        return self._skore

    def pohyb():
        pass
        # nastaveni klavesy, detekce kolize: if isinstance(objekt, Bonuses)

    def vykresli():
        pass    
        # 

    def navyseni_skore():
        pass
    
    def ubirani_zivotu():
        pass

    def detekce_kolize():
        pass

    def end_game():
        pass

class Bonuses:
    def __init__(self, size, position, hodnota):
        self._size = size
        self._position = position
        self._hodnota = hodnota

    def vyskresli():
        pass

class Coin(Bonuses):
    def __init__(self, size, position, hodnota):
        super().__init__(size, position, hodnota)

class Asteroids:
    def __init__(self, size, speed, direction, position):
        self._size = size
        self._speed = speed
        self._direction = direction
        self._position = position

    def pohyb():
        pass
        # pohyb skrze cos, sin
    
    def vykresli():
        pass

    
