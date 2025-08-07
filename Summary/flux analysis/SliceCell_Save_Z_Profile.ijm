// Define the output directory
outputDir = "/Volumes/T7/20250430_JFX549_Heatshock_PopZ_LowerLaser/ROI/50C_2/50C_2_Z-axis/";
imageName = "50C_2_AfterActivation.tif";

// Get the number of ROIs in the ROI Manager
roiCount = roiManager("count");

if (roiCount == 0) {
    print("No ROIs found in ROI Manager");
    exit();
}

selectImage(imageName);
n = nSlices;

// Loop through ROIs
for (i = 0; i < roiCount; i++) {
    roiManager("Select", i);
    selectImage(imageName);

    if (!(selectionType() == 0 || selectionType() == 5 || selectionType() == 6))
        exit("Line or Rectangle Selection Required");

    setBatchMode(true);
    
    // Get X (distance) values from one profile
    run("Plot Profile");
    Plot.getValues(x, y);
    run("Clear Results");
    for (j = 0; j < x.length; j++)
        setResult("x", j, x[j]);
    close(); // close plot window

    // Loop through all slices to collect Z-profile data
    for (slice = 1; slice <= n; slice++) {
        showProgress(slice, n);
        setSlice(slice);
        profile = getProfile();

        // Optional: add label from metadata if needed
        sliceLabel = "Slice_" + slice;

        for (j = 0; j < profile.length; j++) {
            setResult(sliceLabel, j, profile[j]);
        }
    }

    setBatchMode(false);
    updateResults();

    // Save as CSV
    csvFileName = outputDir + "ROI_" + i + "_ZProfile.csv";
    saveAs("Results", csvFileName);
    run("Clear Results");

    print("Saved Z-profile for ROI " + i + " to: " + csvFileName);
}

print("Completed processing " + roiCount + " ROIs");
