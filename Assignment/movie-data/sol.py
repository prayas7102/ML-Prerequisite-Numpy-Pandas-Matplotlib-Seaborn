import pandas as pd
import numpy as np
import os
import seaborn as sn
import matplotlib.pyplot as plt

# Exercise
excel_file_path = "./movie_revenues.csv"
df = pd.read_csv(excel_file_path)

df["revenue"] = df["revenue"] / 10000
std_deviation = 3.5
print(df.describe())

def get_MAD(s, median):
    diff = abs(s - median)
    return np.median(diff)

median = np.median(df["revenue"])
MAD = get_MAD(df["revenue"], median)

def get_modified_z_score(x, median, MAD):
    return 0.6745 * (x - median) / MAD

# removing outlier using zscore
df['modifies_z_score'] = get_modified_z_score(df["revenue"], median, MAD)
df_no_outlier = df[
     (df["modifies_z_score"] < std_deviation)
]

# Specify the path where you want to save the CSV file
csv_file_path = "./output_file.csv"

# Check if the file already exists and delete it
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
    print("\n")

# Write the DataFrame without outliers to a CSV file
df_no_outlier.to_csv(csv_file_path, index=False)

# normal distribution
# if you apply log function to a datset it becomes log normally distributed
sn.histplot(data=df_no_outlier["revenue"], kde=True, log_scale=True)
plt.show()
