import pandas as pd
import random

csv_files = ["data/prompted_data/api_prompted.csv", "data/prompted_data/token_prompted.csv", "data/prompted_data/user_actions_prompted.csv"]
data_frames = [pd.read_csv(file) for file in csv_files]

merged_df = pd.concat(data_frames)
shuffled_df = merged_df.sample(frac=1, random_state=random.seed())

shuffled_csv_file = "data/prompted_data/final_data.csv"
shuffled_df.to_csv(shuffled_csv_file, index=False)

print("Merged and shuffled data saved to", shuffled_csv_file)