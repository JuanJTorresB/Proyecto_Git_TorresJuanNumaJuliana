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
                print("Ciudad no Valida")
                return Datos
    else:
        print("Ciudad no valida")
        return Datos