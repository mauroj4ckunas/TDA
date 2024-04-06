
def BranchAndBound(influencers):
    mejores_influencers = []
    mejor_valor = 0
    estado_actual = {
        "valor": mejor_valor, 
        "influencers_seleccionados": [], 
        "influencers_restantes": influencers
    }
    
    frontera = [estado_actual]
    
    while len(estado_actual["influencers_restantes"]) > 0:
        
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
           
            
            
            
            
def seleccionar_influencer(influencers_restantes):
    # Selecciona el influencer con el mayor valor
    return max(influencers_restantes, key=lambda x: x.valor)

def eliminar_influencers_no_compatibles(influencer, influencers_restantes):
    # Elimina influencers incompatibles con el influencer seleccionado
    influener_filtrados = [x for x in influencers_restantes if x["codigo"] not in influencer["no_compatibles"]]
    return influener_filtrados
    
def suma_del_valor_de():
    pass