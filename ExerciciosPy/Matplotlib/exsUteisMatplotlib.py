import numpy as np
import matplotlib.pyplot as plt
import math
import random

# =============================================================================
# EX 1
# fig, eixo = plt.subplots(nrows=1, ncols=3, figsize=(40, 12))
# x = np.linspace(-3, 3, 100)
# 
# seno = [math.sin(number) for number in x]
# cosseno = [math.cos(number) for number in x]
# tang = [math.tan(number) for number in x]
# 
# 
# eixo[0].plot(x, seno, label="Seno", color="black")
# eixo[0].legend(fontsize=35)
# eixo[0].tick_params(labelsize=35)
# 
# eixo[1].plot(x, cosseno, label="Cosseno", color="purple")
# eixo[1].legend(fontsize=35)
# eixo[1].tick_params(labelsize=35)
# 
# eixo[2].plot(x, tang, label="Tangente", color="blue")
# eixo[2].legend(fontsize=35)
# eixo[2].tick_params(labelsize=35)
# =============================================================================
# =============================================================================
# EX 2
# fig, eixo = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))
# 
# labels = ["Araucária", "Campo Largo", "Colombo", "Fazenda Rio Grande", "Pinhais", "São José dos Pinhais"]
# val = [141410, 130091, 240840, 98368, 130789, 317476]
# 
# p, tx, autotexts = plt.pie(val, labels=labels, autopct="", shadow=True)
# for i, a in enumerate(autotexts):
#     a.set_text(f"{val[i]} hab.")
# =============================================================================

# =============================================================================
# EX 3
# def getRandomY():
#     return random.random()
# 
# points = np.linspace(0, 20, 40)
# eixoY = [getRandomY() for point in points]
# 
# plt.plot(points, eixoY, color="black")
# 
# # calculo da media e DP
# media = np.full((40,), np.mean(eixoY))
# dpPos = np.full((40,), media + np.std(eixoY))
# dpNeg = np.full((40,), media - np.std(eixoY))
# 
# plt.plot(points, media, label='media', color="blue")
# plt.plot(points, dpPos, label='DP', color="blue", linestyle="dotted")
# plt.plot(points, dpNeg, label='DP', color="blue", linestyle="dotted")
# =============================================================================
# =============================================================================
# EX 4
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# # temperaturas máxima média e mínima média (em graus Celsius)
# temp_max = [26.8,	26.8,	26,	24,	20.8,	20.1,	19.7, 21.5,	21.4,	23.1,	25,	26.2]
# temp_min = [17.2,	17.4,	16.5,	14.6,	11.2,	9.7, 9, 9.6, 11.1,	13.2,	14.9,	16.2]
# 
# fig1,ax1 = plt.subplots(figsize=(10,4))
# ax1.grid(zorder=0, linestyle='solid')
# plt.axis(xmin=0, xmax=11, ymin=0, ymax=30)
# plt.plot(meses, temp_max, marker='o', color="red")
# plt.fill_between(meses, temp_max, temp_min, color="red")
# plt.plot(meses, temp_min, marker='o', color="blue")
# plt.fill_between(meses, temp_min, color="blue")
# 
# plt.tight_layout()
# plt.show()
# =============================================================================
