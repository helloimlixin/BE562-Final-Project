R scripts
File Content
This folder contains two files:
Breast_Data_Preprocessing_2ChromP.R: the R script to modifiy the copy number data file in which the cell counts of exactly same gene probe observations is conbined. This script works on senarios when only 2 chromosome probes is used, which including patient 2 and 9 for the data used.

Breast_Data_Preprocessing_3ChromP.R: the R script to modifiy the copy number data file in which the cell counts of exactly same gene probe observations is conbined. This script works on senarios when 3 chromosome probes is used.

test.txt: a test txt file with exactly the origianl data for patient one with DCIS tumor. The original data in the file \breast_cancer_data_filtered\B1\B1_DCIS.txt, where the original Breast Cancer data file is provided in the FISH dataset provided in the folder breast_cancer_data_filtered.
Program Execution
Terminal
With the test.txt in the same directory as the Python script file Breast_Data_Preprocessing_3ChromP.R, the program can be executed as follows:
R Breast_Data_Preprocessing_3ChromP.R



Program Output