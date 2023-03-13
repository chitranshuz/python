# import the lib
# official link  https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageFilter

# create object and use for diff img processing
im = Image.open(".\images\luffy.jfif")
print(im)

# blur the image
fltr_img_blur = im.filter(ImageFilter.BLUR)
fltr_img_blur.save(".\images\luffy_blur.png", "png")

# convert RGB to blank and white, save and show
fltr_img_BlckWht = im.convert('L')
fltr_img_BlckWht.save(".\images\luffy_grey.png", "png")
fltr_img_BlckWht.show()

'''
other methods:-
.rotate(90)
.resize((300, 300))

crop:
box = (ul_pixel, ur_pixel, ll_pixel, lr_pixel)
.crop(box)

.thumbnail((400, 400)) - crop with aspect ratio
'''