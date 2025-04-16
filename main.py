import sys
from rembg import remove
from PIL import Image
import io

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return

    input_path = sys.argv[1]
    output_path = "output.png"

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    result = remove(input_data)

    # Open the result in memory as an image
    img = Image.open(io.BytesIO(result)).convert("RGBA")

    # Create a white background image
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, img)

    # Save as PNG (can also convert to RGB and save as JPG if needed)
    composite.save(output_path, format="PNG")

    print(f"Background removed. Result saved as {output_path}")

if __name__ == "__main__":
    main()
