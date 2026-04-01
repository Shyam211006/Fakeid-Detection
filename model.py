import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset (you can improve later)
data = pd.DataFrame({
    "followers": [100, 10, 500, 5, 300, 20],
    "following": [150, 300, 400, 1000, 200, 800],
    "posts": [10, 1, 50, 0, 25, 2],
    "bio": [1, 0, 1, 0, 1, 0],
    "pic": [1, 0, 1, 0, 1, 0],
    "verified": [0, 0, 1, 0, 1, 0],
    "label": [0, 1, 0, 1, 0, 1]  # 0 = Real, 1 = Fake
})

# Split features & label
X = data.drop("label", axis=1)
y = data["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ model.pkl created successfully!")