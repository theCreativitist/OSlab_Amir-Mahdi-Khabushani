import math
import random
import arcade
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ENEMY_HEIGHT = 40
ENEMY_WIDTH = 40
EXPLOSION_TEXTURES = []
for t in range(17):
    EXPLOSION_TEXTURES.append(arcade.load_texture('explosion/explosion-%s.png' %str(t+1)))
UPDATES_PER_FRAME = 3

class SpaceCraft(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.width = 55
        self.height = 55
        self.score = 0
        self.center_x = SCREEN_WIDTH //2
        self.center_y =  40
        self.change_x = 0
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

    def move(self):
        self.center_x += self.speed * self.change_x

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
        self.speed = 20

    def move(self):
        rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(rad)
        self.center_y += self.speed * math.cos(rad)

    def play_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2)    



class Enemy(arcade.Sprite):
    def __init__(self, speed):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.angle = 180
        self.center_x = random.randint(self.width ,SCREEN_WIDTH - self.width)
        self.center_y = SCREEN_HEIGHT + self.height//2
        self.speed = speed

    def move(self):
        self.center_y -= self.speed

    def explode(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'))


class Boss(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = ENEMY_WIDTH * 2
        self.height = ENEMY_HEIGHT * 2
        self.angle = 180
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT - self.height//2
        self.speed = 10



class Explosion(arcade.Sprite):
    def __init__(self, host):
        super().__init__()
        #self.width = host.width
        #self.height = host.height
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.cur_texture = 1
        self.textures = EXPLOSION_TEXTURES
        self.scale = 0.4
        self.time_to_die = False
        self.life_span = 8
        #self.cur_time = 0
        
    def update_animation(self, delta_time: float = 1 / 60):
        frame = self.cur_texture // UPDATES_PER_FRAME
        self.texture = self.textures[frame]
        #self.cur_time += 1
        #if self.cur_time > self.life_span:
        #    self.time_to_die = True
        self.cur_texture += 1
        if self.cur_texture > self.life_span * UPDATES_PER_FRAME:
            self.time_to_die = True



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="SpaceWars by AMK")
        self.background_image = arcade.load_texture("background.png")
        self.me = SpaceCraft()
        self.enemies = []
        self.e_speed = 3
        self.rand_time = 2
        self.start_time = time.time()
        self.elapsed_time = 0
        self.explosions = []
        self.boss = Boss()
    
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
            for ex in self.explosions:
                ex.draw()
            self.boss.draw()
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
        elif symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.D:
            self.me.change_x = 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.me.change_angle = 0
        elif symbol == arcade.key.A or symbol == arcade.key.D:
            self.me.change_x = 0

    def on_update(self, delta_time: float):
        if self.me.is_alive:
            self.me.rotate()
            self.me.move()
            for b in self.me.bullets:
                b.move()
                if b.center_x > SCREEN_WIDTH or b.center_x < 0 or b.center_y > SCREEN_HEIGHT or b.center_y < 0:
                    self.me.bullets.remove(b)

            for ex in self.explosions:
                ex.update_animation()
                if ex.time_to_die:
                    self.explosions.remove(ex)

            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            if  self.elapsed_time > self.rand_time:
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
                        e.explode()
                        self.explosions.append(Explosion(e))
                        self.enemies.remove(e)
                        self.me.bullets.remove(b)
                        self.me.increase_score()
                e.move()
                


if __name__ == '__main__':
    game = Game()
    arcade.run()

