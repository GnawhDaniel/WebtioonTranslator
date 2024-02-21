import os
from PIL import Image, ImageOps

counter = 0
for file in os.listdir('/home/daniel/Screenshots/'):
    file = "/home/daniel/Screenshots/" + file
    im = Image.open(file)
    im = ImageOps.grayscale(im)
    
    # Remove 120 pixels from the top, 200 pixels from left and right
    im = im.crop((250, 120, im.width - 250, im.height))
    
    im.save(f'/home/daniel/Projects/Webtoon/dataset_raw/{counter}.png')
    counter += 1