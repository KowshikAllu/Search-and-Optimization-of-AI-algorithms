import time
import csv
import os

def start_timer():
    return time.perf_counter()

def stop_timer(start_time):
    return time.perf_counter() - start_time

def log_performance(filepath, algorithm, run_id, time_taken, cost, reward, convergence_point, path):
    file_exists = os.path.isfile(filepath)

    with open(filepath, 'a', newline='') as csvfile:
        fieldnames = ['Algorithm', 'Run', 'TimeTaken', 'Cost', 'Reward', 'ConvergencePoint', 'Path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Algorithm': algorithm,
            'Run': run_id,
            'TimeTaken': time_taken,
            'Cost': cost,
            'Reward': reward,
            'ConvergencePoint': convergence_point,
            'Path': path
        })