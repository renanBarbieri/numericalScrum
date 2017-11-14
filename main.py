import numpy

# Dias em que as medições foram realizadas
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Pontos do projeto a serem feitos em cada medição
remaningPoints = [270, 250, 200, 180, 150, 120, 100, 80, 78, 40]

#Caso 1: Aproximar o gráfico para uma reta
# phi(x) = A*x + b

def generateMatrix():
    """
    Gera a matriz A da função aproximadora
    :return: matriz A
    """
    matrixA = []

    for i in range(len(remaningPoints)):
        # Cada y(x) representa uma linha com um vetor de valores (que valores?)
        matrixA.append([])
        for j in range(len(days)):
            matrixA[i].append(sumFunction(i, j))

    print(matrixA)
    return matrixA


def sumFunction(i,j):
    """
    Realiza o somátorio do elemento (i,j) para ser posto na matriz a.
    :param i: linha i, referente aos valores de remaningPoints
    :param j: coluna j, referente aos valores de days
    :return: valor do somatório
    """
    return 0

generateMatrix()