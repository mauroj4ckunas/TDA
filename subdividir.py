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