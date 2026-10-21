import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 3], [2, 4, 6], "r--")
ax.plot([1, 2, 3], [3, 2, 1], "g-")
ax.set_title("Example plot")
plt.show()

# 1. Does this code create one plotting panel (Axes object) or two?
# Explain briefly. A panel is a plotting area, not an individual x-axis or y-axis.
# Your answer:
#1. the plt.subplots(1, 1) command specifies a grid of 1 row and 1 column that returns a single plotting area (ax). both data lines are plotted on this exact same panel.

# 2. How many data lines are drawn? What are the y-values of the red dashed line?
# Your answer:
#2 data lines are drawn, the y-values of the red dashed line ("r--") are [2, 4, 6].