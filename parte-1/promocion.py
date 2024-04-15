class Influencer:
    def __init__(self, codigo, nombre, valor, no_compatibles):
        self.codigo = codigo
        self.nombre = nombre
        self.valor = valor
        self.no_compatibles = no_compatibles


def suma_del_valor_de(influencers: list, desde: int = 0):
    suma = 0
    for influencer in influencers[desde:]:
        suma += influencer.valor
    return suma


def seleccionar_descendiente_mayor_cota(lista_diccionarios):
    descendiente_mayor_cota = max(lista_diccionarios, key=lambda x: x['cota'])
    lista_diccionarios.remove(descendiente_mayor_cota)
    return descendiente_mayor_cota


def Backtrack (estadoActual, nroInfluencer):
    influencer = estadoActual["influencers"][nroInfluencer]
    
    seleccionadosAmpliado = estadoActual["seleccionados"] + [influencer]
    valorActual = estadoActual["valorActual"]
    valorAmpliado = estadoActual["valorActual"] + influencer.valor
    cantidadInfluencers = len(estadoActual["influencers"])

    if nroInfluencer == cantidadInfluencers -1:
        if valorActual > estadoActual["mayorValor"]:
            estadoActual["mejorSeleccion"] = estadoActual["seleccionados"]
            estadoActual["mayorValor"] = valorActual
        if valorAmpliado > estadoActual["mayorValor"] and influencer not in estadoActual["incompatibles"]:
            estadoActual["mejorSeleccion"] = seleccionadosAmpliado
            estadoActual["mayorValor"] = valorAmpliado

    else:
        sumaRestantes = suma_del_valor_de(estadoActual["influencers"], nroInfluencer + 1)
        CotaActual = valorActual + sumaRestantes
        CotaAmpliada = valorAmpliado + sumaRestantes
        descendientes = []

        if CotaActual > estadoActual["mayorValor"]: 
            descendientes.append({
                                    "seleccionados": estadoActual["seleccionados"],
                                    "valor": valorActual,
                                    "incompatibles": estadoActual["incompatibles"],
                                    "cota": CotaActual
                                })

        if CotaAmpliada > estadoActual["mayorValor"] and influencer not in estadoActual["incompatibles"]:
            descendientes.append({
                                    "seleccionados": seleccionadosAmpliado, 
                                    "valor": valorAmpliado,
                                    "incompatibles": estadoActual["incompatibles"] + influencer.no_compatibles,
                                    "cota": CotaAmpliada
                                })

        while len(descendientes) > 0:
            seleccionadosDesc = {}
            if len(descendientes) > 1:
                seleccionadosDesc = seleccionar_descendiente_mayor_cota(descendientes)
            else: 
                seleccionadosDesc = descendientes.pop()
            if seleccionadosDesc["cota"] > estadoActual["mayorValor"]:
                estadoActual["valorActual"] = seleccionadosDesc["valor"]
                estadoActual["seleccionados"] = seleccionadosDesc["seleccionados"]
                estadoActual["incompatibles"] = seleccionadosDesc["incompatibles"]
                Backtrack(estadoActual, nroInfluencer + 1)







def ObtenerCombinacionMasInfluyente(influencers): 
    nroInfluencer = 0
    estado = {
        "influencers": influencers,
        "mejorSeleccion": [],
        "mayorValor": 0,
        "valorActual": 0,
        "seleccionados": [],
        "incompatibles": []
    }


    Backtrack(estado, nroInfluencer)

    return estado["mejorSeleccion"], estado["mayorValor"]

def cargar_influencers(nombre_archivo):
    influencers = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            codigo = int(parts[0])
            nombre = parts[1]
            valor = int(parts[2])
            no_compatibles = [int(x) for x in parts[3:] if x.strip()]
            influencers.append(Influencer(codigo, nombre, valor, no_compatibles))
    return influencers

def main(nombre_archivo):
    influencers = cargar_influencers(nombre_archivo)
    # Ordeno influencers por valor de menor a mayor, para que obtener el de mayor valor sea O(1)
    influencers_ordenados = sorted(influencers, key=lambda x: x.valor, reverse=True) # O(n log n)
    mejores_influencers, mejor_valor = ObtenerCombinacionMasInfluyente(influencers_ordenados)

    print("Valor conseguido:", mejor_valor)
    print("\n")
    for influencer in mejores_influencers:
        print(influencer.nombre)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python promocion.py <archivo>")
        sys.exit(1)
    main(sys.argv[1])