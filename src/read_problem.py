
def init_problem(problem_file):
    matriz = []
    arquivo = open(problem_file,'r')
    for linha in arquivo:
        valores = linha.split()
        matriz.append(valores) 
    arquivo.close()

    matriz
    matriz.pop(0)

    quant_convidados = int(matriz.pop(0)[0])

    matriz.pop(0)
    matriz.pop(0)

    quant_mesas = int(matriz.pop(0)[0])
    matriz.pop(0)
    matriz.pop(0)
    lista_limite_mesa = []
    for i in range(quant_mesas):
        lista_limite_mesa.append((matriz.pop(0)))
        lista_limite_mesa[i][0] = int(lista_limite_mesa[i][0])
        lista_limite_mesa[i][1] = int(lista_limite_mesa[i][1])

    matriz.pop(0)
    matriz.pop(0)

    lista_beneficio = []
    for i in range(len(matriz)):
        lista_beneficio.append((matriz.pop(0)))
        lista_beneficio[i][0] = int(lista_beneficio[i][0])
        lista_beneficio[i][1] = int(lista_beneficio[i][1])
        lista_beneficio[i][2] = int(lista_beneficio[i][2])

    pessoas = []
    afinidade = []
    for i in range(len(lista_beneficio)):
        pessoas.append((lista_beneficio[i][0],lista_beneficio[i][1]))
        afinidade.append(lista_beneficio[i][2])

    afin_max =  sorted(afinidade)
    afin_max.sort(reverse=True)

    return (quant_convidados,quant_mesas,lista_limite_mesa,lista_beneficio, pessoas, afinidade , afin_max)