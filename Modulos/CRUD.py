def EditarCiudad(Datos):
    ciudades_Elegir = []
    for ciudades in Datos:
        ciudades_Elegir.append(ciudades["nombreCiudad"])
    print("*"*80)
    print("Que Ciudad de estas")
    print("")
    print(ciudades_Elegir)
    print("")
    ciudad_Elegida = input("Deseas Elegir \n>")
    if ciudad_Elegida in ciudades_Elegir:
        for ciudades in Datos:
            if ciudades["nombreCiudad"] == ciudad_Elegida:
                ciudades["nombreCiudad"] = input("Nombre de la ciudad: ")
                ciudades["codigoPostal"] = input("Codigo Postal de la ciuda: ")
                ciudades["poblacionEstimada"] = input("Poblacion Estimada: ")
                ciudades["pais"] = input("Nombre del pais: ")
                return Datos
    else:
        print("Ciudad no valida")
        return Datos
    
def AgregarCiudad(Datos):
    Ciudad = {}
    Ciudad["nombreCiudad"] = input("Nombre de la ciudad: ")
    Ciudad["codigoPostal"] = input("Codigo Postal de la ciuda: ")
    Ciudad["poblacionEstimada"] = input("Poblacion Estimada: ")
    Ciudad["pais"] = input("Nombre del pais: ")
    Datos.append(Ciudad)
    return Datos

def BuscarCiudadNombre(Datos):
    ciudades_Elegir = []
    for ciudades in Datos:
        ciudades_Elegir.append(ciudades["nombreCiudad"])
    print("*"*80)
    print("Que Ciudad de estas")
    print("")
    print(ciudades_Elegir)
    print("")
    ciudad_Elegida = input("Deseas Elegir \n>")
    if ciudad_Elegida in ciudades_Elegir:
        for ciudades in Datos:
            if ciudades["nombreCiudad"] == ciudad_Elegida:
                print("Nombre Ciudad: ", ciudades["nombreCiudad"])
                print("Nombre Codigo Postal: ", ciudades["codigoPostal"])
                print("Nombre Poblacion Estimada: ", ciudades["poblacionEstimada"])
                print("Nombre Pais: ", ciudades["pais"])
    else:
        print("Ciudad no valida")
    
def BuscarCiudadPais(Datos):
    ciudades_Elegir_reps = []
    for ciudades in Datos:
        ciudades_Elegir_reps.append(ciudades["pais"])
    ciudades_Elegir = set(ciudades_Elegir_reps)
    print("*"*80)
    print("De que pais de estos es tu Ciudad")
    print("")
    print(ciudades_Elegir)
    print("")
    ciudad_Elegida = input("\n>")
    if ciudad_Elegida in ciudades_Elegir:
        for ciudades in Datos:
            if ciudades["pais"] == ciudad_Elegida:
                print("Nombre Ciudad: ", ciudades["nombreCiudad"])
                print("Nombre Codigo Postal: ", ciudades["codigoPostal"])
                print("Nombre Poblacion Estimada: ", ciudades["poblacionEstimada"])
                print("Nombre Pais: ", ciudades["pais"])
                print("*"*80)
    else:
        print("Pais no valido")
        
def BuscarCiudadCodigo(Datos):
    ciudades_Elegir = []
    for ciudades in Datos:
        ciudades_Elegir.append(ciudades["codigoPostal"])
    print("*"*80)
    print("Que Codigo Postal de estos")
    print("")
    print(ciudades_Elegir)
    print("")
    ciudad_Elegida = input("Deseas Elegir \n>")
    if ciudad_Elegida in ciudades_Elegir:
        for ciudades in Datos:
            if ciudades["codigoPostal"] == ciudad_Elegida:
                print("Nombre Ciudad: ", ciudades["nombreCiudad"])
                print("Nombre Codigo Postal: ", ciudades["codigoPostal"])
                print("Nombre Poblacion Estimada: ", ciudades["poblacionEstimada"])
                print("Nombre Pais: ", ciudades["pais"])
    else:
        print("Codigo Postal no valida")