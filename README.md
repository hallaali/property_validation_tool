# property_validation_tool

## Contents of the GitHub: 
### Validation/Visualization Python Scripts (https://github.com/hallaali/property_validation_package/tree/main/validation_scripts)
#### Jet-A Fuel 
Within the "validation scripts directory (link above) there is a Python script called "Jet_A_validation_tool" (https://github.com/hallaali/property_validation_tool/blob/main/validation_scripts/jetA_validation_tool.py). This script contains the code used to generate the Jet-A fuel validation and visualization packages. 
#### Hydrogen 
The "validation_scripts" directory also contains a Python Script called "H2_validation_tool" (https://github.com/hallaali/property_validation_tool/blob/main/validation_scripts/H2_validation_tool.py). This script contains the code used to generate the Hydrogen visualization package. 
#### Template 
Lastly, the "validation_scripts" directory also contains a Python Script called "validation_tool_(template) (https://github.com/hallaali/property_validation_tool/blob/main/validation_scripts/validation_tool_(template).py). This script contains a general code for generating a validation/visualization package, where the lines enclosed in the symbol "!" indicate the fields that should be input by the user to complete the script for the selected fuel. 

### Data Files (https://github.com/hallaali/property_validation_tool/tree/main/data_files)
#### Jet-A Fuel
The jetA_data directory (https://github.com/hallaali/property_validation_tool/tree/main/data_files/jetA_data) contains the .csv files used to generate the validation/visualization packages for Jet-A fuel with the Jet-A validation Python script. All of the .csv files contained in this folder are called and read by Python in the validation script to plot the data directly from these files. 
#### Hydrogen
The hydrogen_data directory (https://github.com/hallaali/property_validation_tool/tree/main/data_files/hydrogen_data) contains the .csv files used to generate the visualization packages for Hydrogen with the Hydrogen validation Python script. All of the .csv files contained in this folder are called and read by Python in the validation script to plot the data directly from these files. 

### Validation/Visualization Packages (https://github.com/hallaali/property_validation_tool/tree/main/validation%2Bvisualization_packages)
#### Jet-A Fuel
The jetA_validation_package directory (https://github.com/hallaali/property_validation_tool/tree/main/validation%2Bvisualization_packages/jetA_validation%2Bvisualization_package) contains folders each named after the .csv data files that contain data for Jet-A fuel properties. Each of these folders contain validation/visualization plots from the corresponding .csv data file.
#### Hydrogen
Similarly, the H2_validation_package directory (https://github.com/hallaali/property_validation_tool/tree/main/validation%2Bvisualization_packages/H2_visualization_package) contains folders each named after the .csv data files that contain data for Hydrogen properties. Each of these folders contain visualization plots from the corresponding .csv data file.

## How to Use the Python-Based Property Validation Tool: 

### Using the Thermo Rig to Generate Data

### Generating the Python Validation Script for a Selected Fuel
In the "validation_scripts" folder there is a Python script that can be utilized as a template to be adjusted for a selected fuel (https://github.com/hallaali/property_validation_tool/blob/main/validation_scripts/validation_tool_(template).py). The areas enclosed in two "!" symbols vary with the selected fuel and should be filled in by the user. The H2 and Jet-A validation scripts can be used as examples. This section will outline all of the areas with "!" symbols and how they should be filled in:

**1.** *line 12* - **!filepath!**: Enter the filepath of the first .csv file with data for the selected fuel. This data file should be the "validation" portion (containing percent error between pkg and CEA values)

**2.** *line 24* - **!filepath!**: Enter the filepath of the second .csv file with data for the selected fuel. This data file should be the "visualization" portion (just the thermo properties, no percent error/calculation)

* More files can be added if necessary --> reuse (i.e. copy and paste below) the set of lines 12-18 (for validation) or lines 24-27 (for visualization) and create more dataframes (data3, data4, data5, etc.) 

**3.** *line 49* - **!filepath!**: Enter the filepath of the folder that will contain the visualization package folder

**4.** *line 59* and *line 84*  - **!fuelname!**: Enter the name of the selected fuel (to be displayed on the plot titles)

**5.** *line 96* - **!data!** - Enter the name of the dataframe that contains the data for the visualization portion (e.g. data1)
* More data files can be plotted if necessary --> reuse the set of lines 96-97 (i.e. copy and paste below) and repeat steps 5-7 for that dataframe

**6.** *line 96* - **!x-parameter!** - Enter the symbol of the parameter that will be the x-parameter of each plot enclosed in single quotation marks and brackets (e.g. ['T'] or ['P'])

**7.** *line 96* - **!foldername!** - Enter the name of the visualization package folder - the folder that all of the visualization plots **from the selected data file (i.e. the dataframe input in step 5)** will be stored in (in the examples, we named them after the data file names)

**8.** *line 101* - **!filepath!** - Enter the filepath of the folder that will contain the validation package folder

**9.** *line 113*  - **!fuelname!**: Enter the name of the selected fuel (to be displayed on the plot titles)

**10.** *line 119* - **!data!** - Enter the name of the dataframe that contains the data for the validation portion (e.g. data2)
* More data files can be plotted if necessary --> reuse the set of lines 119-120 (i.e. copy and paste below) and repeat steps 5-7 for that dataframe

**11.** *line 119* - **!x-parameter!** - Enter the symbol of the parameter that will be the x-parameter of each plot enclosed in single quotation marks and brackets (e.g. ['T'] or ['P'])

**12.** *line 119* - **!y-parameter!** - Enter the symbol of the parameter that will be the y-parameter of each plot enclosed in single quotation marks and brackets (e.g. ['T'] or ['P'])

**13.** *line 119* - **!foldername!** - Enter the name of the validation package folder - the folder that all of the validation plots **from the selected data file (i.e. the dataframe input in step 10)** will be stored in (in the examples, we named them after the data file names)

When all of these areas are filled in, the script is ready to be run for the selected fuel. 

### Running the Python Script from the Command Line
The steps to run the Python validation script from the command line are outlined below:
1. Ensure that the altered Python validation script for the selected fuel is saved in a folder on your computer
2. Open the Windows command prompt
3. Using the "cd" command, change the directory to the path of the folder that the Python validation script is saved in
4. Use the "python" command followed by the name of the Python validation script to run it (e.g. python H2_validation_tool.py)
5. Navigate to the folder(s) you set to store the visualization/validation plots (steps 3 and 8 in the previous section) - these folders should now contain a series of visualization/validation plots for the selected fuel
