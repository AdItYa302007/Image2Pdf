import img2pdf
from PIL import Image
import os
  
#Image Path
img_path = r'C:\Users\ADITYA\Pictures\Camera Roll\test.jpg'
#Path Where To Save
pdf_path = r'C:\Users\ADITYA\Pictures\file.pdf'
 

image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
  
print("Successfully made pdf file")