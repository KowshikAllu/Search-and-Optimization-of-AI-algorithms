import time
import csv
import os

def start_timer():
    return time.time()

def stop_timer(start):
    return time.time() - start

def log_performance(filepath, algorithm, run_id, time_taken, reward, convergence_point, path, cost):
    file_exists = os.path.isfile(filepath)
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Algorithm', 'Run', 'TimeTaken', 'Reward', 'ConvergencePoint', 'Path', 'Cost'])
        writer.writerow([algorithm, run_id, time_taken, reward, convergence_point, path, cost])
