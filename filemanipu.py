import os
import shutil
import glob
import re

shutil.rmtree("haha")
shutil.copytree("haha", "nop")
shutil.move()

os.listdir(".")
os.path.exists(".")
os.path.getsize(".")
os.path.isfile(".")
os.path.isdir(".")

os.mkdir("hello")
os.open() #filename flag
os.remove()
os.removedirs()
os.rename()
os.rmdir()

os.system("notepad")

for m in os.listdir("."):
	newm = re.sub(r'\d+', lambda x: str(int(x.group(0)) * 2), m)
	os.rename(m, newm)

mm = os.listdir(".")
mm.sort(key= lambda x: int(re.search("\d+").group(0)))
