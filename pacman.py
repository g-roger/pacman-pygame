import pygame
import colors

SPEED = 0.4
RADIUS = 30

pygame.init()

screen = pygame.display.set_mode((640, 480), flags=0)
x = 10
y = 10

x_speed = SPEED
y_speed = SPEED

while True:
    # rules
    x += x_speed
    y += y_speed

    if x + RADIUS > 640:
        x_speed = -SPEED
    if x - RADIUS < 0:
        x_speed = SPEED
    if y + RADIUS > 480:
        y_speed = -SPEED
    if y - RADIUS < 0:
        y_speed = SPEED

    # graphics
    screen.fill(colors.BLACK)
    pygame.draw.circle(
        screen, colors.YELLOW, (int(x), int(y)), RADIUS, 0
    )

    pygame.display.update()

    # events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
