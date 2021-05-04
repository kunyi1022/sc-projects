"""
File: stanCodoshop.py
Name: 林坤毅 Jordan
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This program will help user find the best picture without moving body or object within several pictures.

"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_diff = pixel.red - red
    green_diff = pixel.green - green
    blue_diff = pixel.blue - blue
    color_dist = (red_diff**2 + green_diff**2 + blue_diff**2) ** (1/2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    rgb = []
    for i in range(len(pixels)):
        red = pixels[i].red
        green = pixels[i].green
        blue = pixels[i].blue
        total_red += red
        total_green += green
        total_blue += blue
    rgb.append(total_red//len(pixels))
    rgb.append(total_green//len(pixels))
    rgb.append(total_blue//len(pixels))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # Set maximum for comparison
    min_dis = float('inf')
    avg_red = get_average(pixels)[0]
    avg_green = get_average(pixels)[1]
    avg_blue = get_average(pixels)[2]
    # Check the difference between every pixel and average pixel
    for i in range(len(pixels)):
        dis = get_pixel_dist(pixels[i], avg_red, avg_green, avg_blue)
        if dis < min_dis:
            min_dis = dis
            pixel = pixels[i]
    return pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels = []
            for i in range(len(images)):
                img = images[i]
                img_pix = img.get_pixel(x, y)
                pixels.append(img_pix)
            final_pix = get_best_pixel(pixels)
            result_pix = result.get_pixel(x, y)
            result_pix.red = final_pix.red
            result_pix.green = final_pix.green
            result_pix.blue = final_pix.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
