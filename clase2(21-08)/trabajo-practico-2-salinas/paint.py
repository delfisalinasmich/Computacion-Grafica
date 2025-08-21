import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import new_canvas, set_pixel, save_png
from bresenhamLine import bresenham_line
from middlePointCircle import middle_point_circle
from ellipse import middle_point_ellipse  # Importar algoritmo de elipse

WIDTH, HEIGHT = 400, 400
COLOR = (255, 255, 255)  # Ahora será variable según el color seleccionado

canvas_data = new_canvas(WIDTH, HEIGHT, (0, 0, 0))

# Tkinter setup
root = tk.Tk()
root.title("Mini Paint Casero")

# Imagen con Pillow para usar en Tkinter 
img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

# Estado
mode = tk.StringVar(value="linea")
current_color = tk.StringVar(value="white")
points = []

def get_current_color():
    color_map = {
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "eraser": (0, 0, 0)  # Negro para borrar
    }
    return color_map.get(current_color.get(), (255, 255, 255))

def redraw_canvas():
    global photo, img
    # Flatten de los píxeles
    pixels = [pix for row in canvas_data for pix in row]
    img.putdata(pixels)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

def on_click(event):
    global points
    points.append((event.x, event.y))
    
    color = get_current_color()

    # --- Dibujar Línea ---
    if mode.get() == "linea" and len(points) == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        linea = bresenham_line(x0, y0, x1, y1)
        for x, y in linea:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        redraw_canvas()
        points = []

    # --- Dibujar Rectángulo ---
    elif mode.get() == "rect" and len(points) == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        # Top side
        top_line = bresenham_line(x0, y0, x1, y0)
        for x, y in top_line:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        # Right side
        right_line = bresenham_line(x1, y0, x1, y1)
        for x, y in right_line:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        # Bottom side
        bottom_line = bresenham_line(x1, y1, x0, y1)
        for x, y in bottom_line:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        # Left side
        left_line = bresenham_line(x0, y1, x0, y0)
        for x, y in left_line:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        redraw_canvas()
        points = []

    # --- Dibujar Círculo ---
    elif mode.get() == "circle" and len(points) == 2:
        (cx, cy), (px, py) = points
        r = int(((px - cx) ** 2 + (py - cy) ** 2) ** 0.5)
        circulo = middle_point_circle(cx, cy, r)
        for x, y in circulo:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
        redraw_canvas()
        points = []

    # --- Dibujar Triángulo ---
    elif mode.get() == "tri" and len(points) == 3:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        
        # First side: point 0 to point 1
        line1 = bresenham_line(x0, y0, x1, y1)
        for x, y in line1:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
            
        # Second side: point 1 to point 2
        line2 = bresenham_line(x1, y1, x2, y2)
        for x, y in line2:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
            
        # Third side: point 2 to point 0
        line3 = bresenham_line(x2, y2, x0, y0)
        for x, y in line3:
            set_pixel(canvas_data, x, y, color)  # Usar color dinámico
            
        redraw_canvas()
        points = []

    elif mode.get() == "ellipse" and len(points) == 2:
        (cx, cy), (px, py) = points
        rx = abs(px - cx)  # Radio en x
        ry = abs(py - cy)  # Radio en y
        elipse = middle_point_ellipse(cx, cy, rx, ry)
        for x, y in elipse:
            set_pixel(canvas_data, x, y, color)
        redraw_canvas()
        points = []

    elif mode.get() == "eraser":
        x, y = points[-1]  # Último punto clickeado
        # Borrar en un área de 7x7 píxeles para hacer más fácil el borrado
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                set_pixel(canvas_data, x + dx, y + dy, (0, 0, 0))  # Negro para borrar
        redraw_canvas()
        # No vaciar points para permitir borrado continuo

tools_frame = tk.Frame(root)
tools_frame.pack()

tk.Button(tools_frame, text="Línea", command=lambda: mode.set("linea")).pack(side=tk.LEFT)
tk.Button(tools_frame, text="Rectángulo", command=lambda: mode.set("rect")).pack(side=tk.LEFT)
tk.Button(tools_frame, text="Círculo", command=lambda: mode.set("circle")).pack(side=tk.LEFT)
tk.Button(tools_frame, text="Triángulo", command=lambda: mode.set("tri")).pack(side=tk.LEFT)
tk.Button(tools_frame, text="Elipse", command=lambda: mode.set("ellipse")).pack(side=tk.LEFT)  # Botón de elipse
tk.Button(tools_frame, text="Borrador", command=lambda: mode.set("eraser")).pack(side=tk.LEFT)  # Botón de borrador

colors_frame = tk.Frame(root)
colors_frame.pack()

tk.Label(colors_frame, text="Colores:").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Blanco", variable=current_color, value="white", bg="white").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Rojo", variable=current_color, value="red", bg="red", fg="white").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Verde", variable=current_color, value="green", bg="green", fg="white").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Azul", variable=current_color, value="blue", bg="blue", fg="white").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Amarillo", variable=current_color, value="yellow", bg="yellow").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Cian", variable=current_color, value="cyan", bg="cyan").pack(side=tk.LEFT)
tk.Radiobutton(colors_frame, text="Magenta", variable=current_color, value="magenta", bg="magenta", fg="white").pack(side=tk.LEFT)

save_frame = tk.Frame(root)
save_frame.pack()

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        save_png(canvas_data, file_path)

tk.Button(save_frame, text="Guardar", command=save_image).pack()

# Me suscribo al evento click izquierdo en el canvas creado con Tkinter
label.bind("<Button-1>", on_click)

# Mostrar fondo con el color de fondo inicial
redraw_canvas()

# Ejecutamos Tkinter para iniciar el bucle de eventos de la ventana.
root.mainloop()
