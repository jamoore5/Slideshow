import os
import glob

def import_images(folder=''):
	path = os.path.realpath(folder)+'/'
	images = glob.iglob(path+'*.jpg')
	entries = map(lambda img: img.replace(path, ''), images)
	return sorted(entries)

images = import_images('../test_images')
for img in images:
	print(img)

