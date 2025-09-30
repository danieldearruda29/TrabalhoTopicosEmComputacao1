def vertices_dos_bombeiros(matriz_adj, qnt_vertices, inicio_fogo, lista_queimados, num_bombeiros):
    lista_vizinhos = proximos_queimados(qnt_vertices, matriz_adj, inicio_fogo, lista_queimados)
    lista_vizinhos_grau2 = []
    netos_vertice = []
    for vizinho in lista_vizinhos:
        for vizinho_grau2 in range(qnt_vertices):
            netos_vertice = []
            if matriz_adj[vizinho][vizinho_grau2] == 1 and vizinho_grau2 not in lista_queimados:
                netos_vertice.append(vizinho_grau2)
        lista_vizinhos_grau2.append((vizinho, netos_vertice))

    #agora, tem que ordenar a lista de netos de acordo com o tamanho da lista de netos
    lista_vizinhos_grau2.sort(key=lambda x: len(x[1]), reverse=True)
    #com isso, retorna os D (numero de bombeiros disponiveis) primeiros elementos da lista de netos
    return [filho for filho, _ in lista_vizinhos_grau2[:num_bombeiros]]

def proximos_queimados(qnt_vertices, matriz_adj, inicio_fogo, lista_queimados):
    lista_vizinhos = []
    for vizinho in range(qnt_vertices):
        if matriz_adj[inicio_fogo][vizinho] == 1 and vizinho not in lista_queimados:
            lista_vizinhos.append(vizinho)
    return lista_vizinhos