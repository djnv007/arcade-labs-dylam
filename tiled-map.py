import math
import arcade
import os
from pathlib import Path
TILE_SPRITE_SCALING = 1
PLAYER_SCALING = 1

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 768
WINDOW_TITLE = "Sprite Tiled Map with Levels Example"


# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 23
GRAVITY = 1.1
BASE_DIR = Path(__file__).resolve().parent
MAP_FILE= BASE_DIR / "assets" / "niveles" / "tilemap" / "lobito.tmj"

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
        

        layer_options = {
            "suelo": {
                "use_spatial_hash": True,
                }
        }

        self.tile_map = arcade.load_tilemap(
            "D:/nivel-prueba/nivel-prueba.tmj", scaling=TILE_SPRITE_SCALING,layer_options=layer_options)
        

        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.scene["suelo"], gravity_constant=GRAVITY
        )
        print(f"DEBUG: Las capas disponibles son: {self.tile_map.object_lists.keys()}")
        print(f"DEBUG: Las capas disponibles son: {self.tile_map.sprite_lists.keys()}")
        self.enemies_layer = self.tile_map.object_lists["Enemies"]
        enemies_layer = self.tile_map.object_lists["Enemies"]
        for enemy_marker in enemies_layer:
            coordinates = self.tile_map.get_cartesian(
                enemy_marker.shape[0], enemy_marker.shape[1]
            )
            enemy_type = enemy_marker.properties["type"]
            if enemy_type == "zombie":
                enemy= arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png")
            enemy.center_x = math.floor(
                coordinates[0] * 1 * self.tile_map.tile_width
            )
            enemy.center_y = math.floor(
                (coordinates[1] + 1) * (self.tile_map.tile_height * 1)
            )
            if "boundary_left" in enemy_marker.properties:
                enemy.boundary_left = enemy_marker.properties["boundary_left"]
            if "boundary_right" in enemy_marker.properties:
                enemy.boundary_right = enemy_marker.properties["boundary_right"]
            if "change_x" in enemy_marker.properties:
                enemy.change_x = enemy_marker.properties["change_x"]

            self.scene.add_sprite("Enemies", enemy)
            
            
            
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