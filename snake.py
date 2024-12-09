#POUR LA PROCHAINE FOIS : transformer le snake en deque et ses éléments (des tuples) en namedtuples 
# (cf 
# from collections import namedtuple 
# Cell = namedtuple("Cell",["x","y"], defaults=(2,2))
# )




from random import randint
import pygame as pg
import collections
from collections import namedtuple
from collections import deque

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# les coordonnées du corps du serpent
#snake = [(10, 15),(11, 15),(12, 15)]
direction = (0,1)

Cell = namedtuple("Cell",["x","y"], defaults=(2,2))
width = 20 # largeur du rectangle en pixels
height = 20 # hauteur du rectangle en pixels
snake = deque([Cell(10, 15),Cell(11, 15),Cell(12, 15)])

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
screen.fill(white)

for i in range(0,601,2*width):
    for j in range(0,601,2*width) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, width, height)
        # appel à la méthode draw.rect()
        color = (255, 0, 0) # couleur rouge
        pg.draw.rect(screen, color, rect)

for i in range(20,601,2*width): 
    for j in range(20,601,2*width) :
        # les coordonnées de rectangle que l'on dessine
        x = i # coordonnée x (colonnes) en pixels
        y = j # coordonnée y (lignes) en pixels
        rect = pg.Rect(x, y, width, height)
        # appel à la méthode draw.rect()
        color = red # couleur rouge
        pg.draw.rect(screen, color, rect)


fruit = Cell(5,5)    

score = 0

while running:

    clock.tick(6)

    pg.display.set_caption(f"Score: {score}")

    #snake movement
    first_x,first_y = snake[0]
    direction_x,direction_y = direction
    queue = snake.pop()
    snake.insert(0, Cell(first_x + direction_x, first_y + direction_y))

    ############

    n,m = queue
    if queue == fruit : 
        snake.append(queue)
        score += 1
        while fruit in snake : 
            fruit = (randint(0,600//width),randint(0,600//width))


    else : 
        rect = pg.Rect(n*width, m*height, width, height)
        if (n+m)%2 == 1 :
            pg.draw.rect(screen,white,rect)
        else :
            pg.draw.rect(screen,red,rect)

    rect_fruit = pg.Rect(fruit[0]*width, fruit[1]*height, width, height)
    pg.draw.rect(screen,blue,rect_fruit)

    for k in snake : 
        #m,n = k
        m,n = k[0],k[1]
        width,height = 20,20
        color = green
        rect = pg.Rect(m*width, n*height, width, height)
        pg.draw.rect(screen, color, rect)
    


    # = (1,0)
    #down = (-1,0)
    #right = (0,1)
    #left = (1,0)


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
            if event.key == pg.K_UP and direction != (0,1):
                direction = (0,-1)
            if event.key == pg.K_DOWN and direction != (0,-1):
                direction = (0,1)
            if event.key == pg.K_RIGHT and direction != (-1,0):
                direction = (1,0)
            if event.key == pg.K_LEFT and direction != (1,0):
                direction = (-1,0)

    a = snake.copy
    b = a.popleft()
    if b in a :
        running = False
    



    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    ##random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    ##screen.fill(random_color)
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()



