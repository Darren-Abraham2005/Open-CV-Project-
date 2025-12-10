## 🎨📸 Posterization of potraits using Open CV Python
This repo provides the code for posterizing the input images using the following libraries.
* **Open CV :** Provides essential functions and techniques for image processing 
* **matplotlib.pyplot :** Provides functions to display images in a plot and display orginal and modified images side by side and more
 * **numpy :** Helps to access array which are essential for the creation of tables

### ⚙️Behind the Code
This code is based on the logic which invovles first reading the image from the path and converting into rgb from bgr as Open CV by default uses bgr and applying median blur to the original image and using matplotlib for displaying the image side by side , original image and median blur image.<br>

Then a function is made for generating Lookup Table. Lookup Tables (LUTs) are one of the most fundamental and powerful tools in digital image processing, computer graphics, and video post-production. They allow for the incredibly fast and efficient application of complex color and tone transformations to images. The function.The function described performs Color Quantization, which is the process of reducing the total number of distinct colors in an image.<br>

Key Mechanism

* **Clustering:** The function analyzes the image colors and maps the original, wide range of colors into a smaller, fixed number of 'n' discrete color buckets (or clusters).

* **LUT Generation:** These 'n' representative colors are compiled into a Look-Up Table (LUT). This LUT acts as the definitive, reduced palette for the image
  
* **Visual Effect:** By mapping many similar original colors to a single color from the LUT, the process creates the characteristic flat areas of color and hard transitions required for a cartoonized or posterized visual style.<br>

cv2.LUT function is then applied which uses the LUT generated from the function and median blur applied to image as arguments which results in posterized image <br>


Finally using matplotlib the original image and posterized image are side by side




   
