import numpy as np
from simplex_iteration import simpleximplementation
def BigM(arr, varnum, constraints):
    nparr = np.array(arr, dtype=float)
    
    # Check if the problem is maximization or minimization
    is_max = nparr[0][varnum]  # Assuming 1 for max, -1 for min
    
    # Define variable names
    vararr = [f"x{i+1}" for i in range(varnum)]
    
    # Remove the constraint type column and RHS temporarily
    tableau = np.delete(nparr, -2, axis=1)  # Remove the second-to-last column
    rhs = tableau[:, -1].reshape(-1, 1)  # Store RHS
    tableau = np.delete(tableau, -1, axis=1)  # Remove RHS from tableau
    
    slack_num = 0
    artificial_num = 0
    basic_vars = []
    non_basic_vars = []
    
    # Process constraints and add slack/artificial variables
    for i in range(constraints):
        constraint_type = int(nparr[i+1, -2])  # The column before RHS
        
        if constraint_type == 0:  # '=' constraint
            vararr.append(f"a{artificial_num}")
            basic_vars.append(f"a{artificial_num}")
            artificial_num += 1
            new_col = np.zeros((len(nparr), 1))
            new_col[i+1, 0] = 1  # Set 1 in the respective row
            tableau = np.hstack((tableau, new_col))
        
        elif constraint_type == -1:  # '<=' constraint
            vararr.append(f"s{slack_num}")
            basic_vars.append(f"s{slack_num}")
            slack_num += 1
            new_col = np.zeros((len(nparr), 1))
            new_col[i+1, 0] = 1
            tableau = np.hstack((tableau, new_col))
        
        elif constraint_type == 1:  # '>=' constraint
            vararr.append(f"s{slack_num}")
            slack_num += 1
            slack_col = np.zeros((len(nparr), 1))
            slack_col[i+1, 0] = -1  # Slack variable with -1
            tableau = np.hstack((tableau, slack_col))
            
            vararr.append(f"a{artificial_num}")
            basic_vars.append(f"a{artificial_num}")
            artificial_num += 1
            artificial_col = np.zeros((len(nparr), 1))
            artificial_col[i+1, 0] = 1  # Artificial variable with 1
            tableau = np.hstack((tableau, artificial_col))
    np.set_printoptions(suppress=True, precision=2)        
    print(tableau)   

    #add rhs
    tableau = np.hstack((tableau, rhs))  
    
    
    # Modify the objective function to include the Big M penalty for artificial variables
    M = 100 if is_max else -100 

    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])  # Remove -0.0
       
    for var in basic_vars:
        if var.startswith("a"):  # Only for artificial variables
            idx = vararr.index(var)
            tableau[0][idx]=M                    # Large number for Big M method
   

    #multiplay the first row "objective row by -1
    
    print(tableau)


    #make col in objective function a col eqyal zeros by row operation Objectivenew=objective+(m)row of a "all a "

    for var in basic_vars: 
        if var.startswith("a"):                   
         idx = basic_vars.index(var) + 1 
         tableau[0, :] += -M * tableau[idx, :] 
   
    
    
    # Identify non-basic variables
    non_basic_vars = [var for var in vararr if var not in basic_vars]
    
    # Add RHS back to tableau
   

    
    # Print results
    print("Final Tableau:")
    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
    
    # Call simplex method (not implemented here, assuming it's available)
    # simplex_method(tableau, basic_vars, non_basic_vars)
    

 # Simplex Iteration

    tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,1)
   
    # Print results
    print("Final Tableau:")
    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
      
# # Example usage
# array = [
#     [1, 2, 1, 1, 0],  # Objective function
#     [1, 1, 1, 0, 7],  # Constraint 1: x1 + x2 ≤ 7
#     [2, -5, 1, 1, 10],  # Constraint 2: 2x1 - 5x2 = 10
# ]
# BigM(array, 3, 2)


# array = [
#     [4, 1,0, 0],  # Objective function
#     [3, 1, 0, 3],  # Constraint 1: x1 + x2 ≤ 7
#     [4,3,1,6],
#     [1, 2, -1, 4],  # Constraint 2: 2x1 - 5x2 = 10
# ]

# simplex(array, 2,3)
array = [
    [1, 5,1, 0],  # Objective function
    [3, 4, -1, 6],  # Constraint 1: x1 + x2 ≤ 7
    [1,3,1,2],
    # Constraint 2: 2x1 - 5x2 = 10
]

BigM(array, 2,2)
