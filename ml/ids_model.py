import numpy as np
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)

train_data = np.array([
    [80,1000],
    [443,1200],
    [22,500],
    [80,900],
    [443,1100],
    [22,600],
    [80,800]
])

model.fit(train_data)

def detect_attack(port, bytes_sent):

    sample = np.array([[port, bytes_sent]])

    prediction = model.predict(sample)

    if prediction[0] == -1:
        return True
    else:
        return False
