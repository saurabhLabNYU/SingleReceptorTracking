import pandas as pd
from pathlib import Path

# Use current working directory
csv_dir = Path(".")

# Get all CSV files (regardless of name)
all_csv_files = list(csv_dir.glob("*.csv"))

# Filter files that contain 'roi' and 'zprofile' (case-insensitive)
csv_files = [f for f in all_csv_files if 'roi' in f.name.lower() and 'zprofile' in f.name.lower()]

print(f"Found {len(csv_files)} matching CSV files")

if not csv_files:
    print("No matching files found. Check the naming convention or try relaxing the filter.")
    exit()

# Process files
for csv_file in sorted(csv_files):
    print(f"Processing {csv_file.name}")
    df = pd.read_csv(csv_file)

    intensity_cols = [col for col in df.columns if col.lower().startswith("slice_")]
    if not intensity_cols:
        print(f"No 'Slice_' columns in {csv_file.name}, skipping.")
        continue

    intensity_data = df[intensity_cols].transpose().reset_index(drop=True)
    frame_numbers = list(range(1, len(intensity_data) + 1))
    avg_intensity = intensity_data.mean(axis=1)

    result_df = pd.DataFrame({
        "Frame": frame_numbers,
        "Intensity": avg_intensity
    })

    txt_file = csv_file.with_suffix(".txt")
    result_df.to_csv(txt_file, sep="\t", index=False, header=False)
    print(f"✅ Saved: {txt_file.name}")
