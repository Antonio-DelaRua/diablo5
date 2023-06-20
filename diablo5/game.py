import pygame
import random
import math
import sys
import os

# Inicializar pygame
pygame.init()

# Establecer tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Cargar imagen de fondo
asset_background = resource_path('assets/images/images/background.png')
background = pygame.image.load(asset_background)

# Cargar icono de ventana
asset_icon = resource_path('assets/images/images/ufo.png')
icon = pygame.image.load(asset_icon)

# Cargar Sonido de fondo
asset_sound = resource_path('assets/audios/audios/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# Cargar imagen del jugador
asset_playerimg = resource_path('assets/images/images/space-invaders.png')
playerimg = pygame.image.load(asset_playerimg)

# Cargar imagen de bala
asset_bulletimg = resource_path('assets/images/images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

# Fuente para texto de GAME OVER
asset_over_font = resource_path('assets/fonts/fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font, 64)

# Fuente para texto de puntuaje
asset_font = resource_path('assets/fonts/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font, 32)

# Establecer título de la ventana
pygame.display.set_caption("Diablo 5")

# Establecer icono de la ventana
pygame.display.set_icon(icon)

# Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

# Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Posicion inicial del jugador
playerX = 370
playerY = 470
playerx_change = 0
playery_change = 0

# Lista para almacenar posiciones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

# Se inicializan las variables para guardar las posiciones de los enemigos
for i in range(no_of_enemies):
    # se carga la imagen del enemigo 1
    enemy1 = resource_path('assets/images/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))
    # se carga la imagen del enemigo 2
    enemy2 = resource_path('assets/images/images/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))
    # se asigna una posicion aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    # se establece la velociad de movimiento del enemigo
    enemyX_change.append(5)
    enemyY_change.append(20)

# Variables para el estado del juego
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score = 0

# Variables para el estado de la interfaz
game_active = False

# Función para mostrar la puntuacion en la pantalla
def show_score(x, y):
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

# Función para dibujar al jugador en la pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

# Función para dibujar al enemigo en la pantalla
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# Función para disparar la bala en la pantalla
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

# Función para detectar colisiones entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Función para mostrar el texto de GAME OVER en la pantalla
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(over_text, text_rect)

# Función para mostrar la interfaz de inicio
def show_start_screen():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    title_text = over_font.render("Diablo 5", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width/2, screen_height/2 - 100))
    screen.blit(title_text, title_rect)

    start_text = font.render("Start", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(start_text, start_rect)

    pygame.display.flip()

# Función principal del juego
def gameloop():
    # Declara variables globales
    global score
    global playerX
    global playerx_change
    global bulletX
    global bulletY
    global Collision
    global bullet_state
    global game_active

    # Mostrar interfaz de inicio
    show_start_screen()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_active:
                        # Reiniciar las variables del juego
                        score = 0
                        playerX = 370
                        bulletX = 0
                        bulletY = 480
                        bullet_state = "ready"

                        # Activar el juego
                        game_active = True

        if game_active:
            # Maneja eventos, actualiza y renderiza el juego
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Maneja el movimiento del jugador y disparo
                    if event.key == pygame.K_LEFT:
                        playerx_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerx_change = 5
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerx_change = 0

            # Actualiza la posición del jugador
            playerX += playerx_change

            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736

            # Bucle que se ejecuta para cada enemigo
            for i in range(no_of_enemies):
                if enemyY[i] > 440:
                    for j in range(no_of_enemies):
                        enemyY[j] = 2000
                    game_active = False
                    show_start_screen()
                    break

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]

                # Comprueba si hay colisión entre la bala y el enemigo
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(0, 150)

                enemy(enemyX[i], enemyY[i], i)

            if bulletY < 0:
                bulletY = 480
                bullet_state = "ready"

            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            player(playerX, playerY)
            show_score(10, 10)

        pygame.display.update()
        clock.tick(120)

# Iniciar el juego
gameloop()
