def draw_circle (centerX, centerY, radio):
    points = []
    x = 0
    y = -radio
    while x < -y:
        points.append ((centerX + x , centerY + y))
        x += 1
    return points