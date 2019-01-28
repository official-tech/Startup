# To work with images in Python we need to download and install 'pillow' package
# Open cmd/terminal and type 'pip install pillow'

##################################################################################################################################

# 1.Image processing using 'PIL' from 'pillow' 

from PIL import Image
a = Image.open("image_name.jpg")
a.show()


b = a.rotate(45)
b.show()


c = a.convert("L")
c.show()
