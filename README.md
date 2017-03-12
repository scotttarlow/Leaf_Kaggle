# Leaf_Kaggle
My code for Leaf Identification Kaggle Competition

Summary: There are around 1/2 million species of plants in the world. Using images of plants to 
identify species be useful for a variety of reasons: crop and food supply management, 
plant based research, species population tracking. In this project I will use 
Convolutional Neural Networks to classify grey-scale images to identify each image as one 
of 99 leaf species. These models will either incorporate multiple convolutional layers as 
well as merging the features extracted by the convolutions with a pre-extracted feature 
set (provided by Kaggle) of each leaf image. Each model will be evaluated by minimizing 
the loss function, log-loss. The best of my Neural Networks earned a log-loss of 0.02312 
on Kaggle's test data set, which translates to 100% accuracy on predicting a leaf's 
species from its corresponding image.

Description of Items in the Repo:

	images: All the images of the leaves for the kaggle competition 

	leaf_gifs: All the images in the training set of the leaves sorted into gifs by their species 

	lib: Various functions for the competition- Loading Data, Resizing Images and Plotting convolutions

	model_ipynb: Jupyter Notebooks for all the models run in this project 

	report_figures: Figures for Tarlow_Capstone_Report.ipynb

	saved_models: pickled models (and model data)

	Tarlow_Capstone_Report.ipynb: A report on the project, with analysis and conclusions

	Visualization.ipynb: A notebook of visualizations that have to do with the project

	test.csv: Kaggle's numerical data for the test set that is used for submission to the Competition

	train.csv:  Kaggle's numerical data for the training of models.