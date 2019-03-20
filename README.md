# Data&GIS Lab Data Wrangling Contest
* Author: Yuan Gao
* Academic Standing: Freshman
* Result: Winner
## Dataset: Hourly Weather Surface - Brazil (Southeast region).
* In this contest I am given a huge csv file (raw file can be downloaded [here](https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region)) with almost 10 million rows of data and with lots of missing values. I have cleaned up these columns and cleaned csv can be downloaded [here](https://drive.google.com/open?id=1Ca0d4G3vW3Fav_rQYOYqtBFRS7lJv1Vm).
## Skills involved
* Language: Python 3.6 and Jupyter Notebook
* Library used: Pandas, Scikit-learn, Numpy, and Matplotlib
* Supervised learning: Linear Regression, and could be implemented by Support Vector Regression
* Others: Ipython kernel memory management, Object-Oriented Programming
## Cleaning methodology
* Null values in `elet`, `lat`, `lon` are implemented by data from GoogleMap, which ensures the accuracy
* Null values in `temp`, `stp`,`dewp`,`hmdy`, are filled by monthly mean value. For instance, if missing `temp` at `2001-11-01`, I use the mean of all the non-missing value at November to fill it.
* Null values in `gbrd`, and part of `temp` are filled by using linear Regression, since they are missing 50% of the total values, and the confidence of the classifier for `gbrd` is almost 60%, which is acceptable for missing values.
* Null values in `wdsp`, `wdct`, `gust` are implemented by using previous five values, with a minimam threshold dealing with consecutive nans.
* Null values in `tmax`, `tmin`, `smax`, `smin`, `dmax`, `dmin` are implemented by adding a value to corresponding columns. For instance, I implement `tmax` by first calculating the mean of the difference between non-missing `tmax` and `temp` and then add the number to `temp` in columns missing `tmax`
* Dropped values: A group in `wsnm` called `JACAREPAGUA` in Rio De Janiero contains mostly (more than 99%) nan values, which could not provide any useful informations, so instead of filling them, I dropped them.
## Cannot view the notbook on github?
Go to the [nbviewer](https://nbviewer.jupyter.org/github/Rabona17/UCSD_Data_Cleaning_Contest/blob/master/Demo.ipynb) for better rendering on this project!
