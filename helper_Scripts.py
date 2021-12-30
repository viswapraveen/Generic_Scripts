# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:28:53 2021

@author: viswa rubini BJ
"""

import os
import shutil
import glob
from PIL import Image
import numpy as np

class helperScripts(object):
    
    # function to reorganize the files from multiple sub folders to single folder
    def reorganize_file(src_path, des_path):
        for root, dirs, files in os.walk((os.path.normpath(src_path)), topdown=False):
            for name in files:
                if name.endswith('.bmp'):
                    print("Found")
                    SourceFolder = os.path.join(root, name)
                    shutil.copy2(SourceFolder, des_path)

    # Function to remane the given file name                
    def rename(path, old, new):
        for f in os.listdir(path):
            os.rename(os.path.join(path, f),
            os.path.join(path, f.replace(old, new)))

    
    # Function to convert bmp format image to png format               
    def bmp_to_png(convert_path):
        out_dir = ''
        for img in glob.glob(f'{convert_path}\*.bmp'):
            new_name = img.replace('bmp', 'png')
            Image.open(img).save(os.path.join(out_dir, new_name))

    # Function to replace black pixel of an image to adjacent pixel 
    def processImage(src_path, des_path):
        for root, dirs, files in os.walk((os.path.normpath(src_path)), topdown=False):
            for file in files:
                img = Image.open(os.path.join(root,file))
                w,h = img.size
                num_arr = np.array(img)
                for i in range(w):
                    for j in range(h):
                        if num_arr[i,j] <50:
                            k=i+2
                            l=j+2
                            num_arr[i,j] = num_arr[k,l] 
                Image.fromarray(num_arr).save(os.path.join(des_path,file))
                