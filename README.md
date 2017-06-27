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
### What was the most common age and sex of a survivor?

<p>I split the original dataframe 'titanic_df' into separate dataframes for men and women.  I named them 'mens_df' and 'womens_df'.</p>

%pylab inline
import seaborn as sns

## Split data into male and female
## Create mens_df and womens_df
mens_df = titanic_df[(titanic_df['Sex'] == 'male')]
womens_df = titanic_df[(titanic_df['Sex'] == 'female')]

<p>Then I found the age that had the most survivors in male dataframe and the age that had the most survivors in the female dataframe.  I used an if statement to show the combination of age and sex had the highest number of survivors.  24 year old females had the highest number of survivals.</p>

male_age_mode = mens_df.groupby('Age').sum()['Survived'].idxmax()
sum_male_age = mens_df.groupby('Age').sum()['Survived'].max()
female_age_mode = womens_df.groupby('Age').sum()['Survived'].idxmax()
sum_female_age = womens_df.groupby('Age').sum()['Survived'].max()

if sum_male_age > sum_female_age:
    print '{} year old males had the most survivals.' .format(male_age_mode)
else:
    print '{} year old females had the most survivals.' .format(female_age_mode)
    
### What was the correlation between sex and survival of a passenger?

## Correlation function
def correlation(x, y):
    standardized_x = (x - x.mean())/(x.std(ddof = 0))
    standardized_y = (y - y.mean())/(y.std(ddof = 0))
    product = standardized_x * standardized_y
    correlation = product.mean()
    return correlation

## Replace male with 1 and female with 0
sex_num = titanic_df.replace(['male', 'female'], [1, 2]) 
print 'correlation between sex and survival:', correlation(sex_num['Sex'], sex_num['Survived'])

<p>I wrote a function to calculate the correlation between two variables and explored the correlation between a passenger's sex and their survival.  Values of correlation range from -1 to 1.  A value of 1 means that a passengers who were a particular sex also had a high number of survivals.  This is a strong positive correlation.  A value of -1 means that passengers who were a particular sex also had a low number of survivals.  This is a strong negative correlation.</p>

<p>The correlation between a passenger's sex and their survival was 0.54.  This means that there was a positive correlation between these variables and the strength of the correlation was almost exactly in the middle between strong and weak.  Although a passenger's sex did not determine their survival, there was a noticable difference between male and female survivals.</p>

### What age group had the most survivors for each sex?

<p>There were a lot of missing values in the age column of the male and female dataframes.  I printed the 5th and 6th rows of the dataframe as an example.  These values appeared in the table as "NaN" which is short for "not a number."</p>

titanic_df.loc[5:6]

<p> I used the pd.isnull() function to only show me the values in the age column that are not equal to a null value such as NaN.  The pd.cut() function was used to split the ages into bins for each age group.  These bins ranged from [-1, 9, 19, 29, ... 89] where each bin of the form [x, y] includes values in the interval (x,y].  For example, [-1, 9] includes the interval from 0 to 9.  Then I used dataframe.groupby() to sum the survivors in each age group for men and women.</p>

## Exclude NaN values in mens_df

mens_df = mens_df[pd.isnull(mens_df['Age']) != True]
womens_df = womens_df[pd.isnull(womens_df['Age']) != True]

## Put passengers into age groups using pd.cut()
## Each bin is in the form (x,y]
## Where y is included in the interval but x is not

bins = [-1, 9, 19, 29, 39, 49, 59, 69, 79, 89]
group_names = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
men_age_groups = pd.cut(mens_df['Age'], bins, labels=group_names)
women_age_groups = pd.cut(womens_df['Age'], bins, labels=group_names)

## I renamed the columns to get the correct legend on the graph

mens_df['Male Survivors'] = mens_df['Survived']
womens_df['Female Survivors'] = womens_df['Survived']

male_survivors_per_age_group = mens_df.groupby(men_age_groups).sum()['Male Survivors']
female_survivors_per_age_group = womens_df.groupby(women_age_groups).sum()['Female Survivors']

#male_survivors_per_age_group.describe()

fig = plt.figure() # Create matplotlib figure

width = 0.4

ax = male_survivors_per_age_group.plot(kind='bar', color='red', width=width, position=1, legend = True)
ax = female_survivors_per_age_group.plot(kind='bar', color='blue', width=width, position=0, legend = True)

fig.suptitle('Total Survivors per Age Group', fontsize = 15)

plt.xlabel('Age Group', fontsize=13)
plt.ylabel('Survivors', fontsize=13)

plt.show()

<p>Women had more survivors in each age group with the exception of small children.  This could be due to the policy of putting women and children on the life boats instead of men.  There were far less male survivors in each age group with the number of small male child survivors very close to the maximum of male survivors.  Women ages 20-39 made up the majority of female survivors and men ages 0-9, and 20-39 made up the majority of male survivors.  The largest gap between male and female survivors occured in men and women ages 10 through 19 where far more females survived.  I'm not sure what the age cut off for male children on life boats was but the gap in survivors in this age group could be correlated to it.</p>

<p>The mean number of male survivors in each age group was &mu; = 10.33 and the standard deviation was &sigma; = 9.80.  The values for the male's survivals had very little variation.  The mean number of female survivors in each age group was &mu; = 28.14 and the standard deviation was &sigma; = 17.95.  This tells us that more females in each age group survived and these values were more spread out than the males data.</p>

print 'Male data: \n', male_survivors_per_age_group.describe()
print 'Female data: \n', female_survivors_per_age_group.describe()

### How many survivors did each cabin section and ticket fare have?

<p>I started by only looking at the cabin sections and encountered two problems.  Of the 891 passenger rows in the dataframe, there were only 204 real values in the cabin number column.  The rest of the rows in the cabin column were NaN.  The second problem was that the cabin values were combinations of letters and strings.  I was only interested in the letters because those showed what section of the ship a passenger was in.  I printed four of the original values in the cabin number column as an example.</p>

titanic_df['Cabin'].loc[10:13]

<p>I used pd.isnull() again to exclude NaN values and grouped the number of survivors in each cabin by their cabin sections.  I made a new column to represent the cabin sections and titled it Cabin_Letter.  I used .str[:1] to only look at the 0th character in each string and grouped the survivors by their cabin letters.</p>

## Exclude NaN values for Cabin column
titanic_df = titanic_df[pd.isnull(titanic_df['Cabin']) != True]

## We have 891 passenger records but only 204 cabin records
print 'Number of rows containing cabin column values:', len(titanic_df)

## Take the first letter of each cabin to get the section each passenger was in.
titanic_df['Cabin Section'] = titanic_df['Cabin'].str[:1]

cabin_survivors = titanic_df.groupby('Cabin Section').sum()['Survived']

fig = plt.figure() # Create matplotlib figure

width = 0.4

ax = cabin_survivors.plot(kind = 'bar', width = 1.0)

fig.suptitle('Total Survivors per Cabin Section', fontsize=15)

plt.xlabel('Cabin Section', fontsize=13)
plt.ylabel('Survivors', fontsize=13)

plt.show()

cabin_survivors.describe()

<p>The histogram above shows the number of survivors in each cabin section.  Cabin sections B and C had the most survivors however, there was only a small amount of cabin data to work with.  Cabin sections A, F, G and T had the fewest survivors.  According to https://www.encyclopedia-titanica.org/cabins.html, a lot of the cabins in sections A through E were first class.  The rest of the cabins in sections E, F and G were a mix of second and third class.  Section T was a boat deck section that contained only one person.  If we are just looking at survivors as function of their cabin sections, it appears that most of the survivors were first class.  The standard deviation for the survivors in each section was 14.42 which means that the number of survivors in each cabin was very spread out.</p>

titanic_df['Cabin Section'].value_counts()

## Replace the letters A-G and T with numbers 1-8 so we can plot them easier
titanic_df['Cabin Section'] = titanic_df['Cabin Section'].replace(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T'], [1, 2, 3, 4, 5, 6, 7, 8])
titanic_df['Cabin Section']


fig = plt.figure() # Create matplotlib figure

width = 0.4
A
ax = plt.scatter(titanic_df['Cabin Section'], titanic_df['Fare'], s = ((titanic_df.groupby('Cabin Section').sum()['Survived'])*10), c = 'blue')
fig.suptitle('Total Survivors per Cabin Section and Ticket Fare', fontsize=15)
plt.xlabel('Cabin Section', fontsize=13)
plt.ylabel('Ticket Fare', fontsize=13)

plt.show()

<p>This plot is similar to the histogram above.  It includes the passenger's ticket fare as a second variable on the y axis and uses the number of survivors in each cabin section as the size of the data points.  The cabin section letters were changed to numbers where section A is 1 and section T is 8.  The smaller circle in the eighth cabin section with a fare around $50 means there were fewer survivors in that section with that ticket fare.  Although it is possible that cabin sections A-E contained a mix of classes, we can tell that most of the survivors had cheaper ticket fares.  Sections B and C had a mix of ticket fares and the remaining sections had only very cheap fares.  There were a small number of survivors with very expensive fares in section B and it is not clear what could have caused this.  Because the data on cabin sections is incomplete, it is difficult to draw conclusions regarding this issue.  There was a large range of ticket fares and it would be interesting to know more about which fares corresponded to first, second or third class and if there were any discounts received.</p>

### Conclusions

<p>My initial hypothesis was that age and class would play large role in whether or not a passenger survived.  I broadened my questions from inquiring about age and survival to sex and survival.  This allowed me to look at the demographic that had the most survivors.  When examining a passenger's status I chose to investigate their cabin sections and ticket fares.  I expected certain cabins to be associated with higher ticket fares, and others to lower ticket fares.</p>

<p>I expected age to be important when examining passengers who survived and did not find anything to surprising in that regard.  I was surprised at how large the disparity between male and female survivors was.  The majority of survivors were women and although I can speculate that this gap was so large because it was customary for men to sacrifice themselves for women and children, I cannot be sure.  I expected to find more of a seperation in ticket fares between the cabins but was surprised to seem them spread out among the various sections.  The majority of ticket fares for survivors were cheap.  It appears to be a connection between passengers who payed a cheaper ticket fare and survival, as well as female passengers aged 20-39 and survival.  It is possible that the port a passenger departed from affected their ticket price.  This would be a good next subject to tackle with this data.  We could use columns regarding ticket fares, ports departed from, and cabin sections to get a more detailed look at the seperation of classes aboard the titanic.</p>
