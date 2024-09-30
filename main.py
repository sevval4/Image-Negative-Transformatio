import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img_path = "./images/mamogram.jpg"
r = cv2.imread(img_path, 0)

# Print the shape of the image
print(r.shape)

# Maximum pixel value in the image (255 for an 8-bit grayscale image)
print(np.max(r))
L = np.max(r)

# Apply negative transformation
s = L - r  # transformation function for negative image

# Stack the original and negative images horizontally and vertically
hStack = np.hstack((r, s))  # horizontally
vStack = np.vstack((r, s))  # vertically

# Display the images
plt.imshow(hStack, cmap="gray")
plt.imshow(vStack, cmap="gray")
plt.show()
