#version 330

in vec3 in_position;
in vec3 in_color;

uniform mat4 model;
uniform mat4 projection;  // Added missing semicolon

out vec3 v_color;

void main() {
    gl_Position = projection * model * vec4(in_position, 1.0);
    v_color = in_color;
}
