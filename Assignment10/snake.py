import random
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Snake(arcade.Sprite): 
    def __init__ (self): 
        super().__init__() 
        self.width = 20
        self.height = 20
        self.color = arcade.color.AVOCADO
        self.change_x = None 
        self.change_y = None 
        self.score = 0 
        self.center_x = SCREEN_WIDTH // 2 
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = 20

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def update_score(self, score):
        self.score += score
        return self.score

class Banana(arcade.Sprite):
    def __init__(self):
        super().__init__() 
        self.width = 10
        self.height = 10
        self.color = arcade.color.YELLOW
        self.change_x = None
        self.change_y = None
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = random.randint(0,SCREEN_HEIGHT)
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def update(self):
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = random.randint(0,SCREEN_HEIGHT)
        self.draw()

class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__() 
        self.width = 10
        self.height = 10
        self.color = arcade.color.BROWN
        self.change_x = None
        self.change_y = None
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = random.randint(0,SCREEN_HEIGHT)
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def update(self):
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = random.randint(0,SCREEN_HEIGHT)
        self.draw()

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.x = 5
        self.y = SCREEN_HEIGHT-30
        self.color = arcade.color.BLACK
        self.size = 25

    def set_score(self, score):
        self.score = score
        self.draw()

    def draw(self):
        arcade.draw_text(str(self.score), self.x, self.y, self.color, self.size)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Mar Bazi!")
        arcade.set_background_color(arcade.color.DESERT_SAND)
        self.snake = Snake()
        self.scoreboard = Scoreboard()
        self.banana = Banana()
        self.poop = Poop()

    def on_draw(self): 
        arcade.start_render() 
        self.snake.draw()
        self.scoreboard.draw()
        self.banana.draw()
        self.poop.draw()

    def on_key_release(self, key: int, modifiers: int): 
        if key == arcade.key.LEFT: 
            self.snake.center_x -= self.snake.speed
        elif key == arcade.key.RIGHT: 
            self.snake.center_x += self.snake.speed
        elif key == arcade.key.UP: 
            self.snake.center_y += self.snake.speed
        elif key == arcade.key.DOWN: 
            self.snake.center_y -= self.snake.speed

    def on_update(self, delta_time):
        if arcade.check_for_collision(self.snake, self.banana):
            self.banana.update()
            new_score = self.snake.update_score(2)
            self.scoreboard.set_score(new_score)

        if arcade.check_for_collision(self.snake, self.poop):
            self.poop.update()
            new_score = self.snake.update_score(-1)
            if new_score <= 0:
                print('Game over!')
                arcade.draw_text("GAME OVER!", SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.RED, 30)
            self.scoreboard.set_score(new_score)



my_game = Game()
arcade.run()
        
