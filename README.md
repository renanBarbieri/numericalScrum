# Análise das Entregas no Scrum
O processo do Scrum consiste, de maneira bem superficial, em listar todas as tarefas do projeto e colocá-las no Product Backlog. Feito isso, um conjunto de tarefas é transferido para o Sprint Backlog atual para serem desenvolvidas e assim é dado o início do desenvolvimento.   
Em alguns momentos, nem todas as tarefas da sprint atual conseguem ser realizadas a tempo de se entregar. Em outros momentos a equipe consegue entregar mais tarefas do que se foi planejado. Esses momentos acabam interferindo na data de entrega e assim, perdendo um pouco a previsão da mesma. E se fosse possível dar um pouco mais de previsão de quando o projeto irá terminar?
## A Ideia
É bem comum a utilização do gráfico de Burndown nas equipes de scrum para medir a velocidade em que as tarefas estão sendo realizadas. Neste gráfico temos a informação de todo o esforço restante para que a sprint seja entregue. Nele não possuímos dados que indiquem um prazo mais real de entrega de todas as tarefas, mas podemos utilizar os dados já inseridos para tentar fazer uma projeção de quando que isso irá ocorrer.   
Desta forma, a ideia consiste em pegar esses dados e gerar uma função que represente o ritmo de entrega da equipe. Desta forma podemos encontrar o ![Zero da função](/images/func_of-x_zero.gif), que representa o momento em que a sprint será entregue se a equipe mantiver o ritmo atual.   

### Minimos Quadrados
O método dos mínimos quadrados tem como objetivo encontrar uma função que seja uma boa aproximação para um conjunto de dados, possibilitando analizar, com uma certa margem de erro, dados que ainda não foram disponibilizados.   
#### Caso Linear
A maneira mais rústica para tentar solucionar o problema é aproximar para a função linear ![Função Linear](/images/linearEquation.gif). Desta forma, o problema passa a ser encontrar o 'a' e o 'b' desta equação.
Para que a aproximação seja o mais fiel possível aos dados reais, é necessário minimizar a soma das diferenças entre a curva aproximadora e o conjunto de dados fornecidos. Essa diferença pode gerar valores nulos, o que significa que a função aproximada é "real". Entretanto, há casos em que a diferença é nula mas a função aproximadora é muito distante da realidade.   
Para contornar este problema, é minimizado o quadrado das diferenças (o que justifica o nome do método).    
Tendo *n* como a quantidade de elementos no conjunto de dados, o problema pode ser matematicamente representado da seguinte forma: ![Representação do problema](/images/func_of-s_ba.gif)   
Ou, em forma matricial, o problema é mostrado como ![Problema em forma matricial](/images/matrix_s_ba.gif)   
Após algumas manipulações, chega-se ao seguinte sistema linear:   
![Sistema linear](/images/linearProblem.gif)   
Onde,   
![Matriz X](/images/matrix_x.gif)   
![Matriz A Transposta vezes A](/images/matrix_at-a.gif)   
![Matriz A Transposta vezes Y](/images/matrix_at-y.gif)    
#### Caso Polinomial

## Implementação
### Caso Linear
A classe [LinearRegression](LinearRegression.py) será responsável por toda a resolução do problema. Para instanciar a classe, é necessário passar dois parâmetros:   
* xInputs - Array de tamano N referente aos valores de X do conjunto de dados
* yInputs - Array de tamano N referente aos valores de Y do conjunto de dados

Instanciada a classe, já é possível realizar o cálculo. Para tal, basta chamar o método [getLinearFunction()](#getlinearfunction). Este método retorna um array com os valores y da função aproximadora no ponto (posição no vetor) x.   
#### getLinearFunction()
O método getLinearFunction() chama a função [getPhi(x)](#getphix) para cada x entre 0 e phi(x)=0 da função aproximadora. O método responsável por encontrar o valor de x para phi(x)=0 é o método [getXSize()](#getxsize).
``` python
returnArr = []
for x in range(self._getXSize()):
    returnArr.insert(x, self._getPhi(x))

return returnArr
```
#### getXSize()
Apenas pega o valor de x do zero da função aproximadora, pelo método [getZeroFunction()](#getZeroFunction), e adiciona cinco valores, com o intuito de tornar a visualização dos dados mais agradável.
``` python
return int(self._getZeroFunction())+5
```
#### getZeroFunction()
Após solicitar a solução do problema pelo método [resolveLinearRegression()](#resolveLinearRegression), encontra o valor de ![Valor de x quando y é zero](/images/eq_zeroy.gif) quando y=0.
``` python
xVector = self._resolveLinearRegression()
yZero = -xVector[0]/xVector[1]
return yZero
```
#### resolveLinearRegression()
``` python
aMatrix = self._calculateAmatrix()
yMatrix = self._calculateYmatrix()
xVector = numpy.linalg.solve(aMatrix, yMatrix)
return xVector
```
#### calculateAmatrix()
``` python
matrixA = []
for i in range(0, 2):
    matrixA.append([])
    for j in range(0, 2):
        matrixA[i].append(self._calculateSumForAmatrix(i + j))

print(matrixA)
return matrixA
```
#### calculateSumForAmatrix()
``` python
valReturn = 0
for i in range(len(self.xValues)):
    valReturn += self.xValues[i] ** j

return valReturn
```
#### calculateYmatrix()
``` python
matrixY = []
for i in range(0, 2):
    matrixY.insert(i, self._calculateSumForYmatrix(i))

print(matrixY)
return matrixY
```
#### calculateSumForYmatrix()
``` python
valReturn = 0
for i in range(len(self.xValues)):
    valReturn += (self.xValues[i] ** j * self.yValues[i])

return valReturn
```
#### getXAxis()
``` python
xAxis = []
for x in range(self._getXSize()):
    xAxis.insert(x, x)

return xAxis
```
#### getPhi(x)
``` python
xVector = self._resolveLinearRegression()
return xVector[1]*x + xVector[0]
```

## Estudo de casos
## Resultados

## Referências
[Blog ScrumHalf](http://blog.myscrumhalf.com/2012/01/burndown-chart-medindo-o-progresso-de-sua-sprint-e-trazendo-indicativos-do-processo-de-trabalho-da-equipe/)   
[DesenvolvimentoAgil.com.br](http://www.desenvolvimentoagil.com.br/scrum/)   
[Cálculo Numérico, Aspectos Teóricos e Computacionais - Márcia A. Gomes Ruggiero e Vera Lúcia da Rocha Lopes]()      
[Mínimos Quadrados - Wikipédia](https://pt.wikipedia.org/wiki/M%C3%A9todo_dos_m%C3%ADnimos_quadrados)   
[Ajuste de curvas por quadrados mínimos lineares - Felipe Aguiar e Wanderley Moreira](http://www.mat.ufmg.br/gaal/aplicacoes/quadrados_minimos.pdf)
