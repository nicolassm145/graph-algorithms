"""
    Salva o tamanho da matriz em um arquivo .txt
    Entrada: instancia - nome do arquivo dado pelo terminal, matriz - matriz numpy
    Saida: cria o arquivo .txt com o tamanho da matriz (nomeInstancia linha coluna)
"""
def salvaTamanho(instancia, matriz):
    linha, coluna = matriz.shape  
    texto = instancia + " " + str(linha) + " " + str(coluna) 
    arquivo = open(f"../Arquivos/Resultados/dimensao{instancia.capitalize()}.txt", 'w')
    arquivo.write(texto + '\n')   
    arquivo.close()