# Algoritmos em Grafos

Repositório para estudo e implementação de algoritmos em grafos usando Python.

## Sobre

Este projeto contém implementações didáticas de algoritmos de grafos. Os algoritmos manipulam grafos representados tanto por **matriz de adjacência** quanto por **lista de adjacências**. O foco é educacional.

## Funcionalidades

- Leitura de matriz de adjacência a partir de arquivos `.txt`
- Conversão entre matriz e lista de adjacências
- Inserção e remoção de vértices e arestas
- Verificação de adjacência entre vértices
- Cálculo de densidade de grafos
- Identificação do tipo de grafo (simples, dirigido, multigrafo, pseudografo)
- Fechamento transitivo com o algoritmo de **Warshall**
- Verificação de existência de **caminho euleriano**
- Implementação das buscas **BFS** e **DFS** (iterativa e recursiva)

## Estrutura do Projeto

```
graph-algorithms/
├── Arquivos/
│   ├── Instâncias/           # Arquivos .txt com as matrizes de adjacência
│   └── Resultados/           # Saídas ou processamentos de testes
├── Códigos/
│   ├── Inicialização/
│   │   ├── cria.py
│   │   └── salva.py
│   └── Manipulação/
│       ├── busca.py
│       ├── densidade.py
│       ├── manipula.py
│       └── teste.py
├── main.py
├── .gitignore
└── README.md
```

##  Pré-requisitos

- Python 3.7 ou superior
- NumPy


## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
