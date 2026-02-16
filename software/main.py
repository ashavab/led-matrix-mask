import time
import board
import neopixel
from effects import rainbow_cycle, color_wipe, theater_chase

# ----------------------------
# Configuration
# ----------------------------
LED_PIN = board.D5        # Pin connected to the LED strip
NUM_LEDS = 60             # Number of LEDs in your mask
BRIGHTNESS = 0.5          # Brightness: 0.0 - 1.0

pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# ----------------------------
# Main Loop
# ----------------------------
try:
    while True:
        # Rainbow animation
        rainbow_cycle(pixels, wait=0.05)
        # Color wipe animation
        color_wipe(pixels, (255, 0, 0), wait=0.05)
        color_wipe(pixels, (0, 255, 0), wait=0.05)
        color_wipe(pixels, (0, 0, 255), wait=0.05)
        # Theater chase animation
        theater_chase(pixels, (255, 255, 255), wait=0.05)

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
    print("Exiting gracefully")

