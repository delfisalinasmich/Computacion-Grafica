#version 330

// recibimos lo que viene del vertex
in vec3 v_color;

// salida del fragment a renderizar
out vec4 f_color; // (r, g, b, alpha) los colores

void main(){
    f_color = vec4(v_color, 1.0); //agrego una coordenada mas para el alpha, porque el vertice no tiene trasnparencia
}

