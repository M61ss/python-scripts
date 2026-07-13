import os
import sys

from PIL import Image
from PIL.ExifTags import TAGS

if len(sys.argv) != 2:
    print(f'usage: {os.path.basename(__file__)} <image_path>')
    exit(1)

img_path = sys.argv[1]

img = Image.open(img_path)

info_dict = {
    "Filename": img.filename,
    "Image Size": img.size,
    "Image Height": img.height,
    "Image Width": img.width,
    "Image Format": img.format,
    "Image Mode": img.mode,
    "Image is Animated": getattr(img, "is_animated", False),
    "Frames in Image": getattr(img, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25} : {value}")

exifdata = img.getexif()

for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25} : {data}")