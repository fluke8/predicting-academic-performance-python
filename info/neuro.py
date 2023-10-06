from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd, seaborn as sb, numpy as np, matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('uspevaemost_raw1.csv')
data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=1)

# df = sb.load_dataset('iris')
# sb.set_style("ticks")
# sb.pairplot(df, hue='species', diag_kind="kde", kind="scatter", palette="husl")
# plt.show()

knn = KNeighborsClassifier(n_neighbors=1)
z = knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Число ошибочно классифицированных образцов персептрон: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))