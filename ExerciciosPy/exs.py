# =============================================================================
# # values = []
#
# # n = 1
# # for i in range(0,10):
# #     value = input(f'Digite o valor {n}: ')
# #     values.append(value)
# #     n += 1
#
# # print(f"\nTamanho da lista: {len(values)}")
# # print("\nLista ordenada:")
#
# # def orderList(list):
# #     return list.sort(key=int)
#
# # orderList(values)
# # for i, value in enumerate(values):
# #     print(f"Valor {i+1}: {value}")
#
# # EX 5
#
# # richPeople = ("Elon Musk", "Jeff Bezos", "Bernard Arnault", "Bill Gates", "Warren Buffett", "Larry Page", "Sergey Brin", "Larry Ellison", "Steve Ballmer", "Mukesh Ambani")
#
# # print(f"Os 10 mais ricos do mundo são: {richPeople}\n\nOs 3 mais ricos do mundo são: {richPeople[:3]}\n\nO mais rico do mundo é: {richPeople[0]}")
# =============================================================================

# =============================================================================
# # EX 6
#
# # class Fastfood:
# #     def __init__(self):
# #         self.menu = {
# #                 'Hamburguer': 10,
# #                 'Hotdog': 6.5,
# #                 'Salada': 4,
# #                 'Suco': 4,
# #                 'Refrigerante': 4.5,
# #                 'Água': 2,
# #             }
#
# #         self.cart = 0
#
# #     def fazerPedido(self):
# #         while True:
# #             print(f"Valor atual do carrinho: R${self.cart:.2f}")
#
# #             print('Escolha o item:')
#
# #             n = 1
# #             for item in self.menu:
# #                 print(f"{n}: {item}: R${self.menu[item]:.2f}")
# #                 n += 1
#
# #             try:
# #                 item = int(input('Número do item: ')) - 1
#
# #                 self.cart += list(self.menu.values())[item]
# #             except:
# #                 print("Erro no pedido.")
#
# #             if input('Deseja adicionar mais itens? (S/N): ').upper() == 'N':
# #                 break
#
# #     def fecharPedido(self):
# #         print(f"Fim do pedido. Valor total: R${self.cart:.2f}")
#
#
# # fastfood = Fastfood()
# # fastfood.fazerPedido()
# # fastfood.fecharPedido()
# =============================================================================

# =============================================================================
# # EX 7
#
# # from random import randint
# # secretNumber = randint(0,10)
#
# # while True:
# #     try:
# #         number = int(input("Tente adivinhar um número de 0 a 10: "))
#
# #         if number == secretNumber:
# #             print(f"Você acertou! O número sorteado foi o {secretNumber}.")
# #             break
# #     except:
# #         print('Erro! Digite um número.')
# =============================================================================

# =============================================================================
# # EX 8
#
# # from datetime import date
#
# # try:
# #     bornAge = int(input("Digite seu ano de nascimento: "))
# # except:
# #     print("Erro: O ano precisa ser um inteiro numeral.")
#
# # actualYear = date.today().year
#
# # age = actualYear - bornAge
# # print(f"Você tem {age} anos.")
#
# # if age < 16:
# #     print("Impossível votar!")
# # elif age >= 16 and age <= 18 or age >= 70:
# #     print("Voto facultativo. Gostaria de votar?")
# # else:
# #     print("Voto obrigatório.")
#
# # EX 9
#
# # limit = int(input("Digite o limite para a soma de valores: ")) + 1
#
# # total = 0
# # for i in range(limit):
# #     total += i
# #     if i != limit - 1:
# #         print(f"{i} + ", end= '')
# #     else:
# #         print(f"{i} = {total}", end= '')
#
# # print(f"\nTotal da soma: {total}.")
# =============================================================================

# =============================================================================
# =============================================================================
# EX 10

def somar(n1, n2):
    return n1 + n2

def subtr(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divi(n1, n2):
    return n1 / n2

menu = """
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
0. Sair
"""

while 1:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input("Digite o segundo número: "))

        print(menu)
        while 1:
            op = int(input("Digite uma operação: "))
            if op in [1, 2, 3, 4]:
                    result = somar(n1, n2) if op == 1 else subtr(n1, n2) if op == 2 else multi(n1, n2) if op == 3 else divi(n1, n2) if op == 4 else None
                    break
            if op == 0:
                raise Exception
            else:
                print('Operação inválida.')
        print(f"Resultado: {result}")
        if input("Deseja continuar? (S/N): ").lower() == 'n':
            break
        
    except ValueError:
        print("Você precisa digitar um número!")
    except ZeroDivisionError:
        print("Impossivel dividir por 0.")
    except Exception:
        print("Obrigado!")
        break
# =============================================================================
# =============================================================================

# =============================================================================
# # EX 11
# # for i in range(0,31):
# #     if i%2 == 0:
# #         print(i)
# =============================================================================

# =============================================================================
# # EX 12
# while 1:
#     try:
#         number = int(input("Digite um número inteiro positivo: "))
#         if number > 0:
#             break
#     except:
#         print("Digite um número válido.")
#
# for i in range(number):
#     for i in range(number - 1):
#         print('x ', end='')
#     print('x')
#
# =============================================================================

# =============================================================================
# EX 13
# while 1:
#     try:
#         number = int(input("Digite um número inteiro positivo: "))
#         if number > 0:
#             break
#     except:
#         print("Digite um número válido.")
#
# if (number==1) or (number==2):
#     print("1")
# else:
#     last = 0
#     penultimate = 1
#     for i in range(1, number):
#         term = last + penultimate
#         penultimate = last
#         last = term
#         print(term)
# =============================================================================
# =============================================================================
# # EX 14
# 
# from random import randint
# 
# 
# print("="*30, "\nNOVO JOGO\n" + "="*30)
# 
# 
# def askOption():
#     while 1:
#         try:
#             op = int(input("1. Par\n2. Ímpar\nEscolha: "))
#             if op in [1, 2]:
#                 choose = 'pair' if op == 1 else 'odd'
#                 break
#             else:
#                 int("")
#         except:
#             print("Digite uma opção válida.")
# 
#     return choose
# 
# 
# def askNumber():
#     while 1:
#         try:
#             number = int(input("Digite um número inteiro positivo: "))
#             if number > 0:
#                 break
#         except:
#             print("Digite um número válido.")
# 
#     return number
# 
# 
# def match(choose, number):
#     global wins
#     cpuChoosen = randint(0, 6)
#     resultNumber = cpuChoosen + number
#     print(f"\nO computador jogou: {cpuChoosen}")
#     print(f"\nResultado: {resultNumber}")
# 
#     result = resultNumber % 2
#     if result == 0:
#         if choose == 'pair':
#             print('Você venceu!')
#             wins += 1
#             print("="*30 + f"\nVitórias: {wins}\n" + "="*30)
#             return True, wins
#         else:
#             print('Você perdeu.')
#             print("="*30 + f"\nVitórias: {wins}\n" + "="*30)
#             return False
#     else:
#         if choose == 'odd':
#             print('Você venceu!')
#             wins += 1
#             print("="*30 + f"\nVitórias: {wins}\n" + "="*30)
#             return True
#         else:
#             print('Você perdeu.')
#             print("="*30 + f"\nVitórias: {wins}\n" + "="*30)
#             return False
# 
# 
# def askToPlayAgain():
#     if input("Continuar? (s/n): ").lower() != 'n':
#         return True
# 
# 
# def game():
#     global wins
#     wins = 0
#     playAgain = True
#     while playAgain:
#         choose = askOption()
#         number = askNumber()
#         matchResult = match(choose, number)
#         if matchResult:
#             playAgain = askToPlayAgain()
#         else:
#             break
# 
# 
# game()
# =============================================================================

# =============================================================================
# # EX 15
# from time import sleep
# 
# def contador(inicio, fim, passo):
#     if inicio > fim:
#         passo = passo * (-1)
#         fim -= 2
#     for i in range(inicio, fim+1, passo):
#         print(i)
#         sleep(0.3)
#         
# 
# inicio = int(input("Digite o início do contador: "))
# fim = int(input("Digite o final do contador: "))
# passo = int(input("Digite o passo do contador: "))
# contador(inicio, fim, passo)
# =============================================================================

# =============================================================================
# # EX 16
# import math
# 
# def operations(num):
#     return {'Raiz quadrada': math.sqrt(num), 'Quadrado': num*num, 'Inverso': num**-1, 'Fatorial': math.factorial(num)}
# 
# num = int(input("Digite um valor: "))
# print(operations(num))
# =============================================================================

# =============================================================================
# # EX 17
# from random import randint
# 
# def createRandomList(inferior, superior, length):
#     list = []
#     for i in range(length):
#         num = randint(inferior, superior)
#         list.append(num)
#     
#     orderedList = list[:]
#     for i in range(len(orderedList)):0,
#         for j in range(len(orderedList)):
#             if orderedList[j] > orderedList[i]:
#                 orderedList[j], orderedList[i] = orderedList[i], orderedList[j]
#     
#     return list, orderedList
#                 
# inferior = int(input("Digite o limite inferior: "))
# superior = int(input("Digite o limite superior: "))
# length = int(input("Digite o tamanho da lista: "))
# 
# listas = createRandomList(inferior, superior, length)
# print(f"LISTA: {listas[0]}\nLISTA ORDENADA: {listas[1]}")
# =============================================================================
