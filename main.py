import random

class dealerHand:
    def __init__(self,card1,card2) -> None:
        self.card1 = card1
        self.card2 = card2

    def makeDealer(self):
        self.card1 = random.randint(1,10)
        self.card2 = random.randint(1,10)
        



class ownHand:
    def __init__(self,own1,own2,title,ascii1,ascii2) -> None:
        self.own1 = own1
        self.own2 = own2
        self.title = title
        self.ascii1 = ascii1
        self.ascii2 = ascii2
        






    def makeHand(self):
        self.own1 = random.randint(1,11)
        self.own2 = random.randint(1,11)

        self.title = """
╦ ╦╔═╗╦ ╦╦═╗  ╦ ╦╔═╗╔╗╔╔╦╗
╚╦╝║ ║║ ║╠╦╝  ╠═╣╠═╣║║║ ║║
 ╩ ╚═╝╚═╝╩╚═  ╩ ╩╩ ╩╝╚╝═╩╝
 """
        
    def makeascii(self):
        num1 = self.own1
        if num1 == 10:
            num1 = "K"

        num2 = self.own2
        if num2 == 10:
            num2 = "K"

        symbolList = ["♠", "♥", "♦", "♣"]

        self.ascii1 = f"""
┌─────────┐
│{num1}        │
│         │
│         │
│    {random.choice(symbolList)}    │
│         │
│         │
│        {num1}│
└─────────┘"""
        
        self.ascii2 = f"""
┌─────────┐
│{num2}        │
│         │
│         │
│    {random.choice(symbolList)}    │
│         │
│         │
│        {num2}│
└─────────┘"""
        

    def output(self):
        print(self.title)
        print(self.ascii1 + self.ascii2)

        


        
        






dealer = dealerHand(0,0)
ownhand = ownHand(0,0,"","","")

dealer.makeDealer()

ownhand.makeHand()

ownhand.makeascii()

ownhand.output()

























