from Modulos.Datos import cargar_datos, guardar_datos
from Modulos.CRUD import EditarCiudad, AgregarCiudad

RUTA_CIUDADES_JSON = "Datos/Ciudades.json"

Datos_Ciudades = cargar_datos(RUTA_CIUDADES_JSON)

""" Datos_Ciudades = EditarCiudad(Datos_Ciudades) """
Datos_Ciudades = AgregarCiudad(Datos_Ciudades)

guardar_datos(Datos_Ciudades, RUTA_CIUDADES_JSON)