import imageio.v3 as iio
import numpy as np
import cv2
import os

def convert_tif_to_images(input_tif, output_folder):
    """
    Converts a multi-frame TIFF file into individual images while handling bit depth and normalization.

    Args:
        input_tif (str): Path to the input TIFF file.
        output_folder (str): Path to the output folder for saving images.

    Returns:
        None
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the multi-frame .tif file
    frames = iio.imread(input_tif, plugin="tifffile")  # Use tifffile plugin for multi-frame TIFFs

    for count, frame in enumerate(frames):
        try:
            # Normalize the frame based on its data type
            if frame.dtype == np.uint16:  # 16-bit image
                normalized_frame = cv2.normalize(frame, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            elif frame.dtype == np.float32:  # Floating-point image
                frame = np.clip(frame, 0, 1)  # Ensure values are in 0-1 range
                normalized_frame = (frame * 255).astype(np.uint8)  # Scale to 0-255
            else:  # Assume 8-bit image
                normalized_frame = frame.astype(np.uint8)

            # Save the frame as a JPEG image
            image_path = os.path.join(output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(image_path, normalized_frame)
            print(f"Saved frame {count} to {image_path}")

        except Exception as e:
            print(f"Error processing frame {count}: {e}")

# Provide the path to the input TIFF file and output folder
input_tif = r'./NRP1_n1a_beforeagonist010.tif'
output_folder = r'./NRP1_n1a_beforeagonist010'

print(f"Input TIFF: {input_tif}")
print(f"Output Folder: {output_folder}")

# Call the function to convert the TIFF to images
convert_tif_to_images(input_tif, output_folder)
