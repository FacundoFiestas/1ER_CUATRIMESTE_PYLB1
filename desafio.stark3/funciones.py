from data_stark import lista_personajes

#0
def stark_normalizar_datos(lista_personajes) -> bool:
    """
    Esta funcion recibe como parametros la 
    Primero verifico que la lista no este vacia, en caso de estarlo, la funcion retornara False, despues verifico que los datos a
    convertir no sean numericos, finalmente los convierto y levanto la bandera datos modificados, en caso de algun error imprimo,
    "error al normalizar los datos".
    """
    if not lista_personajes:
        return False
    altura_normalizada = False
    fuerza_normalizada = False
    peso_normalizado = False
    datos_modificados = False
    for heroe in lista_personajes:
        if(heroe["fuerza"] != int(heroe["fuerza"])):
            heroe["fuerza"] = int(heroe["fuerza"])
            fuerza_normalizada = True

        if(heroe["altura"] != float(heroe["altura"])):
            heroe["altura"] = float(heroe["altura"])
            altura_normalizada = True
        
        if(heroe["peso"] != float(heroe["peso"])):
            heroe["peso"] = float(heroe["peso"])
            peso_normalizado = True

    if(fuerza_normalizada or altura_normalizada or peso_normalizado):
        datos_modificados = True

    if datos_modificados:
        print("Los datos fueron normalizados correctamente")
    else: 
        print("Hubo un error al normalizar los datos.")

#1.1
def obtener_dato(heroe:dict, clave:str):
    """
    primero verifico que el diccionario no este vacio, y chequeo que el diccionario presente una key llamada nombre, si las condiciones
    se cumplen, retorna la clave, de lo contrario, la funcion retornara False.
    """
    if heroe and "nombre" in heroe:
        if clave in heroe:
            return heroe[clave]
        else:
            return False
    else:
        return False


#1.2
def obtener_nombre(heroe: dict):
    """
    primero verifico que el diccionario no este vacio, y que la key nombre este presente en el diccionario, si ambas condiciones
    se cumplen, se imprimira el nombre del heroe, de lo contrario la funcion retornara false.
    """
    if heroe and "nombre" in heroe:
        return f"Nombre: {heroe['nombre']}"
    else:
        return False

#2
def obtener_nombre_y_dato(heroe: dict, dato: str):
    """
    primero verifico que el diccionario no este vacio, despues que la key nombre este presente en el diccionario, si estas dos 
    condiciones se cumplen, la funcion retornara el nombre y el dato elegido, de lo contrario retornara false.
    """
    if heroe and "nombre" in heroe:
        if dato in heroe:
            nombre= heroe["nombre"]
            valor_dato = heroe[dato]
            return print(f"Nombre: {nombre} | {dato}: {valor_dato}")
        else: 
            return False
    else:
        return False

#3.1
def obtener_maximo(lista:list, dato: str):
    """
    primero verifico que la lista no este vacio, despues aplico logica de maximos y minimos para lograr sacar el maximo de la 
    caracteristica a evaluar, no sin antes corroborar que las mismas sean int o float, de lo contrario, la funcion retornara False.
    """
    if not lista:
        return False    
    maximo = None

    for elemento in lista:
        if dato in elemento:
            valor = elemento[dato]
            if type(valor) == int or type(valor) == float:
                if maximo == None or valor > maximo:
                    maximo = valor

    if maximo != None:
        return(maximo)
        
    else:
        return False
#3.2
def obtener_minimo(lista:list, dato: str):
    """
    primero verifico que la lista no este vacio, despues aplico logica de maximos y minimos para lograr sacar el minimo de la 
    caracteristica a evaluar, no sin antes corroborar que las mismas sean int o float, de lo contrario, la funcion retornara False.
    """
    if not lista:
        return False
    minimo = None
    for elemento in lista:
        valor = elemento[dato]
        if dato in elemento:
            if type(valor) == int or type(valor) == float:
                if minimo == None or valor < minimo:
                    minimo = valor
    if minimo != None:
        return (minimo)
    else:
        return  False
#3.3
def obtener_dato_cantidad(lista, valor, dato):
    """
    recibe la lista de personajes como primer parametro, el segundo parametro, indica si se quiere averiguar el maximo o el minimo,
    y ultimo parametro recibe, el dato a averiguar, finalmente, retornara que lo que se pidio, en caso de que se ingrese algun valor
    correcto, la funcion retornara false.
    """
    if valor == "max":
        max_valor = obtener_maximo(lista, dato)
    elif valor == "min":
        min_valor = obtener_minimo(lista, dato)

    if not lista or (valor != "max" and valor != "min"):
        return False
    heroes_cumplen_condicion = []

    for heroe in lista:
        if dato in heroe and type(heroe[dato]) == int or type(heroe[dato]) == float:
            if (valor == "max" and heroe[dato] == max_valor) or (valor == "min" and heroe[dato] == min_valor):
                nombre = heroe["nombre"]
                valor_dato = heroe[dato]
                heroes_cumplen_condicion.append((nombre, valor_dato))

    return heroes_cumplen_condicion

#3.4
def stark_imprimir_heroes(lista: list):
    """
    recibe la lista de personajes como parametro, en caso de que este vacia retornara false, caso contrario, imprimira la lista de heroes
    con los datos de cada personaje.
    """
    if not lista:
        return False

    for heroe in lista:
        print("Nombre:", heroe["nombre"])
        print("Identidad:", heroe["identidad"])
        print("Empresa:", heroe["empresa"])
        print("Altura:", heroe["altura"])
        print("Peso:", heroe["peso"])
        print("Género:", heroe["genero"])
        print("Color de ojos:", heroe["color_ojos"])
        print("Color de pelo:", heroe["color_pelo"])
        print("Fuerza:", heroe["fuerza"])
        print("Inteligencia:", heroe["inteligencia"])
        print("")

#4.1
def sumar_dato_heroe(lista, dato):
    """
    recibe como parametros la lista de personajes, y el dato a evaluar, verifico que ese dato este presente en el diccionario y acumula
    el valor de ese dato, de todos los personajes, finalmente, retorna ese acumulador.
    """
    suma = 0
    
    for heroe in lista:
        if type(heroe) == dict and heroe:  
            if dato in heroe:
                valor = heroe[dato]
                if type(valor) == float or type(valor) == int:  
                    suma += valor
    return (suma)

#4.2
def dividir(dividendo, divisor):
    """
    recibe como parametros, dos numeros, un dividendo, y un divisor, si el divisor es 0, la funcion retornara false, de los contrario
    se realizara la division.
    """
    if type(dividendo) == int or type(dividendo) == float and type(divisor) == int or type(divisor) == float:
        if divisor != 0:
            resultado = dividendo / divisor
        return resultado
    else:
        return False

#4.3
def calcular_promedio(lista:list, dato: str):
    """
    recibe la lista de personajes como parametro, y el dato  a averiguar el promedio, siempre y cuando el dividendo sea mayor a 0,
    se averiguara el promedio, con una funcion anterior, retornara el promedio.
    """
    suma = sumar_dato_heroe(lista, dato)
    tamaño = len(lista)
    if tamaño > 0:
        promedio = dividir(suma, tamaño)
        return promedio
    else:
        return False

#4.4
def mostrar_promedio_dato(lista, dato):
    """
    esta funcion recibe como parametro la lista de personajes, y el dato a evaluar, utiliza funciones anteriores para calcular el promedio
    siempre y cuando el mismo se pueda realizar, finalmente, los muestra.
    """
    for heroe in lista:
        if type(heroe[dato]) == int or type(heroe[dato] == float and lista):
            promedio = calcular_promedio(lista, dato)
            if promedio is not False:
                print(f"El promedio de {dato} es: {promedio}")
        else:
            return False
    
#5.2
def validar_entero(numero_str)-> bool:
    """
    Esta funcion recibe como parametro un numero en formato str, si el numero es posible de convertir a int, la funcion retornara
    true, de lo contrario, false.
    """
    if numero_str.isdigit():
        return True
    else:
        return False
    
#5.1
def imprimir_menu():
    '''Imprime el menú'''
    print("Menú:")
    print("1. Normalizar datos (Seleccione 1 para poder acceder al menú )")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("10. Listar todos los superhéroes agrupados por color de ojos.")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("12. Salir\n")

#5.3
def stark_menu_principal():
    """
    imprime el menu y pide un numero, si el numero es valido, lo convierte a entero, de lo contrario la funcion retorna false.
    """
    imprimir_menu()
    numero = input("Seleccione un numero: ")
    casteo = validar_entero(numero)
    if casteo == True:
        numero_int = int(numero)
        return numero_int
    else:
        return False
    
    
#6
def stark_marvel_app(lista_personajes):
    '''
    Recibe como parametros la lista de heroes, esta funcion sera el disparador de nuestro programa.
    '''
    flag_datos_normalizados = False
    while(True):
        opcion = stark_menu_principal()
        
        if opcion!= False and opcion >= 1 and opcion <= 12:
            if opcion == 1:
                    stark_normalizar_datos(lista_personajes)
                    flag_datos_normalizados =True
                
            if flag_datos_normalizados == True:
                match(opcion) :    
                    case 2:
                        nb_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "NB":
                                nb_superheroes.append(heroe)
                        if nb_superheroes:
                            for heroe in nb_superheroes:
                                nombre_heroe = obtener_nombre(heroe)
                                if nombre_heroe:
                                    print(nombre_heroe)
                                else:
                                    print("Error: No se pudo obtener el nombre del superhéroe.")
                        else:
                            print("NO HAY SUPERHÉROES DE GÉNERO NB.")

                    case 3:
                        f_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "F":
                                f_superheroes.append(heroe)
                        if f_superheroes:
                            heroe_mas_alto_f = obtener_maximo(f_superheroes, "altura")
                            if heroe_mas_alto_f is not False:
                                for heroe in f_superheroes:
                                    if heroe["altura"] == heroe_mas_alto_f:
                                        nombre_mas_alto_f = obtener_nombre(heroe)
                                        print(f"EL SUPERHEROE DE GENERO FEMENINO MAS ALTO ES: {nombre_mas_alto_f}")
                        else:
                            print("No existen superheroes de genero femenino.")
                    case 4:
                        m_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "M":
                                m_superheroes.append(heroe)
                        if m_superheroes:
                            heroe_mas_alto_m = obtener_maximo(m_superheroes, "altura")
                            if heroe_mas_alto_m is not False:
                                for heroe in m_superheroes:
                                    if heroe["altura"] == heroe_mas_alto_m:
                                        nombre_mas_alto_m = obtener_nombre(heroe)
                                        print(f"EL SUPERHEROE DE GENERO MASCULINO MAS ALTO ES: {nombre_mas_alto_m}")
                        else:
                            print("No existen superheroes de genero masculino")            
                    case 5:
                        m_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "M":
                                m_superheroes.append(heroe)
                        if m_superheroes:
                            heroe_mas_debil_m = obtener_minimo(m_superheroes, "fuerza")
                            if heroe_mas_debil_m is not False:
                                for heroe in m_superheroes:
                                    if heroe["fuerza"] == heroe_mas_debil_m:
                                        nombre_mas_debil_m = obtener_nombre(heroe)
                                        print(f"EL SUPERHEROE DE GENERO MASCULINO MAS DEBIL ES: {nombre_mas_debil_m}")
                        else:
                            print("No existen superheroes de genero masculino")
                    case 6:
                        nb_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "NB":
                                nb_superheroes.append(heroe)
                        if nb_superheroes:
                            heroe_mas_debil_nb = obtener_minimo(nb_superheroes, "fuerza")
                            if heroe_mas_debil_nb is not False:
                                for heroe in nb_superheroes:
                                    if heroe["fuerza"] == heroe_mas_debil_nb:
                                        nombre_mas_debil_nb = obtener_nombre(heroe)
                                        print(f"EL SUPERHEROE DE GENERO MASCULINO MAS DEBIL ES: {nombre_mas_debil_nb}")
                        else:
                            print("No existen superheroes de genero NB")
                        
                    case 7:
                        nb_superheroes = []
                        for heroe in lista_personajes:
                            if heroe["genero"] == "NB":
                                nb_superheroes.append(heroe)
                        if nb_superheroes:
                            promedio_fuerza_nb = calcular_promedio(nb_superheroes, "fuerza")
                            if promedio_fuerza_nb is not False:
                                print(f"Promedio de la fuerza de los superhéroes de género NB: {promedio_fuerza_nb}")
                        else:
                            print("No hay superhéroes de género NB en la lista.")
                        
                    case 8:
                        contar_color_ojos(lista_personajes)
                    case 9:
                        contar_color_pelo(lista_personajes)
                    case 10:
                        listar_superheroes_color_ojos(lista_personajes)
                    case 11:
                        listar_superheroes_por_inteligencia(lista_personajes)
                    case 12:
                        break
        else:
            print("Opción incorrecta, porfavor ingrese un valor correcto") 

#FUNCIONES PUNTO 7
#8
def contar_color_ojos(lista_personajes):
    """
    Creo un diccionario que voy a usar para guardar la informacion que necesite, mediante un for, analizo los tipos de color de ojos,
    en caso de encontrar uno nuevo, lo agrego al diccionario con un valor de = 1, y en caso de que el tipo de color de ojos se repita,
    incremento el valor sumandole 1, finalmente los muestro.
    """
    conteo_color_ojos = {}
    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        if color_ojos not in conteo_color_ojos:
            conteo_color_ojos[color_ojos] = 1
        else:
            conteo_color_ojos[color_ojos] += 1
            
    for color_ojos in conteo_color_ojos:
        cantidad = conteo_color_ojos[color_ojos]
        print(f"Hay {cantidad} superhéroes con color de ojos: {color_ojos}.")

        
#9
def contar_color_pelo(lista_personajes):
    """
    Creo un diccionario que voy a usar para guardar la informacion que necesite, mediante un for, analizo los tipos de color de pelo,
    en caso de encontrar uno nuevo, lo agrego al diccionario con un valor de = 1, y en caso de que el tipo de color de pelo se repita,
    incremento el valor sumandole 1, finalmente los muestro.
    """
    conteo_color_pelo = {}
    for heroe in lista_personajes:
        color_pelo = heroe["color_pelo"]
        if color_pelo not in conteo_color_pelo:
            conteo_color_pelo[color_pelo] = 1
        else:
            conteo_color_pelo[color_pelo] += 1
    for color_pelo in conteo_color_pelo:
        cantidad = conteo_color_pelo[color_pelo]
        print(f"Hay {cantidad} superheroes con color de pelo: {color_pelo}.")

#10
def listar_superheroes_color_ojos(lista_personajes):
    """
    Creo un diccionario, y obtengo el valor de cada tipo de color de ojos, si ese tipo no esta incluido en el diccionario, creo una 
    nueva entrada en el diccionario, con el valor "color_ojos" y se le asigna una lista que contiene al superheroe actual, y si color
    ojos ya existe como clave, se agrega al superheroe a la lista ya existente, finalmente, los muestro.
    """
    superheroes_por_color_ojos = {}
    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        if color_ojos not in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos] = [heroe]
        else:
            superheroes_por_color_ojos[color_ojos].append(heroe)
    for color_ojos in superheroes_por_color_ojos:
        superheroes = superheroes_por_color_ojos[color_ojos]
        print(f"Superhéroes con color de ojos: {color_ojos}:")
        for heroe in superheroes:
            print(f"- {heroe['nombre']}") 

#11
def listar_superheroes_por_inteligencia(lista_personajes):
    """
    Creo un diccionario, y obtengo el valor de cada tipo de inteligencia, si ese tipo no esta incluido en el diccionario, creo una
    nueva entrada en el diccionario, con el valor "tipo_inteligencia", y se le asigna una lista que contiene al superheroe actual, y
    si el tipo de inteligencia ya existe como clave, se agrega al superheroe a la lista ya existente, finalmente los muestro.
    """

    superheroes_por_inteligencia = {}
    for heroe in lista_personajes:
        inteligencia = heroe["inteligencia"]
        if inteligencia not in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia] = [heroe]
        else:
            superheroes_por_inteligencia[inteligencia].append(heroe)
    for inteligencia in superheroes_por_inteligencia:
        superheroes = superheroes_por_inteligencia[inteligencia]
        print(f"Superheroes con tipo de inteligencia: {inteligencia} ")
        for heroe in superheroes:
            print(f"- {heroe['nombre']}")  