# To work with images in Python we need to download and install 'pillow' package
# Open cmd/terminal and type 'pip install pillow'

##################################################################################################################################

# 1.Image processing using 'PIL' from 'pillow' 

from PIL import Image
a = Image.open("image_name.jpg")
a.show()

####################################################

from PIL import Image
a = Image.open("image_name.jpg")
b = a.rotate(45) # rotating image at 45 degree
b.show()

##############################################################

from PIL import Image
a = Image.open("image_name.jpg")
c = a.convert("L") # convert image color into gray scale image 
c.show()

########################################################

from PIL import Image
a = Image.open("image_name.jpg")
print(a.size) # to get width and height of image

#######################################################

from PIL import Image
a = Image.open("image_name.jpg")
print(a.mode) # to get the color modde of image 
