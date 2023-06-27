import arcade
from enums import Diretion
from main import (
    BLOCK_SIZE,
    BLOCK_SIZE_HALF,
    CENTER_GRID_HEIGHT,
    CENTER_GRID_WIDTH,
    GRID_HEIGHT,
    GRID_WIDTH,
    SNAKE_HEAD_COLOR,
    SNAKE_PART_COLOR,
)


class SnakePart:
    color = SNAKE_PART_COLOR

    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        arcade.draw_ellipse_filled(
            (self.pos_x * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            (self.pos_y * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            BLOCK_SIZE_HALF,
            BLOCK_SIZE_HALF,
            self.color,
        )


class SnakeHead(SnakePart):
    color = SNAKE_HEAD_COLOR

    def draw(self):
        arcade.draw_circle_filled(
            (self.pos_x * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            (self.pos_y * BLOCK_SIZE) + BLOCK_SIZE_HALF,
            BLOCK_SIZE_HALF,
            self.color,
        )


class Snake:
    def __init__(self):
        self.head = SnakeHead(CENTER_GRID_WIDTH, CENTER_GRID_HEIGHT)
        self.body: list[SnakePart] = []
        self.direction = Diretion.UP
        self.lock_dir = False

    def to_grow(self):
        last_part = self.body[-1] if len(self.body) > 0 else self.head
        new_pos_x = last_part.pos_x
        new_pos_y = last_part.pos_y

        if self.direction == Diretion.RIGHT:
            new_pos_x -= 1
        elif self.direction == Diretion.LEFT:
            new_pos_x += 1
        elif self.direction == Diretion.UP:
            new_pos_y -= 1
        elif self.direction == Diretion.DONW:
            new_pos_y += 1

        # Limiting Snake
        if new_pos_x >= GRID_WIDTH:
            new_pos_x = 0
        elif new_pos_x < 0:
            new_pos_x = GRID_WIDTH

        if new_pos_y >= GRID_HEIGHT:
            new_pos_y = 0
        elif new_pos_y < 0:
            new_pos_y = GRID_HEIGHT

        new_part = SnakePart(new_pos_x, new_pos_y)
        self.body.append(new_part)

    def move(self):
        for idx in reversed(range(0, len(self.body))):
            if idx != 0:
                self.body[idx].pos_x = self.body[idx - 1].pos_x
                self.body[idx].pos_y = self.body[idx - 1].pos_y
            else:
                self.body[idx].pos_x = self.head.pos_x
                self.body[idx].pos_y = self.head.pos_y

        if self.direction == Diretion.RIGHT:
            self.head.pos_x += 1
        elif self.direction == Diretion.LEFT:
            self.head.pos_x -= 1
        elif self.direction == Diretion.UP:
            self.head.pos_y += 1
        elif self.direction == Diretion.DONW:
            self.head.pos_y -= 1

        # Limiting Snake
        if self.head.pos_x >= GRID_WIDTH:
            self.head.pos_x = 0
        elif self.head.pos_x < 0:
            self.head.pos_x = GRID_WIDTH

        if self.head.pos_y >= GRID_HEIGHT:
            self.head.pos_y = 0
        elif self.head.pos_y < 0:
            self.head.pos_y = GRID_HEIGHT

        # Direction Control
        self.lock_dir = False

    def killed_himself(self):
        for part in self.body:
            if part.pos_x == self.head.pos_x and part.pos_y == self.head.pos_y:
                return True
        return False

    def change_direction(self, new_direction: Diretion):
        if self.lock_dir is False and new_direction.is_acceptable(self.direction):
            self.direction = new_direction
            self.lock_dir = True

    def draw(self):
        self.head.draw()
        for part in self.body:
            part.draw()
