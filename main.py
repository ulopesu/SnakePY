"""
SnakePY Game
"""
import arcade

from enums import Diretion

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SNAKE_PY"
UPDATE_SPEED = 0.15

# Grid Constants
BLOCK_SIZE = 20
BLOCK_SIZE_HALF = BLOCK_SIZE // 2
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
CENTER_GRID_WIDTH = GRID_WIDTH // 2
CENTER_GRID_HEIGHT = GRID_HEIGHT // 2

# Color Constants
BACKGROUND_COLOR = arcade.color.AMAZON
SNAKE_HEAD_COLOR = arcade.color.RED_DEVIL
SNAKE_PART_COLOR = arcade.color.BLACK
APPLE_COLOR = arcade.color.ORANGE


class SnakePY(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BACKGROUND_COLOR)
        self.delta_time_counter = 0
        self.score = 0
        self.snake = None
        self.apple = None
        self.fim = False
        self.update_speed = 0

    def setup(self):
        """Set up the game variables. Call to re-start the game."""
        from snake import Snake
        from apple import Apple

        self.snake = Snake()
        self.apple = Apple()
        self.update_speed = UPDATE_SPEED

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.apple.draw()
        self.snake.draw()

    def update(self, delta_time):
        from apple import Apple

        if self.fim:
            return

        self.delta_time_counter += delta_time
        if self.delta_time_counter >= self.update_speed:
            self.snake.move()
            if (
                self.snake.head.pos_x == self.apple.pos_x
                and self.snake.head.pos_y == self.apple.pos_y
            ):
                self.score += 1
                self.apple = Apple()
                self.snake.to_grow()

            if self.snake.killed_himself():
                self.fim = True
            self.delta_time_counter -= self.update_speed

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """

        if key == arcade.key.RIGHT:
            self.snake.change_direction(Diretion.RIGHT)
        if key == arcade.key.LEFT:
            self.snake.change_direction(Diretion.LEFT)
        if key == arcade.key.UP:
            self.snake.change_direction(Diretion.UP)
        if key == arcade.key.DOWN:
            self.snake.change_direction(Diretion.DONW)

        if key == arcade.key.ESCAPE:
            arcade.window_commands.close_window()

        if key == arcade.key.W:
            self.update_speed -= 0.05
        if key == arcade.key.S:
            self.update_speed += 0.05

        if self.update_speed < 0:
            self.update_speed = 0
        if self.update_speed > 1:
            self.update_speed = 1



def main():
    """Main function"""
    game = SnakePY(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
