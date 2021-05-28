from os import system, listdir
from hashlib import sha256

def convert(yesorno="no"):
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


hash = "d1983366c9dc294b9157fd756c9aee69fc413fd7a64df7d3b27b6a74b2b15821" 
def test_file():
    try:
        convert()
        with open("sample.webp", "rb") as f:
             for chunk in iter(lambda: f.read(4096), b""):
                 sha256.update(chunk)
             assert sha256.hexdigest() == hash

    except:
        assert 1 == 2 

if __name__ == '__main__':
    yesorno = input("Should I delete the previous file after conversion?\nWarning! It may not be completely converted.Yes or no?")
    convert(yesorno)
 
