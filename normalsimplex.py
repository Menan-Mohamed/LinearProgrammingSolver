from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: rgba(240, 255, 240, 0.5);")

        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 560, 560))

        self.label = QtWidgets.QLabel("Enter the number of variables in the objective function:", parent=self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 400, 30))

        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 45, 180, 30))
        self.lineEdit.setPlaceholderText("Enter number of variables")

        self.pushButton_setVars = QtWidgets.QPushButton("Set", parent=self.widget)
        self.pushButton_setVars.setGeometry(QtCore.QRect(220, 45, 100, 30))
        self.pushButton_setVars.setStyleSheet("border-radius: 10px; background-color: #4CAF50; color: white;")

        self.label_2 = QtWidgets.QLabel("Enter the coefficients of the objective function:", parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 400, 30))

        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 110, 500, 40))
        self.layout_obj = QtWidgets.QHBoxLayout(self.widget_2)

        self.lineEdits_obj = [] #global stire the objective function
        self.constraintRows = []  # global store constraint rows 
        self._2Darray = []  # global storee the entire 2d matrix

        self.dropdown = QtWidgets.QComboBox(parent=self.widget_2)
        self.dropdown.addItems(["Maximize", "Minimize"])
        self.layout_obj.addWidget(self.dropdown)

        self.pushButton = QtWidgets.QPushButton("Add a constraint row +", parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 200, 30))
        self.pushButton.setStyleSheet("border-radius: 10px; background-color: #4CAF50; color: white;")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 210, 520, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.constraintsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.pushButton_2 = QtWidgets.QPushButton("Submit", parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 450, 161, 30))
        self.pushButton_2.setStyleSheet("border-radius: 10px; background-color:#4CAF50; color: white;")

        self.pushButton_3 = QtWidgets.QPushButton("Back", parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 490, 161, 30))
        self.pushButton_3.setStyleSheet("border-radius: 10px; background-color: #4CAF50; color: white;")

        self.pushButton.clicked.connect(self.addConstraintRow)
        self.pushButton_setVars.clicked.connect(self.updateVariables)
        self.pushButton_2.clicked.connect(lambda: (self.extractValues(),self.extractConstraints()))

    def updateVariables(self):
        num_vars = int(self.lineEdit.text()) if self.lineEdit.text().isdigit() else 4

        # Clear previous input fields
        for lineEdit in self.lineEdits_obj:
            lineEdit.deleteLater()
        self.lineEdits_obj.clear()

        for i in range(num_vars):
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setPlaceholderText(f"x{i+1}")
            self.layout_obj.insertWidget(i, lineEdit)
            self.lineEdits_obj.append(lineEdit)

    def extractValues(self):
        self._2Darray.clear()
        row = []

        # Extract values from the objective function fields
        for lineEdit in self.lineEdits_obj:
            text = lineEdit.text().strip()
            try:
                row.append(float(text))  # Supports negative numbers
            except ValueError:
                row.append(0)  # Default to 0 if the input is invalid

        row.append(0)  # Placeholder for additional values
        row.append(0)

        self._2Darray.append(row)

    def addConstraintRow(self):
        row_widget = QtWidgets.QWidget()
        row_layout = QtWidgets.QHBoxLayout(row_widget)

        num_vars = len(self.lineEdits_obj)
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
        self.constraintRows.append((row, constraint_type, rhs))  # Store references

    def extractConstraints(self):
        """Extract values from constraint rows on submit."""
        constraint_map = {"=": 0, "≤": -1, "≥": 1}

        for row_inputs, constraint_type, rhs in self.constraintRows:
            row_values = []

            for edit in row_inputs:
                text = edit.text().strip()
                try:
                    row_values.append(float(text))  # Supports negative numbers
                except ValueError:
                    row_values.append(0)

            row_values.append(constraint_map[constraint_type.currentText()])

            rhs_text = rhs.text().strip()
            try:
                row_values.append(float(rhs_text))  # Supports negative numbers
            except ValueError:
                row_values.append(0)

            self._2Darray.append(row_values)

        print("2Darray:", self._2Darray)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Linear Programming Solver")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
