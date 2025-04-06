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

def simulated_annealing(problem, max_iter=10000, initial_temp=1000, cooling_rate=0.995):
    n = problem.nPoints
    dist_matrix = problem.dist_matrix

    def swap_two(tour):
        a, b = random.sample(range(n), 2)
        tour[a], tour[b] = tour[b], tour[a]
        return tour

    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_length = compute_length(current_tour, dist_matrix)
    best_tour = current_tour[:]
    best_length = current_length
    convergence = [current_length]

    temp = initial_temp

    for _ in range(max_iter):
        candidate = current_tour[:]
        candidate = swap_two(candidate)
        candidate_length = compute_length(candidate, dist_matrix)

        delta = candidate_length - current_length
        if delta < 0 or random.random() < np.exp(-delta / temp):
            current_tour = candidate
            current_length = candidate_length

            if current_length < best_length:
                best_tour = current_tour[:]
                best_length = current_length

        convergence.append(best_length)
        temp *= cooling_rate

    return best_tour, best_length, convergence

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

                current_tour, current_dist, convergence = simulated_annealing(problem)

                elapsed = stop_timer(start_time)
                all_times.append(elapsed)

                if current_dist < best_overall_dist:
                    best_overall_dist = current_dist
                    best_overall_tour = current_tour
                    np.savetxt("best_sa_tour.txt", best_overall_tour, fmt='%d')

                print(f"Run {run} completed:")
                print(f"Distance: {current_dist:.2f}")
                print(f"Time: {elapsed:.2f}s")
                print(f"Convergence: {convergence[-1]:.2f}")

                log_performance(
                    filepath="simanneal_results.csv",
                    algorithm="SimulatedAnnealing",
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
                filepath="simanneal_results.csv",
                algorithm="SimulatedAnnealing",
                run_id=run,
                time_taken=timeout_seconds,
                cost=-1,
                reward=0,
                convergence_point=-1,
                path="None"
            )
        except Exception as e:
            print(f"An error occurred during Run {run}: {e}")

    if best_overall_tour is not None:
        print("\n=== Best Solution ===")
        print(f"Distance: {best_overall_dist:.2f}")
        print(f"Average Time: {np.mean(all_times):.2f}s")
    else:
        print("\nNo valid solution found in any run!")
