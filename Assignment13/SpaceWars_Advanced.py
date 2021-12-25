import math
import random
import arcade
import time
import threading

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ENEMY_HEIGHT = 40
ENEMY_WIDTH = 40
EXPLOSION_TEXTURES = []
for t in range(17):
    EXPLOSION_TEXTURES.append(arcade.load_texture('explosion/explosion-%s.png' %str(t+1)))
UPDATES_PER_FRAME = 3 # for animation frame rate
BULLET_TEXTURE = arcade.load_texture(':resources:images/space_shooter/laserRed01.png')
BOSS_BULLET_TEXTURE = arcade.load_texture(':resources:images/space_shooter/laserBLUE01.png')
SCORE_TO_REACH_BOSS = 10

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
        super().draw()

    def fire(self):
        self.bullets.append(Bullet(self))
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2)

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
        super().__init__()
        self.texture = BULLET_TEXTURE
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


class BossBullet(Bullet):
    def __init__(self,host):
        super().__init__(host)
        self.texture = BOSS_BULLET_TEXTURE
        self.speed = 10
        self.angle = self.angle + 90
    
    def move(self):
        rad = math.radians(self.angle - 90)
        self.center_x -= self.speed * math.sin(rad)
        self.center_y += self.speed * math.cos(rad)


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



class Boss(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = ENEMY_WIDTH * 2
        self.height = ENEMY_HEIGHT * 2
        self.angle = 180
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT + self.height//2 + 50
        self.change_x = 1
        self.speed = 4
        self.bullets = []
        self.bullet_interval = 30
        self.cur_bullet = 0
        self.health = 20
        self.max_health = 20
        self.is_awake = False

    def move(self): #TODO refine
        if self.center_y > SCREEN_HEIGHT - self.height//2 - 15:
            self.center_y -= 1
        else:
            self.center_x += self.change_x * self.speed
            if self.center_x - self.width // 2 < 0 or self.center_x + self.width // 2 > SCREEN_WIDTH:
                self.change_x = -self.change_x

    def fire(self):
        if not self.center_y > SCREEN_HEIGHT - self.height//2 - 15:
            self.cur_bullet += 1
            if self.cur_bullet == self.bullet_interval:
                self.bullets.append(BossBullet(self))
                arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser3.wav'), 0.2)
                self.cur_bullet = 0

    def decrease_health(self):
        self.health -= 1

    def draw_health_bar(self):
        health_width = (self.health/self.max_health) * (SCREEN_WIDTH - 100)
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT - 10, SCREEN_WIDTH - 100, 10, arcade.color.RED)
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT - 10, health_width, 8, arcade.color.GREEN)


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        


class Explosion(arcade.Sprite):
    def __init__(self, host):
        super().__init__()
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'))
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
        self.explosions = []
        self.boss = Boss()
        self.is_active = True # if the game is running. False if in 'win' or 'lose' situation
        self.kill_threads = False # attribute to help close all side threads before closing the game window
        self.ae_thread = threading.Thread(target=self.add_enemy) # "add_enemy" thread
        self.ae_thread.start()
        self.b_thread = threading.Thread(target=self.boss_method) # "boss" thread
        self.b_thread.start()
        self.e_thread = threading.Thread(target=self.enemy_method) # "enemy" thread
        self.e_thread.start()
        
        
    
    def close(self): #overridden
        self.kill_threads = True
        super().close()

    def restart(self):
        self.enemies.clear()
        self.e_speed = 3
        self.me = SpaceCraft()
        self.boss = Boss()
        self.explosions.clear()
        self.kill_threads = False

        
    def add_enemy(self):
        while not self.kill_threads:
            if self.is_active:
                self.e_speed += 0.2
                self.enemies.append(Enemy(self.e_speed))
                self.rand_time = random.randint(1 ,3)
                time.sleep(self.rand_time)
            else:
                time.sleep(1/60)

    def enemy_method(self):
        while not self.kill_threads:
            if self.is_active:
                for e in self.enemies:
                    if e.center_y < 0:
                        self.enemies.remove(e)
                        self.me.hearts.pop()
                        arcade.play_sound(arcade.sound.Sound(':resources:sounds/gameover5.wav'), 0.2)
                    for b in self.me.bullets:
                        if arcade.check_for_collision(e,b):
                            self.explosions.append(Explosion(e))
                            self.enemies.remove(e)
                            self.me.bullets.remove(b)
                            self.me.increase_score()
                    e.move()
            time.sleep(1/60) #because arcade's frame rate is 60 frames per second

    def boss_method(self):
        while not self.kill_threads:
            if self.boss.is_awake and self.is_active:
                self.boss.move()
                self.boss.fire()
                for bb in self.boss.bullets:
                    bb.move()
                    if bb.center_x > SCREEN_WIDTH or bb.center_x < 0 or bb.center_y > SCREEN_HEIGHT or bb.center_y < 0:
                        self.boss.bullets.remove(bb)
                    elif arcade.check_for_collision(self.me, bb):
                        self.boss.bullets.remove(bb)
                        self.me.hearts.pop()
                        self.explosions.append(Explosion(self.me))
                        arcade.play_sound(arcade.sound.Sound(':resources:sounds/gameover2.wav'), 0.2)
            time.sleep(1/60)

    def on_draw(self):
        if self.me.is_alive():
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH ,SCREEN_HEIGHT,self.background_image )
            self.me.draw()
            for enemy in self.enemies:
                enemy.draw()
            for b in self.me.bullets:
                b.draw()
            if self.boss.is_awake:
                for bb in self.boss.bullets:
                    bb.draw()
            for ex in self.explosions:
                ex.draw()
            if self.boss.is_awake:
                self.boss.draw()
                self.boss.draw_health_bar()
            
            arcade.draw_text(str(self.me.score), start_x= SCREEN_WIDTH-50 , start_y= 20 , font_size=25) 
            
            if not self.boss.is_alive():
                arcade.Window.clear(self)
                arcade.draw_text("YOU WON!", 50, SCREEN_HEIGHT//2, font_size=30)
                arcade.draw_text("Press R to restart the game.", 30, SCREEN_HEIGHT//2 - 150, font_size=30)
                self.enemies.clear()
                self.boss.is_awake = False

        else:
            arcade.Window.clear(self)
            arcade.draw_text("YOU LOST!", 50, SCREEN_HEIGHT//2, font_size=30)
            arcade.draw_text("Press R to restart the game.", 30, SCREEN_HEIGHT//2 - 150, font_size=30)
            self.enemies.clear()
            self.boss.is_awake = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            if self.is_active:
                self.me.fire()
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
        if self.me.is_alive() and self.boss.is_alive():
            self.is_active = True

            if not self.boss.is_awake:
                if self.me.score >= SCORE_TO_REACH_BOSS:
                    self.boss.is_awake = True
            
            self.me.rotate()
            self.me.move()
            
            for b in self.me.bullets:
                b.move()
                if b.center_x > SCREEN_WIDTH or b.center_x < 0 or b.center_y > SCREEN_HEIGHT or b.center_y < 0:
                    self.me.bullets.remove(b)
                if self.boss.is_awake:
                    if arcade.check_for_collision(b, self.boss):
                        self.me.bullets.remove(b)
                        self.explosions.append(Explosion(self.boss))
                        self.boss.decrease_health()

            for ex in self.explosions:
                ex.update_animation()
                if ex.time_to_die:
                    self.explosions.remove(ex)
        else:
            self.is_active = False

                


if __name__ == '__main__':
    game = Game()
    arcade.run()
    

