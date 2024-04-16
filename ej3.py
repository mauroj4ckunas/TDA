def agrupar_diagonales(campo, coordenadas, tamanio, agrupaciones_hechas):
    if campo[coordenadas[0]][coordenadas[1]] != 0:
       agrupaciones_hechas = agrupar_diagonal_esquina1(campo,coordenadas, tamanio, agrupaciones_hechas)
    elif campo[esquinaInferiorDerecha(coordenadas, tamanio)[0]][esquinaInferiorDerecha(coordenadas, tamanio)[1]] !=0 :
        agrupaciones_hechas = agrupar_diagonal_esquina2(campo,coordenadas, tamanio, agrupaciones_hechas)
    elif campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0]][esquinaInferiorDerecha(coordenadas, tamanio)[1]] != 0:
        agrupaciones_hechas = agrupar_diagonal_esquina3(campo,coordenadas, tamanio, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonal_esquina4(campo,coordenadas, tamanio, agrupaciones_hechas)

    return agrupaciones_hechas

def agrupar_diagonal_esquina1(campo, coordenadas, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[coordenadas[0] + i][coordenadas[1] + i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[coordenadas[0] + i][coordenadas[1] + i] = agrupaciones_hechas
            campo[coordenadas[0] + i][coordenadas[1] + i - 1] = agrupaciones_hechas
            campo[coordenadas[0] + i - 1][coordenadas[1] + i] = agrupaciones_hechas
    return agrupaciones_hechas
    
def agrupar_diagonal_esquina2(campo, coordenadas, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[esquinaInferiorDerecha(coordenadas, tamanio)[0] - i][esquinaInferiorDerecha(coordenadas, tamanio)[1] - i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[esquinaInferiorDerecha(coordenadas, tamanio)[0] - i][esquinaInferiorDerecha(coordenadas, tamanio)[1] - i] = agrupaciones_hechas
            campo[esquinaInferiorDerecha(coordenadas, tamanio)[0] - i][esquinaInferiorDerecha(coordenadas, tamanio)[1] - i + 1] = agrupaciones_hechas
            campo[esquinaInferiorDerecha(coordenadas, tamanio)[0] - i + 1][esquinaInferiorDerecha(coordenadas, tamanio)[1] - i] = agrupaciones_hechas
    return agrupaciones_hechas

def agrupar_diagonal_esquina3(campo, coordenadas, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0] + i][esquinaSuperiorDerecha(coordenadas, tamanio)[1] - i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0] + i][esquinaSuperiorDerecha(coordenadas, tamanio)[1] - i] = agrupaciones_hechas
            campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0] + i][esquinaSuperiorDerecha(coordenadas, tamanio)[1] - i + 1] = agrupaciones_hechas
            campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0] + i - 1][esquinaSuperiorDerecha(coordenadas, tamanio)[1] - i] = agrupaciones_hechas
    return agrupaciones_hechas

def agrupar_diagonal_esquina4(campo, coordenadas,tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if campo[esquinaInferiorIzquierda(coordenadas, tamanio)[0] - i][esquinaInferiorIzquierda(coordenadas, tamanio)[1] + i] == 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[esquinaInferiorIzquierda(coordenadas, tamanio)[0] - i][esquinaInferiorIzquierda(coordenadas, tamanio)[1] + i] = agrupaciones_hechas
            campo[esquinaInferiorIzquierda(coordenadas, tamanio)[0] - i][esquinaInferiorIzquierda(coordenadas, tamanio)[1] + i  - 1] = agrupaciones_hechas
            campo[esquinaInferiorIzquierda(coordenadas, tamanio)[0] - i + 1][esquinaInferiorIzquierda(coordenadas, tamanio)[1] + i] = agrupaciones_hechas
    return agrupaciones_hechas


def esquinaSuperiorDerecha(coordenadas, tamanio):
    return (coordenadas[0] , coordenadas[1] + tamanio - 1)

def esquinaInferiorDerecha(coordenadas, tamanio):
    return (coordenadas[0] + tamanio - 1, coordenadas[1] + tamanio - 1)

def esquinaInferiorIzquierda(coordenadas, tamanio):
    return (coordenadas[0] + tamanio - 1, coordenadas[1])


def tiene_esquinas_ocupadas(campo, coordenadas, tamanio):
    return (campo[coordenadas[0]][coordenadas[1]] != 0 
            or campo[esquinaInferiorDerecha(coordenadas, tamanio)[0]][esquinaInferiorDerecha(coordenadas, tamanio)[1]]!= 0 
            or campo[esquinaSuperiorDerecha(coordenadas, tamanio)[0]][esquinaSuperiorDerecha(coordenadas, tamanio)[1]] != 0 
            or campo[esquinaInferiorIzquierda(coordenadas, tamanio)[0]][esquinaInferiorIzquierda(coordenadas, tamanio)[1]] != 0)

def subdividir_campo(coordenada1, silox, siloy, tamanio):
    # Extraer las coordenadas de las esquinas superiores izquierdas e inferiores derechas del campo
    x1, y1 = coordenada1
    # Calcular la mitad de filas y columnas
    mitad_tamanio = int(tamanio / 2)
    # Determinar las coordenadas de las esquinas superiores izquierdas e inferiores derechas de cada submatriz
    campo_subdivididos = []

    campo1 = (x1, y1)
    campo2 = (x1 , y1 + mitad_tamanio)
    campo3 = (x1 + mitad_tamanio, y1)
    campo4 = (x1 + mitad_tamanio, y1 + mitad_tamanio)

    if silox >= mitad_tamanio and siloy < mitad_tamanio:
        campo_subdivididos.extend([campo3, campo1, campo2, campo4])
    elif silox < mitad_tamanio and siloy >= mitad_tamanio:
        campo_subdivididos.extend([campo2, campo1, campo3, campo4])
    elif silox >= mitad_tamanio and siloy >= mitad_tamanio:
        campo_subdivididos.extend([campo4, campo1, campo2, campo3])
    else:
        campo_subdivididos.extend([campo1, campo2, campo3, campo4])
    
    return campo_subdivididos

def divide_y_venceras(campo, coordenadas, tamanio, silox, siloy, agrupaciones_hechas):
    if (tamanio > 2):
        coordenadas_subdivididos = subdividir_campo(coordenadas, silox, siloy, tamanio)
        for  i in range(4):
            if (tiene_esquinas_ocupadas(campo,coordenadas, tamanio)):
                agrupaciones_hechas = agrupar_diagonales(campo, coordenadas, tamanio, agrupaciones_hechas)
            agrupaciones_hechas = divide_y_venceras(campo, coordenadas_subdivididos[i], int (tamanio/2), silox, siloy, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonales(campo, coordenadas, tamanio, agrupaciones_hechas)
    return agrupaciones_hechas


tamanio = int(input())
silox = int(input())
siloy = int(input())
agrupaciones_hechas = 1
campo = []
for i in range(tamanio):
    fila = []
    for j in range(tamanio):
        fila.append(0)
    campo.append(fila)
coordenadas = (0, 0)

campo[silox][siloy] = 1 
agrupaciones_hechas = divide_y_venceras(campo, coordenadas, tamanio, silox, siloy, agrupaciones_hechas)
for fila in range(tamanio):
    for columna in range(tamanio):
        print(campo[fila][columna], end = "")
    print()