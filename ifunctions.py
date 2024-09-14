from PIL import Image, ImageOps
from PIL import ImageEnhance


if __name__=="__main__":
    
    im = Image.open("data/3.jpg")
    print(im.format, im.size, im.mode)
    
    # Invert the image
    inverted_image = ImageOps.invert(im.convert("RGB"))
    
    
    # Create an ImageEnhance object for brightness
    enhancer = ImageEnhance.Brightness(im)

    # Adjust brightness. Factor > 1.0 increases brightness, Factor < 1.0 decreases brightness
    brightness_factor = 0.8  # Example to increase brightness by 50%
    brightened_image = enhancer.enhance(brightness_factor)
    
    
    
    #brightened_image.show()
    #img_invert(img)
    
    # Save image
    brightened_image.save("C:\\Users\\sebas\\OneDrive\\Pictures\\Wallpapers\\brightened_image.jpg")