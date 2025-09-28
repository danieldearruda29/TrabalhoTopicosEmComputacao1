file = input("Digite o nome do arquivo: ")
num_bombeiros = int(input("Digite o número de bombeiros disponíveis: "))

with open(file, "r") as f:
    lines = f.readlines()

qnt_vertices = int(lines[0].strip())
matriz_adj = [[0] * qnt_vertices for _ in range(qnt_vertices)]

inicio_fogo = int(lines[2].strip())

for line in lines[3:]:
    u, v = map(int, line.strip().split())
    matriz_adj[u][v] = 1
    matriz_adj[v][u] = 1

lista_queimados = [inicio_fogo]
lista_defendidos = []

#analisar os vizinhos do ponto de fogo e os seus vizinhos
def analisar_vizinhos(matriz_adj, qnt_vertices, inicio_fogo, lista_queimados):
    lista_filhos = []
    lista_netos = []
    netos_vertice = []
    for filho in range(qnt_vertices):
        if matriz_adj[inicio_fogo][filho] == 1 and filho not in lista_queimados:
            lista_filhos.append(filho)
    for filho in lista_filhos:
        for neto in range(qnt_vertices):
            netos_vertice = []
            if matriz_adj[filho][neto] == 1 and neto not in lista_queimados:
                netos_vertice.append(neto)
        lista_netos.append((filho, netos_vertice))

    #agora, tem que ordenar a lista de netos de acordo com o tamanho da lista de netos
    #com isso, retorna os D (numero de bombeiros disponiveis) primeiros elementos da lista de netos
