import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats


#first, loading the data
df = pd.read_csv("test_set.csv")
# this test dataset has flow_distance, elevation, drainage_area as columns

# getting the stats
# it bins my data by flow distance and calculate the median elevation for each of my bins. In this case I have 12 bins
medians, bin_edges, number = stats.binned_statistic(df["flow_distance"].values, df["elevation"].values, statistic='median', bins=12)

# Creating a figure
fig, ax = plt.subplots()

# First I am plotting ALL the points in grey
ax.scatter(df["flow_distance"], df["elevation"], lw =0, s = 10, c = "grey", label = "original points")
# Now plotting the mdian for each bins in red (note that 1 more edge point so I need to ignore the frst or the last)
ax.scatter(bin_edges[:-1], medians, lw = 0, c = "red", s =50, label = "Median points")

ax.legend()
ax.set_xlabel("Flow distance")
ax.set_ylabel("Elevation")

plt.savefig("test_binned_stat.png", dpi = 300 )