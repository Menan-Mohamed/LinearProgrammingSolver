import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

from constraction import construct_tableau



class SimplexGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Set up the GUI layout."""
        self.setWindowTitle("Simplex Solver with Highlights")
        self.setGeometry(100, 100, 800, 500)

        layout = QVBoxLayout()

        # Text box for output
        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)
        layout.addWidget(self.text_output)

        # Solve button
        self.solve_button = QPushButton("Solve Simplex", self)
        self.solve_button.clicked.connect(self.run_simplex)
        layout.addWidget(self.solve_button)

        self.setLayout(layout)

    def run_simplex(self):
        """Runs the simplex algorithm and updates the GUI output."""
        tableau = np.array([
            [-5, 4, -6, 8, 0, 0, 0, 0],
            [1, 2, 2, 4, 1, 0, 0, 40],
            [2, -1, 1, 2, 0, 1, 0, 8],
            [4, -2, 1, -1, 0, 0, 1, 10]
        ], dtype=float)
        
        vararr = ["x1", "x2", "x3", "x4", "S1", "S2", "S3"]
        basicarr = ["S1", "S2", "S3"]

        output_text,_,_,_ = simpleximplementation(tableau, vararr, basicarr, 0)
        self.text_output.setHtml(output_text)  # Use HTML for formatting



def simpleximplementation(tableau,vararr,basicarr,maxi):

    steps = "<h2>Simplex Method Steps</h2>"
    
    nparr = np.array(tableau, dtype=float)

    row, col = nparr.shape 

    # steps += "<p style='color:red;'><b>Tableau</b></p>"
    # steps += format_tableau_html(nparr, vararr, basicarr)

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

    # print(vararr)
    # print(basicarr)
    # np.set_printoptions(suppress=True, precision=2)
    # print(nparr)

    steps += "<h3>Final Tableau:</h3>" + format_tableau_html(nparr, vararr, basicarr)
    return steps,nparr,vararr,basicarr



def format_tableau_html(tableau, vararr, basicarr, pivotcol=None, pivotrow=None):
        """Formats the tableau into an HTML table with highlighted pivot elements."""
        html = "<table border='1' cellspacing='0' cellpadding='5' style='border-collapse: collapse;'>"

        # Table headers
        html += "<tr><th>Basic</th>"
        for var in vararr:
            html += f"<th>{var}</th>"
        html += "<th>Solution</th></tr>"

        # Rows of tableau
        for i, row in enumerate(tableau):
            html += "<tr>"
            # Basic variable column
            if i == 0:
                html += "<td><b>Z</b></td>"
            else:
                html += f"<td><b>{basicarr[i-1]}</b></td>"

            # Tableau values
            for j, val in enumerate(row):
                cell_color = ""
                if pivotrow == i:  # Highlight pivot row
                    cell_color = "background-color: yellow;"
                if pivotcol == j:  # Highlight pivot column
                    cell_color = "background-color: lightblue;"
                if pivotrow == i and pivotcol == j:  # Highlight pivot element
                    cell_color = "background-color: orange; font-weight: bold;"

                html += f"<td style='{cell_color}'>{val:.2f}</td>"

            html += "</tr>"

        html += "</table><br>"
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimplexGUI()
    window.show()
    sys.exit(app.exec())
