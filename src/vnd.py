from function_movimento_vizinhanca import *
from function_tratamentos import *

def VND (mesa,matrix_afinidade,ja_sentou,quant_convidados,ja_passou_mesa = []):
  r = 3
  k = 1
  

  while (k<=r):
    if (k == 1):
      copia_VND = Reinsertion(mesa,matrix_afinidade)
    elif (k==2):
      copia_VND,ja_passou_mesa = swap(mesa,matrix_afinidade,ja_passou_mesa)
    elif (k==3):
      copia_VND = Mesa_furada(mesa,ja_sentou,matrix_afinidade,quant_convidados)

    if (solution(copia_VND,matrix_afinidade)>solution(mesa,matrix_afinidade)):
      # if(k==2):
        # print("swap encontrou uma solução melhor, voltando ao Reinsertion")
      mesa = copia_VND.copy()
      k = 1
    else:
      # if (k==1):
        # print("Não obteve melhora, passando para o proximo")
      # elif(k+1>r):
        # print("Encontrou uma solução")
      k +=1
  return mesa.copy(),ja_passou_mesa