from rembg import remove
from PIL import Image


class imgClipping:

    def __init__(self, input_img_path):

        self.input_img = Image.open(input_img_path)
        self.output_img = None
        self.output_img_path = "img/bg_removed.png"

    def remove_background(self):

        self.output_img = remove(self.input_img)
        self.output_img.save(self.output_img_path)



# input_path = '../../img/baby_clothes.jpg'
# output_path = '../../img/baby_clothes_bg_removed.png'
#
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)
