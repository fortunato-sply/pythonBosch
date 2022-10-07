# =============================================================================
# EX1
from random import sample
# 
# tupla = tuple(sample(range(0, 10), 5))
# print(f"Tupla: {tupla}")
# print(f"\nMaior valor: {max(tupla)} - Menor valor: {min(tupla)}")
# 
# times5 = tupla.count(5)
# try:
#     position2 = tupla.index(2)
# except:
#     position2 = -1
# 
# print(f"O número 5 aparece {times5} vez(es).\nO primeiro número 2 aparece na posição {'n/a' if position2 == -1 else position2}.")
# 
# =============================================================================
# =============================================================================
# EX2
# peso, altura = float(input("Digite o peso da pessoa: ")), float(input("Digite a altura da pessoa: "))
# 
# imc = peso/(altura**2)
# classificacao = 'Magreza' if imc < 18.5 else 'Normal' if 18.5 <= imc <= 24.9 else 'Sobrepeso' if 25 <= imc <= 29.9 else 'Obesidade' if 30 <= imc <= 39.9 else 'Obesidade grave' if imc > 40 else 'Erro'
# print(f"\nO IMC da pessoa é de {imc:.2f}.\nE está classificada como {classificacao}")
# =============================================================================
# =============================================================================
# EX3
# matheus_alt = 1.5
# jose_alt = 1.1
# 
# anos = 0
# while jose_alt < matheus_alt:
#     matheus_alt += 0.02
#     jose_alt += 0.03
#     anos += 1
# k
# print(f"Levará {anos} anos para José ser maior que Matheus.\nAltura de José: {jose_alt:.2f}m\nAltura de Matheus: {matheus_alt:.2f}m")
# =============================================================================
# =============================================================================
# EX4
# while 1:
#     try:
#         ano = int(input("Digite um ano para verificar se é bissexto: "))
#         break
#     except:
#         print("Digita um ano ai po!")
#         
# print("Bissexto" if ((ano % 4 == 0) and (ano % 400 == 0)) or (ano % 400 != 0) else "Não é bissexto")
# =============================================================================
# =============================================================================
# EX5
# from math import sqrt
# def verificarQP(num):
#     if int(sqrt(num)) == sqrt(num):
#         return True
#     else:
#         return False
# 
# print(verificarQP(16))
# =============================================================================
# =============================================================================
# EX6
# pessoas = {}
# 
# for i in range(5):
#     nome = input(f"Nome pessoa 0{i+1}: ").capitalize()
#     altura = float(input(f"Altura pessoa 0{i+1}: "))
#     pessoas[nome] = altura
# 
# maisAlta, maisBaixa = max(pessoas.keys(), key=(lambda k: pessoas[k])), min(pessoas.keys(), key=(lambda k: pessoas[k]))
# print(f"\nPessoa mais alta: {maisAlta}\nPessoa mais baixa: {maisBaixa}")
# 
# =============================================================================