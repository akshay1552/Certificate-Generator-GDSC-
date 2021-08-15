from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
name = ImageFont.truetype('arial.ttf',80)
num = ImageFont.truetype('arial.ttf',40)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(690,720),text='{}'.format(j['name']),fill=(0,0,0),font=name)
    draw.text(xy=(1000,1205),text='{}'.format(j['id']),fill=(65,62,65),font=num)
    img.save('pictures/{}.jpg'.format(j['name']))