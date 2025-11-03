import detector
import sys

if len(sys.argv) == 2:
    img_filename : str = sys.argv[1]
    metadata : dict[str] = detector.collect_metadata(img_filename)
    for key, value in metadata.items():
        print(f"{key}: {value}")
else:
    raise RuntimeError("Wrong number of parameter.")