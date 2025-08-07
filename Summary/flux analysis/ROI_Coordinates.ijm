// Set output directory and CSV file path
outputDir = "/Volumes/T7/20250430_JFX549_Heatshock_PopZ_LowerLaser/ROI/50C_2/50C_2_Z-axis/";
csvFile = outputDir + "all_roi_coordinates.csv";

// Check ROI count
numROIs = roiManager("count");
if (numROIs == 0) exit("❌ No ROIs in ROI Manager.");

// Clear previous Results
run("Clear Results");

nr = 0; // total point index

for (i = 0; i < numROIs; i++) {
    roiManager("Select", i);
    getSelectionCoordinates(x, y);

    for (j = 0; j < x.length; j++) {
        setResult("Label", nr, "ROI_" + i);
        setResult("X", nr, x[j]);
        setResult("Y", nr, y[j]);
        nr++;
    }
}

// Update and save results table
updateResults();
saveAs("Results", csvFile);
print("✅ Saved all coordinates to: " + csvFile);
