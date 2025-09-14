import pickle
from sklearn.dummy import DummyClassifier
import numpy as np

# Create dummy training data
X = np.array([[0],[1],[2],[3],[4],[5]])
y = np.array([0,1,1,0,1,0])

model = DummyClassifier(strategy="most_frequent")
model.fit(X, y)

with open("reliefx_rf.pkl", "wb") as f:
    pickle.dump(model, f)

print("Dummy model saved as reliefx_rf.pkl")
