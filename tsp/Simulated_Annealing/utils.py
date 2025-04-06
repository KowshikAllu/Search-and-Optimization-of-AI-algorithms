# utils.py
import time
import csv
import os
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

def start_timer():
    return time.time()

def stop_timer(start_time):
    return time.time() - start_time

def log_performance(filepath, algorithm, run_id, time_taken, distance, convergence_point):
    cost = distance  # define it clearly if needed
    file_exists = os.path.isfile(filepath)
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Algorithm', 'Run', 'TimeTaken', 'Distance', 'ConvergencePoint', 'Cost'])
        writer.writerow([algorithm, run_id, time_taken, distance, convergence_point, cost])

