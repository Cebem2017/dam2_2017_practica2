# pip install Pillow    

from PIL import Image

def main():

    imagen = Image.open("Homer_Simpson.png")
    imagen.show()
    imagenblanco_negro = imagen.convert("L")
    imagenblanco_negro.show()
    

main()