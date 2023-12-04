import re
import json

#TP Stark 05 - FACUNDO FIESTAS AVILA

#1.1.
def imprimir_menu_desafio_5():
    '''Imprime menú'''
    print(f"\nA. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
        f"B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n"
        f"C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
        f"D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
        f"E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n"
        f"F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
        f"G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
        f"H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n"
        f"I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n"
        f"J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
        f"K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
        f"L. Determinar cuántos superhéroes tienen cada tipo de inteligencia.\n"
        f"M. Listar todos los superhéroes agrupados por color de ojos.\n"
        f"N. Listar todos los superhéroes agrupados por color de pelo.\n"
        f"O. Listar todos los superhéroes agrupados por tipo de inteligencia.\n"
        f"Z. Salir\n")

#1.2.
def stark_menu_principal_desafio_5()-> str:
    '''No recibe parametros, imprime menú y pide al usuario que seleccione una opción'''
    imprimir_menu_desafio_5()
    opcion_elegida = input("Seleccione una opción: ").strip()
    if re.match(r"^[A-Za-z]$", opcion_elegida):
        return opcion_elegida.upper()
    else:
        return -1
    
#1.3.
def stark_marvel_app_5 (lista_heroes: list):
    '''Recibe lista de heroes como parámetro y se encarga de ejecutar el programa'''
    while(True):
        opcion_elegida = stark_menu_principal_desafio_5()
        match(opcion_elegida) :    
                    case "A":
                        stark_guardar_heroe_genero(lista_heroes,"M")
                    case "B":
                        stark_guardar_heroe_genero(lista_heroes,"F")
                    case "C":
                        stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","maximo")
                    case "D":
                        stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","maximo")
                    case "E":
                        stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","M","minimo")
                    case "F":
                        stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"altura","F","minimo")
                    case "G":
                        stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,"M")
                    case "H":
                        stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,"F")
                    case "I":
                        with open("desafio.stark5\heroes_maximo_altura_M.csv", "r") as archivo: 
                            print(archivo.read())
                        with open("desafio.stark5\heroes_maximo_altura_F.csv", "r") as archivo:
                            print(archivo.read())
                        with open("desafio.stark5\heroes_minimo_altura_M.csv", "r") as archivo: 
                            print(archivo.read())
                        with open("desafio.stark5\heroes_minimo_altura_F.csv", "r") as archivo: 
                            print(archivo.read())
                    case "J":
                        stark_calcular_cantidad_por_tipo(lista_heroes,"color_ojos")
                    case "K":
                        stark_calcular_cantidad_por_tipo(lista_heroes,"color_pelo")
                    case "L":
                        stark_calcular_cantidad_por_tipo(lista_heroes,"inteligencia")
                    case "M":
                        stark_listar_heroes_por_dato(lista_heroes,"color_ojos")
                    case "N":
                        stark_listar_heroes_por_dato(lista_heroes,"color_pelo")
                    case "O":
                        stark_listar_heroes_por_dato(lista_heroes,"inteligencia")
                    case "Z":
                        break
                    case _:
                        print("opción incorrecta\n")

#1.4.
def leer_archivo (path:str)-> list:
    ''' Recibe path, lo abre en modo lectura y retorna la lista de héroes como una lista de diccionarios'''
    archivo = open (path,"r")
    dic_json = json.load (archivo)
    archivo.close()
    return dic_json["heroes"]

#1.5.
def guardar_archivo( nombre_archivo: str, contenido: str):
    ''' Recibe string como el nombre con el cual se guardará el archivo junto con su extensión y como segundo parámetro
    tendrá un string el cual será el contenido a guardar en dicho archivo.'''
    archivo = open(nombre_archivo, "w+")
    if archivo.write(contenido):
        print(f"\nSe creó el archivo: {nombre_archivo}\n")
        archivo.close()
        return True
    else:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
    
#1.6.
def capitalizar_palabras(cadena: str)-> str:
    "Recibe str y retorna cada palabra capitalizada."
    palabras = cadena.split()
    palabras_capitalizas = []
    for palabra in palabras:
        palabras_capitalizas.append(palabra.capitalize())
    cadena_capitalizada = " ".join(palabras_capitalizas)
    return cadena_capitalizada

# 1.7.
def obtener_nombre_capitalizado (heroe: dict)-> str:
    ''' Recibe diccionario como heroe y retorna nombre del heroe capitalizado.'''
    nombre_capitalizado = capitalizar_palabras(heroe["nombre"])
    return f"Nombre: {nombre_capitalizado}"

#1.8.
def obtener_nombre_y_dato(heroe:dict, clave:str) -> str:
    '''Recibe heroe y clave, retorna nombre del heroe con la clave y el valor asociado a la clave.'''
    return  f"{obtener_nombre_capitalizado(heroe)} | {capitalizar_palabras(clave)}: {heroe[clave]}"

#2.1.
def es_genero(heroe:dict, genero_buscado:str) -> bool:
    '''Recibe heroe y genero a buscar. Retorna True si coincide el genero del heroe con genero buscado, si no False.'''
    if genero_buscado == heroe["genero"]:
        return True
    else:
        return False

#2.2. 
def stark_guardar_heroe_genero (lista_heroes:list, genero_buscado:str) -> bool:
    '''Recibe lista y genero a buscar, guarda en archivo csv los nombres de los heroes que sean del genero buscado.'''
    lista_nombres_genero_buscado = []
    for heroe in lista_heroes:
        if (es_genero(heroe,genero_buscado)) == True :
            print(obtener_nombre_capitalizado(heroe))
            lista_nombres_genero_buscado.append(heroe["nombre"])
    nombres_genero_buscado = "\n".join(lista_nombres_genero_buscado)
    path = f"desafio.stark5\heroes_{genero_buscado}.csv"
    if guardar_archivo (path, nombres_genero_buscado) == True:
        return True
    else:
        return False


#3.1.
def calcular_min(lista_heroes: list, clave: str, genero_buscado:str)-> str:
    ''' Recibe lista, clave y genero. Retorna de ese clave el valor minimo'''
    minimo = None
    nombre_heroe_min = None
    for heroe in lista_heroes:
        if heroe["genero"] == genero_buscado :
            if minimo == None or float(heroe[clave]) < minimo:
                minimo = float(heroe[clave])
                nombre_heroe_min = heroe["nombre"]
    return nombre_heroe_min

#3.2. 
def calcular_max(lista_heroes: list, clave: str, genero_buscado:str)-> str:
    ''' Recibe lista, clave y genero. Retorna de ese clave el valor máximo'''
    maximo = None
    nombre_heroe_max = None
    for heroe in lista_heroes:
        if heroe["genero"] == genero_buscado :
            if maximo == None or float(heroe[clave]) > maximo:
                maximo = float(heroe[clave])
                nombre_heroe_max = heroe["nombre"]
    return nombre_heroe_max


#3.3. 
def calcular_max_min_dato_genero(lista_heroes: list, clave: str, genero_buscado: str, calculo: str)-> str:
    ''' Recibe lista, clave, genero y calculo. Retorna de ese clave el calculo solicitado'''
    if calculo == "maximo":
        return calcular_max(lista_heroes,clave,genero_buscado)
    elif calculo == "minimo":
        return calcular_min(lista_heroes,clave,genero_buscado)

#3.4.
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes: list, clave: str, genero_buscado: str, calculo: str)-> bool:
    ''' Recibe lista, clave, genero y calculo. Imprime el nombre del heroe y el dato solicitado. Guarda el resultado en un archivo
    y retorna True si se guardó correctamente, si no False.'''
    heroe_resultante = calcular_max_min_dato_genero (lista_heroes, clave, genero_buscado, calculo)
    
    if calculo == "maximo":
        cantidad = "Mayor"
    else:
        cantidad = "Menor"

    for heroe in lista_heroes:
        if heroe["nombre"] == heroe_resultante:
            mensaje = f"{cantidad} {capitalizar_palabras(clave)}: {(obtener_nombre_y_dato(heroe,clave))}"
            print(mensaje)

    path = f"desafio.stark5\heroes_{calculo}_{clave}_{genero_buscado}.csv"
    if guardar_archivo (path, mensaje) == True:
        return True
    else:
        return False


#4.1.
def sumar_dato_heroe_genero (lista_heroes: list, clave: str, genero_buscado: str) -> int:
    ''' Recibe lista, clave y genero. Retorna la suma de todos los valores de la clave solicitada.'''
    suma = 0
    for heroe in lista_heroes:
        if type(heroe) == dict and (len(heroe)) > 0 and (es_genero(heroe,genero_buscado)) == True:
            suma = float(heroe[clave]) + suma
                        
    if suma > 0:
        return suma
    else:
        return -1
    
#4.2. 
def cantidad_heroes_genero(lista_heroes: list, genero_buscado: str)-> int:
    '''Recibe lista y genero. Retorna la cantidad de heroes que coinciden con el genero buscado.'''
    contador_heroes = 0
    for heroe in lista_heroes:
        if (es_genero(heroe,genero_buscado)) == True:
            contador_heroes = contador_heroes + 1
    return contador_heroes


#4.3
def calcular_promedio_genero (lista_heroes: list, clave: str, genero_buscado: str) -> float:
    '''Recibe lista, clave y genero. Retorna el promedio del dato solicitado'''
    total = sumar_dato_heroe_genero(lista_heroes, clave, genero_buscado)
    cantidad_heroes = cantidad_heroes_genero(lista_heroes, genero_buscado)
    promedio = total / cantidad_heroes
    
        
    return promedio


#4.4.
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list, genero_buscado:str) -> bool:
    ''' Recibe lista y genero. Imprime el promedio de la altura del genero buscado. Guarda el resultado en un archivo
    y retorna True si se guardó correctamente, si no False.'''
    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía")
        return False
    
    promedio = calcular_promedio_genero(lista_heroes,"altura",genero_buscado)
    mensaje = f"Altura promedio genero {genero_buscado}: {promedio:.2f}"
    print(mensaje)
    path = f"desafio.stark5\heroes_promedio_altura_{genero_buscado}.csv"
    if guardar_archivo (path, mensaje) == True:
        return True
    else:
        return False
    

#5.1.
def calcular_cantidad_tipo(lista_heroes: list, tipo_dato: str)-> dict:
    '''Recibe lista y tipo de dato. Si la lista no está vacia, retorna un dicccionario con los valores asociados al tipo de dato
    y la cantidad de cada uno. Si está vacia, retorna dicccionario con error como clave'''
    if len(lista_heroes) == 0:
        return {"Error": "La lista se encuentra vacía"}
    
    contador_tipo_cantidad = {}
    for heroe in lista_heroes:
        valor = heroe[tipo_dato]
        if valor == "":
            valor = "No Tiene"
        valor = capitalizar_palabras(valor)
        if valor in contador_tipo_cantidad:
            contador_tipo_cantidad[valor] = contador_tipo_cantidad[valor] + 1
        
        else:
            contador_tipo_cantidad[valor] = 1

    return contador_tipo_cantidad


#5.2.
def guardar_cantidad_heroes_tipo (diccionario: dict, tipo_dato: str)-> bool:
    '''Recibe diccionario y tipo de dato. Guarda en un archivo cada clave del tipo de dato y su cantidad.
    Retorna True si se guardó correctamente, si no False'''
    
    lineas_texto = []
    for clave in diccionario:
        cantidad = diccionario[clave]
        mensaje = f"Caracteristica: {tipo_dato} {clave} - Cantidad de heroes: {cantidad}"
        print(mensaje)
        lineas_texto.append(mensaje)

    lineas_texto = "".join(lineas_texto)    
    path = f"desafio.stark5\heroes_cantidad_{tipo_dato}.csv"
    if guardar_archivo (path, lineas_texto) == True:
        return True
    else:
        return False


#5.3.
def stark_calcular_cantidad_por_tipo(lista_heroes: list, tipo_dato: str)-> bool:
    '''Recibe lista de heroes y tipo de dato. Guarda en un archivo cada clave del tipo de dato y su cantidad.
    Retorna True si se guardó correctamente, si no False'''
    cantidad_por_clave_en_tipo_dato = calcular_cantidad_tipo(lista_heroes, tipo_dato)
    guardado = guardar_cantidad_heroes_tipo(cantidad_por_clave_en_tipo_dato, tipo_dato)
    if guardado == True:
        return True
    else:
        return False

#6.1.

def obtener_lista_de_tipos(lista_heroes: list, clave: str)-> set:
    '''Recibe lista y clave. Itera la lista y retorna un set con todos los valores asociados a la clave.'''
    lista_valores_de_tipo_dato = []
    
    for heroe in lista_heroes:
        valor = heroe[clave]
        
        if valor == "":
            valor = "N/A"
        valor = capitalizar_palabras(valor)
        lista_valores_de_tipo_dato.append(valor)

    set_valores_de_tipo_dato = set(lista_valores_de_tipo_dato)
    return set_valores_de_tipo_dato

#6.2.
def normalizar_dato(valor: str, valor_por_defecto: str)-> str:
    "Recibe valor y valor por defecto. Si valor está vacio, se le asigna el valor por defecto. Retorna valor"
    if valor == "":
        valor = valor_por_defecto
    
    return valor

#6.3.
def normalizar_heroe(heroe: dict, clave: str)-> dict:
    "Recibe diccionario y clave. Normaliza nombre y valores asociados a la clave. Retorna diccionario normalizado. "
    for _ in heroe:
        valor = capitalizar_palabras(heroe[clave])
        valor_normalizado = normalizar_dato(valor,"N/A")
        heroe[clave] = valor_normalizado
        nombre_capitalizado = capitalizar_palabras(heroe["nombre"])
        heroe["nombre"] = nombre_capitalizado

    return heroe

#6.4.
def obtener_heroes_por_tipo(lista_heroes: list, set_variedades: set, clave: str) -> dict:
    '''Recibe lista, set y clave. Retorna diccionario con las keys como el valor asociadoa la clave ingresada por parametro
    y los nombres que de los heroes.'''
    dict_variedades_con_heroes = {}
    for tipo_valor in set_variedades:
        for heroe in lista_heroes:
            normalizar_heroe(heroe, clave)
            if tipo_valor == heroe[clave]: 
                if tipo_valor not in dict_variedades_con_heroes:
                    dict_variedades_con_heroes[tipo_valor] = []
                dict_variedades_con_heroes[tipo_valor].append(heroe["nombre"])

    return dict_variedades_con_heroes
        

#6.5.
def guardar_heroes_por_tipo(diccionario: dict, tipo_dato: str) -> bool:
    '''Recibe diccionario y tipo de dato. Guarda en un archivo cada clave del tipo de dato y los nombres de los heroes.
    Retorna True si se guardó correctamente, si no False'''
    
    lineas_texto = []
    for clave in diccionario:
        lista_heroes_por_tipo = diccionario[clave]
        lista_heroes_por_tipo = " | ".join(lista_heroes_por_tipo)
        mensaje = f"{tipo_dato} {clave}: {lista_heroes_por_tipo}"
        print(mensaje)
        lineas_texto.append(mensaje)

    lineas_texto = "".join(lineas_texto)   
    path = f"desafio.stark5\heroes_segun_{tipo_dato}.csv"
    if guardar_archivo (path, lineas_texto) == True:
        return True
    else:
        return False
    
#6.6.

def stark_listar_heroes_por_dato(lista_heroes: list, tipo_dato: str)-> bool:
    '''Recibe lista y tipo de dato. Agrupa heroes por los valores asociados al tipo de dato y los guarda en un archivo.
    Retorna True si pudo guardar el archivo, False caso contrario.'''
    set_variedades = obtener_lista_de_tipos(lista_heroes,tipo_dato)
    diccionario = obtener_heroes_por_tipo(lista_heroes,set_variedades,tipo_dato)
    flag_guardado = guardar_heroes_por_tipo(diccionario,tipo_dato)

    if flag_guardado == True:
        return True
    else:
        return False








