import sys
from Códigos.Inicialização import cria as cr
from Inicialização import salva as sv
from Manipulação import densidade as ds, manipula as mp, teste as ts

"""
    Função principal que chama as outras funções.
    Entrada: instancia - nome do arquivo dado pelo terminal
"""
def main(instancia):
    matriz = cr.criaMatriz(instancia)
    sv.salvaTamanho(instancia, matriz)
    print(ds.calcDensidade(matriz))

"""
    Usa do primeiro argumento do terminal como nome do arquivo de entrada (exemplo, ponte, zachary).
    Terminal: py main.py exemplo 
"""
if __name__ == "__main__":
    main(str(sys.argv[1]))