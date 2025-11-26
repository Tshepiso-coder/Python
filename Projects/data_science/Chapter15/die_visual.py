import plotly.express as px

from die import Die

# ===============================================================
# CODE SUMMARY FROM clause.ai
# This code simulates rolling a six-sided die 1,000 times and visualizes the results.

# **What it does:**
# 1. **Rolls the die:** Creates a `Die` object and rolls it 1,000 times, storing each result
# 2. **Tracks frequency:** Counts how many times each number (1-6) appears using a `frequency` list
# 3. **Calculates proportions:** Converts the frequencies to proportions (percentages as decimals rounded to 2 places)
# 4. **Visualizes results:** Creates a bar chart using Plotly showing how often each die face appeared

# The visualization helps demonstrate that with enough rolls, 
# each number should appear roughly equally often (about 16.7% or 1/6 of the time), 
# illustrating the law of large numbers and fair die probability.
# ===============================================================

# Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []

frequency = [0, 0, 0, 0, 0, 0]

prop = []

for roll_num in range(1_000):
    result = die.roll()
    results.append(result)
    frequency[result - 1] += 1
    


for val in frequency:
    prop.append(round(val/sum(frequency), 2))
    
print(f"PROPORTIONS: {prop}")

poss_results = [val for val in range(1, die.num_sides+1)]
# print(results)

print(f"FREQUECY: {frequency}")
print(f"POSS_RESULTS: {poss_results}")

# Visualise the result
title = "Results of rolling One D6 ,1000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequency, title=title, labels=labels)
fig.show()


