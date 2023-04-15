import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        self.image = BIRD
        super().__init__(self.image, self.type)

        self.rect.y = 250
        self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

        if self.step_index >= 10:
            self.step_index = 0

        self.type = 0 if self.step_index < 5 else 1
        self.step_index += 1

        