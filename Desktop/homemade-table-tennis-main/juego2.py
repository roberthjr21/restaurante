import pygame.locals
import random

# Inicializar pygame
pygame.init()

# Definir el tamaño de la ventana del juego
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de palitos y pelota")

# Definir los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir las dimensiones y la posición inicial de los palitos
stick_width = 10
stick_height = 80
stick1_x = 50
stick1_y = height // 2 - stick_height // 2
stick2_x = width - 50 - stick_width
stick2_y = height // 2 - stick_height // 2
stick_speed = 5

# Definir las dimensiones y la posición inicial de la pelota
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = random.choice([-2, 2])
ball_speed_y = random.choice([-2, 2])

# Crear el reloj del juego
clock = pygame.time.Clock()

# Contadores de puntos
puntos_jugador1 = 0
puntos_jugador2 = 0
ventana = pygame.display.set_mode((800, 600))

# Función para dibujar los palitos, la pelota y los puntos en la ventana
def draw_objects():
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (stick1_x, stick1_y, stick_width, stick_height))
    pygame.draw.rect(window, WHITE, (stick2_x, stick2_y, stick_width, stick_height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)
    font = pygame.font.Font(None, 36)
    text = font.render(f"{puntos_jugador1} - {puntos_jugador2}", True, WHITE)  # Muestra los puntos de ambos jugadores
    window.blit(text, (width // 2 - text.get_width() // 2, 10))
    pygame.display.update()

# Función para mostrar un mensaje temporal en la pantalla
def show_message(message):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, WHITE)
    window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)  # Pausa de 1 segundos



    
    
# Función para verificar la condición de victoria
def check_winner():
    if puntos_jugador1 > 5:
        show_message("Jugador 2 ha ganado!")
        return True
    if puntos_jugador2 > 5:
        show_message("Jugador 1 ha ganado!")
        return True
    return False

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    
    # Mover el palito 1
    if keys[pygame.K_w] and stick1_y > 0:
        stick1_y -= stick_speed
    if keys[pygame.K_s] and stick1_y < height - stick_height:
        stick1_y += stick_speed
    
    # Mover el palito 2
    if keys[pygame.K_UP] and stick2_y > 0:
        stick2_y -= stick_speed
    if keys[pygame.K_DOWN] and stick2_y < height - stick_height:
        stick2_y += stick_speed

    # Actualizar la posición de la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Comprobar si la pelota colisiona con los palitos
    if ball_x - ball_radius <= stick1_x + stick_width and stick1_y <= ball_y <= stick1_y + stick_height:
        ball_speed_x *= -1
    elif ball_x - ball_radius <= 0:
        puntos_jugador2 += 1
        if check_winner():
            running = False
        show_message("Jugador 1 perdió")
        ball_x, ball_y = width // 2, height // 2
        ball_speed_x = random.choice([-2, 2])
        ball_speed_y = random.choice([-2, 2])
    if ball_x + ball_radius >= stick2_x and stick2_y <= ball_y <= stick2_y + stick_height:
        ball_speed_x *= -1
    elif ball_x + ball_radius >= width:
        puntos_jugador1 += 1
        if check_winner():
            running = False
        show_message("Jugador 2 perdió")
        ball_x, ball_y = width // 2, height // 2
        ball_speed_x = random.choice([-2, 2])
        ball_speed_y = random.choice([-2, 2])
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y *= -1

    # Dibujar los objetos en la ventana
    draw_objects()

    # Limitar la velocidad de fotogramas
    clock.tick(100)

# Finalizar pygame
pygame.quit()
