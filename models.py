import random
import arcade

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class Alien():
    def __init__(self):
        self.y = 620
        self.x = random.randrange(480)

    def update(self):
        self.y -= 1
        if self.y < 0:
            self.reset_pos()

class Rocket:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

        self.delta_x = 0

    def move(self):
        # Move left/right
        self.x += self.delta_x

        if(self.x < 0 or self.x > 480):
            self.delta_x = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.rocket = Rocket(self, width/2, 60)
        self.alien = Alien()
 
    def update(self, delta):
        self.rocket.move()
        self.alien.update()