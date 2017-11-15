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
        aMatrix = self._calculateAmatrix()
        yMatrix = self._calculateYmatrix()
        xVector = numpy.linalg.solve(aMatrix, yMatrix)
        print("Vetor X é {}".format(xVector))
        return xVector

    def _getPhi(self, x):
        """
        phi(x) = ax + b
        :param x:
        :return:
        """
        xVector = self._resolveLinearRegression()
        return xVector[1]*x + xVector[0]

    def getLinearFunction(self):
        returnArr = []

        for x in range(len(self.xValues)):
            returnArr.insert(x, self._getPhi(x))

        return returnArr
