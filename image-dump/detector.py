import exif
import sys

def collect_metadata(img_filename: str):
    img : exif.Image = exif.Image(img_filename)
    return img.get_all()


if len(sys.argv) == 2:
    img_filename: str = sys.argv[1]
    metadata: dict[str] = collect_metadata(img_filename)
    for key, value in metadata.items():
        print(f"{key}: {value}")
else:
    raise RuntimeError("Wrong number of parameter.")