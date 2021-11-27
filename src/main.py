from function_problem import *
from read_problem import *
from function_movimento_vizinhanca import *
from function_tratamentos import *
from meta_heuristica import *
from vnd import *
import time

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


heuristica_List = []
otimo_list_heuristic = []
tempo_list_heuristic = []
gap_list_heuristic = []
linha_heuristic = []

vnd_List = []
otimo_list_vnd = []
tempo_list_vnd = []
gap_list_vnd = []
linha_vnd = []

ils_List = []
otimo_list_ils = []
tempo_list_ils = []
gap_list_ils = []
linha_ils = []


index = []
interacao = 0


instancias = [
  "../instancias/n20c5_A.txt",
  "../instancias/n20c5_B.txt",
  "../instancias/n20c7_A.txt",
  "../instancias/n30c5_A.txt",
  "../instancias/n30c5_B.txt",
  "../instancias/n30c5_C.txt",
  "../instancias/n30c8_A.txt",
  "../instancias/n30c8_B.txt",
  "../instancias/n50c8_A.txt",
  "../instancias/n50c8_B.txt",
  ]

for i in instancias:
  quant_convidados,quant_mesas,lista_limite_mesa,lista_beneficio, pessoas, afinidade , afin_max = init_problem(i)

  festinhaFelas, mesa = init_networkx ( quant_convidados, quant_mesas, lista_limite_mesa )

  # Preenchendo grafo com suas afinidades 
  passei = []
  grafo_afinidades(quant_convidados,festinhaFelas,afinidade,pessoas,passei)

  matrix_afinidade = Matriz_afinidade(festinhaFelas,quant_convidados)
  print("~~"*32)
  print(f"Iniciando Instancia {interacao}")
  start_time_heuristic = time.time()
  #INICIO DA HEURISTICA CONSTRUTIVA
  # Preenchendo valor minimo das mesas com as duplas de maiores afinidades da lista de afinidades
  ja_sentou = []

  senta_Dupla(mesa,afin_max,pessoas,afinidade,ja_sentou)


  # Cria a Matriz de Afinidades para uso futuro

  # segunda parte da heuristica construtiva, onde verifica qual mesa tem o maior beneficio para cada pessoa
  senta_pessoa(ja_sentou ,quant_convidados,mesa,matrix_afinidade)

  end_time_heuristic = time.time()

  heuristica_local = solution(mesa,matrix_afinidade)
  heuristica_List.append(heuristica_local)
  tempo_list_heuristic.append(round(end_time_heuristic - start_time_heuristic,3))
  otimo_list_heuristic.append(0)
  gap_list_heuristic.append(0)

  print(f"Heuristica Concluida, iniciando vnd")


  #INICIO DO VND
  start_time_vnd = time.time()
  solucao_final_VND = VND(mesa,matrix_afinidade)
  end_time_vnd = time.time()

  vnd_List.append(solution(solucao_final_VND,matrix_afinidade))
  tempo_list_vnd.append(round(end_time_vnd - start_time_vnd,3))
  otimo_list_vnd.append(0)
  gap_list_vnd.append(0)

  print(f"VND concluido, iniciando ILS (Meta Heuristica)")

  #INICIO META_HEURISTICA
  start_time_ils = time.time()
  result_ils = ILS(3,solucao_final_VND,matrix_afinidade)
  end_time_ils = time.time()

  ils_List.append(solution(result_ils,matrix_afinidade))
  tempo_list_ils.append(round(end_time_ils-start_time_ils))
  otimo_list_ils.append(0)
  gap_list_ils.append(0)
  print(f"ILS concluido")


  linha_heuristic.append([otimo_list_heuristic[interacao],heuristica_List[interacao],tempo_list_heuristic[interacao],gap_list_heuristic[interacao]])

  linha_vnd.append([otimo_list_vnd[interacao],vnd_List[interacao],tempo_list_vnd[interacao],gap_list_vnd[interacao]])
  
  linha_ils.append([otimo_list_ils[interacao],ils_List[interacao],tempo_list_ils[interacao],gap_list_ils[interacao]])

  plt.figure(figsize=(15, 15))
  nx.draw(solucao_final_VND ,with_labels=True,node_color="black",node_size=3250,width=1.6, font_color="white",font_weight='bold' )
  plt.savefig(f'../plots/solutions/instancia_{interacao}.png', format='png')
  plt.close()

  plt.figure(figsize=(15, 15))
  nx.draw(mesa ,with_labels=True,node_color="black",node_size=3250,width=1.6, font_color="white",font_weight='bold' )
  plt.savefig(f'../plots/heuristica/instancia_{interacao}.png', format='png')
  plt.close()

  index.append(f"instancia_{interacao}")
  interacao += 1

df_heuristica = pd.DataFrame(linha_heuristic, columns = ['Otimo','Valor_Solução', "Tempo", "gap"], index=[index])
df_vnd = pd.DataFrame(linha_vnd, columns = ['Otimo','Valor_Solução', "Tempo", "gap"], index=[index])
df_ils = pd.DataFrame(linha_ils, columns = ['Otimo','Valor_Solução', "Tempo", "gap"], index=[index])

print("~~"*32)
print("Heuristica Construtiva")
print(df_heuristica)
print("~~"*32)
print("VND")
print(df_vnd)
print("~~"*32)
print("ILS")
print(df_ils)
print("~~"*32)
