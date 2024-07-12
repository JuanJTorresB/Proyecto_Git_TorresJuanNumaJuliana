def Saludo_User():
    print("Bienvenido User")

def menu_principal():
    print("-----------Menú principal-----------")   
    print("Digita [1] para --> Agregar cuidad")
    print("Digita [2] para --> Buscar ciudad")
    print("Digita [3] para --> Editar ciudad existente")
    print("Digita [4] para --> Ver lista de ciudadades registradas")
    print("Digita [0] para --> Salir")
    print("-----------------------------------------------")

def menu_agregar_ciudad():
    print("-------------Menú de Agregar ciudad-------------")  
    print("Digita [1] para --> Ingrese el nombre")
    print("Digita [2] para --> Ingrese el codigo postal")
    print("Digita [3] para --> Ingrese la poblacion estimada")
    print("Digita [4] para --> Ingrese el pais")
    print("Digita [0] para --> Regresar al menu principal")
    print("-----------------------------------------------")
    
def menu_buscar_ciudad():
    print("-------------Menú de Buscar ciudad-------------")  
    print("Digita [1] para --> Buscar por nombre")
    print("Digita [2] para --> Buscar por pais")
    print("Digita [3] para --> Buscar por codigo postal")
    print("Digita [0] para --> Regresar al menu principal")
    print("-----------------------------------------------")
        
def menu_editar_ciudad():
    print("-------------Menú de Editar Ciudad-------------")  
    print("Digita [1] para --> Cambiar nombre")
    print("Digita [2] para --> Cambiar codigo postal")
    print("Digita [3] para --> Cambiar poblacion estimada")
    print("Digita [4] para --> Cambiar pais")
    print("Digita [0] para --> Regresar al menu principal")
    print("-----------------------------------------------")
    
    
def menu_ordenar_lista():
    print("-------------Menú Ordenar lista-------------")  
    print("Digita [1] para --> Ordenar por nombre")
    print("Digita [2] para --> Ordenar por poblacion")
    print("Digita [3] para --> Ordenar por pais")
    print("Digita [0] para --> Regresar al menu principal")
    print("-----------------------------------------------")
        
    
def pedir_opc():
    opc = 0
    try:
        opc = int(input("-->Digita la opción a elegir: "))
        return opc
    except Exception:
        print("Valor inválido")
        return 0