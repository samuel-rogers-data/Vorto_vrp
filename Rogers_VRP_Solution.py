# Import necessary libraries
import sys
import math

# Define a class for points with x, y coordinates
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

# Function to calculate distance between two points
def calc_dist(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

# Read load data from a file
def read_loads(file_path):
    with open(file_path, 'r') as f:
        next(f)  # Skipping the first line as it's the header
        loads = [(int(parts[0]), Point(float(parts[1].strip('()').split(',')[0]), float(parts[1].strip('()').split(',')[1])), 
                  Point(float(parts[2].strip('()').split(',')[0]), float(parts[2].strip('()').split(',')[1])))
                 for parts in (line.split() for line in f)]
    return loads

# Function to find the nearest load to the current location
def find_nearest_load(current_loc, loads):
    closest_load = None
    smallest_distance = float('inf')
    for load in loads:
        dist_to_load = calc_dist(current_loc, load[1])  # Distance from current location to load's pickup
        if dist_to_load < smallest_distance:
            closest_load = load
            smallest_distance = dist_to_load
    return closest_load

# Assign loads to drivers, ensuring they don't exceed max distance
# Uses nearest neighbor, greedy approach
def distribute_loads(loads, max_drive=720):
    routes = []
    while loads:
        route = []
        current_pos = Point(0, 0)  # Starting at the depot
        total_dist = 0

        while loads:
            next_load = find_nearest_load(current_pos, loads)
            if next_load:
                trip_dist = calc_dist(current_pos, next_load[1]) + calc_dist(next_load[1], next_load[2]) + calc_dist(next_load[2], Point(0, 0))
                if total_dist + trip_dist <= max_drive:
                    route.append(next_load[0])
                    total_dist += trip_dist
                    current_pos = next_load[2]
                    loads.remove(next_load)
                else:
                    break
            else:
                break

        if route:
            routes.append(route)

    return routes

# solution output
def print_routes(routes):
    for lane in routes:
        print(f"[{','.join(map(str, lane))}]")

# Main function to run the VRP solver
def main(path):
    load_data = read_loads(path)
    driver_routes = distribute_loads(load_data)
    print_routes(driver_routes)

# Check for command line argument and run
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Retry with correct command: python vrp_submission.py <path_to_input_file>")

