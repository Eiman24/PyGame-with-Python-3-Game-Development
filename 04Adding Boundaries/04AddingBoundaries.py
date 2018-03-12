import pygame


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

def rocket_location(x,y):
	gameDisplay.blit(rocket_im,(x,y))

def game_loop():
	x = (display_width * 0.42)
	y = (display_height * 0.7) 
	x_change = 0

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
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

		x += x_change
		# add boundaries
		if x > display_width - rocket_width or x < 0:
			gameExit = True
		
		gameDisplay.fill(sky_blue)
		
		rocket_location(x,y)

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()