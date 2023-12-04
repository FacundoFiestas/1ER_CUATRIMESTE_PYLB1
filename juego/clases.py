import pygame
import random
from constantes import *
# PERSONAJE
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("personaje.png").convert() #CARGO IMAGEN
        width, height = 70, 70 #ANCHO Y ALTO
        self.image = pygame.transform.scale(self.image, (width, height)) #ESCALA DE IMAGEN 
        self.image.set_colorkey(NEGRO) #REMOVER FONDO NEGRO
        self.rect = self.image.get_rect() # OBTENGO LA RECTA 
        self.rect.centerx = WIDTH // 2 #POSICION INICIAL EN EL CENTRO
        self.rect.bottom = HEIGHT - 10 #POSICION INICIAL ABAJO 
        self.speed_x = 0 #VELOCIDAD INICIAL EN EL EJE X 
        self.escudo = 100 #TOTAL DE ESCUDO DEL JUGADOR
        self.tiempo_invisible_total = 10 * 60   #TIEMPO TOTAL DE INVISIBILIDAD EN FOTOGRAMAS
        self.tiempo_invisible = 0 #TIEMPO RESTANTE DE INVISIBILIDAD 
        self.invisibilidad_utilizada = False #EL PODER DE INVISIBILIDAD HA SIDO UTILIZADO?
        self.invisibilidad_activa = False #EL PODER ESTA ACTIVO ACTUALMENTE? 

    def update(self):
        teclas_presionadas = pygame.key.get_pressed() #OBTENGO LAS TECLAS PRESIONAS 
        self.speed_x = 0 #VELOCIDAD EJE X

        #ACTUALIZO LA VELOCIDAD SEGUN LAS TECLAS PRESIONADAS.
        if teclas_presionadas[pygame.K_a]: 
            self.speed_x = -5
        if teclas_presionadas[pygame.K_d]:
            self.speed_x = 5
        
        self.rect.x += self.speed_x #ACTUALIZO LA POSICION EN EL EJE X 

        #MANEJO DE INVISIBILIDAD 
        if self.tiempo_invisible > 0:
            self.tiempo_invisible -= 1

        #LOGICA DE TITILACION
            if self.tiempo_invisible % 10 == 0:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)
            self.invisibilidad_activa = False

        #LIMITES DE LA PANTALLA 
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, todos_los_sprites, balas, sonido_laser):
        bala = Bala(self.rect.centerx, self.rect.top)
        todos_los_sprites.add(bala)
        balas.add(bala)
        sonido_laser.play()

    def activar_invisibilidad(self):
        if not self.invisibilidad_utilizada:
            self.tiempo_invisible = self.tiempo_invisible_total
            self.invisibilidad_utilizada = True
            self.invisibilidad_activa = True

#METEORO
class Meteoro(pygame.sprite.Sprite):
    def __init__(self):#INICIALIZO LA CLASE
        super().__init__()#SUPERCLASE
        #DEFINO LA IMAGEN Y LOS TAMAÑOS, LOS CUALES SERAN ALEATORIOS A LO LARGO DEL PROGRAMA.
        imagen_meteoro = pygame.image.load("meteoro.png").convert()
        tamaños_predefinidos = [(30, 30), (50, 50), (90, 90)]
        tamaño = random.choice(tamaños_predefinidos)
        self.image = pygame.transform.scale(imagen_meteoro, tamaño)
        self.image.set_colorkey(NEGRO)
        #ESTABLEZCO LA GENERACION DE METEOROS 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40) #EFECTO CAIDA
        #VELOCIDAD ALEATORIA
        self.speedy = random.randrange(5, 7) 
        self.speedx = random.randrange(-5, 5) #MOVIMIENTO "HORIZONTAL"
    
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx #MOVIMIENTO "HORIZONTAL"
        #VUELVO A GENERAR METEORITOS CUANDO LOS MISMOS SALGAN DE LA VENTANA
        if self.rect.top > HEIGHT + 10  or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(5, 7)

#BALA/LASER
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y): #INICIALIZO LA CLASE
        super().__init__() #SUPERCLASE
        #CONFIGURO LA IMAGEN
        self.image = pygame.image.load("laser.png").convert()
        width, height = 40, 40
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(NEGRO)
        #CONFIGURO POSICION Y VELOCIDAD
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10 #DESDE ABAJO 
    #MOVIMIENTO EN SUBIDA Y ELIMINACION DE LA BALA UNA VEZ SALGA DE LA VENTANA 
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

#EXPLOSION
explosion_animacion = []  
class Explosion(pygame.sprite.Sprite): #INCIALIZO LA CLASE
    def __init__ (self, center, explosion_animacion): #POSICION DE LA EXPLOSION
        super().__init__() #SUPERCLASE
        self.image = explosion_animacion[0] #COMENZAMOS CON LA IMAGEN 0
        self.rect = self.image.get_rect() #OBTENEMOS RECTA 
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks() #TIEMPO TRANSCURRIDO 
        self.frame_rate = 50 #VELOCIDAD DE LA EXPLOSION
    def update(self):
        now = pygame.time.get_ticks() #TIEMPO TRANSCURRIDO DESDE LA EXPLOSION 
        if now - self.last_update > self.frame_rate: #HAN TRANSCURRIDO DE 50 MILISEGUNDOS?
            self.last_update = now #ACTUALIZO 
            self.frame += 1 #SIGUIENTE FRAME 
            if self.frame == len(explosion_animacion):
                self.kill() #ELIMINA LA EXPLOSION DEL GRUPO DE SPRITES 
            else:
                center = self.rect.center #POSICION CENTRO 
                self.image = explosion_animacion[self.frame] #ACTUALIZA LA IMAGEN DE LA EXPLOSION 
                self.rect = self.image.get_rect() #OBTENGO EL NUEVO RECTANGULO 
                self.rect.center = center #CENTRO DE LA EXPLOSION 

#NAVES ENEMIGAS 
class Enemigo(pygame.sprite.Sprite):
    def __init__(self): #INICIALIZO LA CLASE 
        super().__init__() #SUPERCLASE 
        self.image = pygame.image.load("navenemiga.png").convert() #CARGO LA IMAGEN 
        width, height = 120, 120 #ANCHO Y ALTO 
        self.image = pygame.transform.scale(self.image,(width, height)) #ESCALO LA IMAGEN 
        self.image.set_colorkey(NEGRO) #ELIMINO EL FONDO NEGRO 
        self.rect = self.image.get_rect() #OBTENGO LA RECTA 
        self.reset() #INICIALIZA LA POSICION Y VELOCIDAD DE LA NAVE ENEMIGA 
    
    def reset(self):
        self.rect.x = random.randrange(WIDTH - self.rect.width) #POSICION X ALEATORIA DENTRO DEL ANCHO DE LA PANTALLA 
        self.rect.y = random.randrange(-100, -40) #POSICION Y ALEATORIA FUERA DE LA PANTALLA (EFECTO DE APARICION)
        self.speedy = random.uniform(5, 6) #VELOCIDAD VERTICAL ALEATORIA 
    
    def update(self):
        self.rect.y += self.speedy #MUEVE LA NAVE HACIA ABAJO SEGUN SU VELOCIDAD 

        # Reiniciar la posición si el enemigo sale de la pantalla
        if self.rect.top > HEIGHT + 10:
            self.reset() #VUELVE A COLOCAR LA NAVE ENEMIGA ARRIBA DE LA PANTALLA 


