import arcade
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.contador=0
        self.pos_x=0
        self.pos_y=0
    
    def on_draw(self):
        self.clear()
        if self.pos_x>800:
            self.pos_x=0
        self.pos_x+=1
        self.contador+=0.2
        self.pos_y=math.sin(self.contador)
        # Poner aquí el código del dibujo
        #casa
        #suelo
        arcade.draw_rect_filled(arcade.XYWH(000, 000, 1600, 350), arcade.color.ARSENIC)
        #lineas carreteras
        #1
        arcade.draw_rect_filled(arcade.XYWH(000, 80, 200, 25), arcade.color.WHITE)
        #2
        arcade.draw_rect_filled(arcade.XYWH(350, 80, 200, 25), arcade.color.WHITE)
        #3
        arcade.draw_rect_filled(arcade.XYWH(700, 80, 200, 25), arcade.color.WHITE)
        #amarillo pavimento
        arcade.draw_rect_filled(arcade.XYWH(000, 180, 1600, 15), arcade.color.AUREOLIN)
        #edificio
        arcade.draw_rect_filled(arcade.XYWH(000, 600, 1600, 350), arcade.color.ARSENIC)
        arcade.draw_rect_filled(arcade.XYWH(400, 613, 450, 850), arcade.color.BROWN)
        arcade.draw_rect_filled(arcade.XYWH(628, 613, 5, 850), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(178, 613, 5, 850), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(340, 263, 3, 150), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(460, 263, 3, 150), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(400, 337, 123, 3), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(460, 460, 3, 123), arcade.color.BLACK)#ventana
        arcade.draw_rect_filled(arcade.XYWH(340, 460, 3, 123), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(400, 520, 123, 3), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(400, 400, 123, 3), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(400, 460, 3, 123), arcade.color.BLACK) #fin ventana
        #farola 
        arcade.draw_rect_filled(arcade.XYWH(100, 313, 10, 250), arcade.color.BLACK)
        arcade.draw_circle_filled(100, 463, 30, arcade.color.CANARY_YELLOW)
        #pomo puerta
        arcade.draw_circle_filled(450, 260, 5, arcade.color.BLACK)
        def dibujar_coche(x: int, y: int, escala: float) -> None:
            arcade.draw_polygon_filled([[x+40*escala, y+150*escala], [x+80*escala, y+200*escala], [x+180*escala, y+200*escala], [x+230*escala, y+150*escala]], arcade.color.COFFEE)
            arcade.draw_rect_filled(arcade.XYWH(155+x*escala, 120+y*escala, 300*escala, 60*escala), arcade.color.COFFEE)
            arcade.draw_circle_filled(x+50*escala, y+90*escala, 30*escala, arcade.color.BLACK)#rueda trasera
            arcade.draw_circle_filled(x+50*escala, y+90*escala, 20*escala, arcade.color.WHITE)#rueda trasera parte arriba
            arcade.draw_circle_filled(x+230*escala, y+90*escala, 30*escala, arcade.color.BLACK)#rueda delantera
            arcade.draw_circle_filled(x+230*escala, y+90*escala, 20*escala, arcade.color.WHITE)#rueda delantera parte arriba
            arcade.draw_polygon_filled([[x+60*escala, y+150*escala], [x+90*escala, y+190*escala], [x+170*escala, y+190*escala], [x+210*escala, y+150*escala]], arcade.color.CELESTE) #ventana coche
            arcade.draw_polygon_outline([[x+60*escala, y+150*escala], [x+90*escala, y+190*escala], [x+170*escala, y+190*escala], [x+210*escala, y+150*escala]], arcade.color.BLACK, 2.5) #ventana coche delineado1
            arcade.draw_line(x+130*escala, y+150*escala, x+130*escala, y+190*escala, arcade.color.BLACK, 2.5) #ventana coche delineado2
        dibujar_coche(self.pos_x, self.pos_y, 1)

        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
