import collections
class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.Cards = []
        self.strengthdic = {}
        for i in range(14):
            self.strengthdic[i] = 0
    def __str__(self):
        return self.name
        
    def cardappend(self,Card):
        self.Cards.append(Card)
        self.strengthdic[Card.strength] += 1
    def gethand(self):
        cardlist = ''
        for card in self.Cards:
            cardlist += str(card) + ' '
        return cardlist

    def handsort(self):
        self.Cards.sort()

    def isslough(self,field):
        f = field.getfield()

        #c = collections.Counter(int(self.Cards))
        print(f)
        pass

    def slough(self,cards):
        removelist = []
        for card in cards:
            for i in range(len(self.Cards)):
                if str(self.Cards[i]) == card:
                    removelist.append(self.Cards[i])
                    break
        for removecard in removelist:
            self.Cards.remove(removecard)
        print(self.gethand())
        return removelist

class CPU(Player):
    def select(self,field):
        self.isslough(field)
        return list(input().split(" "))
class YOU(Player):
    def select(self,field):
        return list(input().split(" "))