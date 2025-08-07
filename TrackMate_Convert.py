import pandas as pd

# Load Excel file
input_file = "30C_Recovery_spots_Trackmate.xlsx"
df = pd.read_excel(input_file)

# Print original columns to confirm names
print("Original columns:")
print(df.columns)

# Rename columns (adjust if necessary based on actual printout)
rename_dict = {
    'TRACK_ID': 'particle',
    'POSITION_X': 'x',
    'POSITION_Y': 'y',
    'MEAN_INTENSITY_CH1': 'mass',
    'TOTAL_INTENSITY_CH1': 'raw_mass',
    'FRAME': 'frame'
}

# Only rename columns that exist in the file
df_renamed = df.rename(columns={k: v for k, v in rename_dict.items() if k in df.columns})

# Define and filter desired columns
desired_columns = ['particle', 'x', 'y', 'mass', 'raw_mass', 'frame']
available_columns = [col for col in desired_columns if col in df_renamed.columns]
df_final = df_renamed[available_columns]

# Drop the first 3 rows from the final output
df_final = df_final.iloc[3:]

# Save to CSV
output_file = "30C_Recovery_spots_Converted.csv"
df_final.to_csv(output_file, index=False)
print(f"\n✅ Converted file saved to: {output_file}")
