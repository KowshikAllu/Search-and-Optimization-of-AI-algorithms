import imageio
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from tqdm import tqdm

def create_enhanced_frame(tour, points, frame_num, total_frames):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Set up plot boundaries with padding
    x_coords = points[:, 1].astype(float)
    y_coords = points[:, 2].astype(float)
    padding = max(x_coords.max()-x_coords.min(), y_coords.max()-y_coords.min()) * 0.1
    ax.set_xlim(x_coords.min()-padding, x_coords.max()+padding)
    ax.set_ylim(y_coords.min()-padding, y_coords.max()+padding)
    ax.set_aspect('equal')
    
    # Plot all cities
    ax.scatter(x_coords, y_coords, color='navy', s=100, zorder=3)
    
    # Label cities
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        ax.annotate(str(i), (x, y), textcoords="offset points",
                    xytext=(0,5), ha='center', fontsize=8)

    # Draw completed path segments
    for i in range(min(frame_num, len(tour)-1)):
        start = points[tour[i]]
        end = points[tour[i+1]]
        ax.plot([float(start[1]), float(end[1])], 
                [float(start[2]), float(end[2])],
                color='crimson', linewidth=2, zorder=2)

    # Draw moving agent
    if frame_num < len(tour):
        current = points[tour[frame_num]]
        agent = Circle((float(current[1]), float(current[2])), 1.0,
                      color='gold', ec='black', lw=1, zorder=4)
        ax.add_patch(agent)

    # Complete the tour on final frame
    if frame_num >= len(tour):
        start = points[tour[-1]]
        end = points[tour[0]]
        ax.plot([float(start[1]), float(end[1])],
                [float(start[2]), float(end[2])],
                color='crimson', linewidth=2, zorder=2)

    ax.set_title(f"TSP Hill Climbing Solution\nStep {min(frame_num, len(tour))}/{len(tour)}")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.grid(True, alpha=0.3)

    os.makedirs("frames", exist_ok=True)
    frame_path = f"frames/frame_{frame_num:03d}.png"
    plt.savefig(frame_path, dpi=100, bbox_inches='tight')
    plt.close()
    return frame_path

def generate_enhanced_gif(tour, points, output="hill_climb.gif"):
    if not tour or len(tour) != len(points):
        raise ValueError("Invalid tour or points data")

    print("\nGenerating visualization...")
    frame_paths = []
    total_frames = len(tour) + 2  # Include start and complete loop
    
    for frame_num in tqdm(range(total_frames)):
        try:
            frame_paths.append(create_enhanced_frame(tour, points, frame_num, total_frames))
        except Exception as e:
            print(f"Error generating frame {frame_num}: {e}")
            continue

    try:
        # Create GIF with pause at end
        images = [imageio.imread(path) for path in frame_paths]
        images.extend([images[-1]] * 5)  # Pause on final frame
        imageio.mimsave(output, images, fps=3)
        print(f"\n GIF saved as '{output}'")
    except Exception as e:
        print(f" Error creating GIF: {e}")
    finally:
        # Clean up frames
        for path in frame_paths:
            try:
                os.remove(path)
            except:
                pass

if __name__ == "__main__":
    from Problem import ProblemInstance
    
    try:
        problem = ProblemInstance("eil76.tsp")
        best_tour = [int(i) for i in np.loadtxt("best_tour.txt")]
        generate_enhanced_gif(best_tour, problem.points)
    except Exception as e:
        print(f" Error: {e}")