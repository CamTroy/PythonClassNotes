from PIL import Image, ImageOps
import os

images_path = "./images"
new_path = "./new_images"
size = (75, 75)

pic_num = 1
filler = 0

if not os.path.exists(new_path):

    os.makedirs(new_path)

for thing in os.scandir(images_path):

    print(thing.name)
    if thing.is_file():

        img = Image.open(f"{images_path}/{thing.name}")
        width, height = img.size
        right = 200

        new_img = img.crop((0, 0, right, height))
        new_img = ImageOps.grayscale(new_img)
        new_img = new_img.resize(size)
        new_img = new_img.rotate(270)
        new_name = f"{new_path}/pic"
        new_img.save(f"{new_name}{pic_num:04d}.png", format="PNG")
        pic_num += 1
        print(f"{new_name}{pic_num:04d}.png")