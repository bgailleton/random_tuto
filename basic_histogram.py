# These two lines deactivate GUI from matplotlib.
# It disable plt.show() so uncomment if you plan to use it
# However some settings does not support GUI and won't let you import matplotlib if these lines are not there
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as bamboo_bears

# Loading the data
df = bamboo_bears.read_csv("test_set.csv", sep = ",")

####
# Here you can process your data
####

# Creating the figure = the background and size
fig = plt.figure(figsize = (3.5,2.7), facecolor = "white")

# Change that if you need several axis
gs = plt.GridSpec(100,100,bottom=0.15,left=0.10,right=0.90,top=0.95)
ax = fig.add_subplot(gs[0:100,0:100], facecolor = "None")

# Plotting whatever, all the options are explained there -> https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.hist.html
## Here I used common parameters to custoise:
## bins: number of bins // facecolor: the color of the bars // edgecolor: the color of the contouring lines
## lw: the width of contour lines // density: normalised to 1 if True // histtype: define the style, here: vertical bars with only the external contours
ax.hist(df["delta_ksn"],bins = 80, facecolor = "gray", edgecolor = "k", lw = 0.5, density = True, histtype = "stepfilled")

# Changing the axis titles
ax.set_xlabel(r"$\Delta k_{sn}$") # r+ $$ tells matplotlib to use LaTex style compiler for mathematical expression
ax.set_ylabel("Frequency")

# Changing the axis ticks location
ax.set_xticks([-5,0,5])
# Changing the axis ticks texts
ax.set_xticklabels(["minus five,zero,five"])

# saving the figure
plt.savefig("basic_histogram.png", dpi = 500)
