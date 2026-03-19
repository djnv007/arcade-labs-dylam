""" Lab 7 - User Control """
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Paisaje:
    pass

class coche:
    def __init__(self, position_x, position_y,escala, change_x, change_y,MOVEMENT_SPEED = 3):
        self.position_x=position_x
        self.position_y=position_y
        self.escala=escala
        self.change_x=change_x
        self.change_y=change_y
        self.MOVEMENT_SPEED = MOVEMENT_SPEED
    def draw(self):
            arcade.draw_polygon_filled([[self.position_x+40*self.escala, self.position_y+150*self.escala], [self.position_x+80*self.escala, self.position_y+200*self.escala], [self.position_x+180*self.escala, self.position_y+200*self.escala], [self.position_x+230*self.escala, self.position_y+150*self.escala]], arcade.color.COFFEE)
            arcade.draw_rect_filled(arcade.XYWH(155+self.position_x*self.escala, 120+self.position_y*self.escala, 300*self.escala, 60*self.escala), arcade.color.COFFEE)
            arcade.draw_circle_filled(self.position_x+50*self.escala, self.position_y+90*self.escala, 30*self.escala, arcade.color.BLACK)#rueda trasera
            arcade.draw_circle_filled(self.position_x+50*self.escala, self.position_y+90*self.escala, 20*self.escala, arcade.color.WHITE)#rueda trasera parte arriba
            arcade.draw_circle_filled(self.position_x+230*self.escala, self.position_y+90*self.escala, 30*self.escala, arcade.color.BLACK)#rueda delantera
            arcade.draw_circle_filled(self.position_x+230*self.escala, self.position_y+90*self.escala, 20*self.escala, arcade.color.WHITE)#rueda delantera parte arriba
            arcade.draw_polygon_filled([[self.position_x+60*self.escala, self.position_y+150*self.escala], [self.position_x+90*self.escala, self.position_y+190*self.escala], [self.position_x+170*self.escala, self.position_y+190*self.escala], [self.position_x+210*self.escala, self.position_y+150*self.escala]], arcade.color.CELESTE) #ventana coche
            arcade.draw_polygon_outline([[self.position_x+60*self.escala, self.position_y+150*self.escala], [self.position_x+90*self.escala, self.position_y+190*self.escala], [self.position_x+170*self.escala, self.position_y+190*self.escala], [self.position_x+210*self.escala, self.position_y+150*self.escala]], arcade.color.BLACK, 2.5) #ventana coche delineado1
            arcade.draw_line(self.position_x+130*self.escala, self.position_y+150*self.escala, self.position_x+130*self.escala, self.position_y+190*self.escala, arcade.color.BLACK, 2.5) #ventana coche delineado2
    def on_update(self, delta_time):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.position_x += self.change_x
        self.position_y += self.change_y
        
        """if self.position_x> SCREEN_WIDTH:
            self.position_x = SCREEN_WIDTH 

        if self.position_y> SCREEN_HEIGHT:
            self.position_y = SCREEN_HEIGHT"""
class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.coche = coche(0, 0, 1,0,0)
        joysticks = arcade.get_joysticks()
         # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None
    def on_draw(self):
        self.clear()
        
        self.coche.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.coche.position_x = x-155
        self.coche.position_y = y-120
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.coche.change_x -= self.coche.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.coche.change_x += self.coche.MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.coche.change_y += self.coche.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.coche.change_y -= self.coche.MOVEMENT_SPEED
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.coche.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.coche.change_y = 0
    def on_update(self, delta_time):
        self.coche.on_update(delta_time)
        if self.joystick:
            self.coche.change_x = self.joystick.x * 5
            self.coche.change_y = -self.joystick.y * 5

def main():
    window = MyGame()
    arcade.run()


main()