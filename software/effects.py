import time

def color_wipe(pixels, color, wait=0.05):
    """Fill the strip with a color, one LED at a time."""
    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

def theater_chase(pixels, color, wait=0.05):
    """Create a moving theater chase effect."""
    for q in range(3):
        for i in range(0, len(pixels), 3):
            pixels[i+q] = color
        pixels.show()
        time.sleep(wait)
        for i in range(0, len(pixels), 3):
            pixels[i+q] = (0, 0, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos*3, 255 - pos*3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos*3, 0, pos*3)
    else:
        pos -= 170
        return (0, pos*3, 255 - pos*3)

def rainbow_cycle(pixels, wait=0.05, iterations=5):
    """Draw rainbow that cycles across all pixels."""
    for j in range(256*iterations):
        for i in range(len(pixels)):
            pixel_index = (i * 256 // len(pixels)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

