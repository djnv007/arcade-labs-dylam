import arcade
import random
COIN_SCALE=0.50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#----------------------------------------
COIN_COUNT=50  
class Coin(arcade.Sprite):
    def __init__(self, position_x, position_y):
        self.center_x = position_x
        self.center_y = position_y
    def on_update(self):
        self.center_y -= 5

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
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
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
            coin.remove_from_sprite_lists()
            self.score += 1
    def on_mouse_motion(self,x,y,dx,dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    
def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()