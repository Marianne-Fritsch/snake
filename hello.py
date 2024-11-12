print("hello world")
print("ça marche")

"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

height = 40
width = 40
size = 20 # each cell size

pg.init()
screen = pg.display.set_mode((width * size, height * size))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
screen.fill(white)

snake = [(4,5), (5,5), (6,5)]
direction = (1,0)

while running:
    clock.tick(1)

    screen.fill(white)

    # snake mouvement
    first_x, first_y = snake[0]
    (direction_x, direction_y) = direction

    snake.pop() 
    snake.insert(0, (first_x + direction_x, first_y + direction_y))

    for x in range(width):
        for y in range(height):
            rect = pg.Rect(x * size, y * size, size, size)
            color = white if (x + y) % 2 == 0 else black
            pg.draw.rect(screen, color, rect)
    
    for (pos_x,pos_y) in snake:
        rect = pg.Rect(pos_x * size, pos_y * size, size, size)

        pg.draw.rect(screen, red, rect)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            print("on a cliquer sur le bouton quit")
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_UP:
                direction = (0, -1)
            if event.key == pg.K_DOWN:
                direction = (0, 1)
            if event.key == pg.K_LEFT:
                direction = (1,0)
            if event.key == pg.K_RIGHT:
                direction = (-1,0)

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    # random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # screen.fill(random_color)
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()