import shutil, random, os, glob


# Count
print("Class count")

os.chdir("plankton_images/0")
negative_count = len(os.listdir())

os.chdir("../1")
postive_count = len(os.listdir())

print("Negative count: ", negative_count)
print("Positive count: ", postive_count)


# Balance number of examples for classess

os.chdir("../0")

src = os.getcwd()
dest = "../0r"

#       First clear destination directory
for file in os.scandir(dest):
    os.remove(file.path)

files = random.sample(os.listdir(src), postive_count)
for f in files:
    src_path = os.path.join(src, f)
    dest_path = os.path.join(dest, f)
    shutil.copyfile(src_path, dest_path)


# Count
print("New class count")

os.chdir("../0r")
negative_count = len(os.listdir())

os.chdir("../1")
postive_count = len(os.listdir())

print("Negative count: ", negative_count)
print("Positive count: ", postive_count)