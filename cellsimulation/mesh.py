from OpenGL.GL import *


class Mesh(object):
    def __init__(self, x, y, z, xrotation, yrotation, zrotation, scale,
    vertices, forces):
        super(Mesh, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.xrotation = xrotation
        self.yrotation = yrotation
        self.zrotation = zrotation
        self.scale = scale
        self.vertices = vertices
        self.forces = forces

    def render_position(self):
        for force in self.forces:
            self.x = self.x + force.x
            self.y = self.y + force.y
            self.z = self.z + force.z
            self.xrotation = self.xrotation + force.xrotation
            self.yrotation = self.yrotation + force.yrotation
            self.zrotation = self.zrotation + force.zrotation
            self.scale = self.scale + force.scale

        glLoadIdentity()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.xrotation, 1.0, 0.0, 0.0)
        glRotatef(self.yrotation, 0.0, 1.0, 0.0)
        glRotatef(self.zrotation, 0.0, 0.0, 1.0)

    def render_vertices(self):
        for vertex in self.vertices:
            glColor3f(vertex.red, vertex.green, vertex.blue)
            glVertex3f(vertex.x*self.scale, vertex.y*self.scale,
                vertex.z*self.scale)
