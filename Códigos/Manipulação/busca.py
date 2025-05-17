"""
    Executa busca em largura (BFS) a partir de v em listaAdj e exibe a sequência de visita.
    Entrada: listaAdj (dict de adjacências), v (vértice inicial).
    Saída: imprime a lista de vértices visitados.
"""
def BFS(listaAdj, v):
    listVisitado = [] 
    q = [v] 
   
    while(len(q) != 0): 
        v = q[0] 
        q.pop(0)
        for adj in listaAdj[v]: 
            if adj not in listVisitado: 
                q.append(adj) 
        if v not in listVisitado: 
            listVisitado.append(v)
            
    for i in listaAdj: 
        if len(listaAdj[i]) == 0: 
            listVisitado.append(i) 
 
    return listVisitado

"""
    Realiza DFS em listaAdj a partir de v e imprime a ordem de visita.
    Entrada: listaAdj (dict de adjacências), v (vértice inicial).
    Saída: lista de vértices visitados.
"""
def DFS(listaAdj, v):
    verificado = []
    addVerificado(listaAdj, v, verificado)
    return verificado
      
"""
    Função recursiva auxiliar que visita v e percorre seus adjacentes.
    Entrada: listaAdj, v (vértice atual), verificado (lista de visitados).
"""
def addVerificado(listaAdj, v, verificado):
    verificado.append(v)
    for adjacente in listaAdj[v]:
        if adjacente not in verificado:
            addVerificado(listaAdj, adjacente, verificado)

"""
    Obtém a sequência dos vértices visitados conforme a DFS com implementação iterativa e vértice origem v.
    Entrada: lista de adjacências, v (int).
    Saída: Lista de inteiros com a sequência dos vértices visitados 
"""
def DFSit(listaAdj, v):
    Q = []
    verificados = []
    nVerificados = []
    Q.append(v)
    
    while Q:
        v = Q[-1]
        if v not in verificados:
            verificados.append(v)
        nVerificados = [adj for adj in listaAdj[v] if adj not in verificados]
        
        if nVerificados:
            proximo = nVerificados[0]
            verificados.append(proximo)
            Q.append(proximo)
        else:
            Q.pop()
    for vertice in listaAdj:
        if not listaAdj[vertice]:
            verificados.append(vertice)
            
    return verificados
    