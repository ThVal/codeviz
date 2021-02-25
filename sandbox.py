from PIL import Image
import numpy as np

"""

Tweak the word cloud by 
changing the .txt and/or the pic

"""


# open data / pics
mask = np.array(Image.open("pics/drapeau.png"))
file = open('data/codepenal.txt', 'r')
