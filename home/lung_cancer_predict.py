import pickle
import numpy as np
import sklearn


def predict_lung_cancer(age, gender, level):
    """load model from txt file and return prediction
    return false if ndarray is incorrect shape"""
    a = np.zeros((1, 23))
    if gender == 'Male':
        g = 0
    else:
        g = 1

    l = np.array(level).astype(np.int)
    a[0, 0] = age
    a[0, 1] = g
    a[0, 2:] = l
    print(a)

    with open("home/static/predict_lung_cancer.txt", "rb") as f:
        model = pickle.load(f)
    return model.predict(a)
