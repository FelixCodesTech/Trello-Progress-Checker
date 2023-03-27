import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
data = pd.read_csv('data.csv')

# Create a line chart
plt.plot(data['Time'], data['Progress']*100)

# Fill the area below the line chart with red color
plt.fill_between(data['Time'], data['Progress']*100, color='blue', alpha=0.2)

# Set the x-axis to start at one
plt.xlim(left=1, right=data['Time'].iloc[-1])

# Set the y-axis to end at one
plt.ylim(bottom=0, top=100)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Progress in %')
plt.title('Development Progress')

# Show the chart
plt.show()