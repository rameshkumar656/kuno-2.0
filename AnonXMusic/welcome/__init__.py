import os

booba = []

for meow in os.listdir("AnonXMusic/welcome"):
    if meow.endswith("png"):
        booba.append(meow[:-4])
