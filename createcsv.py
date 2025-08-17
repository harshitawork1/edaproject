import pandas as pd
import random

# Generate 1000 sample users
data = {
    "Name": [f"User{i}" for i in range(1, 1001)],
    "Age": [random.randint(18, 60) for _ in range(1000)],
    "Department": [random.choice(["HR","IT","Marketing","Finance"]) for _ in range(1000)],
    "Salary": [random.randint(30000, 100000) for _ in range(1000)]
}

df = pd.DataFrame(data)
df.to_csv("user1.csv", index=False)
print("✅ CSV file 'user1.csv' created successfully!")
