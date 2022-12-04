# Dithering
Repo for housing dithering algorithms.

# Color Formatting
Expected image file for color formatting of dithering algorithm.
Expected format is:
r,g,b -> Color0
r,g,b -> Color1

So far has only been tested with 8 bit colors.

# Floyd Steinberg Dithering 
(fs_dither.py)
(https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering)

The Floyd Steinberg dithering algorithm is implemented and uses a nearest 
neighbor search to find the clostest color. The nearest neighbor is simply
a "3D" distance formula to the colors passed in.