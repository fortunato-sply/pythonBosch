import itertools

word = input("Digite uma palavra para verificarmos a quantidade da mesma no texto: ").strip()
quant = 0

palavras = []
with open('arquivo.txt') as arquivo:
    for linha in arquivo:
        line = linha.split(' ')
        palavras.append(line)
        
listaPalavras = list(itertools.chain(*palavras))
for palavra in listaPalavras:
    if word == palavra:
        quant += 1

print(f"Vezes que a palavra {word} aparece: {quant}")