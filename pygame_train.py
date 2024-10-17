import pygame as pg
from numpy import random
pg.init()
pg.font.init()
pos_ball = tuple(random.randint(250,size = 2))
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
run = True

player = pg.Rect(350, 500, 100, 20)
ball = pg.Rect(pos_ball, (10, 10))
speed_ball_vertical = 5
speed_ball_horizonal = 2

hit = 0

font = pg.font.Font('bebas.ttf', 24)
nofi_font = pg.font.Font('bebas.ttf', 70)
time = font.render('', True, (0,0,0))
score = font.render('score: 0', True, (0,0,0))
timeRect = time.get_rect()
scoreRect = score.get_rect()
timeRect.center = (30, 20)
scoreRect.center = (740,20)

the_first_open = 1
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
a = 0
clock = pg.time.Clock()
b = pg.time.get_ticks()

while run:
	pg.display.set_caption('Ping ball')
	if the_first_open == 1:
		nofi_start = nofi_font.render('WELCOME! GAME WILL START IN 3', True, (0,0,0))
		nofi_startRect = nofi_start.get_rect()
		nofi_startRect.center = (400, 300)
		while b < 4000 and run:
			b = pg.time.get_ticks()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					run = False
			screen.blit(nofi_start, nofi_startRect)
			pg.display.flip()
			screen.fill("white")
			nofi_start = nofi_font.render('WELCOME! GAME WILL START IN '+str((4000-b)//1000), True, (0,0,0))
			the_first_open = 0

	pos_ball = tuple(random.randint(250,size = 2))
	pg.display.set_caption('Ping ball')

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	score = font.render('score: '+str(hit), True, (0,0,0))
	screen.fill("white")
	pg.draw.aaline(screen,(84,164,255),(0,40),(800,40))
	pg.draw.rect(screen,(84,164,255),ball,0,5)
	pg.draw.rect(screen,(84,164,255),player)
	screen.blit(time, timeRect)
	screen.blit(score, scoreRect)

	b = pg.time.get_ticks()
	if (b//1000-a*60-5) == 60:
		a +=1
	time = font.render('TOTAL TIME:   '+str(a)+':'+str(b//1000-a*60-5), True, (0,0,0))

	bound_left_player,bound_height_player,_,_ = player
	ball.move_ip(speed_ball_horizonal, speed_ball_vertical)

	key = pg.key.get_pressed()
	if key[pg.K_LEFT] == True and bound_left_player > 0:
		player.move_ip(-10,0)
	elif key[pg.K_RIGHT] == True and bound_left_player <700:
		player.move_ip(10,0)

	bound_left_player,bound_height_player,_,_ = player
	bound_left_ball,bound_height_ball,_,_ = ball

	if bound_height_ball+5 in range(490,510) and bound_left_ball+5 in range(bound_left_player,bound_left_player+101):
		if speed_ball_vertical == 5:
			hit += 1
		speed_ball_vertical = -5

		if key[pg.K_LEFT] == True:
			speed_ball_horizonal = -5
		elif key[pg.K_RIGHT] == True:
			speed_ball_horizonal = 5
	

	elif bound_height_ball < 40:
		speed_ball_vertical = 5
	elif bound_left_ball < 0:
		speed_ball_horizonal = 5
	elif bound_left_ball > 800:
		speed_ball_horizonal = -5
	elif bound_height_ball > 550:
		ball = pg.Rect(pos_ball, (10, 10))
		c = b + 5000
		nofi_lose = nofi_font.render('YOU LOSE! RESTART IN 5', True, (0,0,0))
		nofi_loseRect = nofi_lose.get_rect()
		nofi_loseRect.center = (400, 300)
		nofi_score = nofi_font.render('YOUR SCORE: '+ str(hit), True, (0,0,0))
		nofi_scoreRect = nofi_score.get_rect()
		nofi_scoreRect.center = (400, 400)
		while b < c and run:
			b = pg.time.get_ticks()
			screen.blit(nofi_lose, nofi_loseRect)
			screen.blit(nofi_score, nofi_scoreRect)
			pg.display.flip()
			screen.fill("white")
			nofi_lose = nofi_font.render('YOU LOSE! RESTART IN '+str((c-b)//1000 + 1), True, (0,0,0))
			nofi_score = nofi_font.render('YOUR SCORE: '+ str(hit), True, (0,0,0))
			for event in pg.event.get():
				if event.type == pg.QUIT:
					run = False
		hit = 0
	pg.display.flip()
	clock.tick(60)

pg.quit()
