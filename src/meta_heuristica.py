from function_tratamentos import *
import random
from vnd import *

def Perturbacao(grafo,nivel = 1):
  copia = grafo.copy()
  for i in range (nivel):
    lista_mesas = []
    for i in list(copia.nodes()):
      if (not isinstance(i, str)):
        break
      elif (get_quantidade_alocada(i,copia)-1<int(copia.nodes[i]["menorCadeira"])):
        continue
      else:
        lista_mesas.append(i)
    
    mesa_inicial = random.choice(lista_mesas)
    lista_mesas.pop(lista_mesas.index(mesa_inicial))
    mesa_final = random.choice(lista_mesas)

    valorTroca_1 = random.choice(nodes_edg(mesa_inicial,copia))
    valorTroca_2 = random.choice(nodes_edg(mesa_final,copia))

    copia.remove_edge(mesa_inicial,valorTroca_1)
    copia.remove_edge(mesa_final,valorTroca_2)
    
    copia.add_edge(mesa_inicial,valorTroca_2)
    copia.add_edge(mesa_final,valorTroca_1)
  
  return copia.copy()



def ILS (execucoes,vnd_teste,matrix_afinidade):
  copia_vnd_teste = vnd_teste.copy()
  numero_melhoras = 100

  execucoes = 3
  melhor_dos_melhores = 0

  while(execucoes > 0):
    copia_vnd_teste = vnd_teste.copy()
    beneficio = solution(copia_vnd_teste,matrix_afinidade)
    while(numero_melhoras > 0):
      teste = Perturbacao(copia_vnd_teste,5)
      teste2 = VND (teste,matrix_afinidade)
      if(solution(teste2,matrix_afinidade)>beneficio):
        beneficio = solution(teste2,matrix_afinidade)
        copia_vnd_teste = teste2.copy()
        # print(beneficio)
        numero_melhoras = 100
      else:
        numero_melhoras-=1
    if (beneficio > melhor_dos_melhores):
      melhor_dos_melhores = beneficio
      melhor_no = copia_vnd_teste.copy()
    execucoes -=1
  return melhor_no.copy()