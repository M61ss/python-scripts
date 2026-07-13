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