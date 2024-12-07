from enum import Enum, auto

class CardValue(Enum):
    Ace = auto()
    King = auto()
    Queen = auto()
    Joker = auto()

class CardType(Enum):
    Spade = auto()
    Heart = auto()
    Club = auto()
    Diamond = auto()
