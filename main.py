from Modulos.Datos import cargar_datos, guardar_datos
from Modulos.CRUD import EditarCiudad, AgregarCiudad, BuscarCiudadNombre, BuscarCiudadPais, BuscarCiudadCodigo
from Modulos.Menus import menu_agregar_ciudad, menu_buscar_ciudad, menu_editar_ciudad, menu_ordenar_lista, menu_principal, Saludo_User, pedir_opc

RUTA_CIUDADES_JSON = "Datos/Ciudades.json"

Datos_Ciudades = cargar_datos(RUTA_CIUDADES_JSON)

""" Datos_Ciudades = EditarCiudad(Datos_Ciudades) """
""" Datos_Ciudades = AgregarCiudad(Datos_Ciudades) """
""" BuscarCiudadNombre(Datos_Ciudades) """
""" BuscarCiudadPais(Datos_Ciudades) """
""" BuscarCiudadCodigo(Datos_Ciudades) """

Saludo_User()

while True:
    menu_principal()
    choise = pedir_opc()       # Pide el input int
    if choise == 1:
        Datos_Ciudades = AgregarCiudad(Datos_Ciudades)
    elif choise == 2:
        while True:
            menu_buscar_ciudad()
            choise = pedir_opc()
            if choise == 1:
                BuscarCiudadNombre(Datos_Ciudades)
            elif choise == 2:
                BuscarCiudadPais(Datos_Ciudades)
            elif choise == 3:
                BuscarCiudadCodigo(Datos_Ciudades)
            elif choise == 0:
                break
            else:
                print("Valor Invalido")
    elif choise == 3:
        Datos_Ciudades = EditarCiudad(Datos_Ciudades)
    elif choise == 4:
        print(Datos_Ciudades)
    elif choise == 0:
        break
    else:
        print("Valor Invalido")

print("Gracias por Usar Nuestro Programa")

guardar_datos(Datos_Ciudades, RUTA_CIUDADES_JSON)