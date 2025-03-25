import sys
import numpy as np

def simpleximplementation(tableau,vararr,basicarr,maxi):

    steps = "<h2>Simplex Method Steps</h2>"
    
    nparr = np.array(tableau, dtype=float)

    row, col = nparr.shape 


    flagend = 0
    if maxi :
        for i in range (col-1):
            if nparr[0][i] < 0 :
                flagend = 1
    else: 
        for i in range (col-1):
            if nparr[0][i] > 0 :
                flagend = 1

    while(flagend):

        if maxi :
            pivotcol = np.argmin(nparr[0][:-1])
        else :
            pivotcol = np.argmax(nparr[0][:-1])

        minpos = -1
        minrate = sys.maxsize
        for i in range (1,row):
            if nparr[i][pivotcol] > 0 :
                if nparr[i][col-1] / nparr[i][pivotcol] < minrate :
                    minpos = i
                    minrate = nparr[i][col-1] / nparr[i][pivotcol]

        if(minpos == -1):
            steps += "<p style='color:red;'><b>Solution is infeasible.</b></p>"
            break

        entering = vararr[pivotcol]
        leaving = basicarr[minpos - 1]

        
        steps += format_tableau_html(nparr, vararr, basicarr, pivotcol,minpos)
        steps += f"<h3>Pivot: <span style='color:blue;'>{entering}</span> enters, <span style='color:red;'>{leaving}</span> leaves</h3>"

        basicarr[minpos-1] = vararr[pivotcol]

        nparr[minpos] = nparr[minpos]/nparr[minpos][pivotcol]

        for i in range (row):
            if i == minpos : continue
            nparr[i] = -1*nparr[i][pivotcol]*nparr[minpos] + nparr[i] 


        flagend = 0
        if maxi :
            for i in range (col-1):
                if nparr[0][i] < 0 :
                    flagend = 1
        else: 
            for i in range (col-1):
                if nparr[0][i] > 0 :
                    flagend = 1


    steps += "<h3>Final Tableau:</h3>" + format_tableau_html(nparr, vararr, basicarr)
    for var in basicarr: 
         if var.startswith("a"):                   
           steps += "<p style='color:red;'><b>Problem is infeasible</b></p>"
           return steps,nparr,vararr,basicarr
         
    steps += "<h3>Optimal Solution:</h3>"
    for i in range(1, len(basicarr)+1):
        steps += f"<p>{basicarr[i-1]} = {nparr[i][-1]:.2f}</p>"
    steps += f"<p>Z = {nparr[0][-1]:.2f}</p>"
    return steps,nparr,vararr,basicarr



def format_tableau_html(tableau, vararr, basicarr, pivotcol=None, pivotrow=None):
        """Formats the tableau into an HTML table with highlighted pivot elements."""
        html = "<table border='1' cellspacing='0' cellpadding='5' style='border-collapse: collapse;'>"

        html += "<tr><th>Basic</th>"
        for var in vararr:
            html += f"<th>{var}</th>"
        html += "<th>Solution</th></tr>"

        for i, row in enumerate(tableau):
            html += "<tr>"

            if i == 0:
                html += "<td><b>Z</b></td>"
            else:
                html += f"<td><b>{basicarr[i-1]}</b></td>"


            for j, val in enumerate(row):
                cell_color = ""
                if pivotrow == i:  
                    cell_color = "background-color: yellow;"
                if pivotcol == j:  
                    cell_color = "background-color: lightblue;"
                if pivotrow == i and pivotcol == j:  
                    cell_color = "background-color: orange; font-weight: bold;"

                html += f"<td style='{cell_color}'>{val:.2f}</td>"

            html += "</tr>"
        
        html += "</table><br>"
        # html +="<h4>basic variables: " + str(basicarr) +"</h4>"
        # html +="<h4>non-basic variables: " + str(vararr) + "<br> </h4>"
        return html




# var = ["x1","x2","x3","x4","s1","s2","s3"]
# basic = ["s1","s2","s3"]
# arr = [[-5,4,-6,8,0,0,0,0],
#        [1,2,2,4,1,0,0,40],
#        [2,-1,1,2,0,1,0,8],
#        [4,-2,1,-1,0,0,1,10]]
# maxi = 0
# simpleximplementation(arr,var,basic,maxi)

# arr = [[5,-4,6,-8,0,0],
#        [1,2,2,4,-1,40],
#        [2,-1,1,2,-1,8],
#        [4,-2,1,-1,-1,10]]
# maxi = 0
# tableau,vararr,basic_vars = construct_tableau(arr,[1,1,1,1],4,3)
# tableau[0] *= -1
# simpleximplementation(tableau,vararr,basic_vars,maxi)


