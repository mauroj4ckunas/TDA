def agrupar_diagonales(campo, coordenadas, tamanio, agrupaciones_hechas):
    if campo[coordenadaX1(coordenadas)][coordenadaY1(coordenadas)] != 0:
       agrupaciones_hechas = agrupar_diagonal_esquina1(campo,coordenadas, tamanio, agrupaciones_hechas)
    elif campo[tamanio - 1][tamanio - 1] !=0 :
        agrupaciones_hechas = agrupar_diagonal_esquina2(campo,coordenadas, tamanio, agrupaciones_hechas)
    elif campo[0][tamanio - 1] != 0:
        agrupaciones_hechas = agrupar_diagonal_esquina3(campo,coordenadas, tamanio, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonal_esquina4(campo,coordenadas, tamanio, agrupaciones_hechas)

    return agrupaciones_hechas

def agrupar_diagonal_esquina1(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[i][i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[i][i] = agrupaciones_hechas
            campo[i][i - 1] = agrupaciones_hechas
            campo[i - 1][i] = agrupaciones_hechas
    return agrupaciones_hechas
    
def agrupar_diagonal_esquina2(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[tamanio -1 - i][tamanio -1 - i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[tamanio -1 - i][tamanio -1 - i] = agrupaciones_hechas
            campo[tamanio -1 - i][tamanio - i] = agrupaciones_hechas
            campo[tamanio - i][tamanio -1 - i] = agrupaciones_hechas
    return agrupaciones_hechas

def agrupar_diagonal_esquina3(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[i][tamanio - 1 - i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[i][tamanio - 1 - i] = agrupaciones_hechas
            campo[i][tamanio - i] = agrupaciones_hechas
            campo[i - 1][tamanio - 1 - i] = agrupaciones_hechas
    return agrupaciones_hechas

def agrupar_diagonal_esquina4(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[tamanio - 1 - i][i] != 0:
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[tamanio - 1 - i][i] = agrupaciones_hechas
            campo[tamanio - 1 - i][i - 1] = agrupaciones_hechas
            campo[tamanio - i][i] = agrupaciones_hechas
    return agrupaciones_hechas

def coordenadaX1(coordenadas):
    return coordenadas[0][0]

def coordenadaY1(coordenadas):
    return coordenadas[0][1]

def coordenadaX2(coordenadas):
    return coordenadas[1][0]

def coordenadaY2(coordenadas):
    return coordenadas[1][1]

def esquinaSuperiorDerecha(coordenadas):
    return (coordenadaX1(coordenadas), coordenadaY2(coordenadas))

def esquinaInferiorIzquierda(coordenadas):
    return (coordenadaX2(coordenadas), coordenadaY1(coordenadas))


def tiene_esquinas_ocupadas(campo, coordenadas, tamanio):
    return (campo[coordenadaX1(coordenadas)][coordenadaY1(coordenadas)] != 0 
            or campo[coordenadaX2(coordenadas)][coordenadaY2(coordenadas)]!= 0 
            or campo[esquinaSuperiorDerecha(coordenadas)[0]][esquinaSuperiorDerecha(coordenadas)[1]] != 0 
            or campo[esquinaInferiorIzquierda(coordenadas)[0]][esquinaInferiorIzquierda(coordenadas)[1]] != 0)

def subdividir_campo(coordenada1, coordenada2, silox, siloy, tamanio):
    # Extraer las coordenadas de las esquinas superiores izquierdas e inferiores derechas del campo
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    # Calcular la mitad de filas y columnas
    mitad_filas = tamanio // 2
    mitad_columnas = tamanio // 2
    # Determinar las coordenadas de las esquinas superiores izquierdas e inferiores derechas de cada submatriz
    campo_subdivididos = []

    campo1 = [(x1, y1), (x1 + mitad_columnas - 1, y1 + mitad_filas - 1)]
    campo2 = [(x1 + mitad_columnas, y1), (x2, y1 + mitad_filas - 1)]
    campo3 = [(x1, y1 + mitad_filas), (x1 + mitad_columnas - 1, y2)]
    campo4 = [(x1 + mitad_columnas, y1 + mitad_filas), (x2, y2)]

    if silox >= mitad_columnas and siloy < mitad_filas:
        campo_subdivididos.extend([campo2, campo1, campo3, campo4])
    elif silox < mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.extend([campo3, campo1, campo2, campo4])
    elif silox >= mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.extend([campo4, campo1, campo2, campo3])
    else:
        campo_subdivididos.extend([campo1, campo2, campo3, campo4])
    
    return campo_subdivididos

def divide_y_venceras(campo, coordenadas, tamanio, silox, siloy, agrupaciones_hechas):
    if (tamanio > 2):
        coordenadas_subdivididos = subdividir_campo(coordenadas[0], coordenadas[1], silox, siloy, tamanio)
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
coordenadas = [(0, 0), (tamanio - 1, tamanio - 1)]  

campo[silox][siloy] = 1 
agrupaciones_hechas = divide_y_venceras(campo, coordenadas, tamanio, silox, siloy, agrupaciones_hechas)
for fila in range(tamanio):
    for columna in range(tamanio):
        print(campo[fila][columna], end = "")
    print()