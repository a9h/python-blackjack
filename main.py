import random
import os
import time











class Hand:
    def __init__(self,number1,number2,number3,title,card1,card2,card3,drawThird) -> None:
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.title = title
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.drawThird = drawThird
        






    def makeHand(self):
        self.number1 = random.randint(1,11)
        self.number2 = random.randint(1,11)
        self.number3 = random.randint(1,11)

        self.title = """
╦ ╦╔═╗╦ ╦╦═╗  ╦ ╦╔═╗╔╗╔╔╦╗
╚╦╝║ ║║ ║╠╦╝  ╠═╣╠═╣║║║ ║║
 ╩ ╚═╝╚═╝╩╚═  ╩ ╩╩ ╩╝╚╝═╩╝
"""

        self.dealertitle = """
╔╦╗╔═╗╔═╗╦  ╔═╗╦═╗╔═╗  ╦ ╦╔═╗╔╗╔╔╦╗
 ║║║╣ ╠═╣║  ║╣ ╠╦╝╚═╗  ╠═╣╠═╣║║║ ║║
═╩╝╚═╝╩ ╩╩═╝╚═╝╩╚═╚═╝  ╩ ╩╩ ╩╝╚╝═╩╝
"""
        
    def makecard(self):
        num1 = self.number1
        if num1 == 10:
            num1 = "K"
        elif num1 == 1 or num1 == 11:
            num1 = "A"

        num2 = self.number2
        if num2 == 10:
            num2 = "K"
        elif num2 == 1 or num2 == 11:
            num2 = "A"
        

        num3 = self.number3
        if num3 == 10:
            num3 = "K"
        elif num3 == 1 or num3 == 11:
            num3 = "A"





        symbolList = ["♠", "♥", "♦", "♣"]
        self.card1 = [
            
            "┌─────────┐",
            f"│{num1}        │",
            "│         │",
            "│         │",
            f"│    {random.choice(symbolList)}    │",
            f"│         │",
            "│         │",
            f"│        {num1}│",
            "└─────────┘"]
        








        self.card2 = [

            """┌─────────┐""",
            f"""│{num2}        │""",
            f"│         │",
            "│         │",
            f"│    {random.choice(symbolList)}    │",
            "│         │",
            "│         │",
            f"│        {num2}│",
            "└─────────┘"]
        




        self.blankcard = ['┌─────────┐', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '└─────────┘']
        





        self.card3 = [

            """┌─────────┐""",
            f"""│{num3}        │""",
            f"│         │",
            "│         │",
            f"│    {random.choice(symbolList)}    │",
            "│         │",
            "│         │",
            f"│        {num3}│",
            "└─────────┘"]




    def prBlankcard(self):
        counter = -1

        while counter != 8:
            
            counter += 1 

            print(self.blankcard[counter])



    def print3rd(self):
        counter = -1

        while counter != 8:
            
            counter += 1 

            print(self.card3[counter])



    def output(self):




        counter = -1

        while counter != 8:
            
            counter += 1 

            print(self.card1[counter] + self.card2[counter])



    def dealerOutput(self):




        counter = -1

        while counter != 8:
            
            counter += 1 

            print(self.blankcard[counter] + self.card2[counter])


    
        
        
            

        



        










def makeHands():

    dealer.makeHand()

    dealer.makecard()

    ownhand.makeHand()

    ownhand.makecard()





























def hit():


    os.system("clear")
    print("""


╔╦╗╔═╗╔═╗╦  ╦╔╗╔╔═╗  ╔╗╔╔═╗╦ ╦  ╔═╗╔═╗╦═╗╔╦╗
 ║║║╣ ╠═╣║  ║║║║║ ╦  ║║║║╣ ║║║  ║  ╠═╣╠╦╝ ║║
═╩╝╚═╝╩ ╩╩═╝╩╝╚╝╚═╝  ╝╚╝╚═╝╚╩╝  ╚═╝╩ ╩╩╚══╩╝


""")
    time.sleep(0.8)
    os.system("clear")

    ownhand.output()
    ownhand.prBlankcard()

    input("...")
    os.system("clear")
    ownhand.output()
    ownhand.print3rd()

    if (ownhand.number1 + ownhand.number2 + ownhand.number3) > 21:
        if ownhand.number1 == 11 or ownhand.number2 == 11 or ownhand.number3 == 11:
            pass
        else:
            print("You went bust!")
            exit()

        
    
    print("new card drawn!")
    ownhand.drawThird = True
        

    







def choices():
    os.system("clear")
    print(ownhand.title)
    ownhand.output()
    while True:
        choice = input("/: ")

        match choice:
            
            case ">":
                os.system("clear")
                print(dealer.dealertitle)
                dealer.dealerOutput()

            case "<":
                os.system("clear")
                print(ownhand.title)
                if ownhand.drawThird == True:
                    ownhand.output()
                    ownhand.print3rd()
                else:
                    ownhand.output()
                print("HIT or STAND?")

            case "hit":
                hit()

            case "stand":
                pass








def start():

    print("""


 ▄█     █▄     ▄████████  ▄█        ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ 
███     ███   ███    ███ ███       ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ 
███     ███   ███    █▀  ███       ███    █▀  ███    ███ ███   ███   ███   ███    █▀  
███     ███  ▄███▄▄▄     ███       ███        ███    ███ ███   ███   ███  ▄███▄▄▄     
███     ███ ▀▀███▀▀▀     ███       ███        ███    ███ ███   ███   ███ ▀▀███▀▀▀     
███     ███   ███    █▄  ███       ███    █▄  ███    ███ ███   ███   ███   ███    █▄  
███ ▄█▄ ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███   ███   ███   ███    ███ 
 ▀███▀███▀    ██████████ █████▄▄██ ████████▀   ▀██████▀   ▀█   ███   █▀    ██████████ 
                         ▀                                                            

""")

    a = input("Continue...\n[Y/N]: ")

    if a.lower() == "y":
        print("Starting!")
    else:
        print("No Choice!")




    makeHands()
    choices()

    
dealer= Hand(0,0,0,"","","","", False)
ownhand = Hand(0,0,0,"","","","", False)


start()
    























