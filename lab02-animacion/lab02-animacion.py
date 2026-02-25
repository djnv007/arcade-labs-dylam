import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    
    def on_draw(self):
        self.clear()
        # Poner aquí el código del dibujo
        arcade.draw_polygon_filled([[40, 150], [80, 200], [180, 200], [230, 150]], arcade.color.COFFEE)
        arcade.draw_rect_filled(arcade.XYWH(155, 120, 300, 60), arcade.color.COFFEE)
        arcade.draw_circle_filled(50, 90, 30, arcade.color.BLACK)#rueda trasera
        arcade.draw_circle_filled(50, 90, 20, arcade.color.WHITE)#rueda trasera parte arriba
        arcade.draw_circle_filled(230, 90, 30, arcade.color.BLACK)#rueda delantera
        arcade.draw_circle_filled(230, 90, 20, arcade.color.WHITE)#rueda delantera parte arriba
        arcade.draw_polygon_filled([[60, 150], [90, 190], [170, 190], [210, 150]], arcade.color.CELESTE) #ventana coche
        arcade.draw_polygon_outline([[60, 150], [90, 190], [170, 190], [210, 150]], arcade.color.BLACK, 2.5) #ventana coche delineado1
        arcade.draw_line(130, 150, 130, 190, arcade.color.BLACK, 2.5) #ventana coche delineado2
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
