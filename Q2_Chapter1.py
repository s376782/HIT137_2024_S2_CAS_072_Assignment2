#Question 2: Chapter 1 - The Gatekeeper
#import libraries
import time
from PIL import Image
import numpy as np


# #algorithm generates a number (n) from question
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
print("Result of generated number is:",generated_number)

#function to change color of image with gerated_number
#Read image
def change_color_image(input_image, output_image):
    
    img = Image.open(input_image, "r")
    pixel = np.array(img)

    #New pixels with generated_number
    new_pixel = pixel + generated_number
    
    #esure new pixels values are with in [0, 255]
    new_pixel = np.clip(new_pixel, 0, 255)

    #Create a new image and save as chapter1output.png
    new_img = Image.fromarray(new_pixel.astype("uint8"))
    new_img.save(output_image)

    # Calculate the sum of all red pixel values
    red_pixel_sum = np.sum(new_pixel[:, :, 0])
    print(f"Sum of all red pixel values: {red_pixel_sum}")

input_image = "data/chapter1.jpg"
output_image = "data/chapter1out.png"
change_color_image(input_image, output_image)
