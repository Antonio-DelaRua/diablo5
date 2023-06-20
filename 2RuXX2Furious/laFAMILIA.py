import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configuraciones de la pantalla
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
GRAY = (0, 255, 255)

# Configurar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bicicleta en la autopista")
clock = pygame.time.Clock()

background = pygame.image.load("fondo1.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coche.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        if keystate[pygame.K_UP]:
            self.speed_y = -5
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# Establecer título de la ventana    
pygame.display.set_caption("RuXx & Furious")

# Clase de los vehículos
class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coche2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
vehicles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Cargar la música de fondo
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Reproducir en bucle continuo

# Bucle principal del juego
running = True
spawn_timer = 0
spawn_interval = 2000
speed_timer = 0
speed_interval = 3000
speed_increment = 1
points = 0  # Variable para almacenar los puntos obtenidos
font = pygame.font.Font(None, 36)  # Fuente para el texto de los puntos

while running:
    # Mantener el bucle a la velocidad correcta
    clock.tick(FPS)

    # Procesamiento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Generar un nuevo coche cuando se alcance el intervalo de tiempo
    spawn_timer += clock.get_time()
    if spawn_timer >= spawn_interval:
        vehicle = Vehicle()
        all_sprites.add(vehicle)
        vehicles.add(vehicle)
        spawn_timer = 0

    # Incrementar la velocidad de los vehículos cada cierto intervalo de tiempo
    speed_timer += clock.get_time()
    if speed_timer >= speed_interval:
        for vehicle in vehicles:
            vehicle.speed_y += speed_increment
        speed_timer = 0

    # Incrementar los puntos en función del tiempo transcurrido
    points += clock.get_time() / 1000 * 10  # Convertir milisegundos a segundos y multiplicar por 10

    # Verificar si un vehículo golpea al jugador
    hits = pygame.sprite.spritecollide(player, vehicles, False)
    if hits:
        running = False
        pygame.mixer.music.stop()  # Detener la música de fondo
        messagebox.showinfo("¡Has perdido!", "Puntuación obtenida: {:.0f}".format(points))

    # Dibujar / Renderizar
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Renderizar los puntos en la pantalla
    text = font.render("Puntos: {:.0f}".format(points), True, WHITE)
    screen.blit(text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
