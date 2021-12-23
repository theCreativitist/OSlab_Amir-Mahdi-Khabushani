import math
import random
import arcade
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceCraft(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.width = 55
        self.height = 55
        self.score = 0
        self.center_x = SCREEN_WIDTH //2
        self.center_y =  40
        self.angle = 0
        self.change_angle = 0
        self.speed = 5
        self.hearts = [Heart(30,20), Heart(70,20), Heart(110,20)]
        self.bullets = []

    def draw(self):
        for heart in self.hearts:
            heart.draw()
        return super().draw()

    def fire(self):
        self.bullets.append(Bullet(self))

    def rotate(self):
        self.angle += self.speed * self.change_angle

    def increase_score(self):
        self.score += 1

    def is_alive(self):
        if len(self.hearts) > 0:
            return True
        else:
            return False

    


class Heart(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('heart.png', 0.04, center_x = center_x, center_y= center_y)


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.width = 10
        self.height = 20
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.angle = host.angle
        self.speed = 10

    def move(self):
        rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(rad)
        self.center_y += self.speed * math.cos(rad)

    def play_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2)    



class Enemy(arcade.Sprite):
    def __init__(self, speed):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = 40
        self.height = 40
        self.angle = 180
        self.center_x = random.randint(self.width ,SCREEN_WIDTH - self.width)
        self.center_y = SCREEN_HEIGHT + self.height//2
        self.speed = speed

    def move(self):
        self.center_y -= self.speed

    def play_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'))



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="SpaceWars by AMK")
        self.background_image = arcade.load_texture("background.png")
        self.me = SpaceCraft()
        self.enemies = []
        self.e_speed = 3
        self.rand_time = 2
        self.start_time = time.time()
    
    def restart(self):
        self.enemies.clear()
        self.e_speed = 3
        self.me = SpaceCraft()
        

    def on_draw(self):
        if self.me.is_alive():
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH ,SCREEN_HEIGHT,self.background_image )
            self.me.draw()
            for enemy in self.enemies:
                enemy.draw()
            for b in self.me.bullets:
                b.draw()
            arcade.draw_text(str(self.me.score), start_x= SCREEN_WIDTH-50 , start_y= 20 , font_size=25) 

        else:
            arcade.Window.clear(self)
            arcade.draw_text("YOU LOST!", 50, SCREEN_HEIGHT//2, font_size=30)
            arcade.draw_text("Press R to restart the game.", 30, SCREEN_HEIGHT//2 - 150, font_size=30)
            self.enemies.clear()
            

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            if self.me.is_alive():
                self.me.fire() 
                self.me.bullets[0].play_sound()
        elif symbol == arcade.key.LEFT:
            self.me.change_angle = 1
        elif symbol == arcade.key.RIGHT:
            self.me.change_angle = -1
        elif symbol == arcade.key.R:
            self.restart()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or arcade.key.RIGHT:
            self.me.change_angle = 0

    def on_update(self, delta_time: float):
        if self.me.is_alive:
            self.me.rotate()
            for b in self.me.bullets:
                b.move()
                if b.center_x > SCREEN_WIDTH or b.center_x < 0 or b.center_y > SCREEN_HEIGHT or b.center_y < 0:
                    self.me.bullets.remove(b)

            self.end_time = time.time()
            if self.end_time - self.start_time > self.rand_time:
                random.seed()
                self.e_speed += 0.2
                self.enemies.append(Enemy(self.e_speed))
                self.start_time = time.time()
                self.rand_time = random.randint(1 ,3)

            for e in self.enemies:
                if e.center_y < 0:
                    self.enemies.remove(e)
                    self.me.hearts.pop()
                    arcade.play_sound(arcade.sound.Sound(':resources:sounds/gameover5.wav'), 0.2)
                for b in self.me.bullets:
                    if arcade.check_for_collision(e,b):
                        e.play_sound()
                        self.enemies.remove(e)
                        self.me.increase_score()
                e.move()
                





game = Game()
arcade.run()