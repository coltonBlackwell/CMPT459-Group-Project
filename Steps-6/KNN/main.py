import pandas as pd
import numpy as np
from KNN import KNN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])



df = pd.read_csv("/home/colton/Documents/university/3rd Year/2nd Semester/CMPT 459/Assignments/CMPT459-Final-Group-Project/Steps-4-5/result/oversampled_processed_data.csv")

df = df.drop(columns=['outcome_group', 'sex', 'province', 'country', 'chronic_disease_binary'])

df = df[0:1000]

X = df.iloc[:,:-1].values
y = df.iloc[:, -1].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) #avoid data leakage

#------------------ NECESSARY PRE-PROCESSING STEPS



model=KNN(5) #our model
model.fit(X_train,y_train)

classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)#The default metric is minkowski, and with p=2 is equivalent to the standard Euclidean metric.
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
     

predictions=model.predict(X_test)#our model's predictions

cm = confusion_matrix(y_test, predictions) #our model
print(cm)
print(accuracy_score(y_test, predictions))

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap=cmap, edgecolors='k', s = 20)
plt.show()

#**********************************************************



# y = df['outcome_group_code']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test) #avoid data leakage


# # print(y_train)

# model = KNN(5)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)

# # print(predictions)