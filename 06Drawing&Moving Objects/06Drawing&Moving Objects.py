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
pink = (255,100,100)
sky_blue = (135, 206, 235)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rocket')
clock = pygame.time.Clock()

rocket_im = pygame.image.load('rocket.png')

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def rocket_location(x,y):
	gameDisplay.blit(rocket_im,(x,y))

# render the font and return a rectangle
def text_objects(text,font):
	textSurf = font.render(text,True,black)
	return textSurf, textSurf.get_rect()

def message_display(text):
	# define font
	largeText = pygame.font.Font('freesansbold.ttf',85)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	# A Rect can also be passed as the destination, 
	# and the topleft corner of the rectangle will be used as the position for the blit.
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()

	time.sleep(2)

	#game_loop()

def crash():
	message_display('You Die')

def game_loop():
	x = (display_width * 0.42)
	y = (display_height * 0.7) 
	x_change = 0

	gameExit = False

	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100

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

		# function: things(thingx,thingy,thingw,thingh,color)
		things(thing_startx,thing_starty,thing_width,thing_height,pink)
		thing_starty += thing_speed
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)

		rocket_location(x,y)

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()