'''
This modual details functions functions to visualize convolutions of the NN
'''
import matplotlib.pyplot as plt
from keras import backend as L

def make_figure(figures, nrows=1, ncols=1, titles=False):
	#figure = <title, figure> (dictionary)
	fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows)
	for ind,title in enumerate(sorted(figures.keys(), key=lambda s: int(s[3:]))):
		axeslist.ravel()[ind].imshow(figures[title], cmap=plt.gray())
		if titles:
			axeslist.ravel()[ind].set_title(title)
				
	for ind in range(nrows*ncols):
		axeslist.ravel()[ind].set_axis_off()
	if titles:
		plt.tight_layout()
	plt.show()
	
	
def get_dim(num):
	s = num ** (0.5)
	if round(s) < s:
		return (int(s), int(s) + 1)
	else:
		return (int(s) + 1, int(s) + 1)
		xs

	