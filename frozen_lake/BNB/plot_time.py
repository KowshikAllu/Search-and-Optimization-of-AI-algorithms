import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("results.csv")

bnb_df = df[df['Algorithm'] == 'Branch and Bound']

bnb_df['TimeTaken'] = pd.to_numeric(bnb_df['TimeTaken'], errors='coerce')
bnb_df = bnb_df.dropna(subset=['TimeTaken'])  # Drop rows where TimeTaken couldn't be parsed

# Calculate average time
average_time = bnb_df['TimeTaken'].mean()
print(f"Average Time Taken: {average_time:.8f} seconds")

# Print cost and path for each run (optional for debugging/logging)
for idx, row in bnb_df.iterrows():
    print(f"Run {int(row['Run'])} | Time: {row['TimeTaken']:.6f}s | Cost: {row['Cost']} | Path: {row['Path']}")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(bnb_df['Run'], bnb_df['TimeTaken'], marker='o', label="Time per Run")
plt.axhline(y=average_time, color='r', linestyle='--', label=f"Avg Time = {average_time:.4f}s")
plt.xlabel("Run")
plt.ylabel("Time Taken (s)")
plt.title("Branch and Bound - Frozen Lake\nTime Taken per Run")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("bnb_avg_time.png")
plt.show()
