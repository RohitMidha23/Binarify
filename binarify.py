from PIL import Image
import urllib
import sys
import argparse


"""
@author : Rohit Midha <rohitmidha23.github.io>
"""

binary = ['0','1']

def get_args():
    parser = argparse.ArgumentParser("Image to Binary")
    parser.add_argument("-input", type = str, default = "input.jpg", help="Path to Input image")
    parser.add_argument("-output", type = str, default = "output.txt", help="Path to Output text file")
    parser.add_argument("-width", type = int, default = 100, help="Output Width")
    parser.add_argument("-mode", type = str, default="white", choices=["black", "white"], help="Predominant Color")
    args = parser.parse_args()
    return args

def resize(image,new_width=100):
    width,height = image.size
    aspect_ratio = float(height/width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width,new_height))
    return new_image

def conv_pixels(image):
    initial_pixels = list(image.getdata())
    new_pixels = [binary[pixel_value%2] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def make_binary(image):
    new_width = opt.width
    image = resize(image,new_width)
    image = image.convert('L')

    new_pixels = conv_pixels(image)
    len_pixels = len(new_pixels)

    new_image = [new_pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def binarify(path):
    try:
        image = Image.open(path)
    except Exception:
        print("Image not found at path!")
        return

    image = make_binary(image)
    print(image)

    output_path = opt.output
    with open(output_path,'w') as f:
        f.write(image)

opt = get_args()

if(opt.mode == "white"):
    binary = binary[::-1]
image_path = opt.input
binarify(image_path)
