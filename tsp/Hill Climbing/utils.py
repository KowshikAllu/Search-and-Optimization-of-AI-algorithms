import time
import csv
import os

class TimeoutException(Exception):
    pass

def start_timer():
    """Returns a high-resolution timer"""
    return time.perf_counter()

def stop_timer(start_time):
    """Returns elapsed time in seconds"""
    return time.perf_counter() - start_time

def log_performance(filepath, algorithm, run_id, time_taken, cost, reward, convergence_point, path):
    """Logs performance metrics to CSV file"""
    file_exists = os.path.isfile(filepath)
    
    with open(filepath, 'a', newline='') as csvfile:
        fieldnames = [
            'Algorithm', 
            'Run', 
            'TimeTaken', 
            'Cost', 
            'Reward', 
            'ConvergencePoint', 
            'Path'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Algorithm': algorithm,
            'Run': run_id,
            'TimeTaken': f"{float(time_taken):.6f}",
            'Cost': f"{float(cost):.2f}" if str(cost) != 'None' else '-1',
            'Reward': int(reward),
            'ConvergencePoint': f"{float(convergence_point):.2f}" if str(convergence_point) != 'None' else '-1',
            'Path': str(path)
        })