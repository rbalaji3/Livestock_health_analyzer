import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPClassifier




class Model:

    def __init__(self, file_path):
        self.file = file_path
        df = pd.read_csv(self.file,
                  names=["Room_Number", "Timestamp", "Humidity", "Temperature", "Weather", "Weight", "Percentage"])
        dataset_87 = df
        target_column = ['Weight']
        predictors = list(set(list(dataset_87.columns))-set(target_column) - set(['Room_Number']) - set(['Timestamp']) - set(['Weather']))
        normalized_data_87 = dataset_87[predictors]/dataset_87[predictors].max()
        self.X = df[predictors].values
        self.Y = df[target_column].values

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.Y, test_size=0.20, random_state=40)

        self.mlp = MLPRegressor(hidden_layer_sizes=(4,4), activation='relu',  solver='adam', alpha=1,
                                                batch_size='auto', shuffle=False,max_iter=10000000000)
        self.mlp.fit(X_train,y_train)


    def predict(self, sample):
        predict = self.mlp.predict([sample])
        while predict <= 0:
            predict += 1
        sample_0_init = sample[0]
        sample_2_init = sample[2]
        optimal_weight = predict
        optimal_combination = sample
        for i in range(19):
            sample[0] = sample_0_init * (0.99+i/992)
            for j in range(19):
                sample[2] = sample_2_init * (0.99+j/989)
                new_predict = self.mlp.predict([sample])
                if new_predict > optimal_weight:
                    optimal_weight = new_predict
                    optimal_combination = sample


        # print(predict)
        # print(optimal_weight)
        # print(optimal_combination)
        json_return = {
            "predict_weight" : predict,
            "optimal_weight" : optimal_weight,
            "optimal_parameter_humidity" : optimal_combination[0],
            "optimal_parameter_temperature" : optimal_combination[1]
        }
        return json_return
