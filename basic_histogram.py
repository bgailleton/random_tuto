import matplotlib
matplotlib.use("Agg")
## Uncomment the two first lines if you are working on the server
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

# Plotting whatever
ax.hist(df["delta_ksn"],bins = 80)

# Changing the axis titles
ax.set_xlabel(r"$\Delta k_{sn}$")
ax.set_ylabel("Frequency")

# Changing the axis ticks location
ax.set_xticks([-5,0,5])
# Changing the axis ticks texts
ax.set_xticklabels(["minus five,zero,five"])

# saving the figure
plt.savefig("basic_histogram.png", dpi = 500)
