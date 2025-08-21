from utils import new_canvas, save_png, set_pixel

def draw_circle (centerX, centerY, radio):
    points = []
    x = 0
    y = -radio
    yMid = y + 0.5
    decisionPoint = -radio
    while x < -y: #recorro desde 0 hasta el radio
        if decisionPoint > 0:
            y += 1
            decisionPoint += 2 * (x + y) + 1
        else:
            decisionPoint += 2 * x + 1
        points.append((centerX + x, centerY + y))
        points.append((centerX + y, centerY + x))
        points.append((centerX - x, centerY + y))
        points.append((centerX - y, centerY + x))
        points.append((centerX + x, centerY - y))
        points.append((centerX + y, centerY - x))
        points.append((centerX - x, centerY - y))
        points.append((centerX - y, centerY - x))
        x += 1
    return points
height = 256
width = 256
canvas = new_canvas(width, height)
circle = draw_circle(width // 2, height // 2, 20)
for x,y in circle:
    set_pixel(canvas, x, y)
save_png("seraUnCirculo", canvas)