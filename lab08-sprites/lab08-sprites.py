import math
import arcade
import random
COIN_SCALE=0.50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#----------------------------------------
COIN_COUNT=20  
class Coin(arcade.Sprite):
    def __init__(self, filename, scale ):
        super().__init__(filename, scale)
    def reset_pos(self):
         self.center_x= random.randint(0, SCREEN_WIDTH-10)
         self.center_y=  SCREEN_HEIGHT
    def on_update(self):
        self.center_y-=3
        if self.top < 0:
            self.center_x= random.randint(0, SCREEN_WIDTH)
            self.center_y= SCREEN_HEIGHT
            

class MyGame(arcade.Window):
   
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        arcade.set_background_color(arcade.color.RED)
        self.player_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 1)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = 80
        self.player_list.append(self.player_sprite)
        for i in range (COIN_COUNT):
            coin=Coin(":resources:images/items/coinGold.png",COIN_SCALE)
            coin.center_x= random.randint(0, SCREEN_WIDTH-10)
            coin.center_y= random.randint(0, SCREEN_HEIGHT-10)
            self.coin_list.append(coin)
    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.coin_list.draw()
        arcade.draw_text(f"Score: {self.score}",50.0,50.0,arcade.color.WHITE, 20)
    def on_update(self, delta_time):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        for coin in hit_list:
            coin.reset_pos()
            self.score += 1
        for coin in self.coin_list:
            coin.on_update()
    def on_mouse_motion(self,x,y,dx,dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.center_y += 30
        elif key == arcade.key.S:
            self.player_sprite.center_y -= 30
        elif key == arcade.key.A:
            self.player_sprite.center_x -= 30
        elif key == arcade.key.D:
            self.player_sprite.center_x += 30

def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()