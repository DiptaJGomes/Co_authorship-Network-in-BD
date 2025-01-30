import os
import pandas as pd

# Directory containing the CSV files
input_directory = "./Dataset"  # Change to your directory
output_file = "merged_output.csv"

# List to store data from all CSV files
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        try:
            # Read each CSV file and append to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)
            print(f"Successfully read {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Combine all dataframes
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved as {output_file}")
else:
    print("No CSV files found in the specified directory.")
