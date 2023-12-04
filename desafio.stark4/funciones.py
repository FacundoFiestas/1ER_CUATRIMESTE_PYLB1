from data_stark import lista_personajes
import re

#1.1
def extraer_iniciales(nombre_heroe: str) -> str:
    """
    esta funcion recibe como parametro un string con el nombre del personaje y devuelve sus iniciales separadas por un punto,
    si el string recibido no existe, retonar N/A
    """
    if not nombre_heroe:
        return "N/A"
    nombre_heroe = re.sub(r"\bthe\b", "", nombre_heroe, flags=re.IGNORECASE)
    nombre_heroe = nombre_heroe.replace("-"," ")
    
    iniciales = ''.join(re.findall(r'\b\w', nombre_heroe.upper()))
    iniciales_con_puntos = '.'.join(iniciales) 

    return iniciales_con_puntos

#1.2
def definir_iniciales_nombre(heroe:dict)-> bool:
    """
    Esta funcion recibe como parametros un diccionario, verifica que el mismo lo sea y que tambien tenga presente la key nombre,
    de lo contrario retornara false, despues agrega el dato "iniciales" utilizando la funcion del punto anterior.
    """
    if not type(heroe) == dict and 'nombre' not in heroe: 
        return False
    
    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
    return True

#1.3
def agregar_iniciales_nombre(lista_heroes: lista_personajes)-> bool:
    """
    Esta funcion recibe como parametros una lista de heroes, primero verifica que el parametro sea una lista y que la misma no este 
    vacia, despues con un for utilizara una funcion anterior para agregar la key iniciales a todos los diccionarios de la lista,
    si la funcion se cumple, retornara true, caso contrario, false. 
    """

    if type(lista_heroes) != list and not lista_heroes:
        return False
    
    for heroe in lista_heroes:
        resultado = definir_iniciales_nombre(heroe)
        

    if resultado == False:
        print("El origen de datos no contiene el formato correcto")
        return False
    return True

#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes:lista_personajes):
    """
    Esta funcion recibe como parametros una lista de heroes, primero verifica que el parametro sea una lista y que la misma no este 
    vacia, despues utiliza una funciona anterior para agregar sus iniciales al diccionario, y por ultimo imprime el nombre y las iniciales
    encerradas entre parentesis.
    """

    if not type(lista_heroes) == list and not lista_heroes:
        return False
    
    resultado = agregar_iniciales_nombre(lista_heroes)
    if resultado == False:
        return False
    
    for heroe in lista_heroes:
        print(f"*{heroe['nombre']} ({heroe['iniciales']})")

#2.1
def generar_codigo_heroe(id_heroe: int, genero_heroe: str):
    """
    Esta funcion recibe como primer parametro un entero, y como segundo parametro un str, el cual tiene que ser si o si "F", "M" o "NB"
    para que la funcion actue como se debe, en caso de funcionar, retorna el codigo del heroe, de lo contrario, retornara N/A.
    """
    cantidad_caracteres = 9 - len(genero_heroe)
    if type(id_heroe) == int and (genero_heroe == 'M' or genero_heroe == 'F' or genero_heroe == 'NB'):
        codigo = f"{genero_heroe}-{str(id_heroe).zfill(cantidad_caracteres)}"
        mensaje = codigo
    else:
        mensaje = "N/A"

    return mensaje

#2.2
def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    """
    La funcion recibe como parametros un diccionario que representa a un heroe, y un entero, que sera utilizado para crear el codigo
    del mismo, verifica que el diccionario no este vacio, y que el largo del codigo sea exactamente 10 caracteres, de cumplirse estas
    condiciones, se agregara el valor al diccionario, caso contrario, la funcion retornara false.
    """
    if not heroe:
        return False
    
    codigo = generar_codigo_heroe(id_heroe, heroe.get("genero", ""))
    
    if len(codigo) != 10:
        return False
    heroe["codigo_heroe"] = codigo
    
    return True

#2.3
def stark_generar_codigos_heroes(lista_heroes:list):
    """
    La funcion recibe como parametro una lista de heroes, valida que no este vacia, que contenga diccionarios y que tenga presente
    la clave "genero" y en caso de aprobar todas estas validaciones, le asignara un codigo a cada heroe segun su posicion en la lista,
    los imprimira y tambien imprimira la cantidad de codigos que se asignaron.
    """
    cantidad_codigos = 0
    id_heroe = 1
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
    
    for heroe in lista_heroes:
        if type(heroe) == dict and "genero" in heroe:
                agregar_codigo_heroe(heroe, id_heroe)
                cantidad_codigos += 1
                codigo_heroe = heroe["codigo_heroe"]
                print(f"El código del héroe en la posición {id_heroe} es: {codigo_heroe}")
        else:
                print(f"El héroe en la posición {id_heroe} no contiene el formato correcto")
        
        id_heroe += 1
    print(f"Se asignaron {cantidad_codigos} códigos")

#3.1
def sanitizar_entero(numero_str: str):
    """
    esta funcion recibe como parametro un string, la funcion se encarga de validar si es posible convertirlo a entero o no, utiliza
    strip para eliminar espacios en blancos y regex(match) para hallar caracteres numericos, retornara el numero convertido a entero
    en caso de que sea posible convertirlo, de lo contrario retornara -1, -2 o -3.
    """
    numero_str = numero_str.strip()
    if not numero_str:
        return -3
    
    if re.match(r'^\d+$', numero_str):
        numero_entero = int(numero_str)
        if numero_entero >= 0:
            return numero_entero
        else:
            return -2 
    else:
        return -1 
    
#3.2
def sanitizar_flotante(numero_str: str):
    """
    esta funcion recibe como parametro un string, la funcion se encarga de validar si es posible convertirlo a float o no, utiliza
    strip para eliminar espacios en blancos y regex(match) para hallar caracteres numericos, retornara el numero convertido a flotante
    en caso de que sea posible convertirlo, de lo contrario retornara -1, -2 o -3.
    """
    numero_str = numero_str.strip()
    patron_regex = r'^\d+\.\d+$'
    
    if not numero_str:
        return -3
    if re.match(patron_regex, numero_str):
        numero_flotante = float(numero_str)
        if numero_flotante >= 0:
            return numero_flotante
        else:
            return -2  
    else:
        return -1  
#3.3
def sanitizar_string(valor_str: str, valor_por_defecto = "-"):
    """
    esta funcion recibe como parametro un str y un valor por defecto "-", la funcion se encarga de eliminar espacios en blanco de
    ambos parametros y de reemplazar las "/" por espacios en blanco(en el primer parametro), si el valor str contiene caracteres
    numericos, retornara n/a, de lo contrario retornara el string convertido todo a minusculas.
    """
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    valor_str = valor_str.replace('/', ' ')

    if re.search(r'\d', valor_str):
        return 'N/A'
    if not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()

    return valor_str.lower()
#3.4
def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str) -> bool:
    """
    la funcion recibe tres parametros, un diccionario, y dos strings, valida que el tipo de dato se pueda utilizar si tiene mayusculas
    o minusculas, valida que sea un tipo de dato valido y que la clave este incluida en el diccionario, de pasar todas estas
    validaciones, convertira segun lo indicado a su clase correcta.
    """
    tipo_dato = tipo_dato.lower()
    
    if tipo_dato != "string" and tipo_dato != "entero" and tipo_dato != "flotante":
        print('Tipo de dato no reconocido')
        return False
    
    if clave not in heroe:
        print('La clave especificada no existe en el héroe')
        return False
    
    match tipo_dato:
        case "string":
            heroe[clave] = sanitizar_string(heroe[clave])
        case "entero":
            heroe[clave] = sanitizar_entero(heroe[clave])
        case "flotante":
            heroe[clave] = sanitizar_flotante(heroe[clave])
    return True

#3.5
def stark_normalizar_datos(lista_heroes:list):
    """
    La función recibe como parámetros la lista de héroes, verifica que no esté vacía y, según una serie de claves válidas para normalizar,
    convierte los datos a su tipo de dato correspondiente (flotante, entero o string).
    """
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return
    
    claves_a_normalizar = {
        "altura": "flotante",
        "peso": "flotante",
        "color_ojos": "string",
        "color_pelo": "string",
        "fuerza": "entero",
        "inteligencia": "string"
    }

    for heroe in lista_heroes:
        for clave in claves_a_normalizar:
            if clave in heroe:
                tipo_dato = claves_a_normalizar[clave]
                sanitizar_dato(heroe, clave, tipo_dato)

    print("Datos normalizados")

#4
def generar_indice_nombres(lista_heroes:list):
    """
    la funcion recibe como parametros la lista de heroes, verifica que no este vacia, y mediante un patron de palabras(regex), genera
    una lista lista donde cada elemento es cada palabra que componen el nombre de los personajes.
    """
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
        return None
    
    patron_palabras = r'\b\w+\b'
    lista_palabras_nombre = []
    for heroe in lista_heroes:
        if type(heroe) == dict and 'nombre' in heroe:
            palabras = re.findall(patron_palabras, heroe['nombre'])
            lista_palabras_nombre.extend(palabras)
        else:
            print("El origen de datos no contiene el formato correcto")
            return None
    return lista_palabras_nombre

#4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
    """
    la funcion recibe como parametros la lista de personajes, utiliza la funcion anterior para generar los indices Y utiliza el metodo
    join para separar esos indices con guiones, finalmente los imprime.
    """
    indice_nombres = generar_indice_nombres(lista_heroes)
    
    indice_con_guiones = '-'.join(indice_nombres)
    print(indice_con_guiones)

#5.1
def convertir_cm_a_mtrs(valor_cm):
    """
    esta funcion recibe como parametros un valor numerico que mediante un calculo matematico sera convertido a a metros, en caso de que
    el valor ingresado no sea numerico, o sea menor a 0, la funcion retornara -1
    """
    if not (type(valor_cm) == int or type(valor_cm) == float) or valor_cm < 0:
        return -1
    valor_mtrs = valor_cm / 100.0
    return valor_mtrs
#5.2
def generar_separador(patron, largo, imprimir=True):
    """
    la funcion recibe tres parametros, el patron a tener en cuenta para generar el separador y el largo del mismo, dependiendo si el 
    tercer parametro es true o false, imprimira el separador, por defecto, si no se ingresa tercer parametro, la funcion lo imprimira 
    de todas formas.
    """
    if not (1 <= largo <= 235) or not (1 <= len(patron) <= 2):
        return 'N/A'
    
    separador = patron * largo
    if imprimir:
        print(separador)

    return separador
#5.3
def generar_encabezado(titulo:str)-> str:
    """
    la funcion recibe como parametros un str el cual sera utilzado para crear el titulo, titulo que estara entre medio de dos separadores
    ya definidos, retornara el encabezado completo.
    """
    titulo_en_mayusculas = titulo.upper()
    largo_del_encabezado = 80  

    separador = '*' * largo_del_encabezado

    encabezado = f"{separador}\n{titulo_en_mayusculas}\n{separador}"

    return encabezado

#5.4
def imprimir_ficha_heroe(heroe:dict):
    """
    la funcion recibe como parametro un diccionario, se encarga de imprimir todas las caracteristicas del heroe mediante un sistema 
    de encabezados que creamos utilizando funciones anteriores.
    """
    stark_generar_codigos_heroes(lista_personajes)
    encabezado_principal = generar_encabezado("principal")
    encabezado_fisico = generar_encabezado("fisico")
    encabezado_señas_particulares = generar_encabezado("señas particulares")
    altura =float(heroe["altura"])

    print(encabezado_principal)

    print(f"NOMBRE DEL HÉROE: {heroe['nombre']} ({extraer_iniciales(heroe['nombre'])})")
    print(f"IDENTIDAD SECRETA: {heroe['identidad']}")
    print(f"CONSULTORA: {heroe['empresa']}")
    print(f"CÓDIGO DE HÉROE : {heroe['codigo_heroe']}")

    print(encabezado_fisico)

    print(f"ALTURA: {convertir_cm_a_mtrs(altura)} Mtrs.")
    print(f"PESO: {heroe['peso']} kg")
    print(f"FUERZA: {heroe['fuerza']}")

    print(encabezado_señas_particulares)

    print(f"COLOR DE OJOS: {heroe['color_ojos']}")
    print(f"COLOR DE PELO: {heroe['color_pelo']}")

#5.5
def stark_navegar_fichas(lista_heroes):
    """
    esta funcion recibe como parametros la lista de heroes, dependiendo la opcion que eliga el usuario avanzara o retrocedera un
    heroe e imprimira su ficha.
    """
    indice_actual = 0
    cantidad_heroes = len(lista_heroes)

    while True:
        imprimir_ficha_heroe(lista_heroes[indice_actual])
        opcion = input("Ingrese una opción ('1' izquierda, '2' derecha, 'S' salir): ")

        if opcion == '1':
            indice_actual -= 1
            if indice_actual < 0:
                indice_actual = cantidad_heroes - 1  

        elif opcion == '2':
            indice_actual += 1
            if indice_actual >= cantidad_heroes:
                indice_actual = 0  
        elif opcion == 'S' or opcion == 's':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#6
def imprimir_menu()-> str:
    """
    Esta funcion imprime las opciones posibles del menu.
    """
    print("1 - Imprimir la lista de nombres junto con sus iniciales")
    print("2 - Generar códigos de héroes")
    print("3 - Normalizar datos")
    print("4 - Imprimir índice de nombres")
    print("5 - Navegar fichas")
    print("S - Salir")

#6.2
def stark_menu_principal():
    """
    Esta funcion ademas de imprimir el menu, solicita al usuario el ingreso de una opcion del mismo.
    """
    while True:
        imprimir_menu()
        opcion = input("Por favor, seleccione una opcion: ")
        return opcion

def stark_marvel_app_3(lista_heroes):
    """
    Esta funcion es el disparador de nuestro programa, se encarga de segun la opcion elegida en el menu, elegir la funcion correspondiente
    y mostrarla al usuario.
    """
    while True:
        opcion = stark_menu_principal()

        if opcion == '1':
            stark_imprimir_nombres_con_iniciales(lista_heroes)
        elif opcion == '2':
            stark_generar_codigos_heroes(lista_heroes)
        elif opcion == '3':
            stark_normalizar_datos(lista_heroes)
        elif opcion == '4':
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == '5':
            stark_navegar_fichas(lista_heroes)
        elif opcion == 'S':
            break
        else:
            print("Opción incorrecta. Por favor, seleccione una opción válida.")

