//entrada: del vbo (vertex buffer object)
#version 330 // OpenGL 3.3
in vec2 in_pos;
in vec3 in_color;

//ahora hacemos el out, depende de la info del vertex que necesitemos en el fragment
out vec3 v_color;

//proceso
void main (){
    v_color = in_color
}
