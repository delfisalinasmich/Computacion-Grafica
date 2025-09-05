#version 330

uniform float iTime;
uniform vec2 iResolution;
uniform vec4 iMouse;

out vec4 f_color;

#define PI 3.14159265359
#define N 360

vec3 hsv2rgb( in vec3 c ) {
    float frac = fract(c.x)*6.0;
    vec3 col = smoothstep(vec3(3,0,3),vec3(2,2,4),vec3(frac));
    col += smoothstep(vec3(4,3,4),vec3(6,4,6),vec3(frac)) * vec3(1, -1, -1);
    return mix(vec3(1), col, c.y) * c.z;
}

float sdCapsule( vec2 p, vec2 a, vec2 b, float r ) {
    vec2 pa = p - a, ba = b - a;
    float h = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 );
    return length( pa - ba*h ) - r;
}

float radius(float theta, float n) {
    theta += PI;
    return cos(PI/n)/cos(theta-2.0*PI/n*floor((n*theta+PI)/(2.0*PI)));
}

vec2 getPos(float n, float poly) {
    float theta = n / float(N) * 2.0 * PI;
    return vec2(cos(theta), sin(theta)) * radius(theta, poly);
}

void main() {
    vec2 uv = gl_FragCoord.xy / iResolution.xy * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;
    uv *= 0.55;
    uv.xy = uv.yx;
    
    f_color.rgb = vec3(0);
    f_color.a = 1.0;
    
    float poly = 3.0 + floor((iResolution.y-iMouse.y) * 0.05);
    
    float f = floor(iTime)*poly+1.0;
    if (iMouse.z > 0.0) f = floor(iMouse.x * 0.1);
    
    float top = radius(0.0, poly);
    float bot = -radius(PI, poly);
    float scale = top - bot;
    uv *= scale;
    uv.x += (top + bot) * 0.5;
    
    float acc = 0.0;
    
    float theta = atan(uv.y, uv.x);
    float dist = length(uv) - radius(theta, poly);
    if (dist > 0.0) {
        acc = 1.0;
    } else {
        for (int i = 0 ; i <= N ; i++) {
            float fi = float(i);
            vec2 a = getPos(fi, poly);
            vec2 b = getPos(fi*f, poly);
            float dist = sdCapsule(uv, a, b, 0.0);
            acc += exp(-dist*100.0);
        }

        acc *= 70.0;
        acc /= float(N);
        acc = mix(acc, 1.0, smoothstep(-0.05, 0.0, dist));
    }
    
    f_color.rgb = hsv2rgb( vec3( acc*4.0, 1.0-acc, 1.0-acc));
}
