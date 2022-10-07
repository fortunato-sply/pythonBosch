import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data/respiradores.csv')

# =============================================================================
# # fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (20, 20))
# # eixo[0][0].bar(df.MES,df.TOTAL)
# # eixo[0][1].bar(df.columns[1:-1], df.sum()[1:-1])
# # eixo[1][0].scatter(df['MES'],df['GOIAS'], label = 'Goiás')
# # eixo[1][1].plot(df.MES,df.PARANA, color = 'purple', marker='x', linewidth = 3, markersize=10)
# # eixo[0][0].set_title("Oi")
# # eixo[0][0].set_ylabel("Ola")
# # eixo[0][0].tick_params(axis='x',  labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
# # eixo[0][1].tick_params(axis='x', labelrotation=90)
# # eixo[1][0].tick_params(axis='x', labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
# # eixo[1][1].tick_params(axis='x', labelrotation=90)
# =============================================================================

# =============================================================================
# # Grafico de pizza
# 
# estados_sul = df.loc[:,['PARANA', 'SANTA CATARINA', 'RIO GRANDE DO SUL']]
# 
# def valor():
#     x=estados_sul.sum()["PARANA"]
#     y=estados_sul.sum()["SANTA CATARINA"]
#     z=estados_sul.sum()["RIO GRANDE DO SUL"]
#     
#     return x, y, z
# 
# sizes = valor()
# 
# p, tx, autotexts = plt.pie(estados_sul.sum(), labels=estados_sul.columns, autopct="", shadow=True)
# for i, a in enumerate(autotexts):
#     a.set_text("{}".format(sizes[i]))
# 
# plt.show()
# =============================================================================

# =============================================================================
# print(df.shape)
# print([a-0.25 for a in range(df.shape[0])])
# print([a+0.25 for a in range(df.shape[0])])
# print(df.PARANA)
#     
# plt.bar([i-0.25 for i in range(df.shape[0])],df.PARANA, width = +0.25,
#         label = 'Paraná', align = 'edge')
# 
# plt.bar([a+0.25 for a in range(df.shape[0])],df.TOTAL/30,width = -0.25,
#        label = 'Média brasileira', align = 'edge')
# plt.xticks(np.arange(11),df.MES, rotation=45)
# plt.legend()
# plt.grid(color='lightgray',linestyle='dashed')
# =============================================================================

# =============================================================================
# # Duplo eixo Y
# fig, eixo = plt.subplots(ncols=1,nrows=1,figsize=(10,5))
# eixo.plot(df.MES,df.PARANA,label='Paraná', color='darkblue')
# 
# eixo2 = eixo.twinx()
# eixo2.plot(df.MES,df.TOTAL/30,color='red')
# 
# eixo2.tick_params(axis='y', labelcolor='red')
# eixo.tick_params(axis='y', labelcolor='darkblue')
# 
# eixo.set_ylabel("Paraná", color='darkblue',fontsize=15)
# eixo2.set_ylabel("Média brasileira", color='red',fontsize=15)
# 
# eixo.grid(color='lightblue')
# eixo2.grid(color='pink')
# 
# eixo.set_title('Compra de respiradores PARANÁ X Média brasileira', fontsize= 15)
# =============================================================================

fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(30,15))

regioes = {
    "Norte": df[["AMAZONAS", "ACRE", "RONDONIA", "RORAIMA", "AMAPA", "PARA", "TOCANTINS"]], 
    "Nordeste": df[["MARANHÃO", "PIAUI", "RIO GRANDE DO NORTE", "CEARA", "PARAIBA", "BAHIA", "PERNAMBUCO", "ALAGOAS", "SERGIPE"]], 
    "Centro-oeste": df[["GOIAS", "MATO GROSSO ", "MATO GROSSO DO SUL", "DISTRITO FEDERAL"]], 
    "Sudeste": df[["MINAS GERAIS", "ESPIRITO SANTO ", "RIO DE JANEIRO", "SÃO PAULO"]], 
    "Sul": df[["SANTA CATARINA", "PARANA", "RIO GRANDE DO SUL "]]
}

totalRegioes = {
    "Norte": regioes["Norte"].sum().sum(),
    "Nordeste": regioes["Nordeste"].sum().sum(),
    "Centro-oeste": regioes["Centro-oeste"].sum().sum(),
    "Sudeste": regioes["Sudeste"].sum().sum(),
    "Sul": regioes["Sul"].sum().sum()
}

lista = [totalRegioes[i] for i in list(totalRegioes)]
print(list(totalRegioes))
    
eixo[0].barh(list(totalRegioes),lista, color = 'black')
eixo[0].set_title('TOTAL DE VENDAS POR REGIÃO', fontsize=25)
eixo[0].axis(xmin=0, xmax=5000)
eixo[0].tick_params(labelsize=20)

for i in list(regioes):
    x = regioes[i].sum(axis=1)
    eixo[1].plot(df.MES, x, label = i, marker='v', linewidth = 3)

eixo[1].set_title('VENDAS POR MÊS', fontsize=25)
eixo[1].legend(fontsize=30)
eixo[1].tick_params(axis='x', labelsize=15)
eixo[1].tick_params(axis='y', labelsize=30)
eixo[1].grid(zorder=0, linestyle='dashed')

plt.show()
