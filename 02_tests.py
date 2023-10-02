from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression


dataset = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw.csv')
data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]