

# Dias em que as medições foram realizadas
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Pontos do projeto a serem feitos em cada medição
remaningPoints = [270, 250, 200, 180, 150, 120, 100, 80, 78, 40]

#Caso 1: Aproximar o gráfico para uma reta
# phi(x) = A*x + b


def calculateAmatrix():
    """
    Gera a matriz A(T)*A da função aproximadora
    :return: matriz A(T)*A
    """
    print("Calculando a matriz A ...")
    matrixA = []

    for i in range(len(remaningPoints)):
        matrixA.append([])
        for j in range(0, 2):
            matrixA[i].append(calculateSumForAmatrix(i + j))

    print(matrixA)
    return matrixA


def calculateYmatrix():
    """
    Gera a matriz A(T)*Y da função aproximadora
    :return: matriz A(T)*Y
    """
    print("Calculando a matriz Y ...")
    matrixY = []

    for i in range(len(remaningPoints)):
        matrixY.insert(i, calculateSumForYmatrix(i))

    print(matrixY)
    return matrixY


def calculateSumForAmatrix(j):
    """
    Realiza o somátorio do elemento (i,j) para ser posto na matriz a.
    :param j: potencia do somatório
    :return: valor do somatório
    """
    print("Calculando item {} da matriz A(T)*A ...".format(j))
    valReturn = 0
    for i in range(len(days)):
        valReturn += days[i]**j

    return valReturn


def calculateSumForYmatrix(j):
    """
    Realiza o somátorio do elemento (j) para ser posto na matriz A(T)*Y.
    :param j: potencia do somatório
    :return: valor do somatório
    """
    print("Calculando item {} da matriz A(T)*Y...".format(j))
    valReturn = 0
    for i in range(len(days)):
        valReturn += (days[i]**j * remaningPoints[i])

    return valReturn


def init():
    calculateAmatrix()
    calculateYmatrix()


init()
