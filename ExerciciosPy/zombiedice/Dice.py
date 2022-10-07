from random import shuffle

class Dice():
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color
    
    def roll(self):
        shuffle(self.sides)

def makeDices():
    green = Dice(['brain', 'brain', 'brain', 'pass', 'pass', 'shot'], 'Verde')
    yellow = Dice(['brain', 'brain', 'pass', 'pass', 'shot', 'shot'], 'Amarelo')
    red = Dice(['brain', 'pass', 'pass', 'shot', 'shot', 'shot'], 'Vermelho')
    
    dices = []
    for _ in range(6):
        dices.append(green)
    for _ in range(4):
        dices.append(yellow)
    for _ in range(3):
        dices.append(red)
    
    shuffle(dices)
    return dices
