import sys
from rembg import remove

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return

    input_path = sys.argv[1]
    output_path = "output.png"

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    result = remove(
        input_data,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=10
    )

    with open(output_path, "wb") as output_file:
        output_file.write(result)

    print(f"Background removed. Result saved as {output_path}")

if __name__ == "__main__":
    main()
