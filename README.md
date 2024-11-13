This repository contains the data, code, and graphs for my final project for CMSC6950.



The folder `orig_data` contains the original data files found online.

The folder `data` contains reorganized files that are imported into the notebook. These files were made by reorganizing the data in the original files in Excel.

The folder `org_data` contains organized data files containing all the different datasets into a yearly or monthly list. These data files are those used to create the graphs and calculate statistics. These data files were made in Python by taking data from the files in the `data` folder and reworking it into a pandas dataframe. This dataframe was then saved as a csv file. A second pandas dataframe was made from the calculated annual datasets, and saved as a second csv file.

The folder `images` contains all the generated graphics from the code. These graphics are all saved as PDFs. All graphics in this folder can be generated by running the code in the .ipynb file.

The file `CMSC6950_Project.ipynb` is the jupyter notebook where the data is initially reorganized and the initial plots are created.

There (will be) a series of Python files which will each perform a task on the data with the goal of calculating a new statistic and generating new figures. The functions written in these files will be tested using pytest. Test functions for each function are written in Python files named test_"function_name".
