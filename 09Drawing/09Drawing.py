import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
pink = (255,100,100)
sky_blue = (135, 206, 235)
light_green = (100,225,150)

gameDisplay = pygame.display.set_mode((display_width,display_height))

gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = pink

pygame.draw.line(gameDisplay,sky_blue,(100,200),(300,450),2)

pygame.draw.rect(gameDisplay,pink,(400,400,50,25))

pygame.draw.circle(gameDisplay,white,(150,150),75)

# if the point is in different order, it'll appear different shape of polygon drawn
pygame.draw.polygon(gameDisplay,light_green,((25,75),(476,225),(250,522),(450,230)))
# in different order
# pygame.draw.polygon(gameDisplay,light_green,((25,75),(250,522),(476,225),(450,230)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()