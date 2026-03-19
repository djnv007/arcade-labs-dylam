import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_WALL = 0.5
MOVEMENT_SPEED=7
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        self.player_sprite = None
        self.wall_list = None
        self.player_list = None
        self.physics_engine = None
        
    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.score=0
        self.player_list = arcade.SpriteList()
        self.wall_list=arcade.SpriteList()
        self.player_sprite= arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 96
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING_WALL)
        wall.center_x = 32
        wall.center_y =32
        self.wall_list.append(wall)
        wall_list=[[32,32],[32,96],[32,160],[32,224],[32,288],[32,352],[32,416],[32,480],[32,544],
                   [96,32],[160,32],[224,32],[288,32],[352,32],[416,32],[480,32],[544,32],[608,32],[672,32],[736,32],[800,32],
                   [0,568],[64,568],[128,568],[192,568],[256,568],[320,568],[384,568],[448,568],[512,568],[576,568],[640,568],[704,568],[768,568],
                   [160,96],[160,160],[160,224],[160,288],[160,352]
                   ,[224,352],[288,352],[352,352],[352,288]]
        for wall in wall_list:
            wall_sprite = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_WALL)
            wall_sprite.center_x = wall[0]
            wall_sprite.center_y = wall[1]
            self.wall_list.append(wall_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.wall_list.draw()
    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.player_sprite.center_x > SCREEN_WIDTH - 16:
            self.player_sprite.center_x = SCREEN_WIDTH - 16
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()