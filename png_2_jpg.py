import os 
from PIL import Image

os.chdir("1o")

for f in os.listdir():
    if not f.endswith(".jpg"):
        img = Image.open(f)
        img.save("../1/" + os.path.splitext(os.path.basename(f))[0] + ".jpg")


