from PIL import Image
import numpy as np
import sys

inv_flag = True #True fo wb, False for rwb
width = 800
height = 480
rotate = 0

gray = Image.open(sys.argv[1]).convert('LA')
width_org, height_org = gray.size
aspect_org = width_org/height_org
if aspect_org < 1 :
  gray = gray.rotate(90,expand=True)
  width_org, height_org = height_org, width_org
  aspect_org = width_org/height_org

# resize, monochrome(0/1), padding, and return narray
if aspect_org > width/height: #high aspect -> adjust width & pad height
  height_tmp = round(width/aspect_org)
  img2d = np.vstack(( np.array(gray.resize((width,height_tmp)).convert('1')), np.ones((height-height_tmp,width),dtype=np.uint8) ))
else: #low aspect -> adjust height & pad width
  width_tmp = round(height*aspect_org)
  img2d = np.hstack(( np.array(gray.resize((width_tmp,height)).convert('1')), np.ones((height,width-width_tmp),dtype=np.uint8) ))

if inv_flag: img2d = 1-img2d
shift=np.uint8(range(0,8)[::-1])
with open('tmp.buf','wb') as f:
  for j in range(0,height):
    f.write(np.array( [np.left_shift( img2d[j,i:i+8],shift ).sum() for i in range(0,width,8)], dtype=np.uint8 ))
