#!/usr/bin/python3
#
# Created by Felipe Miguel Nery Lunkes (10/07/2022)
#
# pip install imageio

# First, the filenames

import imageio

IMGFile=input('Filename of the images (in order): ')
Files=IMGFile.split(' ')

for x in range(0, len(Files)):
    print(Files[x])

IMAGES = []

for IMGFilenames in Files:
    IMAGES.append(imageio.imgread(IMGFilenames))

imageio.mimsave('gif.gif', IMAGES, 'GIF', duration=2)

exit()