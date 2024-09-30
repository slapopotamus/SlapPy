import pygame
from pygame.locals import *
import moderngl
import numpy as np
from pyrr import Matrix44
import sys
import os
import time
import aubio

# Initialize Pygame and create a window
pygame.init()

# Initialize Pygame mixer with specific parameters
try:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    print("Pygame mixer initialized successfully.")
except pygame.error as e:
    print(f"Failed to initialize Pygame mixer: {e}")
    sys.exit(1)

width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Python Demo - Rotating Triangle with Audio Sync")

# Get the directory where demo.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to music.wav
music_path = os.path.join(base_dir, 'assets', 'music.wav')

# Load and play the music with error handling
try:
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    print(f"Playing music: {music_path}")
except pygame.error as e:
    print(f"Cannot play the file: {music_path}")
    print(f"Pygame Error: {e}")
    sys.exit(1)

# Create ModernGL context
ctx = moderngl.create_context()

# Compile shaders with error checking
shader_dir = os.path.join(base_dir, 'shaders')
vertex_shader_path = os.path.join(shader_dir, 'vertex_shader.glsl')
fragment_shader_path = os.path.join(shader_dir, 'fragment_shader.glsl')

try:
    with open(vertex_shader_path) as f:
        vertex_shader = f.read()
    with open(fragment_shader_path) as f:
        fragment_shader = f.read()
    prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
    print("Shaders compiled successfully.")
except IOError as e:
    print(f"Shader file not found: {e}")
    sys.exit(1)
except moderngl.Error as e:
    print("Shader compilation failed:", e)
    sys.exit(1)

# Define triangle vertices with positions and colors
vertices = np.array([
    # Positions        # Colors
     0.0,  0.5, 0.0,   1.0, 0.0, 0.0,  # Top vertex (Red)
     0.5, -0.5, 0.0,   0.0, 1.0, 0.0,  # Bottom right vertex (Green)
    -0.5, -0.5, 0.0,   0.0, 0.0, 1.0,  # Bottom left vertex (Blue)
], dtype='f4')

# Create Vertex Buffer Object (VBO)
vbo = ctx.buffer(vertices.tobytes())

# Define the layout of the VBO
vao = ctx.vertex_array(prog, [
    (vbo, '3f 3f', 'in_position', 'in_color')
])

# Set up projection matrix (Orthographic)
projection = Matrix44.orthogonal_projection(-1, 1, -1, 1, -1, 1)
prog['projection'].write(projection.astype('f4').tobytes())

# Enable blending
ctx.enable(moderngl.BLEND)
ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Initialize Aubio for beat detection
win_s = 1024
hop_s = win_s // 2
samplerate = 44100  # Ensure it matches your audio file
try:
    s = aubio.source(music_path, samplerate, hop_s)
    t = aubio.tempo("default", win_s, hop_s, samplerate)
    t.set_threshold(0.5)  # Adjust threshold as needed
    print("Aubio tempo detection initialized.")
except Exception as e:
    print(f"Error initializing Aubio: {e}")
    sys.exit(1)

# Function to detect beats
def detect_beats():
    try:
        samples, read = s()
        is_beat = t(samples)
        if is_beat:
            return True
        return False
    except Exception as e:
        print(f"Error during beat detection: {e}")
        return False

# Main loop
running = True
angle = 0.0
start_time = time.time()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Detect beats
    if detect_beats():
        # Change triangle color on beat
        new_colors = np.random.rand(3, 3).astype('f4')
        vertices = np.array([
            # Positions        # Colors
             0.0,  0.5, 0.0,   new_colors[0][0], new_colors[0][1], new_colors[0][2],
             0.5, -0.5, 0.0,   new_colors[1][0], new_colors[1][1], new_colors[1][2],
            -0.5, -0.5, 0.0,   new_colors[2][0], new_colors[2][1], new_colors[2][2],
        ], dtype='f4')
        vbo.write(vertices.tobytes())
        print("Beat detected! Colors changed.")

    # Calculate rotation angle
    elapsed_time = time.time() - start_time
    angle = elapsed_time * np.radians(90)  # Rotate 90 degrees per second

    # Create model matrix (rotation)
    model = Matrix44.from_z_rotation(angle)
    prog['model'].write(model.astype('f4').tobytes())

    # Clear the screen
    ctx.clear(0.1, 0.1, 0.1)  # Dark gray background

    # Render the triangle
    vao.render()

    # Swap buffers
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
