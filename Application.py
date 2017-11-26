from LinearRegression import LinearRegression
from PolinomialRegression import PolinomialRegression
from matplotlib import style
import matplotlib.pyplot as plt

class Application(object):
    # Dias em que as medições foram realizadas
    _xval = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10
    ]

    _days = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11
    ]
    # Pontos do projeto a serem feitos em cada medição
    _remaningPoints = [
        143,
        141,
        141,
        139,
        134,
        131,
        110,
        76,
        64,
        37,
        13,
    ]


    def __init__(self):
        self._initGraph()
        linearReg = LinearRegression(self._days, self._remaningPoints)
        poliReg = PolinomialRegression(self._days, self._remaningPoints, 3)

        plt.plot(self._xval, self._remaningPoints, label="Dados Originais")
        plt.plot(linearReg.getXAxis(), linearReg.getFunction(), label="Função Linear")
        plt.plot(poliReg.getXAxis(), poliReg.getFunction(), label="Função Polinomial")
        plt.legend()
        self._plotGraph()

    def _initGraph(self):
        plt.title('Numerical Scrum')
        plt.xlabel('Dias das medições')
        plt.ylabel('Pontos retantes')
        plt.xlim([0, len(self._days)+5])  # limites dos eixos
        plt.ylim([0, self._remaningPoints[0]+50])

    def _plotGraph(self):
        plt.show()
        style.use('ggplot')


Application()
