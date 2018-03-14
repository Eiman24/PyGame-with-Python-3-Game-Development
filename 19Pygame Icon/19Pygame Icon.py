import pygame
import time
import random

pygame.init()
# define something
display_width = 800
display_height = 600
# define pic width
rocket_width = 126

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
pink = (255,100,100)
sky_blue = (135, 206, 235)
light_green = (100,225,150)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rocket')
clock = pygame.time.Clock()

rocket_im = pygame.image.load('rocket.png')

rocket_icon = pygame.image.load('rocketicon.png')
pygame.display.set_icon(rocket_icon)

#pause = True
# Scores
def things_dodged(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("Dodged:" + str(count),True,black)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def rocket_location(x,y):
	gameDisplay.blit(rocket_im,(x,y))

# render the font and return a rectangle
def text_objects(text,font,color):
	textSurf = font.render(text,True,color)
	return textSurf, textSurf.get_rect()

def message_display(text):
	# define font
	largeText = pygame.font.Font('freesansbold.ttf',85)
	TextSurf, TextRect = text_objects(text, largeText,black)
	TextRect.center = ((display_width/2),(display_height/2))
	# A Rect can also be passed as the destination, 
	# and the topleft corner of the rectangle will be used as the position for the blit.
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(black)
		largeText = pygame.font.Font('freesansbold.ttf',85)
		TextSurf, TextRect = text_objects('You Crashed', largeText,white)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		# button(massage,x,y,w,h,inicolor,actcolor)
		button("Replay",150,450,100,50,light_green,green,"play")
		button("Quit",550,450,100,50,pink,red,"quit")

		pygame.display.update()
		clock.tick(30)

def button(massage,x,y,w,h,inicolor,actcolor,action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		print(mouse,click)

		# mouse[0] is the x coordinate and mouse[1] is y
		if x + w > mouse[0] > x and y + h > mouse[1] > y:
			pygame.draw.rect(gameDisplay,actcolor,(x,y,w,h))
			if click[0] == 1 and action != None:
				if action == "play":
					game_loop()
				elif action == "quit":
					pygame.quit()
					quit()
				elif action == "unpause":
					unpause()

		else:
			pygame.draw.rect(gameDisplay,inicolor,(x,y,w,h))

		smallText = pygame.font.Font("freesansbold.ttf",20)
		textSurf1,textRect1 = text_objects(massage,smallText,black)
		textRect1.center = ((x + (w/2)),(y + (h/2)))
		gameDisplay.blit(textSurf1,textRect1)

def  unpause():
	global pause
	pause = False

def game_pause():

	global pause
	pause = True

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		largeText = pygame.font.Font('freesansbold.ttf',85)
		TextSurf, TextRect = text_objects('Pause', largeText,black)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		# button(massage,x,y,w,h,inicolor,actcolor)
		button("Continue",150,450,100,50,light_green,green,"unpause")
		button("Quit",550,450,100,50,pink,red,"quit")

		pygame.display.update()
		clock.tick(30)

def game_intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',85)
		TextSurf, TextRect = text_objects('Rocket Dodging', largeText,black)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		# button(massage,x,y,w,h,inicolor,actcolor)
		button("Start!",150,450,100,50,light_green,green,"play")
		button("Quit",550,450,100,50,pink,red,"quit")

		pygame.display.update()
		clock.tick(30)

def game_loop():

	global pause

	x = (display_width * 0.42)
	y = (display_height * 0.7)
	x_change = 0									

	gameExit = False														

	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 5
	# must longer than rocket_width
	thing_width = 128
	thing_height = 128

	dodged = 0

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# quit here
				pygame.quit()
				quit()
			print(event)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5

				if event.key == pygame.K_p:
					game_pause()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					x_change += 5
				if event.key == pygame.K_RIGHT:
					x_change += -5
					
			if x_change == 10:
				x_change = 5
			if x_change == -10:
				x_change = -5
		# 这里有一个bug，只有当event.get()执行时才会从键盘缓存区调用key，
		# 导致残留KEYUP，新游戏会自动运动（x_change != 0）
		if x > display_width - rocket_width or x < 0:
			crash()

		x += x_change

		gameDisplay.fill(sky_blue)

		rocket_location(x,y)

		things_dodged(dodged)

		# function: things(thingx,thingy,thingw,thingh,color)
		things(thing_startx,thing_starty,thing_width,thing_height,pink)
		thing_starty += thing_speed
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width - thing_width)

			# Score plus 1
			dodged += 1
			# challenge here
			thing_speed += 1

		# origin upper left
		if y < thing_starty + thing_height:
			print('y crossover')

			if (x > thing_startx and x < thing_startx + thing_width) or (x + rocket_width > thing_startx and x + rocket_width < thing_startx + thing_width):
				print('x crossover')
				crash()

		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()