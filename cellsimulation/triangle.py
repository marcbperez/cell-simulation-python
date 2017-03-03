from mesh import Mesh
from OpenGL.GL import *


class Triangle(Mesh):
    def render(self):
        self.render_position()
        glBegin(GL_TRIANGLES)
        self.render_vertices()
        glEnd()
