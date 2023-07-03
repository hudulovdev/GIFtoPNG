from PIL import Image

def convert_gif_to_images(gif_path, output_path):
    # Open the GIF file
    gif = Image.open(gif_path)

    # Iterate over each frame and save it as a separate image
    for i in range(gif.n_frames):
        gif.seek(i)
        frame = gif.copy()
        frame.save(f"{output_path}/frame_{i}.png")

    print("GIF conversion complete.")

# Provide the path to the GIF file and the output directory
gif_path = "path_to_gif_file.gif"
output_path = "output_directory"

# Convert the GIF to multiple images
convert_gif_to_images(gif_path, output_path)
