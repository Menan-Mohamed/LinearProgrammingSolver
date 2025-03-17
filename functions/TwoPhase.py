import numpy as np
from simplex_iteration import simpleximplementation



def two_phase_simplex(arr, varnum, constraints):
    nparr = np.array(arr, dtype=float)
    np.set_printoptions(suppress=True, precision=2)        
    
    is_max = nparr[0][varnum]  # 1 for max, -1 for min
    
    vararr = [f"x{i+1}" for i in range(varnum)]
    tableau = np.delete(nparr, -2, axis=1)
    rhs = tableau[:, -1].reshape(-1, 1)
    tableau = np.delete(tableau, -1, axis=1)
    
    slack_num = 0
    artificial_num = 0
    basic_vars = []
    non_basic_vars = []
    
    for i in range(constraints):
        constraint_type = int(nparr[i+1, -2])
        
        if constraint_type == 0:
            vararr.append(f"a{artificial_num}")
            basic_vars.append(f"a{artificial_num}")
            artificial_num += 1
            new_col = np.zeros((len(nparr), 1))
            new_col[i+1, 0] = 1
            tableau = np.hstack((tableau, new_col))
        
        elif constraint_type == -1:
            vararr.append(f"s{slack_num}")
            basic_vars.append(f"s{slack_num}")
            slack_num += 1
            new_col = np.zeros((len(nparr), 1))
            new_col[i+1, 0] = 1
            tableau = np.hstack((tableau, new_col))
        
        elif constraint_type == 1:
            vararr.append(f"s{slack_num}")
            slack_num += 1
            slack_col = np.zeros((len(nparr), 1))
            slack_col[i+1, 0] = -1
            tableau = np.hstack((tableau, slack_col))
            
            vararr.append(f"a{artificial_num}")
            basic_vars.append(f"a{artificial_num}")
            artificial_num += 1
            artificial_col = np.zeros((len(nparr), 1))
            artificial_col[i+1, 0] = 1
            tableau = np.hstack((tableau, artificial_col))
    
    tableau = np.hstack((tableau, rhs))
    non_basic_vars = [var for var in vararr if var not in basic_vars]
    
    # Phase 1: Minimize sum of artificial variables
    tableau[0, :-1] = 0
    for var in basic_vars:
        if var.startswith("a"):
            idx = vararr.index(var)
            tableau[0, idx]=1

    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])  # Remove -0.0
    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)

    for var in basic_vars: 
        if var.startswith("a"):                   
         idx = basic_vars.index(var) + 1 
         tableau[0, :] += 1* tableau[idx, :] 

    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)     
   
    
    tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,0)

    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
#     # Phase 2: Remove artificial variables and restore original objective
   # Phase 2: Remove artificial variables and restore original objective
    artificial_indices = [vararr.index(var) for var in vararr if var.startswith("a")]
    tableau = np.delete(tableau, artificial_indices, axis=1)
    vararr = [var for var in vararr if not var.startswith("a")]  # Remove artificial vars from list
    non_basic_vars = [var for var in non_basic_vars if not var.startswith("a")] 
    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
   
# Restore original objective function
    tableau[0, :] = 0  # Reset the entire objective function row
    tableau[0, :len(nparr[0])-1] = nparr[0, :-1]  # Restore only the original coefficients
    tableau[0, -1] = -1*nparr[0, -1]  # Restore the RHS value (constant term)
 # Copy original objective function coefficients


    print("hhhhhhhhhhhhhhhhhhhhhhhh",nparr[0])


    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])

    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)

# Run simplex again for final optimization
   
   #before call phase2 make the col of current basic varible =0 in other rows
   #as you make in big m
  
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
    for var in basic_vars:
     if var in vararr:  
        row_idx = basic_vars.index(var) + 1  # Get the row index of the basic variable
        coeff = tableau[0, vararr.index(var)]  # Get the coefficient in the objective function
        tableau[0, :] -= coeff * tableau[row_idx, :]  # Adjust the objective function row


    
    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
  

    tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,0)

    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Non-Basic Variables:", non_basic_vars)
    print("Variables:", vararr)
  
    
    
# # Example usage
# array = [
#     [1, 2, 1, 0, 0],  # Objective function
#     [1, 1, 1, 0, 7],  # Constraint 1: x1 + x2 ≤ 7
#     [2, -5, 1, 1, 10],  # Constraint 2: 2x1 - 5x2 = 10
# ]
# two_phase_simplex(array, 3, 2)
array = [
   
    [6, 3, 0, 0],  # Objective function
    [1,1,1,1],
    [2, -1, 1, 1],  # Constraint 1: x1 + x2 ≤ 7
    [0, 3, -1, 2],  # Constraint 2: 2x1 - 5x2 = 10
]

two_phase_simplex(array, 2, 3)