"""
    Calcula a densidade do grafo conforme a sua matriz de adjacências.
    Entrada: matriz - matriz de adjacências 
    Saída: float - valor da densidade com precisão de três casas decimais
"""
def calcDensidadeMatriz(matriz):
    n = len(matriz)
    total = 0
    for i in range(n):
        for j in range(n):
            total += matriz[i][j]
    densidade = total / (n * (n - 1))
    return round(densidade, 3)

"""
    Calcula a densidade de um grafo não direcionado.
    Entrada: listaAdj (dict de listas de adjacências).
    Saída: densidade (float) arredondada a 3 casas decimais.
"""
def calcDensidadeLista(listaAdj):
    numVertices = len(listaAdj)  
    numArestas = sum([len(aux) for aux in listaAdj.values()]) // 2
    maxArestas = (numVertices * (numVertices - 1)) // 2 
    
    return round(numArestas / maxArestas, 3)
