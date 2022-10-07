import Dice
from time import sleep
from random import randint, shuffle
from termcolor import cprint, colored

def chooseColor(diceColor):
    if diceColor == 'Verde':
        return 'green'
    elif diceColor == 'Amarelo':
        return 'yellow'
    else:
        return 'red'

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def turn(self):
        dices = Dice.makeDices()
        dicesInHand = []
        tempscore = {'brains': 0, 'shots': 0}
        cprint(f" Vez de {self.name}! ".center(50, '='), 'green', attrs=['bold'])
        while 1:
            input(colored("pressione enter para continuar", 'white', attrs=['bold']))
            sleep(0.3)
            
            while len(dicesInHand) < 3:
                dicesInHand.append(dices.pop())
            
            n = 1
            for i in range(2, -1, -1):
                cprint("=" * 50, 'green')
                cprint(f"Jogando dado {n}...".center(50, ' '), 'green', attrs=['bold'])
                n += 1
                sleep(0.5)
                
                choosedDice = dicesInHand[i]
                choosedDice.roll()
                choosedSide = choosedDice.sides[randint(0,5)]
                cprint(f"Dado: {choosedDice.color} --- Face: {choosedSide}\n".center(50, ' '), chooseColor(choosedDice.color), attrs=['bold'])
                
                if choosedSide == 'shot':
                    cprint("Tiro de shotgun!\n".center(50, ' '), 'red', attrs=['bold'])
                    tempscore['shots'] += 1
                    dices.append(dicesInHand.pop(i))
                elif choosedSide == 'brain':
                    cprint("Céééérebro...\n".center(50, ' '), 'magenta', attrs=['bold'])
                    tempscore['brains'] += 1
                    dices.append(dicesInHand.pop(i))
                else:
                    cprint("O humano fugiu!\n".center(50, ' '), 'yellow', attrs=['bold'])
                cprint("=" * 50, 'green')
                
            if tempscore['shots'] >= 3:
                cprint(f"Você morreu (de novo). Cérebros perdidos: {tempscore['brains']}".center(50, ' '), 'red', attrs=['bold'])
                break
            else:
                cprint(f"Cérebros atuais: {tempscore['brains']} --- Tiros atuais: {tempscore['shots']}".center(50, ' '), 'green', attrs=['bold'])
                if input("Gostaria de continuar? (s/n)\n-> ").lower() == 'n':
                    self.score += tempscore['brains']
                    cprint(f"Passando a vez! Pontuação: {self.score}".center(50, ' '), 'green', attrs=['bold'])
                    break
                else:
                    cprint("Continuando...", 'green')
                
    
    
def makePlayers() -> list:
    players = []
    while 1:
        try:
            num_players = int(input(colored("Digite quantos jogadores irão jogar (2 a 10): ", 'magenta', attrs=['bold'])))
            if num_players > 1 and num_players < 10:
                break
            else:
                raise Exception
        except:
            cprint("Digite um número válido.", 'red', attrs=['bold'])
    
    for i in range(num_players):
        name = input(colored(f"Nome do jogador {i+1}: ", 'magenta', attrs=['bold'])).capitalize()
        player = Player(name)
        players.append(player)
        
    shuffle(players)
    cprint(" Ordem aleatória para jogar ".center(50, '='), 'green', attrs=['bold'])
    for i, player in enumerate(players):
        cprint(f"{i+1}: {player.name}".center(50, ' '), 'green', attrs=['bold'])
    cprint("=" * 50, 'green', attrs=['bold'])
    
    return players
