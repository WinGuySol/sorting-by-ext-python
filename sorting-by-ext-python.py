import os
import shutil
from os import listdir
from os.path import isfile, join

USERPROFILE = os.environ['USERPROFILE']
DOWNLOADS = os.listdir(f"{USERPROFILE}\\Downloads\\")

cwd = f"{USERPROFILE}\\Downloads\\"
f = []
ext_table = []

onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if
os.path.isfile(os.path.join(cwd, f))]


for i in onlyfiles:
    file_name, file_extension = os.path.splitext(i)
    f.append([file_name,file_extension])

for i in range(len(f)):
    if f[i][1] not in ext_table:
        ext_table.append(f[i][1])

        if not os.path.exists(f"{cwd}\\{ext_table[-1]}"):
            os.makedirs(f"{cwd}\\{ext_table[-1]}")
            # print(f"{cwd}\\{ext_table[-1]}")

print()

for i in range(len(onlyfiles)):
    dst_name = onlyfiles[i][len(cwd):]

    shutil.move(onlyfiles[i], f"{cwd}\\{f[i][1]}\\{dst_name}")