import os

boobs = []

for pussy in os.listdir("AnonXMusic/assets"):
    if pussy.endswith("png"):
        boobs.append(pussy[:-4])
