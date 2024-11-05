"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()


# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)
    
    # les coordonnées du corps du serpent
    snake = [(10, 15),(11, 15),(12, 15)]

    for i in range(0,601,40):
        for j in range(0,601,40) :
            # les coordonnées de rectangle que l'on dessine
            x = i # coordonnée x (colonnes) en pixels
            y = j # coordonnée y (lignes) en pixels
            width = 20 # largeur du rectangle en pixels
            height = 20 # hauteur du rectangle en pixels
            rect = pg.Rect(x, y, width, height)
            # appel à la méthode draw.rect()
            color = (255, 0, 0) # couleur rouge
            pg.draw.rect(screen, color, rect)
    
    for i in range(20,601,40):
        for j in range(20,601,40) :
            # les coordonnées de rectangle que l'on dessine
            x = i # coordonnée x (colonnes) en pixels
            y = j # coordonnée y (lignes) en pixels
            width = 20 # largeur du rectangle en pixels
            height = 20 # hauteur du rectangle en pixels
            rect = pg.Rect(x, y, width, height)
            # appel à la méthode draw.rect()
            color = (255, 0, 0) # couleur rouge
            pg.draw.rect(screen, color, rect)
    
    for k in snake : 
        m,n = k
        width,height = 20,20
        color = (0,255,0)
        rect = pg.Rect(m*width, n*height, width, height)
        pg.draw.rect(screen, color, rect)



    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    ##random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    ##screen.fill(random_color)
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()




