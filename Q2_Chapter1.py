#Question 2: Chapter 1 - The Gatekeeper
#import libraries
import pandas as pd
import time
from PIL import Image
import numpy as np


# #algorithm generates a number (n) from question
current_time = int(time.time())
# print(current_time)
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
print("Result of generated number is:",generated_number)


#Change color of image with gerated_number
#Read image
img = Image.open("data/chapter1.jpg","r")
pixel = np.array(img)


#New pixels with generated_number
new_pixel = pixel + generated_number
#esure new pixels values are with in [0, 255]
new_pixel = np.clip(new_pixel, 0, 255)

#Create a new image and save as chapter1output.png
new_img = Image.fromarray(new_pixel.astype('uint8'))
new_img.save("data/chapter1out.png")

# Calculate the sum of all red pixel values
red_pixel_sum = np.sum(new_pixel[:, :, 0])
print(f"Sum of all red pixel values: {red_pixel_sum}")
