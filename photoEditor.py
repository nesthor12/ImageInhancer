from PIL import Image, ImageEnhance, ImageFilter

import os

path = './imgs'

pathOut = '/editedImages'

for filename in os.listdir(path):

    img_path = path+"/"+filename
    # 
    img = Image.open(f"{img_path}")
    
    # img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 10

    enhancer = ImageEnhance.Brightness(edit).enhance(factor)

    clean_name = os.path.split(filename)[1]

    print('Converting '+clean_name)

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

    
