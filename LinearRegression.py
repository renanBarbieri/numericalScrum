import numpy


class LinearRegression(object):

    xValues = []
    yValues = []

    def __init__(self, xInputs, yInputs):
        self.xValues = xInputs
        self.yValues = yInputs


    def calculateAmatrix(self):
        """
        Gera a matriz A(T)*A da função aproximadora
        :return: matriz A(T)*A
        """
        print("Calculando a matriz A ...")
        matrixA = []

        for i in range(len(self.yValues)):
            matrixA.append([])
            for j in range(0, 2):
                matrixA[i].append(self.calculateSumForAmatrix(i + j))

        print(matrixA)
        return matrixA


    def calculateYmatrix(self):
        """
        Gera a matriz A(T)*Y da função aproximadora
        :return: matriz A(T)*Y
        """
        print("Calculando a matriz Y ...")
        matrixY = []

        for i in range(len(self.yValues)):
            matrixY.insert(i, self.calculateSumForYmatrix(i))

        print(matrixY)
        return matrixY


    def calculateSumForAmatrix(self, j):
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


    def calculateSumForYmatrix(self, j):
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


    def resolveLinearRegression(self):
        aMatrix = self.calculateAmatrix()
        yMatrix = self.calculateYmatrix()
        xVector = numpy.linalg.solve(aMatrix, yMatrix)
        print("Vetor X é {}".format(xVector))
