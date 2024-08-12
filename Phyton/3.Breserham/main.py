import arcade
from breserham import get_line

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Dibujo de múltiples líneas con Bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()
        # Define un conjunto de líneas que quieres dibujar
        lines = [
            (3, 2, 15, 7, arcade.color.RED),
            (3, 10, 15, 10, arcade.color.GREEN),
            (3, 15, 15, 2, arcade.color.BLUE),
            (10, 3, 10, 15, arcade.color.YELLOW)
        ]

        # Dibuja la cuadrícula
        self.draw_grid()

        # Dibuja las líneas utilizando el algoritmo de Bresenham
        for line in lines:
            x0, y0, x1, y1, color = line
            points = get_line(x0, y0, x1, y1)
            self.draw_line_points(points, color)
            self.draw_scaled_line(x0, y0, x1, y1, color)

    def draw_grid(self):
        # Líneas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        # Líneas horizontales
        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                arcade.color.LIGHT_GRAY
            )

    def draw_line_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1, color):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            color,
            5
        )

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
