import random

import numpy as np
import pandas as pd

names = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Edward",
    "Fiona",
    "George",
    "Hannah",
    "Ivan",
    "Julia",
]
groups = ["A", "B", "C"]


data = {
    "Name": random.choices(names, k=100),
    "Age": [random.randint(18, 30) for _ in range(100)],
    "Group": [random.choice(groups) for _ in range(100)],
    "Score": [round(random.uniform(50, 100), 2) for _ in range(100)],
}

df = pd.DataFrame(data)

nan_indices = {
    "Name": random.sample(range(100), 5),
    "Age": random.sample(range(100), 5),
    "Group": random.sample(range(100), 5),
    "Score": random.sample(range(100), 5),
}

# Insert NaNs
for column, indices in nan_indices.items():
    df.loc[indices, column] = np.nan

file_path = "6_pandas/generated_dataset.csv"
df.to_csv(file_path, index=False)
