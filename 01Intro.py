import pygame

# initial pygame
pygame.init()
# set a display resolution
gameDisplay = pygame.display.set_mode((800,600))
# name a caption for the game
pygame.display.set_caption('Demo001')
#fps
clock = pygame.time.Clock()

End = False

while not End:
	#get input
	for event in pygame.event.get():
		# hit red x out of the window to quit, end loop
		if event.type == pygame.QUIT:
			End = True

		print(event)
	# update the display,with update() empty parameter will update entire scene
	# or with parameter updating some specific thing
	# with pygame.display.flip() updating entire window
	pygame.display.update()
	# set fps
	clock.tick(60)

pygame.quit()
quit()