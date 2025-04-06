# AI Assignment 2

## Overview
This project implements various algorithms for solving optimization problems in two environments: Frozen Lake and the Traveling Salesman Problem (TSP). The algorithms included are Branch and Bound, Iterative Deepening A* (IDA*), Hill Climbing, and Simulated Annealing. The project also includes visualizations and results of the experiments conducted.


# ===== CORE DEPENDENCIES =====
pip install numpy==1.26.4 matplotlib==3.8.3 tqdm==4.66.1

# ===== FROZEN LAKE (BnB & IDA*) =====
pip install gymnasium==0.29.1 pygame==2.5.2 imageio==2.34.0
pip install gymnasium[toy-text]  # For rendering

# ===== TSP (Hill Climbing & SA) =====
pip install scipy==1.12.0 pandas==2.2.1 networkx==3.2.1

# ===== VERIFICATION =====
python -c "import gymnasium, numpy, scipy; print('All packages installed successfully')"

# ===== TROUBLESHOOTING (if needed) =====
# For Mac:
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer

# For Linux:
sudo apt-get install python3-pygame

# For Windows:
pip install --prefer-binary pygame.

## Project Structure
```
AI_ASSIGNMENT_2/
│
├── frozen_lake/             # Frozen Lake environment implementations
│ ├── BNB/                   # Branch and Bound algorithm
│ │ ├── bnb.py               # Main algorithm implementation
│ │ ├── bnb_gif.py           # GIF generation script
│ │ ├── bnb_frozenlake.gif   # output GIF
│ │ ├── bnb_avg_time.png     # Performance plot
│ │ ├── results.csv          # Performance metrics
│ │ ├── successful_path.txt  # Best path found
│ │ ├── utils.py             # Utility functions
│ │ └── plot_time.py         # Plotting script
│ │
│ └── IDA/                   # IDA* algorithm
│ ├── ida.py                 # Main algorithm implementation
│ ├── ida_gif.py             # GIF generation script
│ ├── ida_frozenlake.gif     # Sample output GIF
│ ├── ida_time_plot.png      # Performance plot
│ ├── results.csv            # Performance metrics
│ ├── successful_path.txt    # Best path found
│ ├── utils.py               # Utility functions
│ └── plot_time.py           # Plotting script
│
├── tsp/                     # TSP environment implementations
│ ├── Hill_Climbing/         # Hill Climbing algorithm
│ │ ├── hill_climbing.py     # Main algorithm implementation
│ │ ├── generate_gif.py      # GIF generation script
│ │ ├── hill_climb.gif       # Sample output GIF
│ │ ├── hill_climbing_times.png # Performance plot
│ │ ├── eli76.tsp           # TSP problem instance
│ │ ├── best_tour.txt       # Best tour found
│ │ ├── results.csv         # Performance metrics
│ │ ├── Plots.py            # Plotting utilities
│ │ ├── Problem.py           # Problem definition
│ │ ├── utils.py             # Utility functions
│ │ └── plot_time.py        # Plotting script
│ │
│ └── Simulated_Annealing/      # Simulated Annealing algorithm
│ ├── simulated_annealing.py    # Main algorithm
│ ├── generate_gif.py           # GIF generation script
│ ├── simulated_annealing.gif   # Sample output GIF
│ ├── simulated_annealing_times.png # Performance plot
│ ├── eli76.tsp                 # TSP problem instance
│ ├── best_sa_tour.txt          # Best tour found
│ ├── simanneal_results.csv     # Performance metrics
│ ├── Plots.py                  # Plotting utilities
│ ├── Problem.py                # Problem definition
│ ├── utils.py                  # Utility functions
│ └── plot_time.py              # Plotting script
│
├── slides/                     # Presentation materials
│ ├── presentation.pdf          # Final presentation slides
│
│
└── README.md # This file
```

## Instructions to Run

######################################
# 🔹 AI Assignment 2 – RUNNING GUIDE 🔹
######################################

#  STEP 1: Install common dependencies (only once)
pip install numpy matplotlib imageio tqdm

##############################################################
# 1 BRANCH AND BOUND (FrozenLake) —  FrozenLake/BNB
##############################################################

#  Navigate to BNB folder
cd AI_Assignment_2/FrozenLake/BNB

#  Run the Branch and Bound algorithm
python bnb.py

#  Generate GIF of the best path
python bnb_gif.py

#  Plot time graph for performance analysis
python plot_time.py

#  Outputs:
# - results.csv → Reward & time
# - bnb_frozenlake.gif → Animation
# - bnb_time.png → Time plot
# - successful_path.txt → Path taken

##############################################################
# 2️ ITERATIVE DEEPENING A* (FrozenLake) —  FrozenLake/IDA
##############################################################

#  Navigate to IDA folder
cd ../IDA

#  Run the IDA* algorithm
python ida.py

#  Generate GIF of the best path
python ida_gif.py

#  Plot time graph for performance analysis
python plot_time.py

#  Outputs:
# - results.csv → Reward & time
# - ida_frozenlake.gif → Animation
# - ida_time_plot.png → Time plot
# - ida_performance.png → Reward trend
# - ida_successful_path.txt → Path taken

# @@ TSP Instance Used:
# - Dataset: eil76.tsp (standard benchmark TSP with 76 cities)

######################################################################
# 3️ HILL CLIMBING (Traveling Salesman Problem) —  TSP/Hill_Climbing
######################################################################

#  Navigate to Hill Climbing folder
cd ../../TSP/Hill_Climbing

#  Run Hill Climbing algorithm (5 executions with 10-min timeout each)
python hill_climbing.py

#  Generate GIF of final tour
python generate_gif.py

#  Plot average time taken over runs
python plot_time.py

#  Outputs:
# - best_tour.txt → Final city tour
# - hill_climb.gif → Tour animation
# - time_plot.png → Time performance
# - metrics.csv → Execution stats

###########################################################################
# 4️ SIMULATED ANNEALING (Traveling Salesman Problem) —  TSP/Simulated_Annealing
###########################################################################

#  Navigate to Simulated Annealing folder
cd ../Simulated_Annealing

#  Run Simulated Annealing algorithm (5 executions with 10-min timeout each)
python simulated_annealing.py

# Generate GIF of final tour
python generate_gif.py

#  Plot average time taken over runs
python plot_time.py

#  Outputs:
# - best_tour.txt → Final city tour
# - simulated_annealing.gif → Tour animation
# - time_plot.png → Time performance
# - metrics.csv → Execution stats


 **Slides Folder**
All generated GIFs and time plots for each algorithm are saved in the `Slides/` folder. 

click here to view slides

https://www.canva.com/design/DAGj2cgbZpw/TwvcAyNaCOIUJ87_xwVvPw/edit?utm_content=DAGj2cgbZpw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


###  Algorithms Overview

### Frozen Lake (Grid Navigation)

- **🔹 Branch and Bound (`bnb.py`)**  
  A systematic search strategy that **prunes unpromising paths** early, ensuring optimal pathfinding in the Frozen Lake environment.  
  *Located at*: `FrozenLake/BNB`

- **🔹 Iterative Deepening A* (`ida_star.py`)**  
  Combines the **memory efficiency of Depth-First Search** with the **heuristic optimality of A\***. It incrementally deepens the depth limit until the goal is reached.  
   *Located at*: `FrozenLake/IDA`

---

###  Traveling Salesman Problem (TSP)

- **🔹 Hill Climbing (`hill_climbing.py`)**  
  A greedy local search algorithm that incrementally improves a candidate solution by exploring neighbors. May get stuck in **local optima**, but works well for fast approximations.  
   Uses benchmark dataset: `eil76.tsp`  
   *Located at*: `TSP/Hill_Climbing`  
   Based on **ELITSP** problem instance.

- **🔹 Simulated Annealing (`simulated_annealing.py`)**  
  A metaheuristic that introduces randomness by accepting worse solutions with a probability that decreases over time (cooling schedule), helping escape local optima.  
   Uses benchmark dataset: `eil76.tsp`  
   *Located at*: `TSP/Simulated_Annealing`  
   Based on **ELITSP** problem instance.

---

###  Visualization and Reports

- All **GIF animations** of solution paths and **performance time plots** for each algorithm are stored in the  `Slides/` folder.
- These include:
  - **bnb_frozenlake.gif**
  - **ida_frozenlake.gif**
  - **hill_climb.gif**
  - **simulated_annealing.gif**
  - **time plots for all algorithms**


## License
This project is licensed under the MIT License - see the LICENSE file for details.