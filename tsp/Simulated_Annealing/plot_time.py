import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("simanneal_results.csv")
filtered = data[data["TimeTaken"] < 600]

plt.plot(filtered["Run"], filtered["TimeTaken"], marker='o', label='Time (s)')
plt.axhline(y=filtered["TimeTaken"].mean(), color='r', linestyle='--', label=f'Avg Time = {filtered["TimeTaken"].mean():.2f}s')
plt.title("Execution Time per Run - Simulated Annealing")
plt.xlabel("Run")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.savefig("simulated_annealing_times.png")
plt.show()
