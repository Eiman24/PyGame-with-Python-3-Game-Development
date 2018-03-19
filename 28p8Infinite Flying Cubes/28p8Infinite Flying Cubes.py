import pygame
import random

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

ground_vertices = (
	(-10,-0.1,20),
	(10,-0.1,20),
	(-10,-0.1,-100),
	(-10,-0.1,-100),

	)

def ground():
	glBegin(GL_QUADS)
	for vertex in ground_vertices:
		glColor3fv((1,0.5,0.7))
		glVertex3fv(vertex)

	glEnd()


def set_vertices(max_distance):
	x_value_change = random.randrange(-10,10)
	y_value_change = -1	#random.randrange(-10,10)
	z_value_change = random.randrange(-1*max_distance,-2)

	new_vertices = []

	for vert in vertices:
		new_vert = []

		new_x = vert[0] + x_value_change
		new_y = vert[1] + y_value_change
		new_z = vert[2] + z_value_change

		new_vert.append(new_x)
		new_vert.append(new_y)
		new_vert.append(new_z)

		new_vertices.append(new_vert)

	return new_vertices

def Cube(vertices):
	glBegin(GL_QUADS)
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

	glTranslatef(random.randrange(-5,5),0, -30)

	#glRotatef(0,0,0,0)
	object_passed = False

	x_move = 0
	y_move = 0

	max_distance = 300

	cube_dict = {}

	for x in range(75):
		cube_dict[x] = set_vertices(max_distance) 

	while not object_passed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move = 0.3
				if event.key == pygame.K_RIGHT:
					x_move = -0.3
				if event.key == pygame.K_UP:
					y_move = -0.3
				if event.key == pygame.K_DOWN:
					y_move = 0.3

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_move = 0

				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_move = 0
		'''
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1.0)

				if event.button == 5:
					glTranslatef(0,0,-1.0)
		'''
		#glRotatef(1,2,3,0)
		x = glGetDoublev(GL_MODELVIEW_MATRIX)
		camera_x = x[3][0]
		camera_y = x[3][1]
		camera_z = x[3][2]
		
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glTranslatef(x_move,y_move,0.2)

		ground()

		for each_cube in cube_dict:
			Cube(cube_dict[each_cube])
		pygame.display.flip()
		pygame.time.wait(10)
		

		#if camera_z <=0:
			#object_passed = True

for x in range(3):
	main()
pygame.quit()
quit()