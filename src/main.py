import cv2                                  #Importing libraries which are required
import matplotlib.pyplot as plt 
import numpy as np

path="OpenCV_project/assets/Musk.jpg"  #Reading the image from the specified path
img = cv2.imread(path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Converting BGR to RGB as OpenCV reads images in BGR format by default 
median = cv2.medianBlur(img_rgb, 1)              # and displaying the original image and the median blurred image using matplotlib     
fig, axes = plt.subplots(1, 2)                     
axes[0].imshow(img_rgb)
axes[0].set_title('Original')
axes[1].imshow(median) 
axes[1].set_title('Median Blur')
plt.tight_layout()
plt.show()


lut =np.zeros(256, dtype= 'uint8')              #Creating a lookup table to map the pixel values of the input image
n=5
def quantization_lut(n_levels: int) -> np.ndarray:
    bucket_size = 256 // n_levels
    lut = np.zeros(256, dtype=np.uint8)
    
    for i in range(256):
        bucket_index = i // bucket_size
        
        # Generic formula: Maps to the center of the bucket's range
        output_value = (bucket_index * bucket_size) + (bucket_size // 2)
        
        lut[i] = np.clip(output_value, 0, 255) 
    return lut


lut = quantization_lut(n)                        #Mapping input image pixel values accoridng to the lookup table using cv2.LUT function
posterized = cv2.LUT(median, lut)

plt.subplot(1,2,1)                           #Displaying the original and posterized images using matplotlib
plt.imshow(img_rgb)
plt.title('Original')
plt.subplot(1,2,2)
plt.imshow(posterized)
plt.title('Posterized')
plt.tight_layout()
plt.show()

cv2.imwrite("OpenCV_project/results/Cartoonized_Musk.jpg", cv2.cvtColor(posterized, cv2.COLOR_RGB2BGR))  #Saving the cartoonized image to the specified path
