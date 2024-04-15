
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
        if not campo[i][i].esta_agrupada():
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[i][i] = (agrupaciones_hechas)
            campo[i][i - 1] = (agrupaciones_hechas)
            campo[i - 1][i] = (agrupaciones_hechas)
    return agrupaciones_hechas
    
def agrupar_diagonal_esquina2(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[tamanio -1 - i][tamanio -1 - i].esta_agrupada():
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[tamanio -1 - i][tamanio -1 - i] = (agrupaciones_hechas)
            campo[tamanio -1 - i][tamanio - i] = (agrupaciones_hechas)
            campo[tamanio - i][tamanio -1 - i] = (agrupaciones_hechas)
    return agrupaciones_hechas

def agrupar_diagonal_esquina3(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[i][tamanio - 1 - i].esta_agrupada():
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[i][tamanio - 1 - i] = (agrupaciones_hechas)
            campo[i][tamanio - i] = (agrupaciones_hechas)
            campo[i - 1][tamanio - 1 - i] = (agrupaciones_hechas)
    return agrupaciones_hechas

def agrupar_diagonal_esquina4(campo, tamanio, agrupaciones_hechas):
    for i in range(tamanio):
        if not campo[tamanio - 1 - i][i].esta_agrupada():
            agrupaciones_hechas = agrupaciones_hechas + 1
            campo[tamanio - 1 - i][i].agrupar(agrupaciones_hechas)
            campo[tamanio - 1 - i][i - 1].agrupar(agrupaciones_hechas)
            campo[tamanio - i][i].agrupar(agrupaciones_hechas)
    return agrupaciones_hechas

def tiene_esquinas_ocupadas(campo, tamanio):
    return (campo[0][0] != 0 or campo[tamanio - 1][tamanio - 1]!= 0 or campo[0][tamanio - 1] != 0 or campo[tamanio - 1][0] != 0)

def subdividir_campo(campo, silox, siloy, tamanio):
    campo_subdivididos = []
    mitad_filas = tamanio / 2
    mitad_columnas = tamanio / 2

    campo1 = [fila[:mitad_columnas] for fila in campo[:mitad_filas]]
    campo2 = [fila[mitad_columnas:] for fila in campo[:mitad_filas]]
    campo3 = [fila[:mitad_columnas] for fila in campo[mitad_filas:]]
    campo4 = [fila[mitad_columnas:] for fila in campo[mitad_filas:]]
    
    if silox >= mitad_columnas and siloy < mitad_filas:
        campo_subdivididos.append(campo2)
        campo_subdivididos.append(campo1)
        campo_subdivididos.append(campo3)
        campo_subdivididos.append(campo4)
    elif silox < mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.append(campo3)
        campo_subdivididos.append(campo1)
        campo_subdivididos.append(campo2)
        campo_subdivididos.append(campo4)
    elif silox >= mitad_columnas and siloy >= mitad_filas:
        campo_subdivididos.append(campo4)
        campo_subdivididos.append(campo1)
        campo_subdivididos.append(campo2)
        campo_subdivididos.append(campo3)
    else:
        campo_subdivididos.append(campo1)
        campo_subdivididos.append(campo2)
        campo_subdivididos.append(campo3)
        campo_subdivididos.append(campo4)
        
    return campo_subdivididos

def divide_y_venceras(campo, tamanio, silox, siloy, agrupaciones_hechas):
    if (tamanio > 2):
        campo_subdivididos = subdividir_campo(campo, silox, siloy, tamanio)
        for  i in range(4):
            if (tiene_esquinas_ocupadas(campo, tamanio)):
                agrupaciones_hechas = agrupar_diagonales(campo, tamanio, agrupaciones_hechas)
            divide_y_venceras(campo_subdivididos[i], tamanio/2, silox, siloy, agrupaciones_hechas)
    else: agrupaciones_hechas = agrupar_diagonales(campo, tamanio, agrupaciones_hechas)