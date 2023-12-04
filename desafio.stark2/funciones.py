from data_stark import *
#A
def imprimir_nombres_nb(lista_personajes):
    """
    Utilizo una bandera para analizar la presencia de superheroes no binarios en la lista de personajes.
    En caso de si haber, me mostrara el nombre, de lo contrario, imprimira un mensaje negando la existencia del genero en la lista.
    """
    flag_presencia_nobinarios = False
    for heroe in lista_personajes:
        if heroe["genero"] == "NB":
            print(heroe["nombre"])
            flag_presencia_nobinarios = True

    if flag_presencia_nobinarios == False :
        print("No hay superheroes de genero: NB presentes en la lista")
        
#B
def imprimir_maxima_altura_femenino(lista_personajes):
    """
    Utilizo logica de maximos y minimos, para obtener al superheroe de genero femenino mas alto, en caso de haber mas de uno con la 
    misma altura, los agrega a una lista, y muestra el nombre de los dos.
    """
    maxima_altura_fem = None 
    max_altura_fem = []
    flag_femeninos_presentes = False
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            altura = float(heroe["altura"])
            if maxima_altura_fem == None or maxima_altura_fem < altura:
                maxima_altura_fem = altura
                max_altura_fem = [heroe]
            elif max_altura_fem == altura:
                max_altura_fem.append(heroe)
            flag_femeninos_presentes = True
    if flag_femeninos_presentes:
        print("Los femeninos de mayor altura son: ")
        for heroe in max_altura_fem:
            print(heroe["nombre"])
    else:
        print("No se encontraron superheroes de genero femenino")
                
#C
def imprimir_maxima_altura_masculino(lista_personajes):
    """
    Utilizo logica de maximos y minimos para obtener el masculino mas alto, en caso de haber mas de uno con la misma altura,
    muestro el nombre de los dos.
    """
    maxima_altura_masculino = None 
    mas_altos_masc = []
    flag_masculinos_presentes = False
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            altura = float(heroe["altura"])
            if maxima_altura_masculino == None or maxima_altura_masculino < altura:
                maxima_altura_masculino = altura
                mas_altos_masc = [heroe]
            elif mas_altos_masc == altura:
                mas_altos_masc.append(heroe)
            flag_masculinos_presentes = True
        
    if flag_masculinos_presentes:
        print("Los masculinos de mayor altura son: ")
        for heroe in mas_altos_masc:
            print(heroe["nombre"])
    else:
        print("No se encontraron superheroes de genero masculino")
            
#D
def mas_debil_masculino(lista_personajes):
    """
    Utilizo logica de maximos y minimos para obtener al masculino mas debil, y en caso de haber mas de uno, muestro el total
    de masculinos con la misma fuerza
    """
    minima_fuerza_masculino = None
    debiles_masculinos = []
    flag_masculinos_presentes = False
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            fuerza = float(heroe["fuerza"])
            if minima_fuerza_masculino == None or minima_fuerza_masculino > fuerza:
                minima_fuerza_masculino = fuerza
                debiles_masculinos = [heroe]
            elif minima_fuerza_masculino == fuerza:
                debiles_masculinos.append(heroe)
            flag_masculinos_presentes = True
    if flag_masculinos_presentes:
        print("Los superheroes masculinos mas debiles son: ")
        for heroe in debiles_masculinos:
            print(heroe["nombre"])
    else:
        print("No hay superheroes masculinos presentes en la lista")
#E
def mas_debil_nb(lista_personajes):
    """
    evaluo la presencia de superheroes no binarios en la lista de superheroes, en caso de encontrar se imprime el nombre de el/los 
    no binario mas debiles, y en caso de no encontrar se imprime un texto negando la existencia de los mismos.
    """
    flag_presencia_nb = False
    minima_fuerza_nb = None
    debiles_nb = []
    for heroe in (lista_personajes):
        if(heroe["genero"]) == "NB":
            fuerza = float(heroe["fuerza"])
            flag_presencia_nb = True
            if minima_fuerza_nb == None or minima_fuerza_nb > fuerza:
                minima_fuerza_nb = fuerza
                debiles_nb = [heroe["nombre"]]
            elif minima_fuerza_nb == fuerza:
                debiles_nb.append(heroe["nombre"])

    if flag_presencia_nb == False:
        print("No se encontraron superheroes de genero no binario.")
        
#F
def calcular_fuerza_promedio_nb(lista_personajes):
    """
    Calculo el promedio de los superheroes no binarios, en caso de no haber imprimo un texto negando la existencia de los mismos
    """
    suma_fuerza_nb = 0
    contador_nb = 0

    for heroe in lista_personajes:
        if heroe["genero"] == "NB":
            fuerza = float(heroe["fuerza"])
            suma_fuerza_nb += fuerza
            contador_nb += 1

    if contador_nb > 0:
        fuerza_promedio_nb = suma_fuerza_nb / contador_nb
        return print(f"La fuerza promedio de los superheroes de genero no binario es: {fuerza_promedio_nb}")
    
    else:
        return print("No se encontraron superheroes de genero NB")

#G
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

#H
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

#I
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
#J
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













