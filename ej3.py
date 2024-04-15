def agrupar_diagonales(campo, tamanio, agrupaciones_hechas):
    if campo[0][0] != 0:
       agrupaciones_hechas = agrupar_diagonal_esquina1(campo, tamanio, agrupaciones_hechas)
    elif campo[tamanio - 1][tamanio - 1] !=0 :
        agrupaciones_hechas = agrupar_diagonal_esquina2(campo, tamanio, agrupaciones_hechas)
    elif campo[0][tamanio - 1] != 0:
        agrupaciones_hechas = agrupar_diagonal_esquina3(campo, tamanio, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonal_esquina4(campo, tamanio, agrupaciones_hechas)

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

def tiene_esquinas_ocupadas(campo, tamanio):
    return (campo[0][0] != 0 or campo[tamanio - 1][tamanio - 1]!= 0 or campo[0][tamanio - 1] != 0 or campo[tamanio - 1][0] != 0)

def subdividir_campo(campo, silox, siloy, tamanio):
    mitad_filas = int(tamanio / 2)
    mitad_columnas = int(tamanio / 2)

    campo1 = [fila[:mitad_columnas] for fila in campo[:mitad_filas]]
    campo2 = [fila[mitad_columnas:] for fila in campo[:mitad_filas]]
    campo3 = [fila[:mitad_columnas] for fila in campo[mitad_filas:]]
    campo4 = [fila[mitad_columnas:] for fila in campo[mitad_filas:]]
    
    campo_subdivididos = []
    
    if silox >= mitad_columnas and siloy < mitad_filas:
        campo_subdivididos.extend([campo2, campo1, campo3, campo4])
    elif silox < mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.extend([campo3, campo1, campo2, campo4])
    elif silox >= mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.extend([campo4, campo1, campo2, campo3])
    else:
        campo_subdivididos.extend([campo1, campo2, campo3, campo4])
        
    return campo_subdivididos

def divide_y_venceras(campo, tamanio, silox, siloy, agrupaciones_hechas):
    if (tamanio > 2):
        campo_subdivididos = subdividir_campo(campo, silox, siloy, tamanio)
        for  i in range(4):
            if (tiene_esquinas_ocupadas(campo, tamanio)):
                agrupaciones_hechas = agrupar_diagonales(campo, tamanio, agrupaciones_hechas)
            agrupaciones_hechas = divide_y_venceras(campo_subdivididos[i], int (tamanio/2), silox, siloy, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonales(campo, tamanio, agrupaciones_hechas)
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
    
campo[silox][siloy] = 1 
agrupaciones_hechas = divide_y_venceras(campo, tamanio, silox, siloy, agrupaciones_hechas)
for fila in range(tamanio):
    for columna in range(tamanio):
        print(campo[fila][columna], end = "")
    print()