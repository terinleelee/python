##from PIL import Image
##area=(230,155,1110,770)
##size=(640,200)
##
##lion_img = Image.open("Lion.jpg")
##fruit_img = Image.open("fruit.png")
##
##print(lion_img.size, lion_img.format, lion_img.mode)
##print(fruit_img.size,fruit_img.format,fruit_img.mode)
##
##fruit_resz= fruit_img.resize(size)
##lion_cropped=lion_img.crop(area)
##lion_img.show()
##fruit_img.show()
##
##lion_cropped.save("lion_cropped.jpg")
##fruit_resz.save("fruit_resized.png")
##
##from PIL import Image
##
##size=(128,128)
##
##lion_img= Image.open("Lion.jpg")
##lion_rotated= lion_img.rotate(90)
##lion_converted= lion_img.convert('L')
##lion_transpose=lion_img.transpose(Image.FLIP_LEFT_RIGHT)
##lion_img.thumbnail(size)
##
##print("lion_converted.mode=",lion_converted.mode)
##print("lion_img.size =",lion_img.size)
##
##lion_converted.show()
##lion_transpose.show()
##lion_rotated.show()
##lion_rotated.save("lion_rotated.jpg")
##lion_img.save("lion_thumb.jpg")

##from PIL import Image
##
##fruit_png=Image.open("fruit.png")
##fruit_rotated=fruit_png.rotate(270)
##fruit_converted=fruit_png.convert('L')
##
##fruit_rotated.show()
##fruit_converted.show()
##
##fruit_rotated.save("fruit_rotated.png")
##fruit_converted.save("fruit_converted.png")





