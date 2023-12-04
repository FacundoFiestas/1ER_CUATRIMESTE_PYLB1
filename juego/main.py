#FACUNDO FIESTAS, DIVISION 1F
from constantes import *
from funciones import  *
import pygame, random
from clases import *
import sys 
from database import *

#INICIALIZACION DE PYGAME
pygame.init()
pygame.mixer.init()
crear_base_datos_ranking()

#CARGO LA VENTANA Y LE ASIGNO UN NOMBRE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GALAXIAS")

#FPS
clock = pygame.time.Clock()

#ANIMACION EXPLOSION
for i in range(9):
    file = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(file).convert()
    img.set_colorkey(NEGRO)
    img_scale = pygame.transform.scale(img, (70,70)) 
    explosion_animacion.append(img_scale)

#CARGA DE RECURSOS
fondo = pygame.image.load("backgroundd.jpg").convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
sonido_laser = pygame.mixer.Sound("laser-gun-shot-sound-future-sci-fi-lazer-wobble-chakongaudio-174883.mp3")
sonido_explosion = pygame.mixer.Sound("retro-game-sfx-explosion-104422.mp3")
sonido_impacto = pygame.mixer.Sound("video-game-hit-noise-001-135821.mp3")
pygame.mixer.music.load("8bit-music-for-game-68698.mp3")
pygame.mixer.music.set_volume(0.1)

#REPRODUCCION DE LA MUSICA EN UN BUCLE INFINITO
pygame.mixer.music.play(loops=-1)

#BANDERAS DE CONTROL DEL JUEGO
game_over = True
running = True
duracion_level_1 = 30 
show_level_2_text = True 
duracion_level_2 = 60
show_level_3_text = True
score = 0 
enemigos = pygame.sprite.Group()
aparicion_ultimo_enemigo = pygame.time.get_ticks()

#BUCLE PRINCIPAL DEL JUEGO
while running:
    if game_over:
        nivel_actual = 1 
        nombre_jugador  = show_go_screen(screen,fondo, clock)
        todos_los_sprites = pygame.sprite.Group()
        lista_meteoros = pygame.sprite.Group()
        balas = pygame.sprite.Group()
        player = Player()
        lista_naves_enemigas = pygame.sprite.Group()
        todos_los_sprites.add(player)
        Player.invisibilidad_utilizada = False
        for i in range(8):
            meteor = Meteoro()
            todos_los_sprites.add(meteor)
            lista_meteoros.add(meteor)
        start_time = pygame.time.get_ticks()
        show_level_screen(screen, nivel_actual, fondo)
        show_level_2_text = True  
        show_level_3_text = True
        game_over = False
        top_5 = obtener_top_5_puntajes()

    clock.tick(60)
    current_time = pygame.time.get_ticks()
    tiempo_transcurrido = (current_time - start_time) // 1000
    minutos = tiempo_transcurrido // 60
    segundos = tiempo_transcurrido % 60

    # Verificar si ha pasado el tiempo del nivel actual
    if tiempo_transcurrido >= duracion_level_1:
        if nivel_actual == 1 and show_level_2_text:
            show_level_text(screen, "LEVEL 2", "Muy facil? Veamos que te parece esto!", 2)
            show_level_2_text = False  # No volver a mostrar el texto
            nivel_actual += 1
        for meteor in lista_meteoros:
            meteor.speedy = random.randrange(7, 8)  # Velocidad vertical constante
    
    if tiempo_transcurrido >= duracion_level_2:
        if nivel_actual == 2 and show_level_3_text:
            show_level_text(screen,"LEVEL 3", "Me sorprendes! Podras resistir a nuestras tropas?", 2)
            show_level_3_text = False
            nivel_actual += 1
        for meteor in lista_meteoros:
            meteor.speedy = 8
    
    if nivel_actual == 3:
        enemigos.update()
        current_time = pygame.time.get_ticks()
        if (current_time - aparicion_ultimo_enemigo) > 10000:  
            nuevo_enemigo = Enemigo()
            enemigos.add(nuevo_enemigo)
            todos_los_sprites.add(nuevo_enemigo)
            aparicion_ultimo_enemigo = current_time  

    if nivel_actual == 3 and tiempo_transcurrido >= 75:
        guardar_puntaje(nombre_jugador, score)
        show_victory_screen(screen, fondo, clock, score)
        show_top5_screen(screen, fondo, clock)
        score = 0 
        game_over = True  # Vuelve a la pantalla de inicio

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  
                player.shoot(todos_los_sprites, balas, sonido_laser)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                #ACTIVACION DE PODER.
                player.activar_invisibilidad()
                mostrar_mensaje_nivel = False
    todos_los_sprites.update()

#COLISIONES METEORO - BALAS
    hits = pygame.sprite.groupcollide(lista_meteoros, balas, True, True)
    for hit in hits: 
        score += 10
        explosion = Explosion(hit.rect.center, explosion_animacion)
        todos_los_sprites.add(explosion)
        sonido_explosion.play()
        #GENERACION CONTINUA DE METEOROS
        meteor = Meteoro()
        todos_los_sprites.add(meteor) 
        lista_meteoros.add(meteor)

#COLISIONES JUGADOR - METEORO
    hits = pygame.sprite.spritecollide(player, lista_meteoros, True)
    for hit in hits:
        if not player.invisibilidad_activa:
            player.escudo -= 25
        meteor = Meteoro()
        todos_los_sprites.add(meteor) 
        lista_meteoros.add(meteor)
        sonido_impacto.play()  
        if player.escudo <= 0:
            game_over = True

#NAVES ENEMIGAS EN NIVEL 3
    if nivel_actual == 3:
        hits_enemigo = pygame.sprite.spritecollide(player, enemigos, True)
        for hit in hits_enemigo:
            sonido_impacto.play() 
            player.escudo = 0

        for enemigo in enemigos:
            hits_laser_enemigo = pygame.sprite.spritecollide(enemigo, balas, True)
        for laser in hits_laser_enemigo:
            todos_los_sprites.remove(laser)

    screen.blit(fondo, [0,0])

#DIBUJAR TODOS LOS SPRITES.
    todos_los_sprites.draw(screen)

#DIBUJAR TODAS LAS INTERFACES CORRESPONDIENTES.
    dibujar_interfaz(screen, minutos, segundos, player, nivel_actual, score)

    pygame.display.flip()

#GAME OVER 
    if player.escudo <= 0:
        game_over = True
        guardar_puntaje(nombre_jugador, score)
        show_game_over_screen(screen, fondo, clock, score) 
        show_top5_screen(screen, fondo, clock)
        score = 0  

# CIERRE DEL JUEGO
pygame.quit()
eliminar_tabla()

