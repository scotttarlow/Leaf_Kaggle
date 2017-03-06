import numpy as np
import pandas as pd
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import img_to_array, load_img

'''
This module loads all the training/test images, resizes them and 
makes them ready for kaggle.
'''


def rebuild_image(img, dim=64):
	
	# find largest axis
	maxsize = max((0,1), key=lambda i: img.size[i])
	
	#scale both axis
	scale = dim/float(img.size[maxsize])
	
	return img.resize((int(img.size[0] * scale), int(img.size[1]*scale)))
	
	

def load_image(ids,dim=64):

	filepath = 'images/'
	
	IM = np.empty((len(ids),dim,dim,1))
	
	for i, ids in enumerate(ids):
	
		images = rebuild_image(load_img(filepath + str(ids) + '.jpg',
grayscale=True),dim = dim)
		
		images = img_to_array(images)
		x = images.shape[0]
		y = images.shape[1]
		
		#centering
		l_bound_0 = int((dim - x) / 2)
		u_bound_0 = l_bound_0 + x
		l_bound_1 = int((dim - y) / 2)
		u_bound_1 = l_bound_1 + y
		
		IM[i,l_bound_0:u_bound_0,l_bound_1:u_bound_1,0:1] = images
		
		#scale it to grey
	return np.around(IM/ 255.0) 
		