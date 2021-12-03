import os

os.chdir("0")

jpg_count = 0
for f in os.listdir():
    if f.endswith(".jpg"):
        jpg_count += 1

print(jpg_count)


os.chdir("../1")

jpg_count = 0
for f in os.listdir():
    if f.endswith(".jpg"):
        jpg_count += 1

print(jpg_count)
