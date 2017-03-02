import unittest


class CellsimulationCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arg = True

    def test_arg(self):
        self.assertEquals(self.arg, True)
