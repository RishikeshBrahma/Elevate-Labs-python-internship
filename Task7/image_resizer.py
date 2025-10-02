import os
from PIL import Image # type: ignore

# --- Configuration ---
# 1. Folder Paths
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'

# 2. Resizing Parameters
# The target size for the output images (width, height) in pixels.
TARGET_SIZE = (800, 600) 

# 3. Output Format and Quality
# Options: 'JPEG', 'PNG', 'WEBP', etc.
OUTPUT_FORMAT = 'JPEG' 
# Quality setting for JPEG (1-100). Ignored for other formats like PNG.
JPEG_QUALITY = 90

# --- End of Configuration ---


def resize_and_convert_images():
    """
    Finds all images in the INPUT_FOLDER, resizes them to TARGET_SIZE,
    converts them to the OUTPUT_FORMAT, and saves them in the OUTPUT_FOLDER.
    """
    # 1. Validate and Create Output Folder
    if not os.path.exists(OUTPUT_FOLDER):
        print(f"Output folder '{OUTPUT_FOLDER}' not found. Creating it...")
        os.makedirs(OUTPUT_FOLDER)
    
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: Input folder '{INPUT_FOLDER}' not found. Please create it and add images.")
        return

    print(f"Starting image processing...")
    print(f"Input folder: {os.path.abspath(INPUT_FOLDER)}")
    print(f"Output folder: {os.path.abspath(OUTPUT_FOLDER)}")
    print(f"Target size: {TARGET_SIZE[0]}x{TARGET_SIZE[1]} pixels")
    print("-" * 30)

    processed_count = 0
    skipped_count = 0
    
    # 2. Iterate Through Files in Input Folder
    for filename in os.listdir(INPUT_FOLDER):
        # Construct full file path
        input_path = os.path.join(INPUT_FOLDER, filename)

        # Skip directories and non-file items
        if not os.path.isfile(input_path):
            continue

        try:
            # 3. Open the Image
            with Image.open(input_path) as img:
                print(f"Processing '{filename}'...")

                # 4. Resize the Image
                # We use Image.Resampling.LANCZOS for high-quality downscaling.
                resized_img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

                # 5. Handle Image Format and File Extension
                # Get the base name of the file without its original extension
                base_name = os.path.splitext(filename)[0]
                output_extension = OUTPUT_FORMAT.lower()
                
                # Special case for 'jpeg' which should have 'jpg' extension
                if output_extension == 'jpeg':
                    output_extension = 'jpg'

                output_filename = f"{base_name}.{output_extension}"
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)

                # 6. Convert and Save the Image
                # If the output is JPEG, we need to handle transparency by converting to 'RGB' mode.
                if OUTPUT_FORMAT.upper() == 'JPEG':
                    # Convert images with transparency (RGBA) or palettes (P) to standard RGB
                    if resized_img.mode in ('RGBA', 'P'):
                        resized_img = resized_img.convert('RGB')
                    resized_img.save(output_path, OUTPUT_FORMAT, quality=JPEG_QUALITY)
                else:
                    resized_img.save(output_path, OUTPUT_FORMAT)
                
                processed_count += 1

        except (IOError, OSError) as e:
            # This will catch files that are not images or are corrupted
            print(f"Skipping '{filename}': Not a valid image or cannot be opened. Reason: {e}")
            skipped_count += 1
    
    print("-" * 30)
    print("Batch processing complete.")
    print(f"Successfully processed: {processed_count} images.")
    print(f"Skipped: {skipped_count} files.")


if __name__ == "__main__":
    resize_and_convert_images()