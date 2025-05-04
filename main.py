import sys
from rembg import remove, new_session

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return

    input_path = sys.argv[1]
    output_path = "output.png"

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    session = new_session("isnet-general-use")

    result = remove(
        input_data,
        session=session,
        alpha_matting=False,
        only_mask=False,
        post_process_mask=False
    )

    with open(output_path, "wb") as output_file:
        output_file.write(result)

    print(f"Transparent background saved to {output_path}")

if __name__ == "__main__":
    main()
