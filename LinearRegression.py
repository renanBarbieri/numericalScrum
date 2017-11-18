import numpy


class LinearRegression(object):

    _xValues = []
    _yValues = []

    def __init__(self, xInputs, yInputs):
        self.xValues = xInputs
        self.yValues = yInputs

    def _calculateAmatrix(self):
        """
        Gera a matriz A(T)*A da função aproximadora
        :return: matriz A(T)*A
        """
        print("Calculando a matriz A ...")
        matrixA = []

        for i in range(0, 2):
            matrixA.append([])
            for j in range(0, 2):
                matrixA[i].append(self._calculateSumForAmatrix(i + j))

        print(matrixA)
        return matrixA

    def _calculateYmatrix(self):
        """
        Gera a matriz A(T)*Y da função aproximadora
        :return: matriz A(T)*Y
        """
        print("Calculando a matriz Y ...")
        matrixY = []

        for i in range(0, 2):
            matrixY.insert(i, self._calculateSumForYmatrix(i))

        print(matrixY)
        return matrixY

    def _calculateSumForAmatrix(self, j):
        """
        Realiza o somátorio do elemento (i,j) para ser posto na matriz a.
        :param j: potencia do somatório
        :return: valor do somatório
        """
        print("Calculando item {} da matriz A(T)*A ...".format(j))
        valReturn = 0
        for i in range(len(self.xValues)):
            valReturn += self.xValues[i] ** j

        return valReturn

    def _calculateSumForYmatrix(self, j):
        """
        Realiza o somátorio do elemento (j) para ser posto na matriz A(T)*Y.
        :param j: potencia do somatório
        :return: valor do somatório
        """
        print("Calculando item {} da matriz A(T)*Y...".format(j))
        valReturn = 0
        for i in range(len(self.xValues)):
            valReturn += (self.xValues[i] ** j * self.yValues[i])

        return valReturn

    def _resolveLinearRegression(self):
        """
        Pega a matriz (A^T)A e a matriz (A^T)Y, e resolve o sistema linear usando a biblioteca numpy.
        :return: Vetor X com a solução do sistema
        """
        aMatrix = self._calculateAmatrix()
        yMatrix = self._calculateYmatrix()
        xVector = numpy.linalg.solve(aMatrix, yMatrix)
        return xVector

    def _getPhi(self, x):
        """
        y = ax + b
        :param x:
        :return: y
        """
        xVector = self._resolveLinearRegression()
        return xVector[1]*x + xVector[0]

    def getLinearFunction(self):
        """
        Gera um array de valores de phi(x), que representa o valor Y da função aproximadora no ponto X
        :return: array de valores de phi(x)
        """
        returnArr = []

        for x in range(self._getXSize()):
            returnArr.insert(x, self._getPhi(x))

        return returnArr

    def _getXSize(self):
        """
        Pega o valor de x do zero da função aproximadora e adiciona cinco valores,
        Apenas para tornar a visualização dos dados mais agradável.
        :return: valor máximo de x
        """
        return int(self._getZeroFunction())+5

    def getXAxis(self):
        """
        Gera um array com as x posições.
        :return: array com x posições
        """
        xAxis = []

        for x in range(self._getXSize()):
            xAxis.insert(x, x)

        return xAxis

    def _getZeroFunction(self):
        """
        x = -b/a
        :return:
        """
        xVector = self._resolveLinearRegression()
        print("Vetor X é {}".format(xVector))
        yZero = -xVector[0]/xVector[1]
        print("A entrega está prevista para o dia {}".format(yZero))
        return yZero
