# Lucas Vinícius Fortunato

from random import choice

def ex1():
    lista = ['1_palmeiras', '2_coritiba', '1_corinthians', '3_juventude', '2_fluminense', '3_bahia', '1_cuiaba', '2_cascavel', '3_ponte preta', '2_parana clube', '3_voltaredonda']
    primDiv, segDiv, tercDiv = [], [], []
    for time in lista:
        time = time.split('_')
        if int(time[0]) == 1:
            primDiv.append(time[1])
        elif int(time[0]) == 2:
            segDiv.append(time[1])
        else:
            tercDiv.append(time[1])
    
    print(f"Primeira divisão: {primDiv}\nSegunda divisão: {segDiv}\nTerceira divisão: {tercDiv}")
    
def ex2():
    import numpy as np
    
    matriz = np.random.randint(9, size=(5, 5))
    print(f"Array original:\n{matriz}")
    
    registro = open('registrosEx2.txt', 'r')
    cont = int(registro.read())
    
    for i in range(5):
        for j in range(5):
            if matriz[i][j] % 2 != 0:
                matriz[i][j] = matriz[i][j] ** 2
                cont += 1
    
    registro = open('registrosEx2.txt', 'w')
    registro.write(str(cont))
    registro.close()
    print(f"Array substituindo os números ímpares:\n{matriz}")
    print(f"Existem {cont} registros.")

def ex3():
    def receberFrases():
        numFrases = int(input("Quantas frases deseja verificar? "))
        frases = [input(f"Insira a {i+1}º frase\n-> ").lower() for i in range(numFrases)]
        return frases
    
    def isPalindromo(frase):
        frase = frase.split(' ')
        frase = ''.join(frase)
        i = 0
        j = len(frase) - 1
        
        while i != j:  
            if frase[i] != frase[j]:
                return False
            else:
                i+=1
                j-=1
        
        return True
    
    frases = receberFrases()
    palindromos = []
    for frase in frases:
        if isPalindromo(frase):
            palindromos.append(frase.capitalize())
    
    print("\nSão palindromos:\n")
    for frase in palindromos:
        print(frase)

def ex4():
    def notas(*notas, sit = False):
        resumo = {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': round(sum(notas)/len(notas), 2)}
        if sit == True:
            resumo['situação'] = 'Boa' if resumo['média'] >= 7 else 'Razoável' if 5 <= resumo['média'] < 7 else 'Ruim'
        print(resumo)
    
    notas(5.5, 2.5, 1.5)
    notas(5.5, 2.5, 9.9, sit=True)

def ex5():
    def sacar(valor):
        if valor < 10 or valor > 600:
            raise Exception
        
        n100, n50, n10, n5, n1 = 0, 0, 0, 0, 0
        while valor >= 1:
            if valor >= 100:
                n100 += 1
                valor -= 100
            elif valor >= 50:
                n50 += 1
                valor -= 50
            elif valor >= 10:
                n10 += 1
                valor -= 10
            elif valor >= 5:
                n5 += 1
                valor -= 5
            else:
                n1 += 1
                valor -= 1
        
        print(f"Notas para saque:\n{n100} de R$100,00\n{n50} de R$50,00\n{n10} de R$10,00\n{n5} de R$5,00\n{n1} de R$1,00\n")
                
    while 1:
        try:
            sacar(float(input("Insira qual valor deseja sacar: (mínimo R$10,00)\n-> ")))
            break
        except:
            print("Valor não correspondente")

# EX 6
import pandas as pd
import matplotlib.pyplot as plt
    
superheroes = pd.read_csv('superheroes.csv').dropna()
creators = superheroes['creator'].unique()
strength = []

for creator in creators:
    mean = 0
    quant = 0
    x = superheroes[superheroes['creator'] == creator].strength_score.value_counts()
    for i in range(len(x.values)):
        mean += x.values[i] * x.index.values[i]
        quant += x.values[i]
    
    mean = mean/quant
    strength.append(mean)

plt.bar(creators, strength, color='black', zorder=2)
plt.grid(zorder=0, linestyle='solid', color="gray")
plt.xticks(rotation=45)
plt.ylabel("Strength Mean")

immortals = superheroes[superheroes["has_immortality"] == 1].sort_values(by=['combat_score'], ascending=False).name.head(5).values
print("Os melhores imortais em combate são:")
for i, immortal in enumerate(immortals):
    print(f"{i+1} - {immortal}")

def ex7():
    class letraJaDigitada(Exception):
        pass
    
    class inputMaiorQue1Letra(Exception):
        pass
    
    def chutarLetra(tentativas, letra, palavra, aprPalavra: str):
        if letra in tentativas:
            raise letraJaDigitada()
        if len(letra) != 1 or letra.isdigit():
            raise inputMaiorQue1Letra()
        
        global pontos
        aprPalavra = list(aprPalavra)
        palavra = list(palavra)
        if letra in palavra:
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    aprPalavra[i] = letra
        else:
            pontos -= 1
        
        tentativas.append(letra)
        return aprPalavra
    
    banco = open('banco_de_palavras_padrao.txt', 'r', encoding='utf-8')
    palavras = banco.readlines()
    easy = palavras[0].split(',')
    medium = palavras[1].split(',')
    
    
    print("JOGO DA FORCA".center(50, '-'))
    while 1:
        try:
            dificuldade = int(input("Dificuldade:\n1. Fácil\n2. Médio/difícil\n-> "))
            if dificuldade not in [1, 2]:
                raise Exception
            
            if dificuldade == 1:
                palavra = choice(easy)
            else:
                palavra = choice(medium)
            break
        except:
            print("Digite uma opção válida.")

    tentativas = []
    global pontos
    pontos = 6
    aprPalavra = ['_' for _ in range(len(palavra))]
    while pontos > 0:
        print("\n", ' '.join(aprPalavra))
        try:
            tentativa = input(f"Vidas: {pontos}\nLetras já digitadas: {tentativas}\n\nChute uma letra: ")
            aprPalavra = chutarLetra(tentativas, tentativa, palavra, aprPalavra)
            
            if str(aprPalavra).find('_') == -1:
                print(f"Você venceu! A palavra era {palavra}.")
                break
            
            if pontos == 0:
                print(f"Você perdeu. A palavra era {palavra}.")
        except letraJaDigitada:
            print("Você já digitou esta letra!")
        except inputMaiorQue1Letra:
            print("Entrada inválida. Digite uma letra!")

ex7()