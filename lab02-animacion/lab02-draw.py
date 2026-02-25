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
arcade.draw_rect_filled(arcade.XYWH(400, 613, 450, 850), arcade.color.BURNT_UMBER)
arcade.finish_render()
arcade.run()