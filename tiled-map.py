import arcade

TILE_SPRITE_SCALING = 1
PLAYER_SCALING = 1

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 768
WINDOW_TITLE = "Sprite Tiled Map with Levels Example"


# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 23
GRAVITY = 1.1


class GameView(arcade.View):
    """Main application class."""

    def __init__(self):
        
        super().__init__()
        self.tile_map = None
        self.camera = None
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.camera = arcade.Camera2D()
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            scale=PLAYER_SCALING,
        )

        self.player_sprite.center_x = 30
        self.player_sprite.center_y = 260
        self.player_list.append(self.player_sprite)

        self.tile_map = arcade.load_tilemap(
            "C:/Users/Dylam uah/OneDrive - Universidad de Alcala/PRIMERO/2ndo Cuatrimestre/TECNOLOGIA VIDEOJUEGOS/tilemap/lobito.tmj", scaling=TILE_SPRITE_SCALING
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.scene["suelo"], gravity_constant=GRAVITY
        )
        
    def on_draw(self):
      
        self.clear()
        self.scene.draw()
        self.player_list.draw()
        self.coordinates.draw()
        self.camera.use()
        

        

   

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.physics_engine.update()
        self.coordinates= arcade.Text(f"{self.player_sprite.position}",x=30,y=30, color=arcade.color.WHITE,font_size=14)
        self.camera.position =  WINDOW_WIDTH / 2+ self.player_sprite.center_x-64,  WINDOW_HEIGHT / 2

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
    def on_key_release(self, key,modifiers):
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 0
        elif key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = GameView()
    game.setup()

    window.show_view(game)
    window.run()


if __name__ == "__main__":
    main()