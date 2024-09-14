# Image manipilation library 
from PIL import Image
# Access to the files
import os 
from random import randrange

# Define texture sizes 
SIZE_X=SIZE_Y = 64

# Define images folder
textures_folder = os.path.join("data", "textures")

# Create random textures
for i in range(6):
    '''
    Generates 6 random textures representing mock 
    PBR textures of an asset
    '''
    # Generate random color
    c_a = randrange(0, 256)
    c_b = randrange(0, 256)
    c_g = randrange(0, 256)
    
    # Generate a new image with random color
    im = Image.new("RGB", [SIZE_X, SIZE_Y], (c_a, c_g, c_b))
    
    # Generate texutre filename
    if (i == 0):
        filename = "basecolor.jpg"
    if (i == 1):
        filename = "normal.jpg"
    if (i == 2):
        filename = "metallic.jpg"
    if (i == 3):
        filename = "roughness.jpg"
    if (i == 4):
        filename = "ao.jpg"
    if (i == 5):
        filename = "emission.jpg"
    
    # Generate filepath 
    filepath = os.path.join(textures_folder, filename)
    
    # Save image to the textures directory
    im.save(filepath)

# Read textures from disk
textures_list = os.listdir(textures_folder)

# Calculate number of columns based on image number 
col = 3
row = int((len(textures_list) / col))

# Determine the size of images ?
texture_size = Image.open(textures_list[0]).size[0])

# Create blank image 
atlas = Image.new("RGB", (texture_size * col, texture_size * row))

# Paste each image into the atlas 
for index, texture in enumerate(textures_list):
    t = Image.open(os.path.join(textures_folder, texture))
    x_offset = (index % col) * texture_size
    y_offset = (index // col) * texture_size
    atlas.paste(t, (x_offset, y_offset))

# Save the atlas 
atlas.save('texture_atlas.png')



