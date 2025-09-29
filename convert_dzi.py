import os
import pyvips

# Add libvips to PATH (Windows)
os.environ["PATH"] = r"C:\libvips\vips-dev-8.17\bin;" + os.environ["PATH"]

# Path to your TIFF
tiff_file = r"D:\Carol\Personal\NASA_spaceapps_2025\imagedata\heic1502a.tif"

# Load the TIFF (sequential access to save memory)
image = pyvips.Image.new_from_file(tiff_file, access="sequential")

# Output prefix for DZI
dzi_output = r"D:\Carol\Personal\NASA_spaceapps_2025\heic1502a_dzi"

# Generate Deep Zoom tilesimport os
import pyvips

# Add libvips to PATH (Windows)
os.environ["PATH"] = r"C:\libvips\vips-dev-8.17\bin;" + os.environ["PATH"]

# Path to your TIFF
tiff_file = r"D:\Carol\Personal\NASA_spaceapps_2025\imagedata\heic1502a.tif"

# Load the TIFF (sequential access to save memory)
image = pyvips.Image.new_from_file(tiff_file, access="sequential")

# Output prefix for DZI
dzi_output = r"D:\Carol\Personal\NASA_spaceapps_2025\heic1502a_dzi"

# Deep Zoom parameters
tile_size = 512
overlap = 2
suffix = ".jpg"

# Calculate number of tiles in X and Y
tiles_x = (image.width + tile_size - 1) // tile_size
tiles_y = (image.height + tile_size - 1) // tile_size

print(f"Image size: {image.width} x {image.height}")
print(f"Number of tiles: {tiles_x} x {tiles_y} = {tiles_x * tiles_y} total")

# Generate Deep Zoom tiles in "levels"
# This uses dzsave, but we print a message first
print("Starting Deep Zoom generation... (this may take a while)")

image.dzsave(
    dzi_output,
    suffix=suffix,
    overlap=overlap,
    tile_size=tile_size
)

print("Deep Zoom generation complete!")
print("Deep Zoom descriptor (.dzi):", dzi_output + ".dzi")
print("Deep Zoom tiles folder:", dzi_output + "_files/")

image.dzsave(
    dzi_output,    # prefix for .dzi file and tiles folder
    suffix=".jpg", # tile format
    overlap=2,     # overlap between tiles
    tile_size=512  # size of each tile
)

print("Deep Zoom tiles created at:")
print(dzi_output + ".dzi")
print(dzi_output + "_files/")