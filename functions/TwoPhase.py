import numpy as np

# from functions.constraction import construct_tableau
from functions.simplex_iteration import simpleximplementation

# from constraction import construct_tableau



def two_phase_simplex(arr,tableau, vararr, basic_vars,is_max):

    nparr = np.array(arr, dtype=float)
    
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
    print("Variables:", vararr)

    for var in basic_vars: 
        if var.startswith("a"):                   
         idx = basic_vars.index(var) + 1 
         tableau[0, :] += 1* tableau[idx, :] 

    print(tableau)
    print("Basic Variables:", basic_vars)
    print("Variables:", vararr)     
   
    
    tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,0)


    # Phase 2: Remove artificial variables and restore original objective
       
    artificial_indices = [vararr.index(var) for var in vararr if var.startswith("a")]
    tableau = np.delete(tableau, artificial_indices, axis=1)
    vararr = [var for var in vararr if not var.startswith("a")]  # Remove artificial vars from list


   
# Restore original objective function
    tableau[0, :] = 0  # Reset the entire objective function row
    tableau[0, :len(nparr[0])-1] = nparr[0, :-1]  # Restore only the original coefficients
    tableau[0, -1] = -1*nparr[0, -1]  # Restore the RHS value (constant term)
# Copy original objective function coefficients


    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])


    for var in basic_vars:
     if var in vararr:  
        row_idx = basic_vars.index(var) + 1  # Get the row index of the basic variable
        coeff = tableau[0, vararr.index(var)]  # Get the coefficient in the objective function
        tableau[0, :] -= coeff * tableau[row_idx, :]  # Adjust the objective function row

  

    tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,is_max)
  
    
    
# # Example usage
# array = [
#     [1, 2, 1, 0, 0],  # Objective function
#     [1, 1, 1, 0, 7],  # Constraint 1: x1 + x2 ≤ 7
#     [2, -5, 1, 1, 10],  # Constraint 2: 2x1 - 5x2 = 10
# ]
# # two_phase_simplex(array, 3, 2)
# array = [
   
#     [6, 3, 0, 0],  # Objective function
#     [1,1,1,1],
#     [2, -1, 1, 1],  # Constraint 1: x1 + x2 ≤ 7
#     [0, 3, -1, 2],  # Constraint 2: 2x1 - 5x2 = 10
# ]

# tableau,vararr,basic_vars = construct_tableau(array,[1,1],2,3)
# two_phase_simplex(array,tableau,vararr,basic_vars,1)