from function_problem import *

def swap_solution(main, matrix_afinidade):
  pares = []
  copia = main.copy()
  solucao_swap = solution(copia,matrix_afinidade)
  solucao_inicial = solucao_swap
  copia_reserved = copia.copy()
  for i in list(copia):
    if (not isinstance(i, str)):
      break
    for j in nodes_edg(i,copia):
      for k in list(copia):
        if (i==k):
          continue
        elif (not isinstance(k,str)):
          break
        for t in nodes_edg(k,copia):
          if((j,t) in pares or (t,j) in pares):
            continue
          pares.append((j,t))
          pares.append((t,j))

          
          copia.remove_edge(i,j)
          copia.remove_edge(k,t)

          copia.add_edge(i,t)
          copia.add_edge(k,j)
    
          solucao_parcial = solution(copia,matrix_afinidade)
          
          if (solucao_swap < solucao_parcial):
            solucao_swap = solucao_parcial
            copia_reserved = copia.copy()
            
            copia.remove_edge(i,t)
            copia.remove_edge(k,j)
            copia.add_edge(i,j)
            copia.add_edge(k,t)
          else:
            copia.remove_edge(i,t)
            copia.remove_edge(k,j)
            copia.add_edge(i,j)
            copia.add_edge(k,t)

  print(f'solução inicial =  {solucao_inicial}, solucao encontrada (swap) = {solucao_swap}')
  return copia_reserved.copy()


def ReInsertion(main, matrix_afinidade):
  copia = main.copy()
  solucao_swap = solution(copia,matrix_afinidade)
  solucao_inicial = solucao_swap
  swamp_mesa_result = copia.copy()
  for i in list(copia):
    if (not isinstance(i, str)):
      break
    if (get_quantidade_alocada(i,copia)-1<int(copia.nodes[i]["menorCadeira"])):
      continue
    for j in nodes_edg(i,copia):
      for k in list(copia):
        if (i==k):
          continue
        if (not isinstance(k,str)):
          break
        if (get_quantidade_alocada(k,copia)+1>int(copia.nodes[k]["maiorCadeira"])):
          break
        
        
        copia.remove_edge(i,j)
        copia.add_edge(k,j)


        solucao_parcial = solution(copia, matrix_afinidade)
        if (solucao_swap < solucao_parcial):

          solucao_swap = solucao_parcial
          
          swamp_mesa_result = copia.copy()
          

          copia.remove_edge(k,j)
          copia.add_edge(i,j)

        else:

          copia.remove_edge(k,j)
          copia.add_edge(i,j)


  # print(f'solução inicial =  {solucao_inicial}, solucao encontrada (Reinsertion) = {solucao_swap}')
  return swamp_mesa_result.copy()


def swap (grafo,matrix_afinidade):
  copia = grafo.copy()
  melhor_solucao = 0
  ja_passou = []
  for i in list(copia.nodes()):
    if (not isinstance(i, str)):
      break
    for j in nodes_edg(i,copia):
      for k in list(copia.nodes()):
        if (not isinstance(k, str)):
          break
        if (i==k):
          continue
        for t in nodes_edg(k,copia):
          if ((j,t) in ja_passou or (t,j) in ja_passou):
            continue
          beneficio = 0
          # print(f"[{i}][{j}][{k}][{t}]",end=" ")
          mesa_1 = list(copia.neighbors(i))
          mesa_2 = list(copia.neighbors(k))
          removido1 = mesa_1.pop(mesa_1.index(j))
          removido2 = mesa_2.pop(mesa_2.index(t))
          beneficio = beneficio - afin_mesa_local(removido1,mesa_1,matrix_afinidade) - afin_mesa_local(removido2,mesa_2,matrix_afinidade) + afin_mesa_local(removido2,mesa_1,matrix_afinidade) + afin_mesa_local(removido1,mesa_2,matrix_afinidade)
          
          tuplas = (j,t)
          ja_passou.append(tuplas)

          if (beneficio > melhor_solucao):
            melhor_solucao = beneficio
            melhor_indice = (i,j,k,t)

  if(melhor_solucao):
    copia.remove_edge(melhor_indice[0],melhor_indice[1])
    copia.remove_edge(melhor_indice[2],melhor_indice[3])
    
    copia.add_edge(melhor_indice[0],melhor_indice[3])
    copia.add_edge(melhor_indice[2],melhor_indice[1])

    # print(f"melhor solução encontrada = {solution(copia,matrix_afinidade)}")
    return copia.copy()
  else:
    return copia.copy()



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
      for k in list(copia.nodes()):
        if (not isinstance(k, str)):
          break
        if (i==k):
          continue
        if (get_quantidade_alocada(k,copia)+1>int(copia.nodes[k]["maiorCadeira"])):
          break

        beneficio = 0
        # print(f"[{i}][{j}][{k}]",end=" ")
        mesa_1 = list(copia.neighbors(i))
        mesa_2 = list(copia.neighbors(k))
        removido1 = mesa_1.pop(mesa_1.index(j))
        beneficio = beneficio - afin_mesa_local(removido1,mesa_1,matrix_afinidade) + afin_mesa_local(removido1,mesa_2,matrix_afinidade)
        


        if (beneficio > melhor_solucao):
          # print(beneficio)
          melhor_solucao = beneficio
          melhor_indice = (i,j,k)

  if(melhor_solucao):
    copia.remove_edge(melhor_indice[0],melhor_indice[1])
    
    copia.add_edge(melhor_indice[2],melhor_indice[1])

    # print(f"melhor solução encontrada = {solution(copia,matrix_afinidade)}")
    return copia.copy()
  else:
    return copia.copy()
