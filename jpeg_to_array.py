from PIL import Image
from numpy import asarray

#takes name of jpeg and converts to 4-vector array (rgb values)
def jpeg_to_4vector(name: str):
    img = Image.open(name)
    return asarray(img)




