import random
from Card import *
from field import *
from Player import *
class GameManager:
    def __init__(self,player):
        self.player = player
        self.Cards = []
        self.Players = []
        for i in range(1,player+1):
            if i == 0:
                p = YOU('Player'+str(i))
            else:
                p = CPU('Player'+str(i))
            self.Players.append(p)

    def Start(self):
        self.startplayer = random.randint(0,self.player-1)
        self.field = Field()
        self.ranking = []
        suits = ['♠', '♣', '♡', '♢']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for number in numbers:
                card = SuitCard(suit,number)
                self.Cards.append(card)
        self.Cards.append(Joker())
        random.shuffle(self.Cards)
        
        # カードを配布
        i = 0
        while True:
            card = self.Cards.pop(0)
            p = self.Players[i]
            p.cardappend(card)
            i += 1
            if i == self.player:
                i = 0
            if len(self.Cards) == 0:
                break
        # 革命
        self.renovation = False

        pass
    def cards(self):
        return self.Cards

    def game(self):
        self.Start()
        turnplayer = self.startplayer
        remaining = self.player
        c = 0
        while True:
            print(str(self.Players[turnplayer])+'\'s Turn')
            print('field:'+str(self.field))
            print(self.Players[turnplayer].gethand())
            # if str(self.Players[turnplayer]) == 'Player1':
            #     print(self.Players[turnplayer].gethand())
            
            putcard = self.Players[turnplayer].select(self.field)
            self.field.put_to_field(self.Players[turnplayer].slough(putcard))
            print(putcard)
            print()

            if len(self.Players[turnplayer].Cards)==0:
                self.ranking.append(str(self.Players[turnplayer]))
                self.Players.pop(turnplayer)
                remaining -= 1
            turnplayer += 1
            if turnplayer + 1 > remaining:
                turnplayer = 0
            


            c += 1
            if c == 15:
                break
gameA = GameManager(4)
gameA.game()
# for i in gameA.Players[0].Cards:
#     print(i)