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

# image loading
rocket_im = pygame.image.load('rocket.png')

# define function of rocket location,
# for (0,0) at the upper left of screen  
def rocket_location(x,y):
	gameDisplay.blit(rocket_im,(x,y))

# define x y
# the origin of the image is at the upper left corner 
x = (display_width * 0.42)
y = (display_height * 0.7) 

End = False

while not End:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			End = True
		print(event)
	
	# set background(if this line after rocket_location,it'll cover rocket)
	gameDisplay.fill(sky_blue)
	
	# move the rocket
	rocket_location(x,y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()