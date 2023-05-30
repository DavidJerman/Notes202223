import numpy as np
from minisom import MiniSom

# Generate some random data for demonstration
data = np.random.rand(400, 5)  # 100 samples, 5 features

# Define the SOM parameters
input_len = data.shape[1]  # Number of features in the input data
map_size = (20, 20)  # Size of the SOM grid

# Initialize the SOM
som = MiniSom(map_size[0], map_size[1], input_len, sigma=0.3, learning_rate=0.5)

# Train the SOM
som.train_random(data, 100)  # Train for 100 iterations using random order

# Get the winner neuron for each input sample
winners = np.array([som.winner(x) for x in data])

# Visualize the SOM grid and data points
import matplotlib.pyplot as plt

plt.figure(figsize=(map_size[0], map_size[1]))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Distance map as background
plt.colorbar()

# Mark the location of each data point's winner neuron on the SOM grid
for i, (x, y) in enumerate(winners):
    plt.plot(x + 0.5, y + 0.5, 'ro', marker='o', markersize=5, markeredgewidth=1)

plt.show()
