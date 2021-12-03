import math, numpy as np, matplotlib.pyplot as plt
from PIL import Image

# Convert image to numpy array
def img_2_arr(file):
    img = Image.open(file)
    np_img = np.array(img)
    return np_img

# Generate square grayscale image of numpy array
def img_gen_resize(file):

  plt.axis('off')
  
  dec_2d_matrix = img_2_arr(file)

  # reshape matrix into a square
  dec_1d_matrix = dec_2d_matrix.flatten()
  dim = math.ceil(math.sqrt(dec_1d_matrix.size))
  dec_2d_sqmatrix = np.zeros(dim**2, dtype=np.uint8)
  dec_2d_sqmatrix[:dec_1d_matrix.size] = dec_1d_matrix
  dec_2d_sqmatrix = dec_2d_sqmatrix.reshape(dim, dim)

  # generate and save image
  # this will result in images of uniform dimensions
  plt.imshow(dec_2d_sqmatrix, cmap='gray')
  plt.savefig("asdf.jpg", bbox_inches='tight', pad_inches=0)

img_gen_resize("1.jpg")
