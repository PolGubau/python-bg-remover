from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    """
    Remove the background of an image and save the result.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the output image.
    """
    try:
        with open(input_path, "rb") as input_file:
            input_image = input_file.read()
            output_image = remove(input_image)

        # Convert the output binary data to an image and save it
        with open(output_path, "wb") as output_file:
            output_file.write(output_image)

        print(f"Background removed and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# # Example usage
# input_image = "example.jpg"  # Replace with your input image path
# output_image = "example_no_bg.png"  # Replace with your desired output path
# remove_background(input_image, output_image)
