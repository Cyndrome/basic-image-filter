"""
Image Filter application

Allows the user to upload an image and apply a filter to it. Offers a variety of filters to choose from. 
Also allows the user to apply a custom filter by multiplying each of the RGB values of each pixel by their 
desired number.
""" 

DEFAULT_FILE = '/images/lil_josh.png' 

from simpleimage import SimpleImage

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show filter choices
    print ("Which filter would you like to apply? The options are: ")
    print("Grayscale\nRed channel\nGreen channel\nBlue channel\nCustom filter")
    filter_choice = input("\nEnter your choice: ")
    
    # Apply the filter
    if filter_choice == "Custom filter":
        image.show() # Show the image before the transform
        image = custom_filter(image) # Apply the filter
        image.show() # Show the image after the transform
    
    if filter_choice == "Grayscale":
        image.show() # Show the image before the transform
        image = grayscale(image) # Apply the filter
        image.show() # Show the image after the transform

    if filter_choice == "Red channel":
        image.show() # Show the image before the transform
        image = red_channel(image) # Apply the filter
        image.show() # Show the image after the transform

    if filter_choice == "Green channel":
        image.show() # Show the image before the transform
        image = green_channel(image) # Apply the filter
        image.show() # Show the image after the transform

    if filter_choice == "Blue channel":
        image.show() # Show the image before the transform
        image = blue_channel(image) # Apply the filter
        image.show() # Show the image after the transform

def custom_filter(image):
    """
    Allows the user to modify the image by multiplying each of the RGB values of each pixel by their input number. 
    """
    red_constant = float(input ("Multiply the R value of each pixel by: "))
    green_constant = float(input ("Multiply the G value of each pixel by: "))
    blue_constant = float(input ("Multiply the B value of each pixel by: "))

    for pixel in image:
        pixel.red *= red_constant
        pixel.green *= green_constant
        pixel.blue *= blue_constant
    return image

def compute_luminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula to weight red, green, and blue values appropriately.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(image):
    """
    Change the image to be grayscale using the NTSC luminosity formula and return it.
    """
    for pixel in image:
        luminosity = compute_luminosity (pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return image

def red_channel(image): 
    """
    Changes the image as follows:
    For every pixel, set green and blue values to 0, yielding the red channel.
    Return the changed image.
    """
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image

def green_channel(image): 
    """
    Changes the image as follows:
    For every pixel, set red and blue values to 0, yielding the green channel.
    Return the changed image.
    """
    for pixel in image:
        pixel.red = 0
        pixel.blue = 0
    return image

def blue_channel(image): 
    """
    Changes the image as follows:
    For every pixel, set red and green values to 0, yielding the blue channel.
    Return the changed image.
    """

    for pixel in image:
        pixel.red = 0
        pixel.green = 0
    return image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
