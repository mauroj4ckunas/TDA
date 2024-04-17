class Influencer:
    def __init__(self, codigo, nombre, valor, no_compatibles):
        self.codigo = codigo
        self.nombre = nombre
        self.valor = valor
        self.no_compatibles = no_compatibles


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
        if valorAmpliado > estadoActual["mayorValor"] and influencer.codigo not in estadoActual["incompatibles"]:
            estadoActual["mejorSeleccion"] = seleccionadosAmpliado
            estadoActual["mayorValor"] = valorAmpliado

    else:
        sumaRestantes = estadoActual["cota_superior"][influencer.codigo] # O(1)
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

        if CotaAmpliada > estadoActual["mayorValor"] and influencer.codigo not in estadoActual["incompatibles"]:
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







def ObtenerCombinacionMasInfluyente(influencers, cota_superior): 
    nroInfluencer = 0
    estado = {
        "cota_superior": cota_superior,
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


def calcular_cota_superior(influencers):
    total = 0
    cota_superior = {}
    for influencer in influencers: # O(n)
        total += influencer.valor

    suma = 0
    for i in range(len(influencers)): # O(n)                
        suma += influencers[i].valor
        cota_superior[influencers[i].codigo] = total - suma

    return cota_superior

def main(nombre_archivo):
    influencers = cargar_influencers(nombre_archivo)
    cota_superior= calcular_cota_superior(influencers) # O(n)
    mejores_influencers, mejor_valor = ObtenerCombinacionMasInfluyente(influencers, cota_superior) # O(2^n)

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