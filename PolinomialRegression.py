import numpy

class PolinomialRegression(object):

    _degree = 1
    _matrixSize = 2
    _xValues = []
    _yValues = []

    def __init__(self, xInputs, yInputs, polinomialDegree):
        self._xValues = xInputs
        self._yValues = yInputs
        self._degree = polinomialDegree
        self._matrixSize = polinomialDegree + 1

    def getFunction(self):
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
        Retorna um valor arbitrário.
        :return: valor máximo de x
        """
        return 105

    def _getPhi(self, x):
        """
        Calcula o valor da função polinomial (no caso linear, esta função é ax+b), de acordo com o x passado.
        y = a_0 + a_1*x + a_2*x^2 + ... + a_n*x^n
        :param x:
        :return: y
        """
        xVector = self._resolveLinearRegression()
        result = 0
        for n in range(len(xVector)):
            result += xVector[n]*pow(x, n)
        return result

    def _resolveLinearRegression(self):
        """
        Pega a matriz (A^T)A e a matriz (A^T)Y, e resolve o sistema linear usando a biblioteca numpy.
        :return: Vetor X com a solução do sistema
        """
        aMatrix = self._calculateAmatrix()
        yMatrix = self._calculateYmatrix()
        xVector = numpy.linalg.solve(aMatrix, yMatrix)
        print("VETOR X {}".format(xVector))
        print("VETOR B {}".format(aMatrix@xVector))
        return xVector

    def _calculateAmatrix(self):
        """
        Gera a matriz A(T)*A da função aproximadora
        :return: matriz A(T)*A
        """
        print("Calculando a matriz A ...")
        matrixA = []

        for i in range(0, self._matrixSize):
            matrixA.append([])
            for j in range(0, self._matrixSize):
                matrixA[i].append(self._calculateSumForAmatrix(i + j))

        print(matrixA)
        return matrixA

    def _calculateSumForAmatrix(self, j):
        """
        Realiza o somátorio do elemento (i,j) para ser posto na matriz a.
        :param j: potencia do somatório
        :return: valor do somatório
        """
        print("Calculando item {} da matriz A(T)*A ...".format(j))
        valReturn = 0
        for i in range(len(self._xValues)):
            valReturn += self._xValues[i] ** j

        return valReturn

    def _calculateYmatrix(self):
        """
        Gera a matriz A(T)*Y da função aproximadora
        :return: matriz A(T)*Y
        """
        print("Calculando a matriz Y ...")
        matrixY = []

        for i in range(0, self._matrixSize):
            matrixY.insert(i, self._calculateSumForYmatrix(i))

        print(matrixY)
        return matrixY

    def _calculateSumForYmatrix(self, j):
        """
        Realiza o somátorio do elemento (j) para ser posto na matriz A(T)*Y.
        :param j: potencia do somatório
        :return: valor do somatório
        """
        print("Calculando item {} da matriz A(T)*Y...".format(j))
        valReturn = 0
        for i in range(len(self._xValues)):
            valReturn += (self._xValues[i] ** j * self._yValues[i])

        return valReturn

    def getXAxis(self):
        """
        Gera um array com as x posições.
        :return: array com x posições
        """
        xAxis = []

        for x in range(self._getXSize()):
            xAxis.insert(x, x)
        return xAxis
