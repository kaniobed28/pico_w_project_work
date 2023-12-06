import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Load your data from CSV using Pandas
csv_path = 'example.csv'  # Replace with the path to your CSV file
csv_headers = ["temp", "humid"]
df = pd.read_csv(csv_path, header=None, names=csv_headers)
x_data, y_data = [], []

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo-', label='Live Data')  # Empty initial plot

# Set up the plot axis labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Live Plot Example')
ax.legend()

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot data
def update(frame):
    x_data.append(df['temp'].iloc[frame])
    y_data.append(df['humid'].iloc[frame])
    line.set_data(x_data, y_data)
    ax.relim()  # Update the limits of the axes
    ax.autoscale_view(True, True, True)  # Autoscale the view
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True)

# Show the live plot
plt.show()
