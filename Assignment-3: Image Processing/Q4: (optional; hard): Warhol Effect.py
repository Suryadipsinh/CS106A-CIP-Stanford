"""
This program generates the Warhol effect based on the original image.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    fill_canvas(final_image, N_ROWS, N_COLS)
    final_image.show()

# gets 3 random numbers to represent rgb colors and
# passes them to make_recolored_patch
def recolor():
    red = get_random_num()
    green = get_random_num()
    blue = get_random_num()
    patch = make_recolored_patch(red, green, blue)
    return patch


# generates a random number between 0 and 2.0
def get_random_num():
    return random.uniform(0, 2.0)

def fill_canvas(canvas, n_rows, n_columns):
    start_y = 0
    for rows in range(n_rows):
        start_x = 0
        for cols in range(n_columns):
            patch = recolor()
            put_patch(canvas, start_x, start_y, patch)
            start_x += PATCH_SIZE
        start_y += PATCH_SIZE

def put_patch(final_image, start_x, start_y, patch):
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel((x + start_x), (y + start_y), pixel)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    """
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()
    
