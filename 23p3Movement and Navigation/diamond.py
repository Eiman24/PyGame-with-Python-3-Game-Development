import pygame

from pygame.locals import *
#pip install PyOpenGL PyOpenGL_accelerate
from OpenGL.GL import * 
from OpenGL.GLU import *

vertices = (
	(0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1)
	)

edges = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (2,3),
    (3,4),
    (4,1),
    (5,1),
    (5,2),
    (5,3),
    (5,4)
    )

surfaces = (
    (0,1,2),
    (0,2,3),
    (0,3,4),
    (0,4,1),
    (5,1,2),
    (5,2,3),
    (5,3,4),
    (5,4,1)
    )

colors = (
	(1,1,1),
	(0.8,0.8,0.8),
	(0.6,0.6,0.6)



	)

def Cube():
	glBegin(GL_TRIANGLES)
	for surface in surfaces:
		x = 0
		print(surface)
		# all vertexes in this surface
		for vertex in surface:
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
			x += 1
			print(vertex)

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

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glRotatef(10,0,-1,0)
				if event.key == pygame.K_RIGHT:
					glRotatef(10,0,1,0)

				if event.key == pygame.K_UP:
					glRotatef(10,-1,0,0)
				if event.key == pygame.K_DOWN:
					glRotatef(10,1,0,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1.0)

				if event.button == 5:
					glTranslatef(0,0,-1.0)
		#glRotatef(1,2,3,0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)

main()