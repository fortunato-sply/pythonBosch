from Player import makePlayers
from termcolor import colored, cprint
from Texts import textZombieDice

def victory(player):
    cprint('=' * 50 + f"\nVitória!!!\nVencedor: {player.name}", 'green', attrs=['bold'])
    
    cprint("\nPlacar final:".center(50, ' '), 'blue', attrs=['bold'])
    for player in players:
        cprint(f"{player.name}: {player.score} pontos.".center(50, ' '), 'blue', attrs=['bold'])
        

def placar():
    cprint(' PLACAR '.center(50, '='), 'blue', attrs=['bold'])
    for player in players:
        cprint(f"{player.name}: {player.score} pontos".center(50, ' '), 'blue', attrs=['bold'])


def askToPlayAgain():
    if input("Gostaria de jogar novamente? (s/n) -> ") == 's':
        return True


def game():
    textZombieDice()
    print(colored("""
Bem-vindo! Nesse jogo, você é um zumbi faminto por cérebros! Vence quem conseguir comer 13 cérebros primeiro!
Mas cuidado, alguns civis tem espingardas! Bastam três tiros para voar pelos ares e perder todos os cérebros da rodada.
          
No jogo existem três dados: os verdes, vermelhos e amarelos.
Cada um tem seis faces, que variam entre cérebros, tiros e passos. Seguindo a lógica das cores, cada um tem uma dificuldade/chance maior para cada face.
Lembre-se! Caso a face seja 'pass' e o humano fuja, você vai jogar o mesmo dado caso queira continuar.
          
Para mais informações: https://gameplay.pt/pt/jogos-de-tabuleiro/1585-zombie-dice-837654320419.html
""".center(20, ' '), 'red', attrs=['bold']))
    
    global players
    players = makePlayers()
    
    gameOver = False
    while not gameOver:
        for player in players:
            player.turn()
            if player.score >= 13:
                victory(player)
                gameOver = True
                break
        
        if not gameOver:
            placar()
            
        
def playGame():
    playAgain = True
    while playAgain:
        game()
        playAgain = askToPlayAgain()

playGame()