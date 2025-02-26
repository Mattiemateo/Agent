import pytesseract
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"equation.png")
 
# Setting the points for cropped image
left = 0
top = 0
right = 850
bottom = 400
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.save("cropped.png")

def extract_equation(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), config="--psm 5")
    for line in text.split("\n"):
        if "=" in line:
            return line.strip()
    return "No equation found"

# Example usage
image_path = "cropped.png"
print(extract_equation(image_path))
#(5+8')(5-¥)=      [1]
