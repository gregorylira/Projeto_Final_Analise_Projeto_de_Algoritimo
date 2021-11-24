def get_quantidade_alocada(nome_mesa,grafo):
    contador = 0
    mesa_brut = list(grafo.edges)
    for n in list(grafo.edges):
      if (n.count(nome_mesa)):
        contador +=1
    return contador

def get_mesa(indice,grafo):
    mesa_brut = list(grafo.edges)
    for n in list(mesa_brut):
        if (n.count(indice)):
            return n
            
def nodes_edg(nome_mesa,grafo):
    return list(grafo.neighbors(nome_mesa))

def solution(sol, matrix_afinidade):
    soma = 0
    for i in list(sol):
        for j in nodes_edg(i,sol):
            for k in nodes_edg(i,sol):
                if(j==k):
                    continue

                soma += matrix_afinidade[j][k]
    return soma

def Matriz_afinidade (festinhaFelas,quant_convidados):
    matrix_afinidade = []
    for i in range(quant_convidados):

        afinidade_list = []
        for j in range(quant_convidados):
            if (i==j):
                afinidade_list.append(None)
                continue
            f = festinhaFelas.get_edge_data(i,j)["afinidade"]
            afinidade_list.append(f)

        matrix_afinidade.append(afinidade_list)
    return matrix_afinidade
