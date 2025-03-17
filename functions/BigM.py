import numpy as np
from simplex_iteration import simpleximplementation,format_tableau_html
from constraction import construct_tableau


def BigM(tableau,vararr,basic_vars,is_max):

    steps = "<h2>BigM Method Steps</h2>"
     
    # Modify the objective function to include the Big M penalty for artificial variables
    M = 100 if is_max else -100 

    tableau[0] *= -1
    tableau[0] = np.where(tableau[0] == -0.0, 0.0, tableau[0])  # Remove -0.0
       
    for var in basic_vars:
        if var.startswith("a"):  # Only for artificial variables
            idx = vararr.index(var)
            tableau[0][idx]=M                    # Large number for Big M method


    steps += "<h3>Enter M in objective function</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)
    

    #multiplay the first row "objective row by -1
    
    # print(tableau)


    #make col in objective function a col eqyal zeros by row operation Objectivenew=objective+(m)row of a "all a "

    for var in basic_vars: 
        if var.startswith("a"):                   
         idx = basic_vars.index(var) + 1 
         tableau[0, :] += -M * tableau[idx, :] 
   
    steps += "<h3>Remove A's from objective function</h3>"
    steps += format_tableau_html(tableau, vararr, basic_vars)

    # Simplex Iteration

    step,tableau, vararr, basic_vars = simpleximplementation(tableau,vararr,basic_vars,is_max)

    steps += step

    return steps
   
      
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
# array = [
#     [1, 5,1, 0],  # Objective function
#     [3, 4, -1, 6],  # Constraint 1: x1 + x2 ≤ 7
#     [1,3,1,2],
#     # Constraint 2: 2x1 - 5x2 = 10
# ]

# tableau,vararr,basic_vars =  construct_tableau(array,[1,1,1],3,2)
# BigM(tableau,vararr,basic_vars,1)
