from funtion_problem import *

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


def Reinsertion(main, matrix_afinidade):
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


  print(f'solução inicial =  {solucao_inicial}, solucao encontrada (Reinsertion) = {solucao_swap}')
  return swamp_mesa_result.copy()