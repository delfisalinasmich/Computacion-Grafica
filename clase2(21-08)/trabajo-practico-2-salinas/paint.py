import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import new_canvas, set_pixel, save_png
from bresenhamLine import bresenham_line
from middlePointCircle import middle_point_circle

WIDTH, HEIGHT = 400, 400 # Tamaño de canvas/ventana
COLOR = (255, 255, 255) # Color de figuras

canvas_data = new_canvas(WIDTH, HEIGHT, (0, 0, 0)) # Pista: usen la función de utils que crea un lienzo vacío

# Tkinter setup
root = tk.Tk()
root.title("Mini Paint Casero")

# Imagen con Pillow para usar en Tkinter 
img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0)) # Asigno un color de fondo de la ventana de dibujo, modo oscuro
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

# Estado
mode = tk.StringVar(value="linea")
points = [] # Variable global de puntos

# Copia el canvas lógico a la imagen Pillow y la refresca en Tkinter, para poder mantener la lógica de nuestros algoritmos.
def redraw_canvas():
    global photo, img
    # Flatten de los píxeles
    pixels = [pix for row in canvas_data for pix in row]
    img.putdata(pixels)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

# Maneja los clicks de los botones según el modo de dibujo (línea, círculo, etc.)
def on_click(event):
    global points # points es una matriz de puntos donde se hace click points[0] es el primer click points[1] es el segundo y así...
    points.append((event.x, event.y)) # Guarda las posiciones x, y que vienen en el event de click.

    # --- Dibujar Línea ---
    if mode.get() == "linea" and len(points) == 2: # Se necesitan 2 puntos.
        x0, y0 = points[0]
        x1, y1 = points[1]
        linea = bresenham_line(x0, y0, x1, y1)  # reemplazar por el algoritmo correcto
        for x, y in linea:
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas() # Siempre redibujo el canvas luego de agregar una figura.
        points = [] # Vacío points para poder dibujar la siguiente figura.

    # --- Dibujar Rectángulo ---
    elif mode.get() == "rect" and len(points) == 2: # Se necesitan 2 puntos.
        x0, y0 = points[0] # El primer click es un punto arriba a la izquierda.
        x1, y1 = points[1] # El segundo click es un punto abajo a la derecha.
        # Top side
        top_line = bresenham_line(x0, y0, x1, y0)
        for x, y in top_line:
            set_pixel(canvas_data, x, y, COLOR)
        # Right side
        right_line = bresenham_line(x1, y0, x1, y1)
        for x, y in right_line:
            set_pixel(canvas_data, x, y, COLOR)
        # Bottom side
        bottom_line = bresenham_line(x1, y1, x0, y1)
        for x, y in bottom_line:
            set_pixel(canvas_data, x, y, COLOR)
        # Left side
        left_line = bresenham_line(x0, y1, x0, y0)
        for x, y in left_line:
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas() # Siempre redibujo el canvas luego de agregar una figura.
        points = [] # Vacío points para poder dibujar la siguiente figura.

    # --- Dibujar Círculo ---
    elif mode.get() == "circle" and len(points) == 2: # Se necesitan 2 puntos.
        (cx, cy), (px, py) = points # El primer click es el centro del círculo.
        r = int(((px - cx) ** 2 + (py - cy) ** 2) ** 0.5) # Con el segundo click, se calcula el radio.
        circulo = middle_point_circle(cx, cy, r)  # Reemplazar por la función correcta
        for x, y in circulo:
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas() # Siempre redibujo el canvas luego de agregar una figura.
        points = [] # Vacío points para poder dibujar la siguiente figura.

    # --- Dibujar Triángulo ---
    elif mode.get() == "tri" and len(points) == 3: # 3 points needed for triangle
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        
        # First side: point 0 to point 1
        line1 = bresenham_line(x0, y0, x1, y1)
        for x, y in line1:
            set_pixel(canvas_data, x, y, COLOR)
            
        # Second side: point 1 to point 2
        line2 = bresenham_line(x1, y1, x2, y2)
        for x, y in line2:
            set_pixel(canvas_data, x, y, COLOR)
            
        # Third side: point 2 to point 0
        line3 = bresenham_line(x2, y2, x0, y0)
        for x, y in line3:
            set_pixel(canvas_data, x, y, COLOR)
            
        redraw_canvas() # Siempre redibujo el canvas luego de agregar una figura.
        points = [] # Vacío points para poder dibujar la siguiente figura.


def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if filename:
        save_png(filename, canvas_data)  # Acá reemplazar por la función que guarda el canvas en un archivo


# Creamos los botones con Tkinter en un recuadro distinto al canvas
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Línea", command=lambda: mode.set("linea")).pack(side=tk.LEFT)
tk.Button(frame, text="Rectángulo", command=lambda: mode.set("rect")).pack(side=tk.LEFT)
tk.Button(frame, text="Círculo", command=lambda: mode.set("circle")).pack(side=tk.LEFT)
tk.Button(frame, text="Triángulo", command=lambda: mode.set("tri")).pack(side=tk.LEFT)
tk.Button(frame, text="Guardar", command=save_image).pack(side=tk.LEFT)

# Me suscribo al evento click izquierdo en el canvas creado con Tkinter
label.bind("<Button-1>", on_click)

# Mostrar fondo con el color de fondo inicial
redraw_canvas()

# Ejecutamos Tkinter para iniciar el bucle de eventos de la ventana.
root.mainloop()
