# Image Metadata Dumper

A lightweight command-line tool that extracts and prints image metadata directly to the shell. Works reliably with JPEG images.

## Features

- Fast, dependency-light metadata extraction
- Human-readable output straight in the terminal
- Simple, single-purpose script — no bloat

## Requirements

- Python 3.9+
- pip

## Installation

Clone the repository and set up a virtual environment:

```shell
git clone https://github.com/M61ss/python-scripts.git
cd python-scripts/image-dump
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the script and pass the path to the image as an argument:

```shell
python3 metadata-dump.py <image_path>
```

### Example

```shell
python3 metadata-dump.py sample.jpg
```

```text
Filename                  : sample.jpg
Image Size                : (1920, 1080)
Image Height               : 1080
Image Width                : 1920
Image Format              : JPEG
Image Mode                : RGB
Image is Animated         : False
Frames in Image           : 1
Make                      : Canon
Model                     : EOS 80D
DateTime                  : 2024:05:12 14:32:10
```

*(actual fields depend on the metadata embedded in your image; not all images contain EXIF data)*

## Supported Formats

- JPEG (fully supported, including EXIF metadata)
- Other formats supported by Pillow will show basic image info, but may lack EXIF data

## License

[MIT](../LICENSE)