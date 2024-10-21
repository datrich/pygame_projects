import pygame as pg
from numpy import random
pg.init()
pg.font.init()
pos_ball = tuple(random.randint(600,size = 2))
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
run = True
clock = pg.time.Clock()

hit = 0

font = pg.font.Font('bebas.ttf', 24)
nofi_font = pg.font.Font('bebas.ttf', 70)
time = font.render('', True, (255,255,255))
score = font.render('score: 0', True, (0,0,0))
timeRect = time.get_rect()
scoreRect = score.get_rect()
timeRect.center = (30, 20)
scoreRect.center = (740,20)

pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # just windows popup!
screen = pg.display.get_surface()
surface = pg.Surface((800, 560))

a = 0
b = pg.time.get_ticks()
x = 0
y = 0
left  = False
right  = False
up  = False
down  = False
while run:
	r, g, b = 255, 255, 255
	if (pg.time.get_ticks()//1000-a*60-5) == 60:
		a +=1
	time = font.render('TOTAL TIME:   '+str(a)+':'+str(pg.time.get_ticks()//1000-a*60), True, (255,255,255))
	screen.fill("black")
	screen.blit(time,timeRect)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	ar = pg.PixelArray(surface)
	ar[x:x+9, y:y+9] = (r, g, b)
	del ar
	screen.blit (surface, (0, 40))
	ar = pg.PixelArray(surface)

	key = pg.key.get_pressed()
	r, g, b = 255, 255, 255
	if key[pg.K_LEFT] == True and right == False:
		left  = True
		right  = False
		up  = False
		down  = False
		l_time = pg.time.get_ticks()
	elif key[pg.K_RIGHT] == True and left == False:
		left  = False
		right  = True
		up  = False
		down  = False
		l_time = pg.time.get_ticks()
	elif key[pg.K_UP] == True and down == False:
		left  = False
		right  = False
		up  = True
		down  = False
		l_time = pg.time.get_ticks()
	elif key[pg.K_DOWN] == True and up == False:
		left  = False
		right  = False
		up  = False
		down  = True
		l_time = pg.time.get_ticks()

	if left == True and pg.time.get_ticks()-l_time > 100:
		x -= 10
		ar[:,:] = (0, 0, 0)
		ar[x:x+9, y:y+9] = (r, g, b)
		del ar
		screen.blit (surface, (0, 40))
		l_time = pg.time.get_ticks()

	elif right == True and pg.time.get_ticks()-l_time > 100:
		x += 10
		ar[:,:] = (0, 0, 0)
		ar[x:x+9, y:y+9] = (r, g, b)
		del ar
		screen.blit (surface, (0, 40))
		l_time = pg.time.get_ticks()

	elif up == True and pg.time.get_ticks()-l_time > 100:
		y -= 10
		ar[:,:] = (0, 0, 0)
		ar[x:x+9, y:y+9] = (r, g, b)
		del ar
		screen.blit (surface, (0, 40))
		l_time = pg.time.get_ticks()

	elif down == True and pg.time.get_ticks()-l_time > 100:
		y += 10
		ar[:,:] = (0, 0, 0)
		ar[x:x+9, y:y+9] = (r, g, b)
		del ar
		screen.blit (surface, (0, 40))
		l_time = pg.time.get_ticks()

	pg.display.flip()
	clock.tick(60)
pg.quit()
