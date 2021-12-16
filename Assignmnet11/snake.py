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
        self.change_x = 0
        self.change_y = 0
        self.score = 0 
        self.center_x = SCREEN_WIDTH // 2 
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = 8
        self.body = []
        self.goal_x = 0
        self.goal_y = 0
        self.goal_x_range = []
        self.goal_y_range = []

    def move(self):
        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.score:
            self.body.pop(0)

        self.decide_move()
        
        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x <0:
            self.center_x -= self.speed
        if self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y <0:
            self.center_y -= self.speed

    def observe(self, banana_x, banana_y):
        self.goal_x = banana_x
        self.goal_y = banana_y

        #below code is to fix the bug where the snake is stuck at goal_x
        self.goal_x_range = []
        self.goal_y_range = []
        error = self.speed // 2
        for i in range(error+1):
            self.goal_x_range.append(banana_x+i)
            self.goal_x_range.append(banana_x-i)
            self.goal_y_range.append(banana_y+i)
            self.goal_y_range.append(banana_y-i)

    def decide_move(self):
        if self.center_x in self.goal_x_range :
            if self.goal_y > self.center_y:
                self.change_y = 1
                self.change_x = 0
            elif self.goal_y < self.center_y:
                self.change_y = -1
                self.change_x = 0
        else:
            if self.goal_x > self.center_x:
                self.change_x = 1
                self.change_y = 0
            elif self.goal_x < self.center_x:
                self.change_x = -1
                self.change_y = 0
        
            

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

        for i in range(len(self.body)):
            arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color)

        
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
        self.snake.observe(self.banana.center_x, self.banana.center_y)

    def on_draw(self): 
        arcade.start_render() 
        self.snake.draw()
        self.scoreboard.draw()
        self.banana.draw()
        self.poop.draw()

    '''
    def on_key_release(self, key: int, modifiers: int): 
        if key == arcade.key.LEFT: 
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT: 
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP: 
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN: 
            self.snake.change_y = -1
            self.snake.change_x = 0
            '''

    def on_update(self, delta_time):

        self.snake.move()
        
        if arcade.check_for_collision(self.snake, self.banana):
            self.banana.update()
            self.snake.observe(self.banana.center_x, self.banana.center_y) # the snake locates the banana(food)
            new_score = self.snake.update_score(1)
            self.scoreboard.set_score(new_score)

        if arcade.check_for_collision(self.snake, self.poop):
            self.poop.update()
            new_score = self.snake.update_score(-1)
            if new_score <= 0:
                print('Game over!')
                #arcade.draw_text("GAME OVER!", SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.RED, 30)
            self.scoreboard.set_score(new_score)



my_game = Game()
arcade.run()

