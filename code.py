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
tile_grid = displayio.TileGrid(draw_bitmap, pixel_shader=background_pal)

# Center the image
tile_grid.x -= (background.width - display.width) // 2
tile_grid.y -= (background.height - display.height) // 2

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.root_group = group

angle = 0
center_x = int(background.width/2)
center_y = int(background.height/2)
# Loop forever so you can enjoy your image
while True:
    bitmaptools.rotozoom(draw_bitmap, background, angle=angle, ox=center_x, oy=center_x,
        px=center_x, py=center_y, source_clip0=(0,0), source_clip1=(background.width,background.height))

    display.refresh()
    angle += 0.5
    pass
