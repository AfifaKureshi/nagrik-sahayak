import sys
import os
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from image.image_pipeline import process_image


def pick_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    file_path = filedialog.askopenfilename(
        title="Select Civic Issue Image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.webp"),
            ("All files", "*.*")
        ]
    )
    return file_path


def load_image(path):
    image = Image.open(path).convert("RGB")
    return np.array(image)


if __name__ == "__main__":
    print("📂 Please select an image file...")

    image_path = pick_image_file()

    if not image_path:
        print("❌ No image selected. Exiting.")
        sys.exit(0)

    print("🖼️ Selected:", image_path)

    image_np = load_image(image_path)

    print("🔍 Analyzing image...")
    result = process_image(image_np)

    print("\n✅ Result:")
    print(result)
