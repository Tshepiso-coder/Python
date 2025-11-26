import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x **2 for x in x_values]

# # for LOOP ABOVE LONG METHOD
# for x in x_values:
#     y_values.append(x**2)

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
# ax.scatter(2,4, s=200)
# ax.scatter(x_values, y_values, color="red", s=10)
# ax.scatter(x_values, y_values, color=(0.8,0,0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set a value for each axis
ax.axis([0, 1100, 0, 1_000_000])
ax.ticklabel_format(style="plain")

# Set chart title and label axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)
plt.show()
plt.savefig("squares_plot.png", bbox_inches="tight")