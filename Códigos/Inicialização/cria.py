import numpy as np

"""
    Lê a matriz do arquivo .txt e retorna a matriz como um array numpy.
    Entrada: instancia - nome do arquivo dado pelo terminal
    Saida: matriz numpy
"""
def criaMatriz(instancia):
    with open(f"../Arquivos/Instâncias/{instancia}.txt", 'rb') as f:
        matriz = np.genfromtxt(f, dtype="int32") 
    return matriz

"""
    Lê a matriz do arquivo .txt e retorna a lista de adjacencia.
    Entrada: instancia - nome do arquivo dado pelo terminal
    Saida: lista de adjacencia 
"""
def criaListaAdjacencias(matriz):
    matrizNova = np.array(matriz)
    linha, coluna = matrizNova.shape
    listaAdj = {}

    for i in range(linha):
        listaAdj[i] = []
        for j in range(coluna):
            num = matrizNova[i][j] 
            while(num > 0):   # Vai repetir até acabar as repetições
                listaAdj[i].append(j)
                num -= 1

    return listaAdj

import numpy as np

"""
    Calcula o fecho transitiva de um grafo usando o algoritmo de Warshall.
    Entrada: matriz (NxN) binária de adjacência.
    Saída: imprime a matriz resultante onde 1 indica existência de caminho entre vértices.
"""
def warshall(matriz):
    qtd = np.shape(matriz)[0]
    copiaMatriz = np.array(matriz)

    for k in range(qtd):
        for i in range(qtd):
            for j in range(qtd):
                if copiaMatriz[i][j] == 1 or (copiaMatriz[i][k] == 1 and copiaMatriz[k][j] == 1):
                    copiaMatriz[i][j] = 1
                else:
                    copiaMatriz[j][j] == copiaMatriz[i][j]
                    
    return copiaMatriz    