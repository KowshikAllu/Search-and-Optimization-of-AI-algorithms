import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ast import literal_eval

# Read the successful path and map from file
try:
    with open("ida_successful_path.txt", "r") as f:
        content = f.read().split('\n')
        map_str = content[1].strip()
        path_str = content[3].strip()
        
        random_map = literal_eval(map_str)
        path = literal_eval(path_str)
except FileNotFoundError:
    print("Error: 'ida_successful_path.txt' not found. Run ida.py first to generate a successful path.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Create environment with the same map
env = gym.make("FrozenLake-v1", desc=random_map, is_slippery=False)
desc = env.unwrapped.desc.astype(str)
grid_size = 4

# Verify path doesn't go through holes
valid_path = []
for state in path:
    x, y = divmod(state, grid_size)
    tile = desc[x][y]
    if tile == 'H':
        print(f" Warning: Removing hole at state {state} (position {x},{y})")
    else:
        valid_path.append(state)

if not valid_path:
    print(" Error: No valid states remaining in path")
    exit()

print(f"Using path: {valid_path}")

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("IDA* Search Path Visualization")
plt.xticks(np.arange(-0.5, grid_size, 1), [])
plt.yticks(np.arange(-0.5, grid_size, 1), [])
ax.grid(which='major', color='gray', linestyle='-', linewidth=1)
ax.set_xlim(-0.5, grid_size - 0.5)
ax.set_ylim(-0.5, grid_size - 0.5)
ax.invert_yaxis()  # To match FrozenLake coordinates (0,0 at top-left)

# Draw the grid
colors = {'S': 'lightblue', 'F': 'white', 'H': 'black', 'G': 'lightgreen'}
for i in range(grid_size):
    for j in range(grid_size):
        tile = desc[i][j]
        rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, 
                            facecolor=colors.get(tile, 'gray'), 
                            edgecolor='black')
        ax.add_patch(rect)
        ax.text(j, i, tile, ha='center', va='center', 
               fontsize=14, fontweight='bold')

# Create agent marker
agent_dot = plt.Circle((0, 0), 0.3, color='red', zorder=10)
ax.add_patch(agent_dot)

def update(frame):
    if frame >= len(valid_path):
        return agent_dot,
    x, y = divmod(valid_path[frame], grid_size)
    agent_dot.center = (y, x)
    return agent_dot,

ani = animation.FuncAnimation(
    fig, update, frames=len(valid_path)+1, interval=800, blit=True, repeat=False
)

plt.tight_layout()
ani.save("ida_frozenlake.gif", writer='pillow', fps=1.5, dpi=100)
print(" GIF saved as 'ida_frozenlake.gif'")
plt.show()