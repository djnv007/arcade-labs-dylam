import arcade
arcade.open_window(800, 600, "dibujo1")
#fondo principal
arcade.set_background_color(arcade.color.GRAY_BLUE)
arcade.start_render()
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
#coche
arcade.draw_polygon_filled([[40, 150], [80, 200], [180, 200], [230, 150]], arcade.color.COFFEE)
arcade.draw_rect_filled(arcade.XYWH(155, 120, 300, 60), arcade.color.COFFEE)
arcade.draw_circle_filled(50, 90, 30, arcade.color.BLACK)#rueda trasera
arcade.draw_circle_filled(50, 90, 20, arcade.color.WHITE)#rueda trasera parte arriba
arcade.draw_circle_filled(230, 90, 30, arcade.color.BLACK)#rueda delantera
arcade.draw_circle_filled(230, 90, 20, arcade.color.WHITE)#rueda delantera parte arriba
arcade.draw_polygon_filled([[60, 150], [90, 190], [170, 190], [210, 150]], arcade.color.CELESTE) #ventana coche
arcade.draw_polygon_outline([[60, 150], [90, 190], [170, 190], [210, 150]], arcade.color.BLACK, 2.5) #ventana coche delineado1
arcade.draw_line(130, 150, 130, 190, arcade.color.BLACK, 2.5) #ventana coche delineado2


arcade.finish_render()
arcade.run()