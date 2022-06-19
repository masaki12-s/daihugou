class Card:
    def __init__(self) -> None:
        pass
    def __lt__(self,other):
        return self.strength < other.strength

    def __str__(self):
        return self.suit+self.number

class SuitCard(Card):
    def __init__(self,suit,number) -> None:
        self.suit = suit
        self.number = number
        self.numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        intnum = self.numbers.index(number)
        self.strength = (intnum+11)%13 
    # @property
    # def suit(self):
    #     return self.__suit
    # @property
    # def number(self):
    #     return self.__number
    def __int__(self):
        return self.strength
        
class Joker(Card):
    def __init__(self):
        pass
    def __str__(self):
        return "Joker"
    def __lt__(self):
        True
