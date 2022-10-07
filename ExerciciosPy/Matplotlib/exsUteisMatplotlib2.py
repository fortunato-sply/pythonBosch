import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv('data/titanic.csv')

# graph 1 - BAR
survived = titanic.Survived[titanic["Survived"] == 1].count()
notSurvived = titanic.Survived[titanic["Survived"] == 0].count()

fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

eixo[0].bar(['Sobreviventes', 'Não-sobreviventes'], [survived, notSurvived], 0.7, color=["blue", "red"])
eixo[0].axis(ymin=0, ymax=600)
eixo[0].set_title("Sobreviventes", fontsize=20)
eixo[0].tick_params(axis='y', labelsize=15)
eixo[0].tick_params(axis='x', labelsize=10)

# graph 2 - PLOT
titanic["TotalParents"] = titanic["SibSp"] + titanic["Parch"]
eixoX = []

conjuges, filhosEpais, totalParentes = [], [], []
for i in range(0, 11):
    eixoX.append(i)
    n = titanic.SibSp[titanic["SibSp"]==i].count()
    conjuges.append(n)
    
    j = titanic.Parch[titanic["Parch"]==i].count()
    filhosEpais.append(j)
    
    k = titanic.TotalParents[titanic["TotalParents"] == i].count()
    totalParentes.append(k)

eixo[1].plot(eixoX, conjuges, color="orange", label="Número de irmãos/conjuges a bordo",  marker='x')
eixo[1].plot(eixoX, filhosEpais, color="green", label="Número de filhos/pais a bordo",  marker='v')
eixo[1].plot(eixoX, totalParentes, color="blue", label="Total de parentes",  marker='o')
eixo[1].axis([-0.5,10,-20,700])
eixo[1].grid(zorder=0, linestyle='solid', color="gray")
eixo[1].legend(fontsize=8)
eixo[1].set_xlabel('Quantidade de parentes')
eixo[1].set_ylabel('Quantidade de pessoas')
plt.xticks(eixoX)

# graph 3 - SCATTER
menX = titanic[titanic["Sex"] == 'male'].fillna(29).Age.value_counts().index
womenX = titanic[titanic["Sex"] == 'female'].fillna(29).Age.value_counts().index

ageMen = titanic[titanic["Sex"] == 'male'].Age.value_counts()
ageWomen = titanic[titanic["Sex"] == 'female'].Age.value_counts()

fig, eixo = plt.subplots(nrows=1, ncols=1)
plt.scatter(menX, ageMen, color='b', label="Homens")
plt.scatter(womenX, ageWomen, color="r", label="Mulheres")
plt.xticks(np.arange(0,85,3), rotation=45)
plt.xlabel('Idade')
plt.ylabel('Quantidade de pessoas')
plt.tick_params(axis='x', labelsize=8)
plt.legend()
