import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

ida_df = df[df['Algorithm'] == 'IDA*']

if ida_df.empty:
    print("No data found for IDA* in results.csv")
else:
    # Calculate statistics
    avg_time = ida_df['TimeTaken'].mean()
    success_rate = ida_df['Reward'].mean() * 100
    
    print(f"Average Time Taken: {avg_time:.5f} seconds")
    print(f"Success Rate: {success_rate:.1f}%")

    # Create plot
    plt.figure(figsize=(12, 6))
    
    # Time taken plot
    plt.subplot(1, 2, 1)
    plt.bar(ida_df['Run'], ida_df['TimeTaken'], color='blue')
    plt.axhline(avg_time, color='red', linestyle='--', label=f'Avg: {avg_time:.5f} s')
    plt.title("IDA* - Time Taken per Run")
    plt.xlabel("Run")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.grid(True)