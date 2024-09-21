import gradio as gr
from PIL import Image
import io

def text_to_bits(text):
    """Convert a string to a list of bits."""
    bits = []
    for char in text:
        binval = bin(ord(char))[2:].rjust(8, '0')
        bits.extend([int(b) for b in binval])
    return bits

def bits_to_text(bits):
    """Convert a list of bits to a string."""
    chars = []
    for b in range(0, len(bits), 8):
        byte = bits[b:b+8]
        if len(byte) < 8:
            break
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def encode_image(input_image_path, secret_message):
    """Encode a secret message into an image."""
    try:
        image = Image.open(input_image_path)
    except Exception as e:
        return None, f"Error opening image: {e}"

    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')
    
    width, height = image.size
    pixels = list(image.getdata())

    # Convert message to bits and add a delimiter
    message_bits = text_to_bits(secret_message)
    # Prefix the message with its length (32 bits)
    message_length = len(message_bits)
    length_bits = [int(b) for b in bin(message_length)[2:].rjust(32, '0')]
    bits = length_bits + message_bits

    if len(bits) > len(pixels) * 3:
        return None, "The image is too small to hold this message."

    new_pixels = []
    bit_idx = 0
    for pixel in pixels:
        r, g, b = pixel[:3]
        a = pixel[3] if len(pixel) == 4 else None

        if bit_idx < len(bits):
            r = (r & ~1) | bits[bit_idx]
            bit_idx += 1
        if bit_idx < len(bits):
            g = (g & ~1) | bits[bit_idx]
            bit_idx += 1
        if bit_idx < len(bits):
            b = (b & ~1) | bits[bit_idx]
            bit_idx += 1

        if a is not None:
            new_pixels.append((r, g, b, a))
        else:
            new_pixels.append((r, g, b))
    
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(new_pixels)

    # Save to a BytesIO object
    byte_io = io.BytesIO()
    encoded_image.save(byte_io, format='PNG')
    byte_io.seek(0)

    # To return a file path, save the BytesIO to a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(byte_io.read())
        temp_file_path = temp_file.name

    return temp_file_path, "Message encoded successfully!"

def decode_image(input_image_path):
    """Decode a secret message from an image."""
    try:
        image = Image.open(input_image_path)
    except Exception as e:
        return f"Error opening image: {e}"

    pixels = list(image.getdata())

    bits = []
    for pixel in pixels:
        r, g, b = pixel[:3]
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)

    # Extract message length first (32 bits)
    length_bits = bits[:32]
    message_length = int(''.join([str(bit) for bit in length_bits]), 2)
    
    if message_length == 0:
        return "No hidden message found."

    message_bits = bits[32:32 + message_length]
    message = bits_to_text(message_bits)
    return message

# Define Gradio interface components
def encode_interface(image_path, message):
    encoded_image_path, status = encode_image(image_path, message)
    if encoded_image_path:
        return encoded_image_path, status
    else:
        return None, status

def decode_interface(image_path):
    message = decode_image(image_path)
    return message

# Create Gradio Blocks
with gr.Blocks() as demo:
    gr.Markdown("# 🖼️ Steganography Tool with Gradio")
    gr.Markdown("Hide and retrieve secret messages within PNG images using Least Significant Bit (LSB) steganography.")
    
    with gr.Tab("Encode Message"):
        gr.Markdown("### Encode a Secret Message into an Image")
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(label="Input Image (PNG)", type="filepath")  # Changed to 'filepath'
                secret_message = gr.Textbox(label="Secret Message", placeholder="Enter your secret message here...")
                encode_button = gr.Button("Encode")
            with gr.Column():
                encoded_image = gr.Image(label="Encoded Image")
                encode_status = gr.Textbox(label="Status", interactive=False)
        
        encode_button.click(fn=encode_interface, inputs=[input_image, secret_message], outputs=[encoded_image, encode_status])
    
    with gr.Tab("Decode Message"):
        gr.Markdown("### Decode a Hidden Message from an Image")
        with gr.Row():
            with gr.Column():
                decode_image_input = gr.Image(label="Encoded Image (PNG)", type="filepath")  # Changed to 'filepath'
                decode_button = gr.Button("Decode")
            with gr.Column():
                decoded_message = gr.Textbox(label="Decoded Message", lines=4, interactive=False)
        
        decode_button.click(fn=decode_interface, inputs=decode_image_input, outputs=decoded_message)
    
    gr.Markdown("""
    ---
    **Notes:**
    - Ensure that the image you upload for encoding has enough capacity to hold your secret message.
    - Supported image formats: PNG.
    - The encoding process slightly modifies the image, which might introduce minimal changes invisible to the naked eye.
    """)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
