import plotly.express as px

from die import Die

# ===============================================================
# CODE SUMMARY FROM clause.ai
# This code simulates rolling two dice together (a D6 and a D10) 1,000 times and analyzes the distribution of their combined sums.

# **What it does:**
# 1. **Creates two dice:** A standard 6-sided die and a 10-sided die
# 2. **Rolls and sums:** Rolls both dice 1,000 times, adding their results together (possible sums range from 2 to 16)
# 3. **Tracks frequency:** Counts how often each sum appears
# 4. **Calculates proportions:** Converts frequencies to proportions rounded to 2 decimal places
# 5. **Visualizes results:** Creates a bar chart showing the distribution of sums, with x-axis ticks at every integer
# 6. **Saves the chart:** Exports the visualization as an HTML file

# **Key insight:** Unlike a single die where all outcomes are equally likely,
# the sum of two dice creates a non-uniform distribution. Middle values (like 7-9) appear more frequently 
# because there are more combinations that produce them, while extreme values (2 and 16) are rare
# since they can only occur one way each.

# **Note:** The title says "Two D6" but the code actually uses a D6 and D10.
# ===============================================================

# Create a D6 and a D10 dice.
die_1 = Die()
die_2 = Die(10)
# Make some rolls, and store results in a list.
results = []

frequency = [0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

prop = []

for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    frequency[result - 1] += 1    


for val in frequency:
    prop.append(round(val/sum(frequency), 2))
    
print(f"PROPORTIONS: {prop}")

max_result = die_1.num_sides + die_2.num_sides

poss_results = [val for val in range(1, max_result + 1)]
# print(results)

print(f"FREQUECY: {frequency}")
print(f"POSS_RESULTS: {poss_results}")

# Visualise the result
title = "Results of rolling Two D6 ,1000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequency, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html("dice_visual_d6d6.html")


