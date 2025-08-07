# OscarTrackPy
Oscar Gao's tracking and Analysis repo
# OscarTrackPy
Oscar Gao's tracking and Analysis repo
1st category in this github codespace is the python file ended in .py
    1. CSV_Convert is used to convert the csv file ouput from Trackpy to DoM format in order to be used as input for      DiffusionLab. It needs to be used along with NRP1_n1a_beforeagonist010_DoM.csv
    2. tiff_covert_jpeg.py is a script that use to convert tif or avi file into jepg pictures frame by frame
    3. TrackMate_Convert.py is used to convert TrackMate's output csv file to Trackpy format in order to proceed D vs Alpha analysis using same notebook.
2nd category: python notebook
    1. NRP1_n1a_beforeagonist010.ipynb is a tutorial guide and template for basic tracking analysis using Trackpy
    2. 30C_AfterActivation_07282025.ipynb is a template for Trackpy analysis with specific roi region. The roi is defined in 30C_ROI_Coordiantes.csv
3rd category: environment
    use pip install to install the environment_SSLab.yml file before preceeding to Trackpy

The summary folder contains:
    1. Flux analysis by using Spatial_Correlation python notebook and all fiji macro script needed to generate Z-axis profile and ROI coordinates
    2. summary of a bunch of Trackpy python notebook output csv in order to cross compare different experimental conditions.
