# Vorto_vrp
Solution to a version of the Vehicle Routing Problem(VRP). The problem is to minimize the Cost of deliveries. ​C = 500*NumbDrivers + TotDriverMins. ​ ​For simplicity, euclidean distance formula is used to measure distance between points, but is called minutes. ​Drivers have a 12-hour shift and must start and end shifts at (0,0) depo station. 

My solution is a python script titled Rogers_VRP_Solution.py which utilizes a Nearest Neighbor, greedy approach to optimize the scheduling processes of assigning loads to drivers.   

To run my submission and evaluate the script use the following command in a shell: 
    python evaluateShared.py --cmd "python Rogers_VRP_Solution.py" --problemDir trainingProblems

- Python 3.9.1

|      Method      |   Mean Run Time  |    Mean Cost     |
| ---------------- | ---------------- | ---------------- |
| Nearest Neighbor |     65.6 ms      |    80,785.95     |


I tried a few methods. One of them was Simulated Annealing. This approach was abandoned as the temperatures and cooling rate would require tuning to prove effective and the solution could still produce a poor result given the test data.

References: 
- https://www.geeksforgeeks.org/greedy-algorithms/
- https://iopscience.iop.org/article/10.1088/1757-899X/166/1/012029
- 
