from hashlib import sha256
from os import system

new = "sample" 
system(f"cwebp -q 80 {new} -o {new}.webp")


with open("sample.webp", "r") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        sha256.update(chunk)
    hash = sha256.hexdigest()

def file_test():
    assert hash == "d1983366c9dc294b9157fd756c9\
aee69fc413fd7a64df7d3b27b6a74b2b15821" 
