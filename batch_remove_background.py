
import os
from bgRemover import remove_background

def batch_remove_background(input_folder, output_folder):
    """
    Remove the background of all images in a folder.

    Args:
        input_folder (str): Path to the folder with input images.
        output_folder (str): Path to the folder to save output images.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + "_no_bg.png")

        try:
            remove_background(input_path, output_path)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Example usage
batch_remove_background("input_images", "output_images")
