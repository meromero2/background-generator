from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
tiny = img.thumbnail((400, 200))
tiny.show()

