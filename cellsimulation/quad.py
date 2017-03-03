from mesh import Mesh
from OpenGL.GL import *


class Quad(Mesh):
    def render(self):
        self.render_position()
        glBegin(GL_QUADS)
        self.render_vertices()
        glEnd()
