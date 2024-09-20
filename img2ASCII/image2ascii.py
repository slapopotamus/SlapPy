from PIL import Image

# ASCII characters in order of intensity
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    """
    Resizes an image while maintaining aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust for font aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    """
    Converts an image to grayscale.
    """
    return image.convert("L")

def pixels_to_ascii(image):
    """
    Maps each pixel to an ASCII character based on intensity.
    """
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def main():
    # Get image path from user
    path = input("Enter the path to an image file:\n")
    try:
        image = Image.open(path)
    except Exception as e:
        print("Could not open image. Error:", e)
        return

    # Process image
    new_width = 100
    image = resize_image(image, new_width)
    image = grayify(image)

    # Convert to ASCII
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string into lines
    ascii_lines = [
        ascii_str[index: index + new_width]
        for index in range(0, len(ascii_str), new_width)
    ]
    ascii_image = "\n".join(ascii_lines)

    # Output
    print("\nGenerated ASCII Art:\n")
    print(ascii_image)

    # Save to file
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_image)
    print("\nASCII art written to 'ascii_art.txt'.")

if __name__ == "__main__":
    main()
