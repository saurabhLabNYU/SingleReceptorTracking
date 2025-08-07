import pandas as pd

def convert_csv(input_file, reference_file):
    # Load the input CSV file (first file format)
    input_df = pd.read_csv(input_file)

    # Load the reference CSV file (DoM format) to get the correct column order
    reference_df = pd.read_csv(reference_file)
    reference_columns = reference_df.columns  # Extract the correct column order

    # Create an output dataframe with the correct column structure
    output_df = pd.DataFrame(columns=reference_columns)

    # Assign values based on mappings
    output_df["X_(px)"] = input_df["x"]
    output_df["Y_(px)"] = input_df["y"]
    output_df["Frame_Number"] = input_df["frame"]
    output_df["X_(nm)"] = input_df["x"] * 66
    output_df["Y_(nm)"] = input_df["y"] * 66
    output_df["X_loc_error(nm)"] = 0
    output_df["Y_loc_error(nm)"] = 0
    output_df["Z_(nm)"] = 0
    output_df["Z_loc_error(nm)"] = 0
    output_df["Amplitude_fit"] = 0
    output_df["Amp_error"] = 0
    output_df["BGfit"] = 0
    output_df["BGfit_error"] = 0
    output_df["SD_X_(nm)"] = 0
    output_df["SD_X_error(nm)"] = 0
    output_df["SD_Y_(nm)"] = 0
    output_df["SD_Y_error(nm)"] = 0
    output_df["False_positive"] = 0
    output_df["IntegratedInt"] = 0
    output_df["SNR"] = 0
    output_df["R2_fit"] = 1
    output_df["Iterations_fit"] = 3
    output_df["Track_Length"] = input_df["trajectory_length"]

    # Rank Track_IDs in increasing order
    unique_tracks = sorted(input_df["particle"].unique())  # Sort unique track IDs
    track_id_mapping = {old_id: new_id for new_id, old_id in enumerate(unique_tracks, start=1)}
    output_df["Track_ID"] = input_df["particle"].map(track_id_mapping)  # Replace old IDs with new ranked ones

    # Compute Particle_ID and Reverse_numbering
    output_df["Particle_ID"] = 0  # Initialize
    output_df["Reverse_numbering"] = 0  # Initialize

    for track_id, group in output_df.groupby("Track_ID"):
        sorted_group = group.sort_values("Frame_Number")  # Sort by frame number
        particle_id = range(1, len(sorted_group) + 1)  # Assign sequential numbers
        reverse_numbering = range(len(sorted_group), 0, -1)  # Reverse numbering

        output_df.loc[sorted_group.index, "Particle_ID"] = particle_id
        output_df.loc[sorted_group.index, "Reverse_numbering"] = reverse_numbering

    # Ensure the first column is numbered correctly **without creating an empty column**
    output_df.insert(0, "", range(1, len(output_df) + 1))

    # **Remove only truly empty columns (those with all NaN values)**
    output_df.dropna(axis=1, how='all', inplace=True)  # Remove columns where all values are NaN

    # Generate output file name
    output_file = input_file.replace(".csv", "_DoM_format.csv")

    # **Save the converted file, ensuring NO extra index column**
    output_df.to_csv(output_file, index=False)

    print(f"Converted CSV file saved as {output_file}")

if __name__ == "__main__":
    # Define input and reference file names here
    input_csv = "NRP1_n1a_beforeagonist010.csv"  # Change this to your input file name
    reference_csv = "NRP1_n1a_beforeagonist010_DoM.csv"  # Change this to your DoM format file

    convert_csv(input_csv, reference_csv)
