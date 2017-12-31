import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')

average_calorie = np.mean(calorie_stats)

calorie_stats_sorted = np.sort(calorie_stats)

median_calorie = np.median(calorie_stats)

under_100 = np.percentile(calorie_stats, 39)

high_calorie = np.mean(calorie_stats >= 100)

calorie_std = np.std(calorie_stats)

first_quartile = np.percentile(calorie_stats, 25)
third_quartile = np.percentile(calorie_stats, 75)
interquartile_range = third_quartile - first_quartile


# The data contains a large distribution from 50 to 160, however over 83% of the data is above 100, which makes the results below relatively inaccurate. Looking at the interquartile range, it is only 10. That means that for the vast majority of the data, the difference is only 10 and there are a high number of outliers figured into the data, meaning that the outliers are far departures from the norm and should be evaluated as to the cause.

print interquartile_range
