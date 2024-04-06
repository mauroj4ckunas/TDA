
class Influencer:
    def __init__(self, codigo, nombre, valor, no_compatibles):
        self.codigo = codigo
        self.nombre = nombre
        self.valor = valor
        self.no_compatibles = no_compatibles

def BranchAndBound(influencers):
    mejores_influencers = []
    mejor_valor = 0
    estado_actual = {
        "valor": mejor_valor, 
        "influencers_seleccionados": [], 
        "influencers_restantes": influencers
    }
    
    frontera = [estado_actual]
    
    while len(frontera) > 0:
        
        estado_actual = frontera.pop()
        
        if estado_actual["valor"] + suma_del_valor_de(estado_actual["influencers_restantes"]) <= mejor_valor:
            continue
        
        
        if len(estado_actual["influencers_restantes"]) == 0:
            if estado_actual["valor"] > mejor_valor:
               mejores_influencers = estado_actual["influencers_seleccionados"]
               mejor_valor = estado_actual["valor"]
            continue
        
        influencer = seleccionar_influencer(estado_actual["influencers_restantes"])
        nuevos_influencers_restantes = eliminar_influencers_no_compatibles(influencer, estado_actual["influencers_restantes"]) 
        
        frontera.append({
            "valor": estado_actual["valor"] + influencer["valor"],
            "influencers_seleccionados": estado_actual["influencers_seleccionados"] + [influencer["nombre"]],
            "influencers_restantes": nuevos_influencers_restantes
        }) 
    
    return mejores_influencers, mejor_valor
            
            
def seleccionar_influencer(influencers_restantes: list):
    # Selecciona el influencer con el mayor valor
    indice_max = influencers_restantes.index(max(influencers_restantes, key=lambda x: x["valor"]))
    return influencers_restantes.pop(indice_max)

def eliminar_influencers_no_compatibles(influencer, influencers_restantes):
    # Elimina influencers incompatibles con el influencer seleccionado
    influener_filtrados = [x for x in influencers_restantes if x["codigo"] not in influencer["no_compatibles"]]
    return influener_filtrados
    
def suma_del_valor_de(influencers_restantes: list):
    return sum(inf["valor"] for inf in influencers_restantes)


def cargar_influencers(nombre_archivo):
    influencers = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            codigo = int(parts[0])
            nombre = parts[1]
            valor = int(parts[2])
            no_compatibles = [int(x) for x in parts[3:]]
            influencers.append(Influencer(codigo, nombre, valor, no_compatibles))
    return influencers

def main(nombre_archivo):
    influencers = cargar_influencers(nombre_archivo)
    mejores_influencers, mejor_valor = BranchAndBound(influencers)

    print("Valor conseguido:", mejor_valor)
    for influencer in mejores_influencers:
        print(influencer)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python promocion.py <archivo>")
        sys.exit(1)
    main(sys.argv[1])
