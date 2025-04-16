import sys
from rembg import remove, new_session
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

    # Use stable model with no alpha matting, no trimming
    session = new_session("isnet-general-use")  # More conservative

    result = remove(
        input_data,
        session=session,
        alpha_matting=False,
        only_mask=False,
        post_process_mask=False
    )

    # Composite onto white background
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, img)
    composite.save(output_path, format="PNG")

    print(f"Background removed. Result saved as {output_path}")

if __name__ == "__main__":
    main()
