import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plot simples

#criando alguns valores do eixo x
#x= np.array([1,2,3,4])
#criando alguns valores do eixo y
#y=x*2

#criando novo eixo y
#y2=x*x

#label das cordenadas x e y
#plt.xlabel('Valores de X')
#   plt.ylabel('Valores de Y')

#executando o plot, colocando um grafico verde, linha tracejada e marcador bolinha, largura da linha = 3, tamanho da bolinha  = 20
#plt.plot(x,y, 'o--g', linewidth =3,markersize=20)

#plotando dois graficos no mesmo plano
#plt.plot(x,y, 'r-', x ,y2, 'b--')

#plotando dois graficos separados
#plt.subplot(1,2,1)
#plt.title('Linear')
#plt.plot(x,y,'r-')
#plt.subplot(1,2,2)
#plt.title('Exponencial')
#plt.plot(x, y2,'b--')

#lendo o dataset paises.csv
Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#extraindo somente dados dos 6 maiores paises do mundo
dfpaises = Paises.nlargest(6, 'Area(sq. mi.)')
#plotadno qual desses paises possui a maior renda per capita
#observe o tamanho de cada ponto ilustra o tamanho destes paises
plt.scatter(dfpaises['Country'], dfpaises['GDP($ per capita)'], s=dfpaises['Area(sq. mi.)']/10000)


#Mostrando o plot
plt.show()