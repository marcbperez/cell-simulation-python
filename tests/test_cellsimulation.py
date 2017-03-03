import unittest

from cellsimulation.force import Force
from cellsimulation.vertex import Vertex
from cellsimulation.triangle import Triangle
from cellsimulation.quad import Quad
from cellsimulation.scene import Scene

import threading, time


class CellsimulationCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gravity = Force(0, -0.098, 0, 0, 0, 0, 0)
        cls.spin = Force(0, 0, 0, 0, 10, 0, 0)

        cls.pyramid = Triangle(-1.5, 0.0, -30.0, 0.0, 0.0, 0.0, 1, [
            Vertex(0.0, 1.0, 0.0, 1.0, 0.0, 0.0),
            Vertex(-1.0, -1.0, 1.0, 0.0, 1.0, 0.0),
            Vertex(1.0, -1.0, 1.0, 0.0, 0.0, 1.0),
            Vertex(0.0, 1.0, 0.0, 1.0, 0.0, 0.0),
            Vertex(1.0, -1.0, 1.0, 0.0, 0.0, 1.0),
            Vertex(1.0, -1.0, -1.0, 0.0, 1.0, 0.0),
            Vertex(0.0, 1.0, 0.0, 1.0, 0.0, 0.0),
            Vertex(1.0, -1.0, -1.0, 0.0, 1.0, 0.0),
            Vertex(-1.0, -1.0, -1.0, 0.0, 0.0, 1.0),
            Vertex(0.0, 1.0, 0.0, 1.0, 0.0, 0.0),
            Vertex(-1.0, -1.0, -1.0, 0.0, 0.0, 1.0),
            Vertex(-1.0, -1.0, 1.0, 0.0, 1.0, 0.0),
        ], [
            cls.spin
        ])

        cls.cube = Quad(1.5, 10.0, -30.0, 0.0, 0.0, 0.0, 1, [
            Vertex(1.0, 1.0, -1.0, 0.0, 1.0, 0.0),
            Vertex(-1.0, 1.0,-1.0, 0.0, 1.0, 0.0),
            Vertex(-1.0, 1.0, 1.0, 0.0, 1.0, 0.0),
            Vertex(1.0, 1.0, 1.0, 0.0, 1.0, 0.0),
            Vertex(1.0, -1.0, 1.0, 1.0, 0.5, 0.0),
            Vertex(-1.0, -1.0, 1.0, 1.0, 0.5, 0.0),
            Vertex(-1.0, -1.0, -1.0, 1.0, 0.5, 0.0),
            Vertex(1.0, -1.0, -1.0, 1.0, 0.5, 0.0),
            Vertex(1.0, 1.0, 1.0, 1.0, 0.0, 0.0),
            Vertex(-1.0, 1.0, 1.0, 1.0, 0.0, 0.0),
            Vertex(-1.0, -1.0, 1.0, 1.0, 0.0, 0.0),
            Vertex(1.0, -1.0, 1.0, 1.0, 0.0, 0.0),
            Vertex(1.0, -1.0, -1.0, 1.0, 1.0, 0.0),
            Vertex(-1.0, -1.0, -1.0, 1.0, 1.0, 0.0),
            Vertex(-1.0, 1.0, -1.0, 1.0, 1.0, 0.0),
            Vertex(1.0, 1.0, -1.0, 1.0, 1.0, 0.0),
            Vertex(-1.0, 1.0, 1.0, 0.0, 0.0, 1.0),
            Vertex(-1.0, 1.0, -1.0, 0.0, 0.0, 1.0),
            Vertex(-1.0, -1.0, -1.0, 0.0, 0.0, 1.0),
            Vertex(-1.0, -1.0, 1.0, 0.0, 0.0, 1.0),
            Vertex(1.0, 1.0, -1.0, 1.0, 0.0, 1.0),
            Vertex(1.0, 1.0, 1.0, 1.0, 0.0, 1.0),
            Vertex(1.0, -1.0, 1.0, 1.0, 0.0, 1.0),
            Vertex(1.0, -1.0, -1.0, 1.0, 0.0, 1.0),
        ], [
            cls.gravity
        ])

        cls.scene = Scene('Simulation', 640, 480, [cls.pyramid, cls.cube])
        cls.thread = threading.Thread(target=cls.scene.start)

    def test_forces(self):
        self.assertIsInstance(self.gravity, Force)
        self.assertIsInstance(self.spin, Force)

    def test_meshes(self):
        self.assertIsInstance(self.pyramid, Triangle)
        self.assertIsInstance(self.cube, Quad)

    def test_window(self):
        self.thread.start()
        self.scene.resize(0, 0)

        time.sleep(5)

        with self.assertRaises(SystemExit):
            self.scene.key_pressed(Scene.ESCAPE, None, None)
