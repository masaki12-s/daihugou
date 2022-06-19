from Card import *
class Field:
    def __init__(self):
        self.fieldCards = []
        self.strength = -1

    def put_to_field(self,Cards):
        self.fieldCards = Cards
        for card in self.fieldCards:
            if str(card) == 'Joker':
                if len(self.fieldCards) == 1:
                    self.strength = 1000
                else:
                    self.strength = int(card)
            self.strength = int(card)
        print(self.strength)

    def getfield(self):
        return (self.strength,len(self.fieldCards))

    def __str__(self):
        cardlist = ''
        for card in self.fieldCards:
            cardlist += str(card) + ' '
        return cardlist
