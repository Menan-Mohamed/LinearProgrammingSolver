import numpy as np
from simplex_iteration import simpleximplementation,format_tableau_html
from constraction import construct_tableau



def two_phase_simplex(arr,tableau, vararr, basic_vars,is_max):

    nparr = np.array(arr, dtype=float)

    steps = "<h2>Two Phase Method Steps</h2>"
    
    # Phase 1: Minimize sum of artificial variables
    tableau[0, :-1] = 0
    for var in basic_vars:
        if var.startswith("a"):
            idx = vararr.index(var)
            tableau[0, idx]=1
    
    steps += "<h3>Phase 1: Minimize sum of artificial variables</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)

    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])  # Remove -0.0


    for var in basic_vars: 
        if var.startswith("a"):                   
         idx = basic_vars.index(var) + 1 
         tableau[0, :] += 1* tableau[idx, :] 

      
    # steps += "<h3>Phase 1: Minimize sum of artificial variables</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)
   
    
    step,tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,0)

    steps += step

    # Phase 2: Remove artificial variables and restore original objective
       
    artificial_indices = [vararr.index(var) for var in vararr if var.startswith("a")]
    tableau = np.delete(tableau, artificial_indices, axis=1)
    vararr = [var for var in vararr if not var.startswith("a")]  # Remove artificial vars from list

    steps += "<h3>Phase 2: Remove artificial variables and restore original objective</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)

   
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

    steps += "<h3>Restore original objective function</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)

    step,tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,is_max)

    steps += step

    return steps
  
    
    
# # Example usage
# array = [
#     [1, 2, 1, 0, 0],  # Objective function
#     [1, 1, 1, 0, 7],  # Constraint 1: x1 + x2 ≤ 7
#     [2, -5, 1, 1, 10],  # Constraint 2: 2x1 - 5x2 = 10
# ]
# two_phase_simplex(array, 3, 2)
# array = [
   
#     [6, 3, 0, 0],  # Objective function
#     [1,1,1,1],
#     [2, -1, 1, 1],  # Constraint 1: x1 + x2 ≤ 7
#     [0, 3, -1, 2],  # Constraint 2: 2x1 - 5x2 = 10
# ]

# tableau,vararr,basic_vars,maxi = construct_tableau(array,0,[1,1],2,3)
# two_phase_simplex(array,tableau,vararr,basic_vars,maxi)