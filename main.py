from os import system, listdir

dir = listdir()

new = ""
num = 0

for inputed in dir:
    new = str(inputed).replace(".png", "")
    system(f"cwebp -q 80 {new}.png -o {new}.webp")
    print(new, "converted")
    num += 1

print(num, "convert successful")
