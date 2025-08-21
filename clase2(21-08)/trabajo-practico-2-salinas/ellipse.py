def middle_point_ellipse(cx, cy, rx, ry):
    """
    Algoritmo de punto medio para dibujar elipses
    cx, cy: centro de la elipse
    rx: radio en x
    ry: radio en y
    """
    points = []
    
    # Región 1
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    p = ry2 - (rx2 * ry) + (0.25 * rx2)
    px = 0
    py = tworx2 * y
    
    # Región 1
    while px < py:
        # Agregar los 4 puntos simétricos
        points.extend([(cx + x, cy + y), (cx - x, cy + y), 
                      (cx + x, cy - y), (cx - x, cy - y)])
        
        x += 1
        px += twory2
        
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= tworx2
            p += ry2 + px - py
    
    # Región 2
    p = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2
    
    while y > 0:
        # Agregar los 4 puntos simétricos
        points.extend([(cx + x, cy + y), (cx - x, cy + y), 
                      (cx + x, cy - y), (cx - x, cy - y)])
        
        y -= 1
        py -= tworx2
        
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += twory2
            p += rx2 - py + px
    
    return points
