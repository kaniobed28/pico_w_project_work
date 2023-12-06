import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd

data_path = "example.csv"

fig = plt.figure()
ax1= fig.add_subplot(1,1,1)


def animate(i):
    csv_path = data_path 
    csv_headers = ["temp", "humid","date"]
    df = pd.read_csv(csv_path, header=None, names=csv_headers)


    average_temp = df["temp"].mean()
    min_temp = df["temp"].min()
    max_temp = df["temp"].max()
    ax1.clear()
    
    ax1.scatter(df["date"],df["temp"], label= 'temperature',c='g')

    ax1.set_xlabel("Time")
    ax1.set_title(f"Average temp: {average_temp} max temp: {max_temp} min temp: {min_temp}")

    ax1.set_xticks([])
    ax1.legend()

ani = animation.FuncAnimation(fig,animate,interval = 1000)
plt.show()