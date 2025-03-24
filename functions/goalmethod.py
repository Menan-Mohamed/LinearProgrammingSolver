import numpy as np

def goals(goal_arr, constr_arr, num_goals, num_constr,maxi):

    steps = "<h2>Goal Method</h2>"

    num_vars = len(goal_arr[0]) - 2  # Excluding type and RHS columns
    total_vars = num_vars + num_goals * 2 + num_constr  # Extra vars for slacks
    
    tableau = np.zeros((num_goals + num_constr + num_goals, total_vars + 1))  # Adjusted row size
    
    # Create variable names
    vararr = [f"x{i+1}" for i in range(num_vars)]
    
    for i in range(num_goals):
        vararr.append(f"s{i+1}-")
    for i in range(num_goals):
        vararr.append(f"s{i+1}+")
    for i in range(num_constr):  # Add slacks for constraints
        vararr.append(f"slack{i+1}")
    
    # Basic variables (start with -s for goal rows + slack variables)
    basic_vars = [f"s{i+1}-" for i in range(num_goals)]
    goalvar = [f"Z{i+1}" for i in range(num_goals)]

    for i in range(num_constr):
        basic_vars.append(f"slack{i+1}")
    
    # Artificial rows for deviation variables
    for i in range(num_goals):
        tableau[i, num_vars + i] = -1  # -s_i-
    
    # Goal constraints with deviation variables
    for i in range(num_goals):
        tableau[num_goals + i, :num_vars] = goal_arr[i][:num_vars]
        tableau[num_goals + i, num_vars + i] = 1   # +s_i+
        tableau[num_goals + i, num_vars + num_goals + i] = -1  # -s_i-
        tableau[num_goals + i, -1] = goal_arr[i][-1]  # RHS
    
    # Constraint rows with slack variables
    for i in range(num_constr):
        tableau[num_goals + num_goals + i, :num_vars] = constr_arr[i][:num_vars]
        tableau[num_goals + num_goals + i, num_vars + num_goals * 2 + i] = 1  # Assign slack variable
        tableau[num_goals + num_goals + i, -1] = constr_arr[i][-1]  # RHS
    
    
    steps += tableau_html(tableau, vararr, basic_vars,goalvar, num_goals)   



    # Adjusting tableau by adding artificial variables' contributions
    for i in range(num_goals):
        tableau[i] += tableau[i + num_goals]

    print("Updated Tableau:")
    print(tableau)

    #simplex

    row, col = tableau.shape

    flag = 1
    pointer = 0

    while(flag):

        while(pointer <= num_goals):
            np.set_printoptions(suppress=True, precision=2)
            print(tableau)
            print(basic_vars)
            if maxi :
                pivotcol = np.argmin(tableau[pointer][:-1])
                if tableau[pointer][pivotcol] < 0 and (pointer == 0 or (tableau[:pointer, pivotcol] == 0).all()):
                    #minpos = pointer
                    break
                else:
                    pointer += 1
                     
            else: 
                pivotcol = np.argmax(tableau[pointer][:-1])
                if tableau[pointer][pivotcol] > 0 and (pointer == 0 or (tableau[:pointer, pivotcol] == 0).all()):
                    #minpos = pointer
                    break
                else:
                    pointer += 1
        
        if pointer == num_goals : break


        minpos = -1
        minrate = float('inf')
        for i in range (num_goals,row):
            if tableau[i][pivotcol] > 0 :
                print(minrate,tableau[i][col-1] / tableau[i][pivotcol])
                if round(tableau[i][col-1] / tableau[i][pivotcol],5) <= round(minrate, 5):
                    minpos = i
                    minrate = tableau[i][col-1] / tableau[i][pivotcol]

        if(minpos == -1):
            break

        print(minpos,pivotcol)

        steps += tableau_html(tableau, vararr, basic_vars,goalvar, num_goals,pivotcol,minpos)

        basic_vars[minpos-num_goals] = vararr[pivotcol]

        tableau[minpos] = tableau[minpos]/tableau[minpos][pivotcol]

        for i in range (row):
            if i == minpos : continue
            tableau[i] = -1 * tableau[i][pivotcol] * tableau[minpos] + tableau[i]

        steps += tableau_html(tableau, vararr, basic_vars,goalvar, num_goals)  



    np.set_printoptions(suppress=True, precision=2)
    print (tableau)
    print(basic_vars)
    print(vararr)

    return steps


def tableau_html(tableau, vararr, basicarr,goalarr, num_goals, pivotcol=None, pivotrow=None):
    """Formats the tableau into an HTML table with highlighted pivot elements."""
    html = "<table border='1' cellspacing='0' cellpadding='5' style='border-collapse: collapse;'>"

    # Header row
    html += "<tr><th>Basic</th>"
    for var in vararr:
        html += f"<th>{var}</th>"
    html += "<th>Solution</th></tr>"

    # Tableau rows
    for i, row in enumerate(tableau):
        html += "<tr>"

        # First row (Objective function or Artificial Row)
        if i < num_goals:
            html += f"<td><b>{goalarr[i]}</b></td>"
        else:
            html += f"<td><b>{basicarr[i - num_goals]}</b></td>"

        # Tableau data
        for j, val in enumerate(row):
            cell_color = ""
            if pivotrow == i:  
                cell_color = "background-color: yellow;"
            if pivotcol == j:  
                cell_color = "background-color: lightblue;"
            if pivotrow == i and pivotcol == j:  
                cell_color = "background-color: orange; font-weight: bold;"

            if i < num_goals:
                if val != 0:
                    html += f"<td style='{cell_color}'>{val:.2f}P{i+1}</td>"
                else:
                    html += f"<td style='{cell_color}'>{val:.2f}</td>"
            else:
                html += f"<td style='{cell_color}'>{val:.2f}</td>"      

        
        html += "</tr>"

    html += "</table><br>"
    return html


# Sample Input Data
# constr = [[100, 60, -1, 600]]  # More than one constraint
# goal = [[7, 3, -1, 40], [10, 5, -1, 60], [5, 4, -1, 35]]
# num_goals = len(goal)
# num_constr = len(constr)

# goals(goal, constr, num_goals, num_constr,0)
