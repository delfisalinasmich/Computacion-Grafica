# Decisiones de Implementación - Mini Paint Casero

## Resumen del Proyecto
Este documento explica las decisiones tomadas para completar el Trabajo Práctico 2 - Mini Paint Casero, un programa de dibujo que implementa figuras geométricas básicas usando algoritmos de rasterización.

## Arquitectura del Sistema

### Estructura de Archivos
- **`utils.py`**: Funciones de utilidad para manejo del canvas (new_canvas, set_pixel, save_png)
- **`bresenhamLine.py`**: Implementación del algoritmo de Bresenham para líneas
- **`middlePointCircle.py`**: Implementación del algoritmo de punto medio para círculos
- **`paint.py`**: Archivo principal con la interfaz gráfica y lógica de dibujo

### Decisiones de Diseño

#### 1. Canvas Lógico vs Visual
**Decisión**: Mantener un canvas lógico separado (`canvas_data`) de la representación visual de Tkinter.
**Razón**: Permite usar los algoritmos de rasterización desarrollados en clase mientras se mantiene compatibilidad con la interfaz gráfica de Tkinter.

#### 2. Sistema de Puntos Globales
**Decisión**: Usar una lista global `points` para almacenar clicks del usuario.
**Razón**: Simplifica el manejo de estado entre clicks múltiples requeridos para cada figura (2 para línea/rectángulo/círculo, 3 para triángulo).

#### 3. Algoritmos Utilizados

##### Líneas (Bresenham)
- **Uso**: Líneas directas, lados de rectángulos y triángulos
- **Implementación**: Llamada directa a `bresenham_line(x0, y0, x1, y1)`
- **Razón**: Algoritmo eficiente que evita operaciones de punto flotante

##### Círculos (Punto Medio)
- **Uso**: Dibujo de círculos completos
- **Implementación**: Cálculo de radio usando distancia euclidiana, luego `middle_point_circle(cx, cy, r)`
- **Razón**: Aprovecha la simetría del círculo para mayor eficiencia

#### 4. Implementaciones Específicas

##### Rectángulo
**Decisión**: Dibujar como 4 líneas separadas (top, right, bottom, left).
**Implementación**:
\`\`\`python
top_line = bresenham_line(x0, y0, x1, y0)
right_line = bresenham_line(x1, y0, x1, y1)
bottom_line = bresenham_line(x1, y1, x0, y1)
left_line = bresenham_line(x0, y1, x0, y0)
\`\`\`
**Razón**: Reutiliza el algoritmo de línea existente, garantiza consistencia visual.

##### Círculo
**Decisión**: Primer click = centro, segundo click = punto en la circunferencia.
**Cálculo de radio**: `r = int(((px - cx) ** 2 + (py - cy) ** 2) ** 0.5)`
**Razón**: Interfaz intuitiva que permite control visual del tamaño.

##### Triángulo
**Decisión**: Requiere 3 clicks, dibuja 3 líneas conectando los vértices.
**Implementación**: Tres llamadas a `bresenham_line` conectando puntos consecutivos y cerrando el triángulo.
**Razón**: Flexibilidad para crear triángulos de cualquier forma.

#### 5. Manejo de Estado
**Decisión**: Vaciar `points = []` después de completar cada figura.
**Razón**: Evita interferencia entre figuras consecutivas y permite dibujo continuo.

#### 6. Actualización Visual
**Decisión**: Llamar `redraw_canvas()` después de cada figura completada.
**Razón**: Sincroniza el canvas lógico con la representación visual de Tkinter.

## Resultados
El programa implementa exitosamente todas las funcionalidades requeridas:
- ✅ Dibujo de líneas con algoritmo de Bresenham
- ✅ Dibujo de rectángulos usando 4 líneas
- ✅ Dibujo de círculos con algoritmo de punto medio
- ✅ Dibujo de triángulos con 3 líneas
- ✅ Guardado de imágenes en formato PNG
- ✅ Interfaz gráfica funcional con Tkinter
