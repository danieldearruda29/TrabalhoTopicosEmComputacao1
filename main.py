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

