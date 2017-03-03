import sys

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Scene(object):
    ESCAPE = '\033'
    PANGLE = 45.0

    def __init__(self, title, width, height, elements):
        super(Scene, self).__init__()
        self.window = None
        self.title = title
        self.width = width
        self.height = height
        self.elements = elements

    def perspective(self, width, height):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(Scene.PANGLE, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def start(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)

        self.window = glutCreateWindow(self.title)

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        self.perspective(self.width, self.height)

        glutDisplayFunc(self.render)
        glutIdleFunc(self.render)
        glutReshapeFunc(self.resize)
        glutKeyboardFunc(self.key_pressed)

        glutMainLoop()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for element in self.elements:
            element.render()

        glutSwapBuffers()

    def resize(self, width, height):
        if height == 0:
            height = 1

        glViewport(0, 0, width, height)
        self.perspective(width, height)

    def key_pressed(self, key, x, y):
        if key == Scene.ESCAPE:
            sys.exit()
