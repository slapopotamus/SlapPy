
# 🎨 img2ASCII - Image 2 ASCII Converter

Welcome to **img2ASCII**, where we turn your everyday images into stunning works of ASCII art. Forget pixels, we’re talking characters! Let’s dive into how this magical transformation happens.

## 🎯 What Does It Do?

This Python script takes an image of your choice and converts it into ASCII art, using different characters to represent the intensity of pixels. Want to see your face made out of '@' and '#' signs? Look no further!

1. **Select an Image**: Provide the path to the image file you want to transform.
2. **Watch the Magic**: The script resizes the image, grayscales it, and maps each pixel to an ASCII character.
3. **Get ASCII Art**: Voilà! Your image is now a beautiful wall of characters.
4. **Save It**: The ASCII art is saved to a text file so you can cherish it forever (or for as long as you need).

## 🧩 How It Works

- **Resizing the Image**: To maintain the aspect ratio while converting the image to ASCII, the script resizes it to a manageable width (default 100 characters wide) while adjusting the height to account for the font's natural aspect ratio.
- **Grayifying the Image**: The image is converted to grayscale, making it easier to represent different pixel intensities with ASCII characters.
- **Pixel-to-ASCII Mapping**: Each pixel’s intensity is mapped to a corresponding character from a list, where darker pixels get heavier characters (like '@' and '#') and lighter pixels get lighter ones (like '.' and ',').

## 🚀 Quick Breakdown of the Code

- **`resize_image(image, new_width=100)`**: Resizes the image based on the width you want, while keeping the aspect ratio intact.
- **`grayify(image)`**: Converts the image to grayscale, because fancy colors are just too mainstream.
- **`pixels_to_ascii(image)`**: Turns each pixel into a corresponding ASCII character based on its brightness. The result is one big string of ASCII characters.
- **`main()`**: The brains of the operation. This function handles everything, from receiving your input to generating the ASCII masterpiece and saving it.

## 🏆 Example Output

Here's what a small portion of the output might look like:

***************************#S##S#@#SS####S####S#@###S###@@@@?***************************************
**************************?#S##S@##SS#S#S#####S##@######@@@@?***************************************
**************************?##@SS@###S#S#S#@SS#@###S#####@@@@%***************************************
**************************?#@@S###S#SS#S#SS######S#S###@@@@@%***************************************
***************************#@@S#######SSS%??%%%SSSS###@@@@@@%***************************************
***************************S##S#####S%%%S?**?**????%S#@@@@@#****************************************
***************************?@##S####%%SS%*??%?***??%%S#@#@@#?***************************************
*************************?%#@S####S##S##S%%%%%%%?*?%%SS@@@@@@##%************************************
**********************?%S@@@@#S@@#S#SS##SSSSSS%%?*?%SSS@@@@@@@@@#%**********************************
***************??%%%SS#@@@@@@@##@@##S##SS##SS%%%%SSSSS##@@@@@@@@@#S*********************************
********?%%S##@@@@@@@@@@@@@@@@S#S@@SSSSSSS#S%#######SS###@@@@@@@@@#S********************************
****?%##@@@@@@@@@@@@@@@@@@@@@@#S##@S###SSSS%?SS%%???%S##@@@@@@@@@@##********************************
?%S#@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@SS#SS%SS??%%?**??%S@@@@@@@@@@@@##********************************
@@@@###@@@#@@@@@#@@@@@@@@@@@@@@@@@@##S#SSS?**%%%?*?%S#@@@@@@@@@@@@##********************************
@@@@##@@@#@@@@@#@@@@@@@@@@@@@@@@@@@@#S#S%??%?%S%?*?S#@@@@@@@@@@@@@#@********************************
@@@@##@@@#@@@@@#@@@@@@@@@@@@@@@@@@@##S#S???SSS%?%??S#@@@@@@@@@@@@#@@?*******************************
@@@@##@@@@#@@@@@@@@@@@@@@@@@@@@@##@SS##S???%%%%%??%#S@@#@@@@@@@@@#@@@#%?****************************
@@@@@@#@@@@@@@#@@@@@@@@@@@@@@##@#@@S%S##%*?%%%%?%SSSS@@#@@@@@@@@#@@@@@@@##S%S#####SS%??*****??%%SSS#
@@@@@@@@@@@@@@#@@@@@@@@@@@@###@@#####SS##%?**?%##SSS####@@##@@@##@@@@@@@@@@@@@@@@@@@@@@#####@@@@@@@@
@@@@@@##@@@@@@#@@@@@@@@@@@@###@@######SS#@SS%S##SS######@@##@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@#@@@@@@@@@@@@@@@@#####@@######SSS##SS##SS#######@@###@##@@@@@@@@@@@#@@@@@@@@@@@@@@@@########
@@@@@@@@@#@@@@@@@@@@@@@@@#####@###S####SS#@S%##S########@@##@##@@@@@@###@@@##@@@####@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@##SS#####S####S#@SS@#SS#######@#S###@@@@@#@@@@@@@@###@@@@@@@@@@@#######@@@
@@@@@@@@@@#@@@@@@@@@@@@@@@@##SSS####S###S####@#S#####@@@#S###@##@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@
@@#@@@@@@@#@@@@@@@@@@@@@@@@@@##SS@######S###@####S##@@@#S##@@#@@####@@@@@@@@@@@@@@#@@@@@@@##@@@@@@@@
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##S@@@@###SS#####S#@@@@###@@@@@###@@@@@@@@@@@@@@@@@@@@@#######@@@@##@
@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@#S#@@@@##########@@@@@S#@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@####@@@@
@@@@@@@@@@@@@@@@@@@@@#@@@@##@@@@@#@@@@@@@#######@@@@@@@@@@@@@@@@@@@S?SS@@@@@@@@@@@@@@@@@@@@@@@@###@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@#####@@@###@@@@@@@@@@@@@@#%###@@@@@@@@@@@@@@@@@@@@@#@@@@###
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@###@@@#@@@@@@@@@@@@@@##@##@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@##

## 🎉 Why You’ll Love It

- Turn any image into **ASCII art** for your retro visual needs!
- It’s perfect for adding some artsy, nostalgic flair to your projects.
- It’s **fun, simple**, and saves the result to a text file for easy sharing.

---

Enjoy converting your images into masterpieces of ASCII art with img2ASCII!
