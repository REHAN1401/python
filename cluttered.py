import os

# os.rename("sorted/file.txt", "sorted/newfile.txt")

files =os.listdir("sorted")
i = 0
for f in files:
    if f.endswith(".png"):
      os.rename(f"sorted/{f}", f"sorted/{i}.png")
      i = i + 1