import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Read csv into dataframe

filename = 'https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57e9a84c_titanic-data/titanic-data.csv'
titanic_df = pd.read_csv(filename)

# Print first 5 lines of dataframe
#titanic_df.head()

# I split the original datafram into 'mens_df' and 'womens_df'

%pylab inline

mens_df = titanic_df[(titanic_df['Sex'] == 'male')]
womens_df = titanic_df[(titanic_df['Sex'] == 'female')]

# I found the combination of age and sex that had the highest number of survivors

male_age_mode = mens_df.groupby('Age').sum()['Survived'].idxmax()
sum_male_age = mens_df.groupby('Age').sum()['Survived'].max()
female_age_mode = womens_df.groupby('Age').sum()['Survived'].idxmax()
sum_female_age = womens_df.groupby('Age').sum()['Survived'].max()

if sum_male_age > sum_female_age:
    print '{} year old males had the most survivals.' .format(male_age_mode)

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
else:
    print '{} year old females had the most survivals.' .format(female_age_mode)

# How many survivors did each cabin section and ticket fare have?

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

# Plotting number of survivors as a function of cabin section and ticket fare

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
