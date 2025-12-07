# Data Analysis for Manufacturing

import pandas as pd

data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Value': [73.64, 78.02, 73.4, 80.38]
}

df = pd.DataFrame(data)
average = df['Value'].mean()
print(f"Average: {average:.2f}")
print("Recommendation: implement predictive maintenance program")
