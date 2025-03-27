import numpy as np
import sys

def criaMatriz(instancia):
    with open('C:/Users/Nicolas/Documents/UNIFEI/grafos/Arquivos/Instancias/' + instancia + '.txt', 'rb') as f:
        matriz = np.genfromtxt(f, dtype="int64") 
    return matriz
   
def salvaTamanho(instancia, matriz):
    linha, coluna = matriz.shape  
    string = instancia + " " + str(linha) + " " + str(coluna)
    arquivo = open('C:/Users/Nicolas/Documents/UNIFEI/grafos/Arquivos/Resultados/' + instancia + '_exemplo.txt', 'w')
    arquivo.write(string + '\n')   
    arquivo.close()

def main(instancia):
    matriz = criaMatriz(instancia)
    salvaTamanho(instancia, matriz)  

if __name__ == "__main__":
    main(str(sys.argv[1]))