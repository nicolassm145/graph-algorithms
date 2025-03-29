import numpy as np
import sys

"""
    Lê a matriz do arquivo .txt e retorna a matriz como um array numpy.
    Entrada: instancia - nome do arquivo dado pelo terminal
    Saida: matriz numpy
"""
def criaMatriz(instancia):
    with open('C:/Users/Nicolas/Documents/UNIFEI/grafos/Arquivos/Instancias/' + instancia + '.txt', 'rb') as f:
        matriz = np.genfromtxt(f, dtype="int32") 
    return matriz

"""
    Salva o tamanho da matriz em um arquivo .txt
    Entrada: instancia - nome do arquivo dado pelo terminal, matriz - matriz numpy
    Saida: cria o arquivo .txt com o tamanho da matriz (nomeInstancia linha coluna)
"""
def salvaTamanho(instancia, matriz):
    linha, coluna = matriz.shape  
    texto = instancia + " " + str(linha) + " " + str(coluna) 
    arquivo = open('C:/Users/Nicolas/Documents/UNIFEI/grafos/Arquivos/Resultados/' + instancia + '_exemplo.txt', 'w')
    arquivo.write(texto + '\n')   
    arquivo.close()
    print(texto)  

"""
    Função principal que chama as outras funções.
    Entrada: instancia - nome do arquivo dado pelo terminal
"""
def main(instancia):
    matriz = criaMatriz(instancia)
    salvaTamanho(instancia, matriz)  

"""
    Usa do primeiro argumento do terminal como nome do arquivo de entrada (exemplo, ponte, zachary).
    Terminal: py main.py exemplo 
"""
if __name__ == "__main__":
    main(str(sys.argv[1]))