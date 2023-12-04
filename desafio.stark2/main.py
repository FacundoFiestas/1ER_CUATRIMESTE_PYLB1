from funciones import *
while True:
        print("¡Bienvenidos a la base de datos de Stark Industries! Por favor, seleccione una opción:")
        print("")
        print("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
        print("B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
        print("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
        print("D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
        print("E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
        print("F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
        print("G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
        print("H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
        print("I. Listar todos los superhéroes agrupados por color de ojos.")
        print("J. Listar todos los superhéroes agrupados por tipo de inteligencia")
        print("K. Salir.")
        opcion = input("Seleccione una opcion: ")
        

        match (opcion):
                case "A":
                    imprimir_nombres_nb(lista_personajes)
                case "B":
                    imprimir_maxima_altura_femenino(lista_personajes)
                case "C":
                    imprimir_maxima_altura_masculino(lista_personajes)
                case "D":
                    mas_debil_masculino(lista_personajes)
                case "E":
                    mas_debil_nb(lista_personajes)
                case "F":
                    calcular_fuerza_promedio_nb(lista_personajes)
                case "G":
                    contar_color_ojos(lista_personajes)
                case "H":
                    contar_color_pelo(lista_personajes)
                case "I":
                    listar_superheroes_color_ojos(lista_personajes)
                case "J":
                    listar_superheroes_por_inteligencia(lista_personajes)
                case "K":
                    break
                    print("Salio del menu.")
                case _:
                    print("Ingrese una opcion correcta.")
