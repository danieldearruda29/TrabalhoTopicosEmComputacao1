from analisar_vizinho import *

file = input("Digite o nome do arquivo: ")
num_bombeiros = int(input("Digite o número de bombeiros disponíveis: "))

with open(file, "r") as f:
    lines = f.readlines()

qnt_vertices = int(lines[0].strip())
#print(f"Quantidade de vértices: {qnt_vertices}")
qnt_arestas = int(lines[1].strip())
#print(f"Quantidade de arestas: {qnt_arestas}")
matriz_adj = [[0] * qnt_vertices for _ in range(qnt_vertices)]

inicio_fogo = int(lines[2].strip())

for line in lines[3:]:
    u, v = map(int, line.strip().split())
    matriz_adj[u][v] = 1
    matriz_adj[v][u] = 1

lista_queimados = [inicio_fogo]
lista_defendidos = []

for vertice_queimado in lista_queimados:
    defendidos_atual = vertices_dos_bombeiros(matriz_adj, qnt_vertices, vertice_queimado, lista_queimados, num_bombeiros, lista_defendidos)
    #print(defendidos_atual)
    for defendido in defendidos_atual:
        if defendido not in lista_defendidos:
            lista_defendidos.append(defendido)
    lista_queimados_proximo = proximos_queimados(qnt_vertices, matriz_adj, vertice_queimado, lista_queimados, lista_defendidos)
    for proximo in lista_queimados_proximo:
        if proximo not in lista_queimados:
            lista_queimados.append(proximo)
    
vertices_salvos = qnt_vertices - len(lista_queimados)
#print("Queimados:", lista_queimados)
#print("Defendidos:", lista_defendidos)
print(f"Foram salvos {vertices_salvos} vértices.")
#print(len(lista_queimados))
#print(lista_queimados)
#tem alguma coisa errada ainda 