from random import sample, randint

easyWords = []
mediumWords = []
hardWords = []

with open('palavras.txt') as wordsDb:
    for word in wordsDb:
        word = word.strip().lower()
        
        if len(word) <= 4:
            easyWords.append(word)
        elif len(word) <= 8:
            mediumWords.append(word)
        else:
            hardWords.append(word)

def askDifficulty():
    menu = '''1. Fácil: 4 letras\n2. Médio: 5 a 8 letras\n3. Difícil: mais de 8 letras\n'''.center(50, '-')
    while 1:
        try:
            print(menu)
            difficulty = int(input("Digite a dificuldade desejada: "))
            if difficulty in [1, 2, 3]:
                break
            else:
                raise Exception
        except:
            print("Digite uma opção válida.")
    
    return difficulty
    
    
def askPointsToLoss():
    while 1:
        try:
            pointsToLoss = int(input("Quantidade de pontos a perder a cada falha (10 a 100 pontos): "))
            if 10 <= pointsToLoss <= 100:
                break
            else:
                raise Exception
        except:
            print("Digite uma opção válida.")
    
    return pointsToLoss
    

def chooseWord(difficulty):
    if difficulty == 1:
        wordNumber = randint(0, len(easyWords) - 1)
        word = easyWords[wordNumber]
    elif difficulty == 2:
        wordNumber = randint(0, len(mediumWords) - 1)
        word = mediumWords[wordNumber]
    else:
        wordNumber = randint(0, len(hardWords) - 1)
        word = hardWords[wordNumber]
    
    return word


def shuffleWord(word):
    word = sample(word, len(word)) # Divide a palavra em uma lista, e posteriormente embaralha os index das letras.
    word = ''.join(word) # Une novamente a lista em string, já embaralhada
    return word


def game():
    print(" ANAGRAMA ".center(100, '-'))
    
    points = 100
    attempts = 0
    difficulty = askDifficulty()
    pointsToLoss = askPointsToLoss()
    word = chooseWord(difficulty)
    shuffledWord = shuffleWord(word)
    
    while points > 0:
        print('=' * 30)
        print(f"Tentativas: {attempts}\nPontos restantes: {points}\nPalavra: {shuffledWord}")
        print('=' * 30)
        attempts += 1
        answer = input("-> ").lower()
        
        if answer == word:
            print("Você venceu!!!")
            print('=' * 30)
            break
        else:
            points -= pointsToLoss
            print(f"Errou! Pontos restantes: {points}")
            print('=' * 30)
        
        if points < 1:
            print('=' * 30)
            print(f"Você perdeu!\nA palavra correta era: {word}\nMais sorte da próxima vez :)")
            print('=' * 30)
            break
    
game()