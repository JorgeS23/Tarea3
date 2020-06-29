# Tarea3
## Parte 1
Para esta parte se encuentra la mejor curva de ajuste para las funciones de densidades marginales de X y Y.
Esto se logra realizar al leer los datos del xy.csv y sumar todos los valores de probabilidad que existen para un solo valor de X. Esto se hace para todos los X que existen y se obtiene la probabilidad de que suceda cada X, asumiendo que la probabilidad de que suceda Y es 1.

Lo anterior se realiza igualmente para los Y, en donde se tiene las probabilidades de que sucedan cada una de las Y por separado.

Con estos valores de probabilidad, se realizan dos gráficas para identificar la curva de mejor ajuste para los valores de X y los de Y, identifacándose que la curva de mejor ajuste para ambas es la gaussiana. Para X se obtiene un valor esperado de 9.9 con una desviación estándar de 3.3. Para Y se obtiene un valor esperado de 15 con desviación estándar de 6.

Entonces, para los valores de X se obtiene la siguiente función de densidad marginal:

fX(x) = (1/sqrt(2*pi*(3.299)^2))*exp(-(x-9.905)^2/(2*(3.299)^2))

Para los valores de Y se obtiene la función de densidad marginal:

fY(y) = (1/sqrt(2*pi*(6.029)^2))*exp(-(x-15.079)^2/(2*(6.029)^2))

## Parte 2

En esta parte, se pide encontrar la función de densidad conjunta de forma analítica, asumiendo que existe independencia entre X y Y.

Para lograr esto simplemente se multiplican las funciones de densidad marginales obtenidas en la parte 1, para conseguir la función de densidad conjunta, la cual da:

fXY(xy) = 0.008003*exp(-(1/2)*(((x-9.905)^2/((3.299)^2))-((x-15.079)^2/((6.029)^2)))

## Parte 3
Se pide encontrar los valores de correlación, covarianza y coeficiente de relación (Pearson) para los datos. Para esto se leen los datos de xyp.csv.

La correlación es una medida del grado en que dos o más cantidades están linealmente asociadas y se representa por RXY. Para este caso se calcula al realizar la sumatoria de la multiplicación de la probabilidad con los respectivos valores de sus pares (xyP). Al realizar la suma para todas las combinaciones posibles de X y Y, se obtiene un valor de 149.54. Para conocer si los dos valores están correlacionados hay que calcular la multiplicación de los valores esperados para X y Y, cuyos valores se encuentran en la Parte 1 y se obtiene un valor de  149.36.

Como el valor de la correlación es casi identico al de la multiplicación de los valores esperados, se podría decir que RXY = E[X]E[Y] y esto daría que no existe correlación entre las variables aleatorias X y Y. 

La covarianza refleja en que cantidad dos variables aleatoria varían en forma conjunta. Para realizar el cálculo, se hace el mismo procemiento que para la correlación, solo que esta vez el valor de X se le resta E[X] y a los valores de Y se les resta E[Y] ((x-E[X])(y- E[Y])P). Al realizar esto, se obtiene un valor de covarianza de 0.067. Este valor da tan pequeño por que no existe correlación entre las dos variables, ya que otro método para calcular la covarianza es CXY = RXY - E[X]E[Y]. Por lo tanto, las variables aleatorias no varían en forma conjunta.

Por último se hizo el cálculo del coeficiente de relación, el caul es una medida para cuantificar el grado de variación conjunta entre dos variables aleatorias. Este calcula simplemete por p=CXY/(sigmaXsigmaY), donde los valores de sigma son los dados en la parte 1 como desviación estándar. Para este coeficiente se obtiene un coeficiente de variación de 0.00335, el cual da pequeño nuevamente por la no correlación entre las variables.

## Parte 4
Se grafican las curva para las funciones de densidad marginales de la parte 1 y para la función de densidad conjunta de la parte 2.





