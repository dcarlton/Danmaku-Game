class Object(object):
    def __init__(self):
        self.xPosition = None
        self.yPosition = None
        self.xSpeed = 0
        self.ySpeed = 0
        self.xAcceleration = 0
        self.yAcceleration = 0

        self.hitbox = None
        self.image = None

    def update(self):
        self.xSpeed += self.xAcceleration
        self.ySpeed += self.yAcceleration
        self.xPosition += self.xSpeed
        self.yPosition += self.ySpeed