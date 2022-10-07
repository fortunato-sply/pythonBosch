import pandas as pd

titanic = pd.read_csv('data/titanic.csv', sep=",")
nome = titanic['Name']

boston = pd.read_csv('data/BostonHousing.csv')
# =============================================================================
# print(boston.loc[:14,["crim","medv"]])
# =============================================================================

# =============================================================================
# # Valores unicos
# # print(titanic["Embarked"].unique())
# =============================================================================

# =============================================================================
# # Contagem de quantas vezes eles aparecem, normalize
# print(titanic["Embarked"].value_counts())
# =============================================================================

# =============================================================================
# Excluir todas as linhas com not a number
# print(titanic.head())
# titanic = titanic.dropna()
# print(titanic)
# =============================================================================

# =============================================================================
# # Preencher onde é encontrado NaN(not a number)
# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
# print(titanic.head())
# =============================================================================

# =============================================================================
# # Filtrar uma coluna
# titanic = titanic[titanic["Age"] > 20]
# =============================================================================

# =============================================================================
# # Comando sort_values
# 
# titanic = titanic.sort_values(by="Age", ascending=False)
# =============================================================================

# =============================================================================
# cars = pd.read_csv('data/cars.csv', usecols=['Manufacturer','Make','Price','MPG.city','Type','Passengers']).dropna()
# cars = cars[cars["Passengers"] == 5].sort_values(by="MPG.city", ascending=False).head(10).sort_values(by="Price").head(5)
# 
# print(cars)
# =============================================================================

# =============================================================================
# titanic = titanic[((titanic["Pclass"] == 1) & (titanic["Survived"] == 1)) | ((titanic["Pclass"] == 3) & (titanic["Survived"] == 0))]
# print(titanic) 
# =============================================================================

# =============================================================================
# pessoaProcurada = titanic[(titanic["Embarked"] == 'S') & (titanic["Pclass"] == 2) & (titanic["Age"] == 29) & (titanic["Name"].str.find("Anne") > 0)]
# survived = "ela sobreviveu" if pessoaProcurada['Survived'].values[0] == 1 else "ela não sobreviveu"
# print(f"A mulher que ele está procurando é {pessoaProcurada['Name'].values[0]}, {survived}")
# =============================================================================

# =============================================================================
# Cria coluna
titanicsoma = titanic["SibSp"] + titanic["Parch"]
titanic["Relatives"] = titanicsoma

# Deleta coluna criada
# titanic.pop('Testenova')
# =============================================================================

# =============================================================================
# # Comando COUNT
# 
# # peopleWhoSurvived = titanic.Survived[titanic["Survived"] == 1].count()
# # print(f"Pessoas que sobreviveram: {peopleWhoSurvived}")
# =============================================================================

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""

    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

# =============================================================================
# # total = titanic.Survived.count()
# # sem_familia = titanic.Survived[titanic["Relatives"] == 0].count()
# # com_familia = titanic.Survived[titanic["Relatives"] > 0]. count()
# 
# # # print(calculate_percentage(sem_familia, total))
# # # print(calculate_percentage(com_familia, total))
# 
# # mortos = titanic[titanic["Survived"] == 0]
# # mortos_sem_familia = mortos.Survived[mortos["Relatives"] == 0].count()
# # mortos_com_familia = mortos.Survived[mortos["Relatives"] > 0].count()
# # nao_sobreviveu = titanic.Survived[titanic["Survived"] == 0].count()
# # print("Não sobreviveu que NÃO tem família no Barco", calculate_percentage(mortos_sem_familia,nao_sobreviveu))
# # print("Não sobreviveu que TEM família no Barco",calculate_percentage(mortos_com_familia,nao_sobreviveu))
# =============================================================================

# =============================================================================
# class1 = titanic.Pclass[titanic["Pclass"] == 1].count()
# class2 = titanic.Pclass[titanic["Pclass"] == 2].count()
# class3 = titanic.Pclass[titanic["Pclass"] == 3].count()
# total = titanic.Pclass.count()
# print(f"Primeira classe: {calculate_percentage(class1, total)}\nSegunda classe: {calculate_percentage(class2, total)}\nTerceira classe: {calculate_percentage(class3, total)}")
# 
# class1 = titanic[titanic["Pclass"] == 1]
# diedClass1 = class1.Survived[class1["Survived"] == 0].count()
# print(f"\nMortos na primeira classe: {diedClass1}")
# class2 = titanic[titanic["Pclass"] == 2]
# diedClass2 = class2.Survived[class2["Survived"] == 0].count()
# print(f"Mortos na segunda classe: {diedClass2}")
# class3 = titanic[titanic["Pclass"] == 3]
# diedClass3 = class3.Survived[class3["Survived"] == 0].count()
# print(f"Mortos na terceira classe: {diedClass3}")
# 
# totalDied = titanic.Survived[titanic["Survived"] == 0].count()
# print(f"\nNão sobreviveu da primeira classe: {calculate_percentage(diedClass1, totalDied)}\nNão sobreviveu da segunda classe: {calculate_percentage(diedClass2, totalDied)}\nNão sobreviveu da terceira classe: {calculate_percentage(diedClass3, totalDied)}")
# 
# survivedClass1 = class1.Survived[class1["Survived"] == 1].count()
# survivedClass2 = class2.Survived[class2["Survived"] == 1].count()
# survivedClass3 = class3.Survived[class3["Survived"] == 1].count()
# print(f"\nSobreviventes na primeira classe: {survivedClass1}\nSobreviventes na segunda classe: {survivedClass2}\nSobreviventes na terceira classe: {survivedClass3}")
# 
# totalSurvived = titanic.Survived[titanic["Survived"] == 1].count()
# print(f"\nSobreviveu da primeira classe: {calculate_percentage(survivedClass1, totalSurvived)}\nSobreviveu da segunda classe: {calculate_percentage(survivedClass2, totalSurvived)}\nSobreviveu da terceira classe: {calculate_percentage(survivedClass3, totalSurvived)}")
# 
# =============================================================================

def faixa_etaria(linhas):
    idade = linhas["Age"]
    if idade < 12:
        return "criança"
    elif idade >= 12 and idade < 18:
        return "adolescente"
    elif idade >= 18 and idade < 65:
        return "adulto"
    elif idade >= 65:
        return "idoso"
    else:
        return "NaN"
    
# =============================================================================
# # Criando a coluna faixa_etaria onde atribuimos o valor da serie resultante do apply
# titanic["faixa_etaria"] = titanic.apply(faixa_etaria, axis=1)
# 
# totalDied = titanic.Survived[titanic["Survived"] == 0].count()
# totalSurvived = titanic.Survived[titanic["Survived"] == 1].count()
# 
# womanOrKidsDied = titanic.Survived[((titanic["Survived"] == 0) & ((titanic["faixa_etaria"] == "criança") | (titanic["Sex"] == "female")))].count()
# womanOrKidsSurvived = titanic.Survived[((titanic["Survived"] == 1) & ((titanic["faixa_etaria"] == "criança") | (titanic["Sex"] == "female")))].count()
# 
# print(f"Número de mulheres e crianças que morreram: {womanOrKidsDied}\nNúmero de mulheres e crianças que sobreviveram: {womanOrKidsSurvived}")
# print(f"\nPorcentagem de mortos que são mulheres ou crianças: {calculate_percentage(womanOrKidsDied, totalDied)}\nPorcentagem de sobreviventes que são mulheres ou crianças: {calculate_percentage(womanOrKidsSurvived, totalSurvived)}")
# =============================================================================

# =============================================================================
# # Apagando colunas
# titanic = titanic.drop(["Name"], axis=1)
# =============================================================================

# =============================================================================
# # Alterando nome da coluna
# titanic.rename(columns={'faixa_etaria': 'AgeRange'})
# =============================================================================
