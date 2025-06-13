#!/usr/bin/env python3
import os
from PIL import Image
import pillow_heif

# Folder with your .heic files
folder = 'path/to/folder/with/.heic files'

# Register HEIF support for Pillow
pillow_heif.register_heif_opener()

# Process each file in the folder
for filename in os.listdir(folder):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(folder, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(folder, jpg_filename)

        try:
            image = Image.open(heic_path)
            image.save(jpg_path, "JPEG")
            os.remove(heic_path)  # Delete original .heic file
            print(f"✅ Converted and deleted: {filename} → {jpg_filename}")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")

