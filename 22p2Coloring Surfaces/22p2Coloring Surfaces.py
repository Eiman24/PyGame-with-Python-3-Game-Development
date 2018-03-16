import pygame

from pygame.locals import *
#pip install PyOpenGL PyOpenGL_accelerate
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
	)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
	(1,0.85,0.0),
	(1,0.85,0.2),
	(1,0.85,0.4),
	(1,0.85,0.6)


	)

def Cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		# all vertexes in this surface
		for vertex in surface:
			glColor3fv(colors[x])
			x += 1
			glVertex3fv(vertices[vertex])


	glEnd()
'''
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
'''
def main():
	pygame.init()
	display = (800,600)
	# double buffer双缓存区
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

	gluPerspective(45,(display[0]/display[1]),0.1,50.0)

	glTranslatef(0.0,0.0,-5)

	glRotatef(0,0,0,0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glRotatef(1,2,3,0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)

main()