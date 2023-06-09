from worldometer import api
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Function to update the data
def update_data(frame):
    api.update_metrics()
    # Get the population data from the get_population() function
    population_data = api.current_world_population() # The get_population() function returns a dictionary
    # Get the list of population values
    population_values = list(population_data.values())
    # Get the current time
    now = datetime.now()


    # Format the new time
    current_time = now.strftime("%H:%M:%S")
    # Update the plot data
    x_data.append(current_time)
    y_data.append(population_values[-1])  # Get the latest value

    # Redraw the plot
    ax.clear()
    ax.plot(x_data, y_data)

    # Set the title and axis labels
    ax.set_title("World Population Chart")
    ax.set_xlabel("Time")
    ax.set_ylabel("Population (billions)")

    # Set the x-axis limit to show the most recent data
    ax.set_xlim(max(0, len(x_data) - 5), len(x_data))
    # Set the y-axis limit based on the current data
    ax.set_ylim(max(y_data)-500, max(y_data)+500)

    # Calculate the population change compared to the previous second
    population_change = y_data[-1] - y_data[-2]

    # Set the title to display the population change
    ax.set_title(f"World Population Chart: {y_data[-1]}\nChange: +{population_change} people/time")


# Initialize the plot
fig, ax = plt.subplots()

# Initialize the data
t = api.current_world_population()
l = t["current_world_population"]
x_data = []
y_data = []
x_data.append(l)
y_data.append(l)

# Create the animation object
ani = animation.FuncAnimation(fig, update_data, interval=1000) # Update every second (1000ms)

# Display the plot
plt.show()


