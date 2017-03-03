class Force(object):
    def __init__(self, x, y, z, xrotation, yrotation, zrotation, scale):
        super(Force, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.xrotation = xrotation
        self.yrotation = yrotation
        self.zrotation = zrotation
        self.scale = scale#
