
# * Watermark-it-all
# * Created by JacobEM.com
# * This program is licensed under the MIT License


from os import listdir, getcwd
from os.path import isfile, join

from PIL import Image
import sys

def addWatermark(inputPath, outputPath, watermarkPath, position, show, name):
    baseImage = Image.open(inputPath)
    watermark = Image.open(watermarkPath)

    wmWidth, wmHeight = watermark.size

    width, height = baseImage.size

    transparent = Image.new('RGB', (width, height), (0,0,0))
    transparent.paste(baseImage, (0,0))

    if position == 'tl':
        position = (10, 10)
    elif position == 'tr':
        position = (((width - 10) - wmWidth), 10)
    elif position == 'bl':
        position = (10, ((height - 10) - wmHeight))
    elif position == 'br':
        position = (((width - 10) - wmWidth), ((height - 10) - wmHeight))
    elif position == 'c':
        position = (
            int(
                (width / 2) - (wmWidth / 2)
            ),
            
            int(
                (height / 2) - (wmHeight / 2)
            )
        )
    else:
        position = (0, 0)
    
    transparent.paste(watermark, position, mask=watermark)

    if show != 'no-show':
        transparent.show()

    transparent.save(outputPath)

    print(f'Saved {name} with a watermark.')




path = getcwd() + '/img'
pathOut = getcwd() + '/output'

files = [f for f in listdir(path) if isfile(join(path, f))]

for thisFile in files:

    fileType = thisFile.split('.')[1]

    addWatermark(
        path + '/' + thisFile,
        pathOut + '/WM ' + thisFile,
        'watermark.png',
        position = sys.argv[1],
        show = sys.argv[2],
        name = thisFile
    )