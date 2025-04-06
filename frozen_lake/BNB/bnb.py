import gym
import numpy as np
import heapq
import time
from utils import start_timer, stop_timer, log_performance
from gym.envs.toy_text.frozen_lake import generate_random_map

# Generate random 4x4 map and create environment
random_map = generate_random_map(size=4)
print("Generated Map:")
for row in random_map:
    print(' '.join(row))
print("\n")

env = gym.make("FrozenLake-v1", desc=random_map, is_slippery=True)
grid_size = 4
goal_state = env.observation_space.n - 1

def state_to_xy(state):
    return divmod(state, grid_size)

def manhattan_distance(state):
    sx, sy = state_to_xy(state)
    gx, gy = state_to_xy(goal_state)
    return abs(sx - gx) + abs(sy - gy)

def branch_and_bound(env, timeout=600):
    visited = set()
    pq = []
    heapq.heappush(pq, (manhattan_distance(0), 0, [0], 0))

    start_time = time.time()

    while pq:
        if time.time() - start_time > timeout:
            print(" Timeout! Goal not reached within time limit.")
            return None, None

        _, cost, path, state = heapq.heappop(pq)

        if state == goal_state:
            return path, cost

        if state in visited:
            continue
        visited.add(state)

        for action in range(env.action_space.n):
            for prob, next_state, reward, _ in env.env.P[state][action]:
                if prob == 0.0:  # Skip impossible transitions
                    continue
                    
                x, y = state_to_xy(next_state)
                tile = env.unwrapped.desc[x][y]
                
                # Skip holes and already visited states
                if tile == b'H' or next_state in visited:
                    continue
                    
                priority = cost + 1 + manhattan_distance(next_state)
                heapq.heappush(pq, (priority, cost + 1, path + [next_state], next_state))

    return None, None

if __name__ == "__main__":
    successful_path = None
    for run in range(1, 11):
        env.reset()
        start = start_timer()

        path, cost = branch_and_bound(env, timeout=600)
        time_taken = stop_timer(start)

        reward = 1 if path else 0
        convergence = path[-1] if path else "None"

        print(f"Run {run} | Time: {time_taken:.4f}s | Cost: {cost} | Path: {path}")

        if path and reward == 1:
            successful_path = path  # Store the first successful path

        log_performance(
            filepath="results.csv",
            algorithm="Branch and Bound",
            run_id=run,
            time_taken=time_taken,
            reward=reward,
            convergence_point=str(convergence),
            path=path,
            cost=cost
        )
    
    # Save the successful path and map for the GIF generation
    if successful_path:
        with open("successful_path.txt", "w") as f:
            f.write(f"MAP:\n{random_map}\n")
            f.write(f"PATH:\n{successful_path}\n")
        print(f"\n Successful path saved to 'successful_path.txt'")
    else:
        print("\n No successful path found in 10 runs")