from PIL import Image

# Funcion para crear un canvas.
def new_canvas(width, height, backgroundColor = (0,0,0)):
    return [[backgroundColor for _ in range(width)] for _ in range(height)]        

# Funcion para pintar "pixeles" en el canvas.
def set_pixel(canvas, x, y, color=(255,255,255)):
    """color debe ser (r,g,b)"""
    h = len(canvas)
    w = len(canvas[0])
    if 0 <= x < w and 0 <= y < h:
        # fuerza a que cada componente sea int (por si viene como float)
        r, g, b = map(int, color)
        canvas[y][x] = (r, g, b)