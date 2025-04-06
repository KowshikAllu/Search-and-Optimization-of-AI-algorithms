import gym
import numpy as np
import time
from utils import start_timer, stop_timer, log_performance
from gym.envs.toy_text.frozen_lake import generate_random_map

# Generate random 4x4 map
random_map = generate_random_map(size=4)
env = gym.make("FrozenLake-v1", desc=random_map, is_slippery=False)
grid_size = 4
goal_state = env.observation_space.n - 1
TIMEOUT_SECONDS = 600

print("Generated Map:")
for row in random_map:
    print(' '.join(row))
print("\n")

def state_to_xy(state):
    return divmod(state, grid_size)

def manhattan_distance(state):
    sx, sy = state_to_xy(state)
    gx, gy = state_to_xy(goal_state)
    return abs(sx - gx) + abs(sy - gy)

def dfs(state, path, g, bound, visited, env, start_time):
    f = g + manhattan_distance(state)
    if time.time() - start_time > TIMEOUT_SECONDS:
        return "timeout", None
    if f > bound:
        return f, None
    if state == goal_state:
        return "found", path
        
    x, y = state_to_xy(state)
    tile = env.unwrapped.desc[x][y]
    if tile == b'H':  # Skip holes
        return float("inf"), None
        
    visited.add(state)
    min_bound = float("inf")

    for action in range(env.action_space.n):
        for prob, next_state, _, _ in env.env.P[state][action]:
            if prob == 0.0 or next_state in visited:
                continue
                
            result, new_path = dfs(next_state, path + [next_state], g + 1, bound, visited.copy(), env, start_time)
            if result == "found":
                return "found", new_path
            if result == "timeout":
                return "timeout", None
            if isinstance(result, (int, float)) and result < min_bound:
                min_bound = result
    return min_bound, None

def ida_star(env):
    bound = manhattan_distance(0)
    path = [0]
    start_time = time.time()
    while True:
        result, new_path = dfs(0, path, 0, bound, set(), env, start_time)
        if result == "found":
            return new_path, len(new_path) - 1, False
        if result == "timeout":
            return None, None, True
        if result == float("inf"):
            return None, None, False
        bound = result

if __name__ == "__main__":
    successful_path = None
    for run in range(1, 11):
        env.reset()
        start = start_timer()
        path, cost, is_timeout = ida_star(env)
        time_taken = stop_timer(start)

        reward = 1 if path else 0
        convergence = path[-1] if path else "Timeout" if is_timeout else "None"

        print(f"Run {run} | Time: {time_taken:.5f}s | Cost: {cost} | Path: {path}")

        if path and reward == 1 and successful_path is None:
            successful_path = path  # Store the first successful path

        log_performance(
            filepath="results.csv",
            algorithm="IDA*",
            run_id=run,
            time_taken=time_taken,
            cost=cost,
            reward=reward,
            convergence_point=str(convergence),
            path=path
        )
    
    # Save the successful path and map for the GIF generation
    if successful_path:
        with open("ida_successful_path.txt", "w") as f:
            f.write(f"MAP:\n{random_map}\n")
            f.write(f"PATH:\n{successful_path}\n")
        print(f"\nSuccessful path saved to 'ida_successful_path.txt'")
    else:
        print("\n No successful path found in 10 runs")