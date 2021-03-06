import math
import random
import time
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, w, h,speed):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.speed = speed
        self.center_x = random.randint(0 , w)
        self.center_y = h
        self.angle = 180
        self.width = 48
        self.height = 48
        
    def move(self):
       
        self.center_y -= self.speed 
        
class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png") 
        self.speed = 8
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.bullet_sound = arcade.load_sound(":resources:sounds/lose2.wav")
    
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 48
        self.height = 48
        self.center_x = w // 2
        self.center_y =48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 4
        self.jon = 3
        self.score = 0
        self.bullet_sound = arcade.load_sound(":resources:sounds/lose2.wav")

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(self.bullet_sound)
        
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(width=self.w,height=self.h,title="Silver_SpaceCraft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image=arcade.load_texture("sayare.jpg")
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list =[]
        self.start_time = time.time()
        self.score = 0
        self.num_enemy = 0
        self.me.jon_image = arcade.load_texture('R.jpg')
        self.speed = 1
    def on_draw(self):
        arcade.start_render()

        if self.me.jon <= 0:
            arcade.set_background_color(arcade.color.BLACK) 
            arcade.draw_text("GAME OVER !", start_x = self.w //2,start_y = self.h //2,color = arcade.color.RED)
            time.sleep(1)
            return
        arcade.draw_lrwh_rectangle_textured(0, 0,self.w,self.h, self.background_image)
        self.me.draw()   

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(self.me.jon):

            arcade.draw_lrwh_rectangle_textured(i*40 ,5 ,40 ,40 ,self.me.jon_image)
        arcade.draw_text(f"score: {self.score}", 700, 10, arcade.color.WHITE, 14)
    
    def on_update(self, delta_time):

        self.end_time = time.time()
        r = random.randrange(2,6,2)
        if self.end_time - self.start_time > r :

          self.enemy_list.append(Enemy(self.w, self.h,self.speed))
          self.start_time = time.time()
        #self.enemy.move()
        self.num_enemy =+ 1
        self.me.rotate()
    
        for i in range(len(self.me.bullet_list)):
           self.me.bullet_list[i].move()


        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()


        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy,bullet):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1

        for enemy in self.enemy_list:
            if enemy.center_y <= 0:
                    self.me.jon -= 1
                    print(self.me.jon.imag)
                    self.enemy_list.remove(enemy)
            
             

        self.speed += 0.005
    def on_key_press(self, key, modifires):
        if key ==arcade.key.RIGHT:
            self.me.change_angle = -1
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
        elif key == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, key, modifiers):
       self.me.change_angle = 0
    
game=Game()
arcade.run()






#def main():
 #   """ Main function """
  #  window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
 #   window.setup()
 #   arcade.run()


#if __name__ == "__main__":
 #   main()