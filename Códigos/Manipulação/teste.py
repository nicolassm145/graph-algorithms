import numpy as np
"""


                                Testes na Matriz de Adjacências


"""
"""
    Verifica se há aresta de vi para vj em uma matriz de adjacência ponderada.
    Entrada: matriz, vi, vj — índices dos vértices.
    Saída: True se o peso > 0, caso contrário False.
"""
def verificaAdjacenciaMatriz(matriz, vi, vj):
    if matriz[vi][vj] > 0:
        result = True
    else:
        result = False
    return result 
   
"""
    Determina o tipo de grafo a partir de uma matriz de adjacência ponderada.
    Retorna: 0 - simples; 1 - dirigido; 20 - multigrafo; 30 - pseudografo; 
    Combina flags somando valores conforme o caso
    Entrada: matriz (array ou lista de listas) de inteiros.
    Saída: inteiro indicando o tipo de grafo.
"""
def tipoGrafoMatriz(matriz):
    digrafo = 0
    multi = 0
    pseudo = 0
    matriz = np.array(matriz)
    linha, coluna = matriz.shape

    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] > 1: # Multigrafo (Existe mais de uma aresta)
                multi = 20
            if i == j and matriz[i][j] > 0: # Pseudografo (Tem laços)
                pseudo = 30
            if matriz[i][j] != matriz[j][i]: # Dirigido (Não é simetrica)
                digrafo = 1
        # Se for pseudografo ou multigrafo 
        # e também dirigido tem que somar as duas flags
        if pseudo != 0:
            result = pseudo + digrafo # 30 + 1
        else: 
            result = multi + digrafo # 20 + 1
    # Se não passar em nenhum if então é um grafo simples (0)
    return result

"""


                                Testes na Lista de Adjacências


"""
"""
    Verifica se existe aresta entre vi e vj em listaAdj.
    Entrada: Lista de adjacências e vértices vi, vj.
    Saída: True se conectados, False caso contrário.
"""
def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi] or vi in listaAdj[vj]:
        return True
    else:
        return False

"""
    Classifica o grafo em listaAdj: 0 - simples; 1 - dirigido; 20 - multigrafo; 30 - pseudografo; 
    Combina flags somando valores conforme o caso.
    Entrada: lista de adjacências.
    Saída: inteiro indicando o tipo.
"""
def tipoGrafoLista(listaAdj):
    digrafo = 0
    multi = 0
    pseudo = 0
    #Simples ou digrafo:
    for i in listaAdj:
        k = -1
        for j in listaAdj[i]:
            if (i not in listaAdj[j]):  #Digrafo (Não é simetrica)
                digrafo = 1
            if k == j: #Multigrafo
                multi = 20
            if j == i:  #Pseudografo
                pseudo = 30
            k = j
    # Se for pseudografo ou multigrafo 
    # e também dirigido tem que somar as duas flags
    if pseudo != 0:
        result = pseudo + digrafo
    else:
        result = multi + digrafo
    # Se não passar em nenhum if então é um grafo simples (0)
    return result

"""
    Verifica se existe caminho ou circuito euleriano em grafo não direcionado.
    Entrada: matriz (NxN) de adjacência.
    Saída: True se <=2 vértices de grau ímpar, caso contrário False.
"""
def caminhoEuleriano(matriz):
    qtd = np.shape(matriz)[0]
    total = 0
    i = 0
    
    while (total <= 2) and (i < qtd):
        for vertice in range(qtd):
            if np.sum(matriz[vertice]) % 2 != 0: 
                total += 1
        i += 1
    
    if total > 2:
        return False
    else:
        return True