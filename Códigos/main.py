import sys
from Inicialização import matriz as mt, salva as sv
from Manipulação import densidade as ds, manipula as mp, teste as ts

"""
    Função principal que chama as outras funções.
    Entrada: instancia - nome do arquivo dado pelo terminal
"""
def main(instancia):
    matriz = mt.criaMatriz(instancia)
    sv.salvaTamanho(instancia, matriz)
    print(ds.calcDensidade(matriz))

"""
    Usa do primeiro argumento do terminal como nome do arquivo de entrada (exemplo, ponte, zachary).
    Terminal: py main.py exemplo 
"""
if __name__ == "__main__":
    main(str(sys.argv[1]))