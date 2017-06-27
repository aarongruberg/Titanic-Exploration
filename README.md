### This is an exploration of data on the Titanic
<p>The data set included information on 891 of the 2224 passengers aboard the Titanic.  This is an iPython Notebook file which allows me to display blocks of code together with html text explaining my code.  Each of the following blocks contain the input of my code and the output it produced.</p>  

<p>I used the PANDAS library in Python to read the csv file into a dataframe which can viewed in the output below.  The dataframe creates a table for the data.  I named my dataframe 'titanic_df' and used the head() function to print only the first 5 rows of the table to make sure it was made correctly.</p>

<p>Once the table printed correctly I began asking questions about the data.</p>

``` Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57e9a84c_titanic-data/titanic-data.csv'
titanic_df = pd.read_csv(filename)

## Print first 5 lines of dataframe
titanic_df.head()
```
