from load_pre_data import load_train, load_test
from load_images import load_image
from sklearn.model_selection import StratifiedShuffleSplit

random_state = 42
split = 0.8

def load_train_data(filepath, split = split, random_state = random_state):

	id, features_train, target_train = load_train(filepath)
	image_train = load_image(id)
	
	sss = StratifiedShuffleSplit(n_splits = 1, train_size=split,random_state=random_state)
	train_i,val_i = next(sss.split(features_train,target_train))
	features_val,val_img,val_target = features_train[val_i],image_train[val_i], target_train[val_i]
	features_train,train_img,train_target = features_train[train_i],image_train[train_i],target_train[train_i]
	
	return (features_train,train_img,train_target),(features_val,val_img,val_target)
	

def load_test_data(filepath):

	id, test_features = load_test(filepath)
	test_images = load_image(id)
	
	return (id,test_features,test_images)
	
	