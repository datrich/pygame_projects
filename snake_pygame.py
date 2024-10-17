import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))
player = pg.Rect(350, 500, 100, 20)

run = True
while run:
    pg.display.set_caption('Ping ball')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.draw.rect(screen,(84,164,255),player)
    screen.fill("white")

    pg.display.update()
pg.quit()
