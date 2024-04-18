from guage_display import DisplayScreen

import displayio
import bitmaptools
import busio
import adafruit_imageload
import time

displayScreen = DisplayScreen()
display = displayScreen.display
display.rotation = 180

background,background_pal = adafruit_imageload.load('round-display-ruler-720p.bmp')
draw_bitmap = displayio.Bitmap(background.width, background.height, len(background_pal))

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(background, pixel_shader=background_pal)

# Center the image
tile_grid.x -= (background.width - display.width) // 2
tile_grid.y -= (background.height - display.height) // 2

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.root_group = group

display.auto_refresh = True

# Loop forever so you can enjoy your image
while True:
    time.sleep(1.5)
    pass
