from hashlib import sha256
from os import system, listdir

dir = listdir()

new = ""
num = 0

for inputed in dir:
    new = str(inputed).replace(".png", "")
    system(f"cwebp -q 80 {new}.png -o {new}.webp")
    print(new, "converted")
    num += 1
print(num, "convert(s) successful")
if yesorno == "yes":
    system("rm *.png")
    print("remove successful.\n\t goodluck!")

with open("sample.webp", "r") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        sha256.update(chunk)
    hash = hash_md5.hexdigest()

def file_test():
    assert hash == "d1983366c9dc294b9157fd756c9\
aee69fc413fd7a64df7d3b27b6a74b2b15821" 
