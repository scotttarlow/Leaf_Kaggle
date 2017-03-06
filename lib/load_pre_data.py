import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
'''
This module takes a file path and loades pre_extracted features 
from leaf kaggle competiton. The input is the file path for
train or test files. 
'''

def load_train(filepath):

	#loading
	train_df = pd.read_csv(filepath)
	id = train_df.pop('id')
	target = train_df.pop('species')
	
	#scaling
	target = LabelEncoder().fit(target).transform(target)
	features = StandardScaler().fit(train_df).transform(train_df)
	
	return id,features,target
	

def load_test(filepath):
	
	#loading
	test_df = pd.read_csv(filepath)
	id = test_df.pop('id')
	
	#scaling
	features = StandardScaler().fit(test_df).transform(test_df)
	
	return id, features
	

	
	


