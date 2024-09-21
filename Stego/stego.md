
# 🖼️ Steganography Tool with Gradio

This project is a Python-based steganography tool that allows you to hide and retrieve secret messages within PNG images using Least Significant Bit (LSB) steganography. The project leverages `Gradio` to provide a simple user interface for encoding and decoding messages within images.

## Features
- **Encode Messages**: Hide a secret message inside a PNG image.
- **Decode Messages**: Extract a hidden message from a PNG image.
- **Gradio Interface**: Provides a user-friendly interface for performing both encoding and decoding tasks.

## Installation

To run this project, you need to install the required dependencies. You can install them using pip:

```bash
pip install -r requirements.txt
```

Make sure you include the following libraries in your `requirements.txt`:

```
gradio
Pillow
```

## How to Use

### Encode a Message
1. Select the "Encode Message" tab.
2. Upload a PNG image.
3. Enter your secret message.
4. Click the "Encode" button. The modified image will be generated with the hidden message.

### Decode a Message
1. Select the "Decode Message" tab.
2. Upload a PNG image containing a hidden message.
3. Click the "Decode" button. The hidden message will be displayed.

## Code Overview

- `text_to_bits(text)`: Converts a string into a list of bits.
- `bits_to_text(bits)`: Converts a list of bits back into a string.
- `encode_image(input_image_path, secret_message)`: Encodes the secret message into the image.
- `decode_image(input_image_path)`: Decodes and retrieves the secret message from the image.
- Gradio provides a clean UI for users to interact with these functions.

## Running the Application

To start the Gradio app, run the following command:

```bash
python stego.py
```

Once the server starts, you'll see a local URL where you can interact with the app through your browser.

## Notes
- Ensure that the image you upload for encoding has enough capacity to hold your secret message.
- Supported image formats: **PNG**.
- The encoding process may introduce minor, nearly invisible changes to the image.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
