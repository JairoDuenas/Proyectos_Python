# TODO ! $ pip3 install Pillow
# Import pillow
# Open up the image we want to resize using Python
# Print the current size of that image
# Specify the size we wanna change it to
# Save the new resized image

from PIL import Image

def resize_image(size1, size2):
  image = Image.open('image/img1.jpeg')
  # image.show()
  print(f"Current size: {image.size}")

  resised_image = image.resize((size1, size2))

  resised_image.save("img1-"+ str(size1) + ".jpeg")

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image(size1, size2)