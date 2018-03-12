import pygame


pygame.init()
# define something
display_width = 800
display_height = 600
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

x = (display_width * 0.42)
y = (display_height * 0.7) 
# define location changes
x_change = 0

End = False

while not End:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			End = True
		print(event)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			if event.key == pygame.K_RIGHT:
				x_change = 5

		# Make balance between KEYDOWN & KEYUP
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_change += 5
			if event.key == pygame.K_RIGHT:
				x_change += -5
				
		# avoid KEYDOWN & KEYUP pressed the same time making x_change = +-10
		if x_change == 10:
			x_change = 5
		if x_change == -10:
			x_change = -5

	x += x_change
	
	gameDisplay.fill(sky_blue)
	
	
	rocket_location(x,y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()