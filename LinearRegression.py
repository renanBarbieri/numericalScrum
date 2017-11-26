from PolinomialRegression import PolinomialRegression

class LinearRegression(PolinomialRegression):

    def __init__(self, xInputs, yInputs):
        super().__init__(xInputs, yInputs, 1)

    def _getXSize(self):
        """
        Pega o valor de x do zero da função aproximadora e adiciona cinco valores,
        Apenas para tornar a visualização dos dados mais agradável.
        :return: valor máximo de x
        """
        return int(self._getZeroFunction())+5


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
