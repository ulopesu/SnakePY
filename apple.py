import random
import arcade
from main import APPLE_COLOR, BLOCK_SIZE, BLOCK_SIZE_HALF, GRID_HEIGHT, GRID_WIDTH


class Apple:
    color = APPLE_COLOR

    def __init__(self):
        self.pos_x = random.randint(0, GRID_WIDTH - 1)
        self.pos_y = random.randint(0, GRID_HEIGHT - 1)

    def draw(self):
        arcade.draw_circle_filled(
            (self.pos_x * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            (self.pos_y * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            BLOCK_SIZE_HALF,
            self.color,
        )
