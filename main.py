from os import system, listdir

dir = listdir()

yesorno = input("Should I delete the previous file after conversion?\nWarning! It may not be completely converted.
Yes or no?")

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

