
from PIL import Image, ImageFilter

img = Image.open("./images/taj-mahal.jpg")

print(img.size)

print(img.format)

print(img.mode)

blur_img = img.filter(ImageFilter.BLUR)

blur_img.save("./images/blur-taj-mahal.png", "png")

grey_img = img.convert("L")

grey_img.save("./images/grey-taj-mahal.png", "png")