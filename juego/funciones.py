import pygame
from constantes import *
import sys
import re
import time
from database import obtener_top_5_puntajes, eliminar_tabla

def show_options_screen(screen, fondo, clock):
    global sonido_silenciado  # Declarar la variable como global para poder modificarla

    bucle = True
    while bucle:
        screen.blit(fondo, [0, 0])
        dibujar_texto(screen, "OPCIONES", 65, WIDTH // 2, HEIGHT // 40)

        # Agregar un breve texto
        texto_bienvenida = ("Bienvenido a Galaxias, un emocionante juego de accion en el espacio")
        dibujar_texto(screen, texto_bienvenida, 15, WIDTH // 2, HEIGHT // 5)

        texto_movimiento = ("Utiliza las teclas A y D para desplazarte de izquierda a derecha")
        dibujar_texto(screen, texto_movimiento, 15, WIDTH // 2, HEIGHT // 5 + 60)

        texto_disparo = ("Utiliza el click izquierdo del mouse para disparar")
        dibujar_texto(screen, texto_disparo, 15, WIDTH // 2, HEIGHT // 5 + 90)

        texto_objetivo = ("Esquiva asteroides para sobrevivir y alcanzar la puntuacion mas alta!")
        dibujar_texto(screen, texto_objetivo, 15, WIDTH // 2, HEIGHT // 5 + 150)

        texto_comodin = ("Recuerda activar la invisibilidad utilizando la tecla F!")
        dibujar_texto(screen, texto_comodin, 15, WIDTH // 2, HEIGHT // 5 + 180 )

        texto_final = ("Preparate para la aventura en el espacio y demuestra tus habilidades!")
        dibujar_texto(screen, texto_final, 13, WIDTH // 2, HEIGHT // 5 + 220)

        # Agregar el botón "ATRAS"
        font = pygame.font.SysFont("04b 30", 20)
        back_text = font.render("ATRAS", True, BLANCO)
        back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(back_text, back_rect)

        # Agregar el botón "MUTE"
        font_mute = pygame.font.SysFont("04b 30", 20)
        mute_text = font_mute.render("MUTE", True, BLANCO)
        mute_rect = mute_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        screen.blit(mute_text, mute_rect)

        # Mostrar el estado actual del sonido (Silenciado o no)
        estado_sonido = "Desactivada" if sonido_silenciado else "Activado"
        estado_text = font_mute.render(f"MUSICA: {estado_sonido}", True, BLANCO)
        estado_rect = estado_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
        screen.blit(estado_text, estado_rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if back_rect.collidepoint(x, y):
                    bucle = False  # Salir del bucle de opciones
                    break
                elif mute_rect.collidepoint(x, y):
                    sonido_silenciado = not sonido_silenciado
                    if sonido_silenciado:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

    # Después de salir del bucle de opciones, vuelve a la pantalla principal
    show_go_screen(screen, fondo, clock)


#FUNCION PARA DIBUJAR TEXTO
def dibujar_texto(surface, text, size, x, y, color=VIOLETA, fondo = None):
    font = pygame.font.SysFont("04b 30", size) #FUENTE
    text_surface = font.render(text, True, VIOLETA) #RENDERIZACION
    text_rect = text_surface.get_rect() #OBTENER RECTA
    text_rect.midtop = (x, y) #POSICION
    surface.blit(text_surface, text_rect) # PINTARLO EN PANTALLA


#FUNCION PARA DIBUJAR LA BARRA DE SALUD
def dibujar_barra_salud(surface, x, y, escudo):
    bar_lenght = 100 #LARGO DE LA BARRA
    bar_height = 10 #ALTURA DE LA BARRA
    porcentaje = escudo / 100   #PORCENTAJE DE SALUD RESTANTE 
    fill_width = int(bar_lenght * porcentaje) #ANCHO DE LA PARTE RELLENA DE LA BARRA

    #DETERMINAR EL COLOR DE LA BARRA SEGUN EL PORCENTAJE DE SALUD 
    if porcentaje > 0.75:
        fill_color = VERDE
    elif porcentaje > 0.5:
        fill_color = AMARILLO
    elif porcentaje > 0.25:
        fill_color = NARANJA
    else:
        fill_color = ROJO

    fill = pygame.Rect(x, y, fill_width, bar_height) #CREAR UN RECTÁNGULO PARA LA PARTE RELLENA
    border = pygame.Rect(x, y, bar_lenght, bar_height)  # CREAR UN RECTÁNGULO PARA EL BORDE COMPLETO

    pygame.draw.rect(surface, fill_color, fill) #DIBUJAR EL RECTÁNGULO RELLENO CON EL COLOR DETERMINADO
    pygame.draw.rect(surface, BLANCO, border, 2) #DIBUJAR EL BORDE DE LA BARRA CON UN GROSOR DE 2 PÍXELES


#FUNCION PANTALLA INICIO

def show_go_screen(screen, fondo, clock):
    screen.blit(fondo, [0, 0])
    dibujar_texto(screen, "GALAXIAS", 65, WIDTH // 2, HEIGHT // 4)
    dibujar_texto(screen, "BY FACUNDO FIESTAS", 15, WIDTH - 130, HEIGHT - 20)
    dibujar_texto(screen, "Ingrese su nombre para continuar", 30, WIDTH // 2, HEIGHT // 2 - 50)

    font = pygame.font.SysFont("04b 30", 20)
    play_text = font.render("PLAY", True, BLANCO)
    exit_text = font.render("EXIT", True, BLANCO)
    options_text = font.render("OPCIONES", True, BLANCO)


    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    options_rect = options_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))

    screen.blit(play_text, play_rect)
    screen.blit(exit_text, exit_rect)
    screen.blit(options_text, options_rect)

    waiting = True
    user_input = ""
    nombre_ingresado = False

    while waiting:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                eliminar_tabla()
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                # Comprobar si el clic fue en los textos
                if play_rect.collidepoint(x, y) and user_input:
                    waiting = False  # Clic en PLAY
                elif exit_rect.collidepoint(x, y):
                    pygame.quit()  # Clic en EXIT
                    sys.exit()
                elif options_rect.collidepoint(x, y):
                    show_options_screen(screen, fondo, clock)  # Clic en OPCIONES
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if user_input and not nombre_ingresado: 
                        if re.match(r'^[a-zA-Z]{1,7}$', user_input):# Verificar que hay un nombre y no se haya ingresado antes
                            nombre_ingresado = True
                            waiting = False
                elif evento.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif len(user_input) < 7 and re.match(r'^[a-zA-Z]$', evento.unicode):
                    user_input += evento.unicode
        # Dibujar cuadro de entrada con fondo transparente
        input_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 32)
        pygame.draw.rect(screen, (255, 255, 255), input_rect)
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
        dibujar_texto(screen, user_input, 30, WIDTH // 2, HEIGHT // 2 + 5, fondo=(255, 255, 255))

        pygame.display.flip()

    return user_input

#PANTALLA NIVEL 1
def show_level_screen(screen, level, fondo):
    screen.blit(fondo, [0, 0])  
    font_level = pygame.font.SysFont("04b 30", 50)
    font_ready = pygame.font.SysFont("04b 30", 30)  
    font_start = pygame.font.SysFont("04b 30", 20)

    #TEXTO LEVEL 
    text = font_level.render(f"LEVEL {level}", True, VIOLETA)  
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    #TEXTO PREPARADO
    ready_text = font_ready.render("Preparado? A jugar!", True, VIOLETA)
    ready_rect = ready_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(ready_text, ready_rect)

    #TEXTO ENTER 
    start_text = font_start.render("Presiona Enter para comenzar", True, VIOLETA)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(start_text, start_rect)

    pygame.display.flip()

    esperar_para_iniciar_nivel = True
    while esperar_para_iniciar_nivel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperar_para_iniciar_nivel = False
                                

#FUNCION PANTALLA TEMPORAL ENTRE NIVELES 
def show_level_text(screen, level_text, additional_text, duration):
    font = pygame.font.SysFont("04b 30", 50)
    level_rendered = font.render(level_text, True, VIOLETA)
    level_rect = level_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))

    font = pygame.font.SysFont("04b 30", 20)
    additional_rendered = font.render(additional_text, True, VIOLETA)
    additional_rect = additional_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    screen.blit(level_rendered, level_rect)
    screen.blit(additional_rendered, additional_rect)

    pygame.display.flip()
    pygame.time.delay(duration * 1000)  # Espera el tiempo especificado en milisegundos

def show_game_over_screen(screen, fondo, clock, score):
    bucle = True
    while bucle:
        screen.blit(fondo, [0, 0])
        dibujar_texto(screen, "GAME OVER", 65, WIDTH // 2, HEIGHT // 4)
        dibujar_texto(screen, f"Score: {score}", 40, WIDTH // 2, HEIGHT // 2)
        dibujar_texto(screen, "PRESIONA ENTER PARA VOLVER A INTENTARLO", 20, WIDTH // 2, HEIGHT * 3 // 4)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    bucle = False  # Salir del bucle de Game Over
                    break


#FUNCION PANTALLA VICTORIA 
def show_victory_screen(screen, fondo, clock, score):
    screen.blit(fondo, [0, 0])
    dibujar_texto(screen, "VICTORIA!", 60, WIDTH // 2, HEIGHT // 4)
    dibujar_texto(screen, f"Score: {score}", 30, WIDTH // 2, HEIGHT // 2)
    dibujar_texto(screen, "Presiona ENTER para volver a comenzar", 20, WIDTH // 2, HEIGHT * 3 // 4)
    pygame.display.flip()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_key = False
                    return  # Sal del bucle y retorna al código principal

        clock.tick(30)

def show_top5_screen(screen, fondo, clock):
    bucle = True
    font = pygame.font.SysFont("04b 30", 50)
    while bucle:
        screen.blit(fondo, [0,0])
        texto_top5 = font.render("TOP 5", True, BLANCO)
        rect_top5 = texto_top5.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        screen.blit(texto_top5, rect_top5)
        # Obtiene y dibuja el top 5 de puntajes
        top_5 = obtener_top_5_puntajes()
        y_pos = HEIGHT // 4
        for i, (nombre, puntaje) in enumerate(top_5, start=1):
            texto_ranking = font.render(f"{i}. {nombre}: {puntaje}", True, BLANCO)
            rect_ranking = texto_ranking.get_rect(center=(WIDTH // 2, y_pos))
            screen.blit(texto_ranking, rect_ranking)
            y_pos += 60  # Ajusta la posición vertical para cada línea del ranking

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bucle = False  # Sal del bucle si se presiona Enter
    show_go_screen(screen, fondo, clock)

#FUNCION PARA DIBUJAR TODOS LOS ELEMENTOS DENTRO DE LA PANTALLA
def dibujar_interfaz(screen, minutos, segundos, player, nivel_actual, score):
    # Dibujar tiempo en pantalla
    texto_tiempo = f"Tiempo: {minutos:02}:{segundos:02}"
    dibujar_texto(screen, texto_tiempo, 25, WIDTH // 2, 40)

    # Dibujar estado del poder
    estado_poder = "utilizado" if player.invisibilidad_utilizada else "no utilizado"
    texto_poder = f"Poder: {estado_poder}"
    dibujar_texto(screen, texto_poder, 18, 133, HEIGHT - 20)

    # Dibujar nivel en pantalla
    texto_nivel = f"Nivel: {nivel_actual}"
    dibujar_texto(screen, texto_nivel, 20, WIDTH - 80, HEIGHT - 30)

    # Dibujar el score en pantalla
    texto_score = f"SCORE: {score}"
    dibujar_texto(screen, texto_score, 25, 110, 10)

    # Dibujar barra de salud en pantalla
    dibujar_barra_salud(screen, WIDTH - 105, 15, player.escudo)
