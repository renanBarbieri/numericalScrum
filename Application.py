from LinearRegression import LinearRegression
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Application(object):
    # Dias em que as medições foram realizadas
    _days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Pontos do projeto a serem feitos em cada medição
    _remaningPoints = [270, 260, 250, 248, 220, 190, 150, 120, 78, 40]

    def __init__(self):
        self._initGraph()
        linearReg = LinearRegression(self._days, self._remaningPoints)

        plt.plot(self._days, self._remaningPoints)
        plt.plot(linearReg.getXAxis(), linearReg.getLinearFunction())
        self._plotGraph()

    def _initGraph(self):
        plt.title('Numerical Scrum')
        plt.xlabel('Dias das medições')
        plt.ylabel('Pontos retantes')
        plt.xlim([0, len(self._days)+5])  # limites dos eixos
        plt.ylim([0, self._remaningPoints[0]])

    def _plotGraph(self):
        plt.show()
        style.use('ggplot')

