from PyQt6 import QtCore,  QtWidgets
from functions.goalmethod import goals

class Ui_Dialog(object):

    def setupUi(self, Dialog,main_app):

        self.goalRows = []
        self.constraintRows = []
        self.constraints = []
        self.goals = []
        self.lineEdits_vec = []  

        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: rgba(220, 220, 220, 0.5);")

        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 560, 560))
        self.widget.setStyleSheet("""
            background-color: rgba(245, 245, 245, 0.7);  /* Semi-transparent gray */
        """)
        
        self.label = QtWidgets.QLabel("Enter the number of variables in the objective function:", parent=self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 400, 30))
        self.label.setStyleSheet("border-radius: 2px;font-size: 14px; font-weight: bold; color: #333;")
          
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 180, 30))
        self.lineEdit.setPlaceholderText("Enter Here")
        self.lineEdit.setStyleSheet("border: 0.5px solid rgba(150, 150, 150, 0.9);border-radius: 2px;font-size: 14px; font-weight: bold; color: #334;")
        
        self.pushButton_setVars = QtWidgets.QPushButton("Set", parent=self.widget)
        self.pushButton_setVars.setGeometry(QtCore.QRect(220, 60, 100, 30))
        self.pushButton_setVars.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")

        self.pushButton_4 = QtWidgets.QPushButton("Add a goal row", parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 110, 200, 30))
        self.pushButton_4.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")

        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.widget)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 150, 520, 100))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.goalsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)

        self.pushButton = QtWidgets.QPushButton("Add a constraint row", parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 200, 30))
        self.pushButton.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 300, 520, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.constraintsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.label_3 = QtWidgets.QLabel("Enter decision variables' constraints (≤ restricted,- unrestricted)", parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 419, 500, 30))
        self.label_3.setStyleSheet("border-radius: 2px;font-size: 14px; font-weight: bold; color: #333;")

        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 450, 500, 40))
        self.widget_3.setStyleSheet("border: 0.5px solid rgba(150, 150, 150, 0.9);border-radius: 2px;font-size: 14px; font-weight: bold; color: #333;")
        self.layout_vec = QtWidgets.QHBoxLayout(self.widget_3)

        self.pushButton_2 = QtWidgets.QPushButton("Submit", parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 510, 161, 30))
        self.pushButton_2.setStyleSheet("border-radius: 2px; background-color:#008CBA; color: white;")

        self.pushButton_3 = QtWidgets.QPushButton("Back", parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 510, 161, 30))
        self.pushButton_3.setStyleSheet("border-radius: 2px; background-color:#008CBA; color: white;")

        self.pushButton.clicked.connect(self.addConstraintRow)
        self.pushButton_4.clicked.connect(self.addGoalRow)
        self.pushButton_setVars.clicked.connect(self.updateVariables)
        self.pushButton_2.clicked.connect(self.onSubmit)


    def updateVariables(self):
        
        num_vars = int(self.lineEdit.text()) if self.lineEdit.text().isdigit() else 4

        for lineEdit, constraint_type in self.lineEdits_vec:
            lineEdit.deleteLater()
            constraint_type.deleteLater()
        self.lineEdits_vec.clear()

        for i in reversed(range(self.constraintsLayout.count())):
            item = self.constraintsLayout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        self.constraintRows.clear()

        for i in reversed(range(self.goalsLayout.count())):
            item = self.goalsLayout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        self.goalRows.clear()                

        for i in range(num_vars):
            label = QtWidgets.QLabel(f"x{i+1}")
            self.layout_vec.insertWidget(i*2, label)

            constraint_type = QtWidgets.QComboBox()
            constraint_type.addItems(["≤", "-"])
            self.layout_vec.insertWidget(i * 2 + 1,constraint_type)

            self.lineEdits_vec.append((label, constraint_type))
    
    def addConstraintRow(self):
        row_widget = QtWidgets.QWidget()
        row_layout = QtWidgets.QHBoxLayout(row_widget)

        num_vars = num_vars = int(self.lineEdit.text()) if self.lineEdit.text().isdigit() else 4
        row = []

        for i in range(num_vars):
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setPlaceholderText(f"x{i+1}")
            row_layout.addWidget(lineEdit)
            row.append(lineEdit)

        constraint_type = QtWidgets.QComboBox()
        constraint_type.addItems(["≤", "=", "≥"])
        row_layout.addWidget(constraint_type)

        rhs = QtWidgets.QLineEdit()
        rhs.setPlaceholderText("RHS")
        row_layout.addWidget(rhs)

        self.constraintsLayout.addWidget(row_widget)
        self.constraintRows.append((row, constraint_type, rhs)) 

    def addGoalRow(self):
        row_widget = QtWidgets.QWidget()
        row_layout = QtWidgets.QHBoxLayout(row_widget)

        num_vars = num_vars = int(self.lineEdit.text()) if self.lineEdit.text().isdigit() else 4
        row = []

        for i in range(num_vars):
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setPlaceholderText(f"x{i+1}")
            row_layout.addWidget(lineEdit)
            row.append(lineEdit)

        constraint_type = QtWidgets.QComboBox()
        constraint_type.addItems(["≤", "=", "≥"])
        row_layout.addWidget(constraint_type)

        rhs = QtWidgets.QLineEdit()
        rhs.setPlaceholderText("RHS")
        row_layout.addWidget(rhs)

        self.goalsLayout.addWidget(row_widget)
        self.goalRows.append((row, constraint_type, rhs))

    def extractConstraints(self):
        """extract values from constraint rows on submit."""
        constraint_map = {"=": 0, "≤": -1, "≥": 1}

        for row_inputs, constraint_type, rhs in self.constraintRows:
            row_values = []

            for edit in row_inputs:
                text = edit.text().strip()
                try:
                    row_values.append(float(text))  
                except ValueError:
                    row_values.append(0)

            row_values.append(constraint_map[constraint_type.currentText()])
            if(constraint_map[constraint_type.currentText()] == 1):
                self.simplex = 0
                print(constraint_map[constraint_type.currentText()],self.simplex)

            rhs_text = rhs.text().strip()
            try:
                row_values.append(float(rhs_text))  
            except ValueError:
                row_values.append(0)

            self.constraints.append(row_values)

        print("constraints", self.constraints)
    def extractGoals(self):
        """extract values from goal rows on submit."""
        constraint_map = {"=": 0, "≤": -1, "≥": 1}

        for row_inputs, constraint_type, rhs in self.goalRows:
            row_values = []

            for edit in row_inputs:
                text = edit.text().strip()
                try:
                    row_values.append(float(text))  
                except ValueError:
                    row_values.append(0)

            row_values.append(constraint_map[constraint_type.currentText()])
            if(constraint_map[constraint_type.currentText()] == 1):
                self.simplex = 0
                print(constraint_map[constraint_type.currentText()],self.simplex)

            rhs_text = rhs.text().strip()
            try:
                row_values.append(float(rhs_text))  
            except ValueError:
                row_values.append(0)

            self.goals.append(row_values)

        print("goals:", self.goals)

    def onSubmit(self):
        self.extractConstraints()
        self.extractGoals()
        vec = []
        for _, constraint_type in self.lineEdits_vec:
            vec.append(1 if constraint_type.currentText() == "≤" else -1)

        goals(self.goals, self.constraints, len(self.goals), len(self.constraints),0)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Goal Programming Solver"))
        self.label.setText(_translate("Dialog", "Goal Programming Solver"))
        self.pushButton.setText(_translate("Dialog", "Goal Programming Solver"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())