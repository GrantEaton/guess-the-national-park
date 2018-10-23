import os
import subprocess

np_dirs = [x[0] for x in os.walk("../data/")]
for np in np_dirs:
    img_dirs = [x[2] for x in os.walk(np)]
    for img in img_dirs[0]:
        if ".DS_Store" not in img:

            # rename file
            ext = "." + img.split(".")[-1]
            bash_command = ['mv', np + "/" + img, np + "/" + str(hash(img)) + ext]
            process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, cwd="../data/")
