import numpy as np
"""


                                Manipulação de Matriz de Adjacências


"""
"""
    Insere uma aresta na matriz de adjacências, incrementando em 1 as posições correspondentes aos vértices.
    Entrada: matriz, vertices de origem e destino (vi, vj)
    Saída: matriz atualizada.
"""
def insereArestaMatriz(matriz, vi, vj):
    
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1
    return matriz

"""
    Insere um novo vértice na matriz de adjacências, adicionando uma nova linha e coluna preenchida com zeros.
    Entrada: matriz
    Saída: matriz atualizada.
"""
def insereVerticeMatriz(matriz):
   
    # Cria uma nova linha de zeros, do mesmo tamanho das linhas existentes
    zeros = [0] * len(matriz)
    matriz.append(zeros)
    
    # Adiciona um zero em cada linha para representar a nova coluna
    for linha in matriz:
        linha.append(0)
    
    matrizNova = np.array(matriz)
    return matrizNova

"""
    Remove uma aresta da matriz de adjacências, definindo as posições correspondentes como zero.
    Entrada: matriz, vertices de origem e destino (vi, vj)
    Saída: matriz atualizada.
"""
def removeArestaMatriz(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0
    return matriz

"""
    Remove um vértice da matriz de adjacências, definindo as arestas incidentes a este vértice como -1.
    Entrada: matriz, índice do vértice a ser removido (v)
    Saída: matriz atualizada.
"""
def removeVerticeMatriz(matriz, v):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == v or j == v:
                matriz[i][j] = -1
    
    matrizNova = np.array(matriz)
    return matrizNova

"""


                                Manipulação de Lista de Adjacências


"""

"""
    Insere a aresta (vi, vj) em listaAdj; replica para (vj, vi) se o grafo for não direcionado.
    Entrada: listaAdj - dict de listas de adjacências, vi, vj - vértices a conectar
    Saída: listaAdj atualizado com a nova aresta
"""
def insereArestaLista(listaAdj, vi, vj):
    digrafo = False
    # Verifica se é um grafo dirigido
    for i in listaAdj:
        for j in listaAdj[i]:
            if (i not in listaAdj[j]):  #Digrafo (Não é simetrica)
                digrafo = True
    # Sempre adiciona no vi
    listaAdj[vi].append(vj)
    listaAdj[vi].sort()
    
    if not digrafo: # Só adiciona se não for digrafo
        listaAdj[vj].append(vi)
        listaAdj[vj].sort()
    
    return listaAdj

"""
    Adiciona um novo vértice sem arestas em um dicionário de listas de adjacências.
    Entrada: lista de adjacências.
    Saída: lista atualizada com o vértice n.
"""
def insereVerticeLista(lista):
    for i in lista:
        if i == len(lista)-1:
            lista[i+1] = []
            break
        
    return lista

"""
    Remove a aresta (vi, vj) de um grafo não direcionado representado por lista de adjacências.
    Entrada: lista, vi, vj - vértices da aresta.
    Saída: lista atualizada (remove vi de lista[vj] e vj de lista[vi]).
"""
def removeArestaLista(lista, vi, vj):
    listaVi = lista[vi] 
    listaVj = lista[vj]

    for i in range(len(lista[vi])):
        if listaVi[i] == vj:
            lista[vi].pop(i)
            break
    for j in range(len(lista[vj])):
        if listaVj[j] == vi: 
            lista[vj].pop(j)
            break

    return lista

"""
    Remove um vértice e todas as arestas associadas em um grafo representado por lista de adjacências.
    Entrada: lista de adjacências, v (int) — vértice a remover.
    Saída: lista atualizada sem o vértice v.
"""
def removeVerticeLista(lista, v):
    del lista[v] # Deleta o vertice v inteiro
    for j in lista:
        listaV = lista[j]
        for i in range(len(listaV)):
            if listaV[i] == v:
                while i < len(listaV) and listaV[i] == v:
                    lista[j].pop(i)
                break
    return lista