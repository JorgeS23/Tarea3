#Jorge Sancho
#B77150
#Tarea 03

import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

# Parte 1
print('Parte 1')
xy1 = np.genfromtxt('xy.csv',delimiter=',')
xy2 = np.delete(xy1, 0, axis=1) #Se elimina la primera columna
xy = np.delete(xy2, 0, 0) #Se elimina la primera fila

xs = np.linspace(5, 15, num = 11) #Datos x
ys = np.linspace(5, 25, num = 21) #Datos y

#Se suman los valores de probabilidad para todos los x
Px = np.sum(xy, axis=1)
print('Valores de probabilidad para x:', Px)
#Se suman los valores de probabilidad para todos los y
Py = np.sum(xy, axis=0)
print('Valores de probabilidad para y:', Py)

#Gráficas para identificar la curva de mejor ajuste
plt.figure()
plt.title('Gráfica con datos reales de probabilidad para x')
plt.ylabel('$f_X(x)$')
plt.xlabel('$x$')
plt.plot(xs, Px)
plt.savefig('Pxvsx.png')

plt.figure()
plt.title('Gráfica con datos reales de probabilidad para y')
plt.ylabel('$f_Y(y)$')
plt.xlabel('$x$')
plt.plot(ys, Py)
plt.savefig('Pyvsy.png')

#Ambas curvas tienen formas parecida a una gaussiana, por lo tanto esta es la curva de mejor ajuste
#Función de la gaussiana
def gaussiana(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))

#Parámetros de la gaussiana
paramx, _ =curve_fit(gaussiana, xs, Px)
paramy, _ =curve_fit(gaussiana, ys, Py)
print('Parámetros de las funciones de densidad marginales')
print('Para fx(x):', 'Valor esperado =', paramx[0], 'Desviación estándar = ', paramx[1])
print('Para fy(y):', 'Valor esperado =', paramy[0], 'Desviación estándar = ', paramy[1])

#Parte 2
print('')
print('Parte 2')
#Función para la densidad conjunta
def fxy(x,y):
    return 1/((np.sqrt(2*np.pi*paramx[1]**2))*(np.sqrt(2*np.pi*paramy[1]**2)))* np.exp(-(x-paramx[0])**2/(2*paramx[1]**2))* np.exp(-(y-paramy[0])**2/(2*paramy[1]**2))
print('La función de densidad conjunta es:')
print('fXY(xy)=', 1/((np.sqrt(2*np.pi*paramx[1]**2))*(np.sqrt(2*np.pi*paramy[1]**2))),
'e^-(((x-', paramx[0],')^2/', 2*paramx[1]**2,')-((y-', paramy[0],')^2/', 2*paramy[1]**2,'))' )

#Parte 3
print('')
print('Parte 3')

xyp1 = np.genfromtxt('xyp.csv',delimiter=',')
xyp = np.delete(xyp1, 0, 0)

#Se calcula la correlacion
correlacion = 0
for rows in xyp:
    multi = rows[0]*rows[1]*rows[2]
    correlacion = correlacion + multi

print('El valor de la correlación es:')
print('Rxy =', correlacion)

#Se comprueba si existe correlación
comprobacion = paramx[0]*paramy[0]
print('El valor de E[X]E[Y] es:')
print('E[X]E[Y]=', comprobacion)
print('Como los valores son casi iguales, no existe correlación entre X y Y')

#Cálculo de covarianza
#Método1
covarianza1 = correlacion - comprobacion
#Método2
covarianza2 = 0
for rows in xyp:
    multi2 = (rows[0]-paramx[0])*(rows[1] - paramy[0])*rows[2]
    covarianza2 = covarianza2 + multi2
print('Se realizan dos métodos diferentes para calcular covarianza')
print('CXY1=', covarianza1, 'CXY2=', covarianza2)

#Cálculo del coeficiente de correlación(pearson)
#Para los cálculos se utiliza covarianza2
coeficiente = covarianza2/(paramx[1]*paramy[1])
print('El coeficiente de correlación es')
print('p=', coeficiente)

#Parte 4
plt.cla()
plt.figure()
plt.title('Gráfica de la función marginal de x')
plt.ylabel('$f_X(x)$')
plt.xlabel('$x$')
plt.plot(xs, gaussiana(xs, paramx[0], paramx[1]))
plt.savefig('2Dx.png')

plt.cla()
plt.figure()
plt.title('Gráfica de la función marginal de y')
plt.ylabel('$f_X(x)$')
plt.xlabel('$x$')
plt.plot(ys, gaussiana(ys, paramy[0], paramy[1]))
plt.savefig('2Dy.png')

plt.cla()
fig = plt.figure()
ax = plt.axes(projection="3d")
X, Y = np.meshgrid(xs,ys)
Z = fxy(X, Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='winter', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.savefig('3D.png')
