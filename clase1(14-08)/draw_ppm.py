def bresenham(x0, y0, x1, y1):
    """Dibuja una línea en el canvas usando el algoritmo de Bresenham."""
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        if x0 == x1 and y0 == y1:
            points.append((x0, y0))
            break
        points.append((x0, y0))
        err2 = err * 2
        if err2 > -dy:
            err -= dy
            x0 += sx
        if err2 < dx:
            err += dx
            y0 += sy        
    return points

def new_canvas(width, height, background=(0, 0, 0)):
    """Crea un canvas con colores RGB."""
    return [[background for _ in range(width)] for _ in range(height)]

def set_pixel_colores(canvas, x, y, color=(255, 255, 255)):
    """Pinta un pixel en el canvas con color RGB."""
    height = len(canvas)
    width = len(canvas[0])
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = color

def save_ppm_p3(canvas, filename):
    """Guarda el canvas como archivo PPM en formato P3."""
    height = len(canvas)
    width = len(canvas[0])

    with open(filename, 'w', encoding='ascii') as f:
        # Header PPM
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")

        # Datos de pixels
        for row in canvas:
            line = []
            for (r, g, b) in row:
                line.append(f"{r} {g} {b}")
            f.write(" ".join(line) + "\n")

def dibujar_linea(canvas, x0, y0, x1, y1, color=(255, 255, 255)):
    """Dibuja una línea en el canvas usando Bresenham."""
    linea = bresenham(x0, y0, x1, y1)
    for x, y in linea:
        set_pixel_colores(canvas, x, y, color)

# Crear canvas de 300x300 con fondo negro
canvas = new_canvas(300, 300, (0, 0, 0))

# Definir el centro y tamaño de la estrella
centro_x = 150
centro_y = 150

# Puntos de la estrella de 5 puntas (calculados manualmente)
# Punta superior
p1 = (centro_x, centro_y - 80)
# Punta superior derecha  
p2 = (centro_x + 76, centro_y - 25)
# Punta inferior derecha
p3 = (centro_x + 47, centro_y + 65)
# Punta inferior izquierda
p4 = (centro_x - 47, centro_y + 65)
# Punta superior izquierda
p5 = (centro_x - 76, centro_y - 25)

# Dibujar la estrella conectando las puntas en el orden correcto
# para formar el patrón de estrella de 5 puntas
color_estrella = (255, 215, 0)  # Dorado

# Conectar p1 -> p3 -> p5 -> p2 -> p4 -> p1
dibujar_linea(canvas, p1[0], p1[1], p3[0], p3[1], color_estrella)
dibujar_linea(canvas, p3[0], p3[1], p5[0], p5[1], color_estrella)
dibujar_linea(canvas, p5[0], p5[1], p2[0], p2[1], color_estrella)
dibujar_linea(canvas, p2[0], p2[1], p4[0], p4[1], color_estrella)
dibujar_linea(canvas, p4[0], p4[1], p1[0], p1[1], color_estrella)

# Agregar una segunda estrella más pequeña en rojo
centro2_x = 80
centro2_y = 80
radio_pequeno = 30

# Puntos de la estrella pequeña
p1_small = (centro2_x, centro2_y - radio_pequeno)
p2_small = (centro2_x + 29, centro2_y - 9)
p3_small = (centro2_x + 18, centro2_y + 24)
p4_small = (centro2_x - 18, centro2_y + 24)
p5_small = (centro2_x - 29, centro2_y - 9)

color_rojo = (255, 0, 0)

# Dibujar estrella pequeña
dibujar_linea(canvas, p1_small[0], p1_small[1], p3_small[0], p3_small[1], color_rojo)
dibujar_linea(canvas, p3_small[0], p3_small[1], p5_small[0], p5_small[1], color_rojo)
dibujar_linea(canvas, p5_small[0], p5_small[1], p2_small[0], p2_small[1], color_rojo)
dibujar_linea(canvas, p2_small[0], p2_small[1], p4_small[0], p4_small[1], color_rojo)
dibujar_linea(canvas, p4_small[0], p4_small[1], p1_small[0], p1_small[1], color_rojo)

# Agregar una tercera estrella en azul
centro3_x = 220
centro3_y = 220
radio_medio = 25

p1_blue = (centro3_x, centro3_y - radio_medio)
p2_blue = (centro3_x + 24, centro3_y - 8)
p3_blue = (centro3_x + 15, centro3_y + 20)
p4_blue = (centro3_x - 15, centro3_y + 20)
p5_blue = (centro3_x - 24, centro3_y - 8)

color_azul = (0, 100, 255)

# Dibujar tercera estrella
dibujar_linea(canvas, p1_blue[0], p1_blue[1], p3_blue[0], p3_blue[1], color_azul)
dibujar_linea(canvas, p3_blue[0], p3_blue[1], p5_blue[0], p5_blue[1], color_azul)
dibujar_linea(canvas, p5_blue[0], p5_blue[1], p2_blue[0], p2_blue[1], color_azul)
dibujar_linea(canvas, p2_blue[0], p2_blue[1], p4_blue[0], p4_blue[1], color_azul)
dibujar_linea(canvas, p4_blue[0], p4_blue[1], p1_blue[0], p1_blue[1], color_azul)

# Guardar como archivo PPM
save_ppm_p3(canvas, "estrella_simple.ppm")

print("¡Archivo 'estrella_simple.ppm' creado exitosamente!")
print("El dibujo contiene:")
print("- Una estrella grande dorada en el centro")
print("- Una estrella pequeña roja arriba a la izquierda") 
print("- Una estrella pequeña azul abajo a la derecha")
print("- Total: 15 líneas dibujadas usando Bresenham")
print("- Sin usar ninguna librería externa")