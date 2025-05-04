import os 
import shutil

a = os.listdir("09 File IO\\dir")
print(a)
print(os.getcwd())
# os.remove("09 File IO/dir/sample1.txt")

shutil.rmtree("09 File IO\\dir")