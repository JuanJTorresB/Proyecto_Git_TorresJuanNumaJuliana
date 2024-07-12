from Modulos.Datos import cargar_datos, guardar_datos
from Modulos.CRUD import EditarCiudad, AgregarCiudad, BuscarCiudadNombre, BuscarCiudadPais, BuscarCiudadCodigo

RUTA_CIUDADES_JSON = "Datos/Ciudades.json"

Datos_Ciudades = cargar_datos(RUTA_CIUDADES_JSON)

""" Datos_Ciudades = EditarCiudad(Datos_Ciudades) """
""" Datos_Ciudades = AgregarCiudad(Datos_Ciudades) """
""" BuscarCiudadNombre(Datos_Ciudades) """
""" BuscarCiudadPais(Datos_Ciudades) """
BuscarCiudadCodigo(Datos_Ciudades)

guardar_datos(Datos_Ciudades, RUTA_CIUDADES_JSON)