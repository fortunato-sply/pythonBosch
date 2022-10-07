from random import randint
import pandas as pd
import matplotlib.pyplot as plt

def ex1():
    def isTriangle(a, b, c) -> bool:
        if (abs(b-c) < a < b + c) and (abs(a-c) < b < a + c) and (abs(a-b) < c < a + b):
            return True
        
        return False
    
    def typeofTriangle(a, b, c) -> str:
        if a == b == c:
            return 'equilátero'
        elif a == b or a == c or b == c:
            return 'isósceles'
        else:
            return 'escaleno'
    
    a = int(input("Digite o lado A: "))
    b = int(input("Digite o lado B: "))
    c = int(input("Digite o lado C: "))
    
    if isTriangle(a, b, c):
        print(f"É um triângulo {typeofTriangle(a, b, c)}")
    else:
        print("Isso não é um triângulo!")

def ex2():
    times = {'Palmeiras': 30, 'Corinthians': 24, 'Fluminense': 17, 'Vasco da Gama': 12}
    
    rounds = int(input("Insira o número de rodadas: "))
    points = [3, 0, 1]
    for i in range(rounds):
        for key, value in times.items():
            print(f"\nResultado da partida para {key}\n1 - Vitória\n2 - Derrota\n3 - Empate")
            result = int(input("-> "))
            times[key] += points[result-1]
    
    bestTeam = max(times.keys(), key=(lambda k: times[k]))
    bestScore = times[max(times, key=times.get)]
    print(f"\nO time com maior pontuação é o {bestTeam} com {bestScore}")

def ex3():
    def sumAlg(n) -> int:
        if n <= 0:
            raise Exception
        else:
            soma = 0
            for number in str(n):
                soma += int(number)
            
            return soma
    
    try:
        n = int(input("Digite um número maior que zero: "))
        result = sumAlg(n)
        print(f"A soma dos algarismos é igual a {result}")
    except:
        print("Número inválido.")
    
def ex4():
    feedback = ['a', 'e', 'c', 'd', 'b', 'a', 'b', 'e', 'c', 'd']
    note = 0
    wrongAnswers = []
    
    for i in range(10):
        answer = input(f"Qual a sua resposta para a questão {i+1}? -> ").lower()
        if answer == feedback[i]:
            note += 1
        else:
            
            wrongAnswers.append(i+1)
    
    print(f"\nSua nota foi {note}.\nVocê errou as respostas: {wrongAnswers}")

def ex5():
    generated = randint(1,1000)
    attempts = 0
    entry = 0
    while entry != generated:
        attempts += 1
        entry = int(input("\nTente acertar o número sorteado: "))
        if generated+3 >= entry >= generated-3:
            print("Quase lá!")
        elif entry > generated:
            print("Muito alto!")
        elif entry < generated:
            print("Muito baixo!")
            
    print(f"\nParabéns, você acertou! O número é {generated}.\nForam necessárias {attempts} tentativas.")
    
ex5()

def ex6():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001'}
    
    def encryptPassword(password: str) -> str:
        encrypted = []
        for char in password:
            if char in ['-', '_', '!', '@', '?', '(', ')']:
                encrypted.append(0)
            elif char in alfabeto:
                index = alfabeto.index(char)
                if index > 9:
                    for n in str(index):
                        encrypted.append(n)
                else:
                    encrypted.append(index)
            else:
                encrypted.append(char)
        
        for i, char in enumerate(encrypted):
            encrypted[i] = numeros[int(char)]
        
        encrypted = '_'.join(encrypted)
        return encrypted
    
    password = input("Insira a senha para ser codificada: ")
    encryptedPassword = encryptPassword(password)
    print(f"Codificação = {encryptedPassword}")

def ex7():
    class Student:
        def __init__(self, name: str, grades: list):
            self.name = name
            self.grades = grades
            
    
    def createStudent() -> Student:
        name = input("Nome do aluno: ").capitalize()
        
        grades = []
        nGrades = int(input("Número de notas a serem cadastradas: "))
        for i in range(nGrades):
            grade = float(input(f"Nota {i+1}: "))
            grades.append(grade)
        
        return Student(name, grades)
    
    def menu():
        print(' ESCOLA PAIXÃO '.center(70, '='))
        while 1:
            option = int(input(("1 - Cadastrar alunos\n2 - Exibir alunos e/ou mostrar médias\n0 - Sair\n-> ")))
            
            if option == 1:
                while 1:
                    student = createStudent()
                    
                    alunosDb = open("alunos.txt", "r+")
                    content = alunosDb.readlines()
                    content.append(f"{student.name} {student.grades}\n")
                    
                    alunosDb = open('alunos.txt', 'w')
                    alunosDb.writelines(content)
                    alunosDb.close()
                    
                    if input("Deseja cadastrar mais alunos? (s/n): ").lower() == 'n':
                        break
            elif option == 2:
                while 1:
                    alunosDb = open("alunos.txt", "r+")
                    content = alunosDb.readlines()
                    
                    names = []
                    for line in content:
                        name = line[:line.index('[')].strip()
                        names.append(name)
                    
                    print("\nNomes:")
                    for i, name in enumerate(names):
                        if i+1 != len(names):
                            print(f"{name}, ", end='')
                        else:
                            print(name, end='')
                            
                    name = input("Escolha um aluno: ").capitalize()
                    if name not in names:
                        print("O aluno em questão não está cadastrado.")
                    else:
                        for line in content:
                            if name in line:
                                grades = line[line.index('['):-1]
                        grades = list(grades)
                        for i, char in enumerate(grades):
                            if char in ['[', ']', ',', '\n', ' ']:
                                grades.pop(i)
                        
                        grades = ''.join(grades)
                        grades = grades.split()
                        
                        mean = 0
                        for grade in grades:
                            mean += float(grade)
                        mean = mean/len(grades)
                        print(f"\nMédia de {name} em {len(grades)} notas: {mean:.2f}")
                        
                    if input("Deseja consultar mais notas? (s/n): ").lower() == 'n':
                        alunosDb.close()
                        break
            else:
                break
            
    menu()

# EX 8 - MATPLOTLIB
# netflix = pd.read_csv('data/netflix_titles.csv')
# netflix = netflix.dropna()
# netflixMovies = netflix.loc[(netflix['type']=='Movie') & (netflix['country']=='United States') & (netflix['release_year'] <= 2020) & (netflix['release_year'] >= 2015)]

# y = [netflixMovies.show_id[netflix['release_year'] == i].count() for i in range(2015,2021)]
# plt.bar([i for i in range(2015,2021)], y, color='black', zorder=2)
# plt.grid(zorder=0, linestyle='solid', color="gray")
# plt.title('Filmes americanos 2015 - 2020')

# def convertToInt(line):
#     return int(line[:line.index('m')])

# # FILMES BRASILEIROS
# filmesBr = netflix.loc[(netflix['type']=='Movie') & (netflix['country']=='Brazil')]
# filmesBr['duration'] = filmesBr['duration'].apply(convertToInt)
# filmesMaisLongos = filmesBr.sort_values(by=['duration'], ascending=False)
# nomes = filmesMaisLongos.title.values[:5]
# for i, nome in enumerate(nomes):
#     print(f"{i+1}: {nome}")
