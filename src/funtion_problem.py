import networkx as nx
from function_tratamentos import *


def init_networkx (quant_convidados, quant_mesas,lista_limite_mesa):
    festinhaFelas = nx.Graph()    
    mesa = nx.Graph()
    for i in range(quant_convidados):
        festinhaFelas.add_node(i)

    for i in range(quant_mesas):
        mesa.add_node(f"mesa_{i}",menorCadeira = lista_limite_mesa[i][0], maiorCadeira = lista_limite_mesa[i][1])
    
    return festinhaFelas.copy(), mesa.copy()

def grafo_afinidades(quant_convidados,festinhaFelas,afinidade,pessoas,passei):
    for i in range(quant_convidados):
        for j in range(quant_convidados):
            if (i==j):
                continue
            festinhaFelas.add_edge(i,j)
            if ((i,j) in pessoas ):
                festinhaFelas.edges[i,j]["afinidade"] = afinidade[pessoas.index((i,j))]
                passei.append((j,i))
            else:
                if ((i,j) in passei):
                    continue
                festinhaFelas.edges[i,j]["afinidade"] = 0




def senta_Dupla (mesa,afin_max,pessoas,afinidade,ja_sentou):
    for i in list(mesa):
        if (int(mesa.nodes[i]["menorCadeira"]/2)):
            for j in range(int(mesa.nodes[i]["menorCadeira"]/2)):
                while(1):
                    maior = afin_max.pop(0)
                    ovo_sentar = pessoas[afinidade.index(maior)]
                    pessoas.pop(afinidade.index(maior))
                    afinidade.pop(afinidade.index(maior))
                    if (ovo_sentar[0] not in ja_sentou and ovo_sentar[1] not in ja_sentou):
                        mesa.add_edge(i,ovo_sentar[0])
                        mesa.add_edge(i,ovo_sentar[1])
                        ja_sentou.append(ovo_sentar[0])
                        ja_sentou.append(ovo_sentar[1])
                        break
                
                    else:
                        continue
        else:
            if (int(mesa.nodes[i]["maiorCadeira"]/2)):
                for j in range(int(mesa.nodes[i]["maiorCadeira"]/2)):
                    while(1):
                        maior = afin_max.pop(0)
                        ovo_sentar = pessoas[afinidade.index(maior)]
                        pessoas.pop(afinidade.index(maior))
                        afinidade.pop(afinidade.index(maior))
                        if (ovo_sentar[0] not in ja_sentou and ovo_sentar[1] not in ja_sentou):
                            mesa.add_edge(i,ovo_sentar[0])
                            mesa.add_edge(i,ovo_sentar[1])
                            ja_sentou.append(ovo_sentar[0])
                            ja_sentou.append(ovo_sentar[1])
                            break
                        
                        else:
                            continue

def senta_pessoa(ja_sentou ,quant_convidados,mesa,matrix_afinidade):
    while(len(ja_sentou)<quant_convidados):
        for i in list(mesa):
            maior_soma = -999
            if (not isinstance(i, str)):
                break
            elif(len(ja_sentou)<quant_convidados):
                for j in range(quant_convidados):
                    if(j in ja_sentou):
                        continue
                    else:
                        soma = 0
                        for k in (nodes_edg(i,mesa)):
                            soma += matrix_afinidade[j][k]

                        if(soma> maior_soma):
                            maior_soma=soma
                            indice_maior=j

                if(get_quantidade_alocada(i,mesa)<int(mesa.nodes[i]["maiorCadeira"]) and not indice_maior in ja_sentou):
                    mesa.add_edge(i,indice_maior)
                    ja_sentou.append(indice_maior)
            else:
                break

