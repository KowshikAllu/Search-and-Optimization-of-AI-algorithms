import numpy as np
import random
import threading
import time
import os
from Problem import ProblemInstance, compute_length
from utils import start_timer, stop_timer, log_performance, TimeoutException

class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds
        self.timer = None

    def handle_timeout(self):
        raise TimeoutException()

    def __enter__(self):
        self.timer = threading.Timer(self.seconds, self.handle_timeout)
        self.timer.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.timer:
            self.timer.cancel()

def heuristic(tour, dist_matrix):
    total_length = compute_length(tour, dist_matrix)
    max_edge = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_length + 0.01 * max_edge

def hill_climb(problem, max_iter=10000):
    n = problem.nPoints
    dist_matrix = problem.dist_matrix

    def get_neighbors(tour):
        neighbors = []
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new_tour = tour.copy()
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                neighbors.append(new_tour)
        return neighbors

    current_tour = list(range(n))
    random.shuffle(current_tour)

    current_length = compute_length(current_tour, dist_matrix)
    convergence = [current_length]

    for iteration in range(max_iter):
        neighbors = get_neighbors(current_tour)
        if not neighbors:
            break

        next_tour = min(neighbors, key=lambda t: heuristic(t, dist_matrix))
        next_length = compute_length(next_tour, dist_matrix)

        if next_length < current_length:
            current_tour = next_tour
            current_length = next_length
            convergence.append(current_length)
        else:
            break

    return current_tour, current_length, convergence

if __name__ == '__main__':
    problem = ProblemInstance("eil76.tsp")
    runs = 5
    timeout_seconds = 600  # 10 minutes

    if not os.path.exists("frames"):
        os.makedirs("frames")

    best_overall_tour = None
    best_overall_dist = float('inf')
    all_times = []

    for run in range(1, runs + 1):
        try:
            with Timeout(timeout_seconds):
                print(f"\n--- Starting Run {run} ---")
                start_time = start_timer()

                current_tour, current_dist, convergence = hill_climb(problem)

                elapsed = stop_timer(start_time)
                all_times.append(elapsed)

                if current_dist < best_overall_dist:
                    best_overall_dist = current_dist
                    best_overall_tour = current_tour
                    np.savetxt("best_tour.txt", best_overall_tour, fmt='%d')

                print(f"Run {run} completed:")
                print(f"Distance: {current_dist:.2f}")
                print(f"Time: {elapsed:.2f}s")
                print(f"Convergence: {convergence[-1]:.2f}")

                log_performance(
                    filepath="results.csv",
                    algorithm="HillClimbing",
                    run_id=run,
                    time_taken=elapsed,
                    cost=current_dist,
                    reward=1,
                    convergence_point=convergence[-1],
                    path=",".join(map(str, current_tour))
                )
        except TimeoutException:
            print(f"Run {run} timed out after {timeout_seconds//60} minutes")
            log_performance(
                filepath="results.csv",
                algorithm="HillClimbing",
                run_id=run,
                time_taken=timeout_seconds,
                cost=-1,
                reward=0,
                convergence_point=-1,
                path="None")
        except Exception as e:
            print(f"An error occurred during Run {run}: {e}")

    if best_overall_tour is not None:
        print("\n=== Best Solution ===")
        print(f"Distance: {best_overall_dist:.2f}")
        print(f"Average Time: {np.mean(all_times):.2f}s")
        print(f"Best Tour: {best_overall_tour}")
        print(f"Convergence: {convergence[-1]:.2f}")    
    else:
        print("\nNo valid solution found in any run!")
