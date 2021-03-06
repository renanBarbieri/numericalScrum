# Análise das Entregas no Scrum
## Introdução
O processo do Scrum consiste, de maneira bem superficial, em listar todas as tarefas do projeto e colocá-las no Product Backlog. Feito isso, um conjunto de tarefas é transferido para o Sprint Backlog atual para serem desenvolvidas e assim é dado o início do desenvolvimento.   
Em alguns momentos, nem todas as tarefas da sprint atual conseguem ser realizadas a tempo de se entregar. Em outros momentos a equipe consegue entregar mais tarefas do que se foi planejado. Esses momentos acabam interferindo na data de entrega e assim, perdendo um pouco a previsão da mesma. E se fosse possível dar um pouco mais de previsão de quando o projeto irá terminar?
É bem comum a utilização do gráfico de Burndown nas equipes de scrum para medir a velocidade em que as tarefas estão sendo realizadas. Neste gráfico temos a informação de todo o esforço restante para que a sprint seja entregue. Nele não possuímos dados que indiquem um prazo mais real de entrega de todas as tarefas e nem de quantos pontos restariam ao final da sprint, mas podemos utilizar os dados já inseridos para tentar fazer uma projeção de quando que isso irá ocorrer.   
Desta forma, a ideia consiste em pegar esses dados e gerar uma função que represente o ritmo de entrega da equipe. Desta forma podemos encontrar o ![Zero da função](/images/func_of-x_zero.gif), que representa o momento em que a sprint será entregue se a equipe mantiver o ritmo atual, e também podemos ter uma noção de quantos pontos faltarão para serem entregues ao final da sprint.   

## Metodologia
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
Para tentar encontrar um aproximação mais fiel à realidade, podemos utiliar o caso polinomial do mínimos quadrados. Desta maneira, teremos que encontrar as variáveis ![Variáveis Polinomiais](/images/var_polinomial.gif) da equação ![Função Polinomial](/images/polinomialEquation.gif).   
A resolução do problema segue o mesmo conceito do caso linear. A diferença está na construção do sistema linear ![Sistema linear](/images/linearProblem.gif), onde no caso polinomial:   
![Matriz X](/images/matrix_x_poli.gif)   
![Matriz A Transposta vezes A](/images/matrix_at-a_poli.gif)   
![Matriz A Transposta vezes Y](/images/matrix_at-y_poli.gif)   

## Implementação
A classe [LinearRegression](LinearRegression.py) será responsável por toda a resolução do problema linear. Para instanciar a classe, é necessário passar dois parâmetros:   
* xInputs - Array de tamano N referente aos valores de X do conjunto de dados
* yInputs - Array de tamano N referente aos valores de Y do conjunto de dados   

   
Esta classe é filha de [PolinomialRegression](PolinomialRegression.py), que é responsável pela resolução de um problema polinomial e necessita de mais um parâmetro para ser instanciada:
* polinomialDegree - Número inteiro que representa o grau da função aproximadora desejada.

Instanciada as classes, já é possível realizar o cálculo. Para tal, basta chamar o método [getFunction()](#getfunction), que retorna um array com os valores y da função aproximadora no ponto (posição no vetor) x.    
### getFunction()
O método getFunction() chama a função [getPhi(x)](#getphix) para cada x entre 0 e algum valor dado pelo método [getXSize()](#getxsize).
``` python
returnArr = []
for x in range(self._getXSize()):
    returnArr.insert(x, self._getPhi(x))

return returnArr
```
### getXSize()
#### Caso Linear
Apenas pega o valor de x do zero da função aproximadora, pelo método [getZeroFunction()](#getzerofunction), e adiciona cinco valores, com o intuito de tornar a visualização dos dados mais agradável.
``` python
return int(self._getZeroFunction())+5
```
#### Caso Polinomial
No caso polinomial, esta função retorna um inteiro abitrário, tendo que ser definido manualmente conforme a necessidade. 
### getZeroFunction()
Após solicitar a solução do problema pelo método [resolveLinearRegression()](#resolvelinearregression), encontra o valor de ![Valor de x quando y é zero](/images/eq_zeroy.gif) quando y=0.
``` python
xVector = self._resolveLinearRegression()
yZero = -xVector[0]/xVector[1]
return yZero
```
Este método só está disponível para o caso linear.
### getPhi(x)
Calcula o valor da função polinomial (no caso linear, esta função é ax+b), de acordo com o x passado. Utiliza o método [resolveLinearRegression()](#resolvelinearregression) para popular o vetor com os valores de x. 
``` python
xVector = self._resolveLinearRegression()
result = 0
for n in range(len(xVector)):
    result += xVector[n]*pow(x, n)
return result
```
### resolveLinearRegression()
Após gerada a matriz (A^T)A, pelo método [calculateAmatrix()](#calculateamatrix), e a matriz (A^T)Y, pelo método [calculateYmatrix()](#calculateymatrix), utiliza a resolução de sistema linear fornecida pela biblioteca numpy. O resultado da operação é o vetor X.
``` python
aMatrix = self._calculateAmatrix()
yMatrix = self._calculateYmatrix()
xVector = numpy.linalg.solve(aMatrix, yMatrix)
return xVector
```
### calculateAmatrix()
Utiliza o método [calculateSumForAmatrix(position)](#calculatesumforamatrixposition) para gerar a matriz (A^T)A do sistema linear. O valor de matrixSize é definido na inicialização da classe. Seu valor é o valor do grau da função aproximadora acrescido de 1.      
Exemplo: se a função for x²,  matrixSize terá o valor 3. 
``` python
matrixA = []
for i in range(0, self._matrixSize):
    matrixA.append([])
    for j in range(0, self._matrixSize):
        matrixA[i].append(self._calculateSumForAmatrix(i + j))

print(matrixA)
return matrixA
```
### calculateSumForAmatrix(position)
De acordo com a posição passada, realiza o somatório de ![x elevado a position](/images/pow_x-position.gif). O valor da posição está entre 0 e 2.
``` python
valReturn = 0
for i in range(len(self._xValues)):
    valReturn += self._xValues[i] ** j

return valReturn
```
### calculateYmatrix()
Utiliza o método [calculateSumForYmatrix(position)](#calculatesumforymatrixposition) para gerar a matriz (A^T)Y do sistema linear
``` python
matrixY = []
for i in range(0, self._matrixSize):
    matrixY.insert(i, self._calculateSumForYmatrix(i))

print(matrixY)
return matrixY
```
### calculateSumForYmatrix(position)
De acordo com a posição passada, realiza o somatório de ![x elevado a position (vezes) y elevado a position](/images/pow_xy-position.gif). O valor da posição está entre 0 e 2.
``` python
valReturn = 0
for i in range(len(self._xValues)):
    valReturn += (self._xValues[i] ** j * self._yValues[i])

return valReturn
```
### getXAxis()
Gera um array com as x posições. O tamanho desse array é gerado pelo método [getXSize()](#getzsize) 
``` python
xAxis = []
for x in range(self._getXSize()):
    xAxis.insert(x, x)
return xAxis
```

## Estudo de casos
Para analisar o comportamento da metodologia proposta, foram utilizados dados das sprints de um projeto desenvolvido na Radix do período de 30 de Maio de 2017 a 24 de Julho de 2017, observando 2 sprints¹.    
Para cada sprint realizada, foram realizados 4 análises:   
1. Gerar uma função com os dados das três primeiras medições
2. Gerar uma função com os dados das cinco primeiras medições
3. Gerar uma função faltando apenas três medições para o fim da sprint
4. Gerar uma função com todas as medições realizadas
   
Para aproximar a função no caso polinomial, foram realizados testes apenas com uma função do 3º grau.
### Análises
#### Sprint 01
Para essa sprint, o desempenho do time foi:   
         
Data da Medição | Pontos Restantes     
--------------- | ----------------   
30 de Maio      | 108
31 de Maio      | 108
01 de Junho     | 108
02 de Junho     | 108
05 de Junho     | 108
06 de Junho     | 108
07 de Junho     | 108
08 de Junho     | 108
09 de Junho     | 108
12 de Junho     | 108
13 de Junho     | 108
14 de Junho     | 108
16 de Junho     | 108
19 de Junho     | 108
20 de Junho     | 108
21 de Junho     | 67 
##### Três primeiras medições
Ao rodar o programa neste caso, obtivemos o seguinte erro ao tentar pegar o zero da função linear:
``` shell 
OverflowError: cannot convert float infinity to integer
```
Isso significa que a função linear encontrada não possui um zero de função. O que é um resultado esperado, visto que os pontos restantes não modificaram e assim, criam uma reta em y=108.   
Usando apenas o caso polinomial, foi obtido este resultado:   
![Estudo de caso da primeira sprint com 3 medições](/images/sp1_c1.png)
##### Cinco primeiras medições
Assim como na primeira análise, não foi possível encontrar o zero da função linear.
Usando apenas o caso polinomial, foi obtido este resultado:   
![Estudo de caso da primeira sprint com 5 medições](/images/sp1_c2.png)
##### Faltando três medições para o fim da sprint
Assim como nas demais análise, não foi possível encontrar o zero da função linear.
Usando apenas o caso polinomial, o resultado obtido foi o mesmo da segunda análise:   
![Estudo de caso da primeira sprint faltando 3 medições](/images/sp1_c3.png)
##### Todas as medições realizadas
Nesta análise, foi possível obter resultado tanto no caso linear quando no caso polinomial. Segue abaixo o resultado obtido:
![Estudo de caso da primeira sprint com todas as medições - Parte 1](/images/sp1_c4(a).png)
![Estudo de caso da primeira sprint com todas as medições - Parte 2](/images/sp1_c4(b).png)
#### Sprint 03
Para essa sprint, o desempenho do time foi:   
 
Data da Medição | Pontos Restantes     
--------------- | ----------------   
10 de Julho     | 143
11 de Julho     | 141
12 de Julho     | 141
13 de Julho     | 139
14 de Julho     | 134
17 de Julho     | 131
18 de Julho     | 110
19 de Julho     | 76
20 de Julho     | 64
21 de Julho     | 37
24 de Julho     | 13

##### Três primeiras medições
Como os pontos restantes foram decaindo, foi possível obeter resultados desde a primeira análise:   
![Estudo de caso da terceira sprint com 3 medições - Parte 1](/images/sp2_c1(a).png) 
![Estudo de caso da terceira sprint com 3 medições - Parte 2](/images/sp2_c1(b).png)
##### Cinco primeiras medições   
![Estudo de caso da primeira sprint com 5 medições](/images/sp2_c2(a).png) 
![Estudo de caso da primeira sprint com 5 medições](/images/sp2_c2(b).png)
##### Faltando três medições para o fim da sprint
![Estudo de caso da primeira sprint faltando 3 medições](/images/sp2_c3(a).png) 
![Estudo de caso da primeira sprint faltando 3 medições](/images/sp2_c3(b).png)
##### Todas as medições realizadas
![Estudo de caso da primeira sprint com todas as medições - Parte 1](/images/sp2_c4.png)
## Discussão e Conclusões
Para definir se a utilização do método foi eficiente ou não, foi realizada uma análise de quantos pontos restavam ao final da sprint. Na entrega da primeira sprint restaram 64 pontos. Na entrega da terceira sprint retaram 13 pontos.    
Após análise dos gráficos gerados, podemos afirmar que a utilização de mínimos quadrados no caso linear não é recomendada para tentar projetar um futuro andamento do time. Essa aproximação ficar muito distante do real quando há algum problema nas entregas do projeto.   
O peso dos problemas² na projeção das entregas usando o caso linear é muito alto, colocando a previsão de conclusão muito além do que acontece e uma projeção de pontos restantes muito acima do real, como visto em todas as análises da primeira sprint e da terceira sprint.   
Já a utilização de mínimos quadrados para gerar uma função aproximadora de grau 3 parece ser uma solução plausível, pelo menos quando se tem mais algumas medições e sem muitos problemas no projeto.   
A primeira sprint é um caso muito particular que não acontece sempre, mas usando ela como base, pode-se observar que se o projeto não evoluir diariamente, nenhuma projeção testada neste trabalho possui um resultado aceitável.    
Na segunda sprint, que já é um caso bem mais comum, foi possível realizar uma análise mais detalhada e conseguimos assim ter uma projeção mais próxima do real. Apesar de não ter acertado nenhuma projeção, a utilização do caso polinomial (com polinômio de 3º grau) do mínimos quadrados se mostrou um caminho a ser seguido para tentar realizar essa aproximação.
   
## Referências
[Blog ScrumHalf](http://blog.myscrumhalf.com/2012/01/burndown-chart-medindo-o-progresso-de-sua-sprint-e-trazendo-indicativos-do-processo-de-trabalho-da-equipe/)   
[DesenvolvimentoAgil.com.br](http://www.desenvolvimentoagil.com.br/scrum/)   
[Cálculo Numérico, Aspectos Teóricos e Computacionais - Márcia A. Gomes Ruggiero e Vera Lúcia da Rocha Lopes]()      
[Mínimos Quadrados - Wikipédia](https://pt.wikipedia.org/wiki/M%C3%A9todo_dos_m%C3%ADnimos_quadrados)   
[Ajuste de curvas por quadrados mínimos lineares - Felipe Aguiar e Wanderley Moreira](http://www.mat.ufmg.br/gaal/aplicacoes/quadrados_minimos.pdf)

###### Nota
1. Foram analisadas apenas a primeira e a terceira sprint. A segunda sprint não possuída dados suficientes para que a análise fosse realizada por completo.
2. Quando há um problema no projeto, a entrega de pontos fica prejudicada. Isso é claramente visto na primeira sprint, em que 15 das 16 coletas de dados o time não entregou nenhum ponto do projeto.  