from LinearRegression import LinearRegression


class Application(object):
    # Dias em que as medições foram realizadas
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Pontos do projeto a serem feitos em cada medição
    remaningPoints = [270, 250, 200, 180, 150, 120, 100, 80, 78, 40]

    def __init__(self):
        linearReg = LinearRegression(self.days, self.remaningPoints)
        linearReg.resolveLinearRegression()

