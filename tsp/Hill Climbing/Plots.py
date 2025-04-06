from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def getPoints(name_tsp):
    with open(name_tsp) as f_o:
            data= f_o.read()
            lines = data.splitlines()
    # store metadata set information 
    name = lines[0].split(' ')[1]
        # here we expect the name of the problem

    nPoints =  np.int(lines[3].split(' ')[1])
        # here we expect the number of points in the considered instance
        
#     best_sol = np.float(lines[5].split(' ')[1])
        # here the lenght of the best solution
        
        
        # read all data points and store them 
    points = np.zeros((nPoints, 3)) # this is the structure where we will store the pts data 
    for i in range(nPoints):
        line_i = lines[7 + i].split(' ')
        points[i, 0] = int(line_i[0])
        points[i, 1] = float(line_i[1])
        points[i, 2] = float(line_i[2])
    return points

def plotPoints(points, nPoints):
    plt.figure(figsize=(8, 8))
    plt.scatter(points[:, 1], points[:, 2])
    for i, txt in enumerate(np.arange(nPoints)):  # tour_found[:-1]
        plt.annotate(txt, (points[i, 1], points[i, 2]))
    plt.show()


def plotSolution(tour, points, save_path=None):
    plt.figure()
    for i in range(len(tour)):
        start = points[tour[i]]
        end = points[tour[(i + 1) % len(tour)]]
        plt.plot([start[0], end[0]], [start[1], end[1]], 'bo-')
    plt.title("TSP Solution")
    plt.axis("equal")
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()
