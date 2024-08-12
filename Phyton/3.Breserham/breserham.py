def get_line(x0, y0, x1, y1):
    points = []  # Inicialización de la lista de puntos
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Determinar la dirección de movimiento
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    
    # Caso cuando la línea es más horizontal
    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            points.append((x0, y0))
            err -= dy
            if err < 0:
                y0 += sy
                err += dx
            x0 += sx
    # Caso cuando la línea es más vertical
    else:
        err = dy / 2.0
        while y0 != y1:
            points.append((x0, y0))
            err -= dx
            if err < 0:
                x0 += sx
                err += dy
            y0 += sy
    
    # Añadir el punto final
    points.append((x1, y1))
    return points


if __name__ == "__main__":
    x0 = 3
    y0 = 2
    x1 = 15
    y1 = 11
    points = get_line(x0, y0, x1, y1)
    print(points)
