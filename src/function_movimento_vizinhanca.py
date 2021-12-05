from function_problem import *

def swap (grafo,matrix_afinidade,ja_passou_mesa):
  copia = grafo.copy()
  melhor_solucao = 0
  ja_passou= []
  for i in list(copia.nodes()):
    if (not isinstance(i, str)):
      break
    for j in nodes_edg(i,copia):
      mesa_1 = list(copia.neighbors(i))
      removido1 = mesa_1.pop(mesa_1.index(j))
      if (removido1+0.1 in ja_passou_mesa):
        afinidade_mesa_1 = ja_passou_mesa[ja_passou_mesa.index(removido1+0.1)+1]
      else:
        afinidade_mesa_1 = afin_mesa_local(removido1,mesa_1,matrix_afinidade)
        ja_passou_mesa.append(removido1+0.1)
        ja_passou_mesa.append(afinidade_mesa_1)

      for k in list(copia.nodes()):
        if (not isinstance(k, str)):
          break
        if (i==k):
          continue
        for t in nodes_edg(k,copia):
          if ((j,t) in ja_passou or (t,j) in ja_passou):
            continue
          beneficio = 0
          mesa_2 = list(copia.neighbors(k))
          removido2 = mesa_2.pop(mesa_2.index(t))
          if (removido2+0.1 in ja_passou_mesa):
            afinidade_mesa_2 = ja_passou_mesa[ja_passou_mesa.index(removido2+0.1)+1]
          else:  
            afinidade_mesa_2 = afin_mesa_local(removido2,mesa_2,matrix_afinidade)
            ja_passou_mesa.append(removido2+0.1)
            ja_passou_mesa.append(afinidade_mesa_2)


          beneficio = beneficio - afinidade_mesa_1 - afinidade_mesa_2 + afin_mesa_local(removido2,mesa_1,matrix_afinidade) + afin_mesa_local(removido1,mesa_2,matrix_afinidade)
          
          tuplas = (j,t)
          ja_passou.append(tuplas)

          if (beneficio > melhor_solucao):
            melhor_solucao = beneficio
            melhor_indice = (i,j,k,t)

  if(melhor_solucao):
    copia.remove_edge(melhor_indice[0],melhor_indice[1])
    copia.remove_edge(melhor_indice[2],melhor_indice[3])
    ja_passou_mesa.pop(ja_passou_mesa.index(melhor_indice[1]+0.1)+1)
    ja_passou_mesa.pop(ja_passou_mesa.index(melhor_indice[1]+0.1))
    ja_passou_mesa.pop(ja_passou_mesa.index(melhor_indice[3]+0.1)+1)
    ja_passou_mesa.pop(ja_passou_mesa.index(melhor_indice[3]+0.1))
    
    copia.add_edge(melhor_indice[0],melhor_indice[3])
    copia.add_edge(melhor_indice[2],melhor_indice[1]) 
    ja_passou_mesa.append(melhor_indice[1]+0.1)
    ja_passou_mesa.append(afin_mesa_local(melhor_indice[1],list(copia.neighbors(melhor_indice[0])),matrix_afinidade))
    ja_passou_mesa.append(melhor_indice[3]+0.1)
    ja_passou_mesa.append(afin_mesa_local(melhor_indice[3],list(copia.neighbors(melhor_indice[2])),matrix_afinidade))

    return copia.copy(),ja_passou_mesa
  else:
    return copia.copy(),ja_passou_mesa



def Reinsertion (grafo,matrix_afinidade):
  copia = grafo.copy()
  melhor_solucao = 0
  ja_passou = []
  for i in list(copia.nodes()):
    if (not isinstance(i, str)):
      break
    if (get_quantidade_alocada(i,copia)-1<int(copia.nodes[i]["menorCadeira"])):
      continue
    for j in nodes_edg(i,copia):
      mesa_1 = list(copia.neighbors(i))
      removido1 = mesa_1.pop(mesa_1.index(j))
      afinidade_na_mesa = afin_mesa_local(removido1,mesa_1,matrix_afinidade)

      for k in list(copia.nodes()):
        if (not isinstance(k, str)):
          break
        if (i==k):
          continue
        if (get_quantidade_alocada(k,copia)+1>int(copia.nodes[k]["maiorCadeira"])):
          break

        beneficio = 0

        mesa_2 = list(copia.neighbors(k))
        beneficio = beneficio - afinidade_na_mesa + afin_mesa_local(removido1,mesa_2,matrix_afinidade)
        


        if (beneficio > melhor_solucao):
          melhor_solucao = beneficio
          melhor_indice = (i,j,k)

  if(melhor_solucao):
    copia.remove_edge(melhor_indice[0],melhor_indice[1])
    
    copia.add_edge(melhor_indice[2],melhor_indice[1])

    # print(f"melhor solução encontrada = {solution(copia,matrix_afinidade)}")
    return copia.copy()
  else:
    return copia.copy()








def Mesa_furada(grafo,ja_sentou,matrix_afinidade,quant_convidados):
  copia_sentados = ja_sentou.copy()
  copia = grafo.copy()
  beneficio = solution(copia,matrix_afinidade)
  for i in list(copia.nodes()):
    em_pe = nodes_edg(i,copia)
    copia.remove_node(i)
    copia.add_node(i)

    for j in em_pe:
      copia_sentados.pop(copia_sentados.index(j))

    mais_afim = -999
    indice_maior = []
    indice_maior_local = []
    for k in em_pe:
      for j in em_pe:
        if (k==j):
          continue
        if (matrix_afinidade[k][j] > mais_afim):
          mais_afim = matrix_afinidade[k][j]
          indice_maior = [k,j]

    copia.add_edge(i,indice_maior[0])
    copia.add_edge(i,indice_maior[1])

    copia_sentados.append(indice_maior[0])
    copia_sentados.append(indice_maior[1])
    
    execucoes = 10
    while(len(copia_sentados)<quant_convidados and execucoes>0): #da pra utilizar o reinsertion mas dessa forma ta mais otimizado
      mais_afim = -9999
      for i in em_pe:
        if (i in copia_sentados):
          continue
        for j in list(copia.nodes()):
          if (not isinstance(j,str)):
            break
          afinidade_na_mesa = afin_mesa_local(i,nodes_edg(j,copia),matrix_afinidade)
          if (afinidade_na_mesa > mais_afim and get_quantidade_alocada(j,copia)<int(copia.nodes[j]["maiorCadeira"])):
            mais_afim = afinidade_na_mesa
            indice_maior_local = [i,j]
      
      if(indice_maior_local):
        copia.add_edge(indice_maior_local[1],indice_maior_local[0])
        copia_sentados.append(indice_maior_local[0])
        execucoes = execucoes - 1

      execucoes = execucoes - 1
    

    if (solution(copia,matrix_afinidade) > beneficio):
      return copia.copy()
    else:
      return grafo.copy()
      