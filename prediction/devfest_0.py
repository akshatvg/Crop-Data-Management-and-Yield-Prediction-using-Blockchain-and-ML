import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import os

def predict(crop,rf,tm):
	if(rf==0): return 0
	if(tm==0): return 0
	features = pd.read_csv(os.getcwd()+'/prediction/crop_data/'+crop+'.csv')
	features = pd.get_dummies(features)
	labels = np.array(features['YIELD'])
	features.drop('YIELD', axis=1)
	feature_list = list(features.columns)
	features = np.array(features)

	train_features, test_features, train_labels, test_labels = train_test_split(features,labels,test_size=0, random_state=42)
	test_features = np.array([[0,rf,tm]])
	rf = RandomForestRegressor(n_estimators=1000, random_state=42)

	#training
	rf.fit(train_features, train_labels)

	#predicting
	predictions = rf.predict(test_features)

	return predictions[0]



# #-----CODE------
# inp = input().strip().split(",")
# print(predict(inp[0],float(inp[1]),float(inp[2])))
