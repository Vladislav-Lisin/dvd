import pygame
from random import randint

x_size = 800
y_size = 500
length = 200
height = 98

location_x = 800 - length
location_y = 500 - height
speed = 2
x = randint(0, x_size - length)
y = randint(0, y_size - height)
vector = 1
colour = (randint(0, 255), randint(0, 255), randint(0, 255))
zn = 1
img = pygame.image.load('pngwing.com (1).jpg')

pygame.display.set_caption("Загрузка")
size = vx, vx1 = x_size, y_size
screen = pygame.display.set_mode(size)

pygame.init()
while zn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            zn = 0

    if y < 0: 
        colour= (randint(0, 255), randint(0, 255), randint(0, 255))
        if vector == 3:
            vector = 2
        elif vector == 4:
            vector = 1
    elif x > x_size - length:
        colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        if vector == 1:
            vector = 2
        elif vector == 4:
            vector = 3
    elif x < 0:
        colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        if vector == 2:
            vector = 1
        elif vector == 3:
            vector = 4
    elif y > y_size - height: 
        colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        if vector == 1:
            vector = 4
        elif vector == 2:
            vector = 3
    if vector == 1:
        x += speed
        y += speed
    elif vector == 2:
        x -= speed
        y += speed
    elif vector == 3:
        x -= speed
        y -= speed
    elif vector == 4:
        x += speed
        y -= speed

    screen.fill((0, 0, 0))
    pygame.time.delay(30)
    pygame.draw.rect(screen, colour, (x, y, length, height))
    screen.blit(img,(x,y))

    pygame.display.flip()


pygame.quit()