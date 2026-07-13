import exif

def collect_metadata(img_filename : str):
    img : exif.Image = exif.Image(img_filename)
    return img.get_all()