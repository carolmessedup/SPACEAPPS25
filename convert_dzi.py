import os
import pyvips

# Add libvips to PATH (Windows)
os.environ["PATH"] = r"C:\libvips\vips-dev-8.17\bin;" + os.environ["PATH"]

# Path to your TIFF
tiff_file = r"D:\Carol\Personal\NASA_spaceapps_2025\imagedata\opo0328a.tif"

# Load the TIFF (random access for tiled/compressed TIFFs)
image = pyvips.Image.new_from_file(tiff_file, access="random")

# Output prefix for DZI
dzi_output = r"D:\Carol\Personal\NASA_spaceapps_2025\opo0328a_dzi"

# Deep Zoom parameters
tile_size = 512
overlap = 2
suffix = ".jpg"

# Calculate number of tiles in X and Y
tiles_x = (image.width + tile_size - 1) // tile_size
tiles_y = (image.height + tile_size - 1) // tile_size

print(f"Image size: {image.width} x {image.height}")
print(f"Number of tiles: {tiles_x} x {tiles_y} = {tiles_x * tiles_y} total")

print("Starting Deep Zoom generation... (this may take a while)")

# Generate Deep Zoom tiles
image.dzsave(
    dzi_output,
    suffix=suffix,
    overlap=overlap,
    tile_size=tile_size
)

print("Deep Zoom generation complete!")
print("Deep Zoom descriptor (.dzi):", dzi_output + ".dzi")
print("Deep Zoom tiles folder:", dzi_output + "_files/")
