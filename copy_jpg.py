import os, shutil

os.chdir("1o")

src = os.getcwd()
dest = "../1"

for f in os.listdir():
    if f.endswith(".jpg"):
        src_path = os.path.join(src, f)
        dest_path = os.path.join(dest, f)
        shutil.copyfile(src_path, dest_path)