from data_stark import lista_personajes
#FACUNDO FIESTAS AVILA, DIVISION 1F

while True:
    print("¡Bienvenidos a la base de datos de Stark Industries! Por favor, seleccione una opción:")
    print("")
    print("A. Imprimir todos los datos de cada superhéroe")
    print("B. Mostrar la identidad y el peso del superhéroe con mayor fuerza")
    print("C. Mostrar nombre e identidad del superhéroe más bajo")
    print("D. Calcular el peso promedio de los superhéroes masculinos")
    print("E. Mostrar nombre y peso de superhéroes con fuerza superior al promedio femenino")
    print("F. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "A":
            for heroe in lista_personajes:
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
            

        case "B":
            maximo_fuerza = None
            superheroes_mas_fuerte = []
            for heroe in lista_personajes:
                fuerza = int(heroe["fuerza"])
                if(maximo_fuerza == None or maximo_fuerza < fuerza):
                    maximo_fuerza = fuerza
                    superheroes_mas_fuerte = [heroe]
                elif maximo_fuerza == fuerza:
                    superheroes_mas_fuerte.append(heroe)
            if superheroes_mas_fuerte:
                print("Los superheroes con maxima fuerza son: ")
                for heroe in superheroes_mas_fuerte:
                    print("Identidad:", heroe["identidad"])
                    print("Peso", heroe["peso"])
                    print("")
            else:
                print("No se encontraron superheroes con maxima fuerza. ")
            
        case "C":
            minimo_altura = None
            heroes_mas_bajos = []
            
            for heroe in lista_personajes:
                altura = float(heroe["altura"])
                if minimo_altura == None or minimo_altura > altura:
                    minimo_altura = altura
                    heroes_mas_bajos = [heroe]
                elif minimo_altura == altura:
                    heroes_mas_bajos.append(heroe)
            if heroes_mas_bajos:
                print("Los superheroes mas bajos son:")
                for heroe in heroes_mas_bajos:
                    print("Nombre: ", heroe["nombre"])
                    print("Identidad:", heroe["identidad"])
                    print("")
            else:
                print("No existen superheroes con altura minima.")
            
        case "D":
            cantidad_masculinos =  0
            acumulador_peso_masculinos = 0
            for heroe in lista_personajes:
                if heroe["genero"] == "M":
                    peso = float(heroe["peso"])
                    cantidad_masculinos += 1
                    acumulador_peso_masculinos += peso
            if cantidad_masculinos > 0:
                promedio_peso_masculinos = acumulador_peso_masculinos / cantidad_masculinos
                print(f"El promedio de peso de los heroes masculinos es: {promedio_peso_masculinos}")
            else:
                print("No hay heroes de genero masculino")
            

        case "E":
            cantidad_femeninos = 0
            acumulador_fuerza_femeninos = 0
            heroes_mas_fuertes_promedio_femenino = []
            for heroe in lista_personajes:
                if heroe["genero"] == "F":
                    fuerza = int(heroe["fuerza"])
                    cantidad_femeninos +=1
                    acumulador_fuerza_femeninos += fuerza
            if cantidad_femeninos > 1:
                promedio_fuerza_femeninos = acumulador_fuerza_femeninos / cantidad_femeninos
                
            for heroe in lista_personajes:
                if int(heroe["fuerza"]) > promedio_fuerza_femeninos:
                    heroes_mas_fuertes_promedio_femenino.append(heroe)
            if heroes_mas_fuertes_promedio_femenino:
                print("Los superheroes con fuerza mayor al promedio femenino son:")
            for heroe in heroes_mas_fuertes_promedio_femenino:
                print("Nombre:", heroe["nombre"])
                print("Peso:", heroe["peso"])
                print("")
            
        case "F":
            break
        case _:
            print("Ingrese una opcion correcta")
            break
            
            









        
