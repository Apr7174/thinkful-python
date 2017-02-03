import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

#split data based on new line
# data.split('\n')
data = data.splitlines()

#split each item using the commas
data = [i.split(',') for i in data]

#create a pandas dataframe
column_names = data[0] #this is the first row
data_rows = data[1::] #these are all the following rows
df = pd.DataFrame(data_rows, columns=column_names)

print(df)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alcMean = df['Alcohol'].mean() 
print("The mean of Alcohol is {0}".format(alcMean))
# 5.4436363636363634

alcMedian = df['Alcohol'].median() 
print("The median of Alcohol is {0}".format(alcMedian))
# 5.63

# If all numbers occur equally often, stats.mode() will return the smallest number
alcMode = stats.mode(df['Alcohol']) 
print("The mode of Alcohol is {0}".format(alcMode))
# 4.02

df['Tobacco'].mean() 
# 3.6181818181818186
df['Tobacco'].median() 
# 3.53
stats.mode(df['Tobacco']) 
# 2.71

alcRange = max(df['Alcohol']) - min(df['Alcohol'])
print('The range of alcohol is {0}'.format(alcRange))
# 2.4500000000000002

alcStd = df['Alcohol'].std() 
print('The standard deviation of alcohol is {0}'.format(alcStd))
# 0.79776278087252406

alcVar = df['Alcohol'].var() 
print('The variance of Alcohol is {0}'.format(alcVar))
# 0.63642545454546284

max(df['Tobacco']) - min(df['Tobacco'])
# 1.8499999999999996
df['Tobacco'].std() 
# 0.59070835751355388
df['Tobacco'].var() 
# 0.3489363636363606