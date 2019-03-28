# https://python-graph-gallery.com/392-use-faceting-for-radar-chart/
#
#
#             per_noun     per_verb     per_adj     per_adverb
# style               
# Brief      17.002634     15.777084    8.644375    8.481646
# Drama      19.185251     15.481722    7.189818    5.680463
# Epik       19.238434     16.858595    8.374700    7.617986
# Gedicht    21.907033     12.396593    8.606924    5.365494
# Historie   21.881628     14.877931    9.522846    6.572920
# Nacherz    19.111306     14.417974    7.146650    6.682052
# Philo      20.600199     15.153603    9.831002    8.378756
#
#
#

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = pd.DataFrame({
'Werkart': ['Gedicht', 'Philo', 'Drama', 'Epik', 'Nacherz', 'Historie', 'Brief'],
'Substantive': [8.6, 9.8, 7.2, 8.4, 7.1, 9.5, 8.6],
'Verben': [5.4, 8.4, 5.7, 7.6, 6.7, 6.6, 8.5],
'Adjektive': [ 21.9, 20.6, 19.2, 19.2, 19.1, 21.9, 17],
'Adverben': [12.4, 15.2, 15.5, 16.9, 14.4, 14.9, 15.8]
})

df2 = df[['Substantive', 'Verben', 'Adjektive', 'Adverben']]
# ------- PART 1: Define a function that do a plot for one line of the dataset!


def make_spider( row, title, color):
    # number of variable
    categories=list(df2)
    N = len(categories)
 
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
 
    # Initialise the spider plot
    ax = plt.subplot(3,3,row+1, polar=True )
 
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
 
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=7)
    plt.tight_layout()
 
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,40)
 
    # Ind1
    values=df.loc[row].drop('Werkart').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
 
    # Add a title
    plt.title(title, size=12, color=color, y=1.2)
    # some spacing in between
    plt.tight_layout()


# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
plt.show()

# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title=df['Werkart'][row], color=my_palette(row))

