import pygame as pg
from numpy import random
pg.init()
pg.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
run = True
clock = pg.time.Clock()

hit = 0
white = (255, 255, 255)
black = (0, 0, 0)
blue_s = (80, 80, 255)
font = pg.font.Font('bebas.ttf', 24)
time = font.render('', True, white)
score = font.render('score: 0', True, black)
timeRect = time.get_rect()
scoreRect = score.get_rect()
timeRect.center = (30, 20)
scoreRect.center = (740,20)

pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # just windows popup!
screen = pg.display.get_surface()
surface = pg.Surface((800, 560))

pos_ball_x = random.randint(800)//10*10
pos_ball_y = random.randint(560)//10*10
a = 0
b = pg.time.get_ticks()
x = random.randint(800)//10*10
y = random.randint(560)//10*10
k = 1
direct = ''
snake_pos = [[0,0]]

while run:

	if (pg.time.get_ticks()//1000-a*60-5) == 60:
		a +=1
	time = font.render('TOTAL TIME:   '+str(a)+':'+str(pg.time.get_ticks()//1000-a*60), True, black)
	screen.fill((255,128,0))
	screen.blit(time,timeRect)

	score = font.render('score: '+str(hit), True, black)
	screen.blit(score,scoreRect)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	ar = pg.PixelArray(surface)

	ar[:,:] = black
	key = pg.key.get_pressed()

	if key[pg.K_LEFT] == True and direct != 'right':
		direct = 'left'
	elif key[pg.K_RIGHT] == True and direct != 'left':
		direct = 'right'
	elif key[pg.K_UP] == True and direct != 'down':
		direct = 'up'
	elif key[pg.K_DOWN] == True and direct != 'up':
		direct = 'down'

	if direct == 'left':
		x -= 10
		if x < 0:
			break
		if [x,y] in snake_pos:
			break

	elif direct == 'right':
		x += 10
		if x > 800:
			break
		if [x,y] in snake_pos:
			break

	elif direct == 'up':
		y -= 10
		if y < 0:
			break
		if [x,y] in snake_pos:
			break

	elif direct == 'down':
		y += 10
		if y > 560:
			break
		if [x,y] in snake_pos:
			break

	snake_pos.append([x,y])
	if len(snake_pos) != k:
			snake_pos.pop(0)
	for i in range(len(snake_pos)):
		ar[snake_pos[i][0]:snake_pos[i][0]+9, snake_pos[i][1]:snake_pos[i][1]+9] = white
	ar[pos_ball_x:pos_ball_x+9,pos_ball_y:pos_ball_y+9] = blue_s
	del ar
	screen.blit (surface, (0, 40))
	# eat
	if x == pos_ball_x and y == pos_ball_y:
		pos_ball_x = random.randint(800)//10*10
		pos_ball_y = random.randint(560)//10*10
		k += 1
		hit += 1

	pg.display.flip()
	clock.tick(10)

font1 = pg.font.Font('bebas.ttf', 72)
score1 =  font1.render('score: '+str(hit), True, black)
scoreRect1 = score1.get_rect()
scoreRect1.center = (400,220)

run = True
c = pg.time.get_ticks() + 5000
while pg.time.get_ticks() < c and run:
	screen.blit(score1,scoreRect1)
	pg.display.flip()
	screen.fill((255,128,0))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
pg.quit()
