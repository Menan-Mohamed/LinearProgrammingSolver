from PyQt6 import QtWidgets
from start import Ui_Dialog as StartPage
from normalorgoal import Ui_Dialog as MethodSelectionPage
from normalsimplex import Ui_Dialog as SimplexPage
from solution import Ui_Dialog as OutputPage
from goal import Ui_Dialog as GoalPage
import sys

class MainApp(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        
        self.start_page = QtWidgets.QDialog()
        self.method_selection_page = QtWidgets.QDialog()
        self.simplex_page = QtWidgets.QDialog()
        self.output_page = QtWidgets.QDialog()
        self.goal_page = QtWidgets.QDialog()
        
        self.start_ui = StartPage()
        self.start_ui.setupUi(self.start_page)
        
        self.method_selection_ui = MethodSelectionPage()
        self.method_selection_ui.setupUi(self.method_selection_page)

        self.simplex_ui = SimplexPage()
        self.simplex_ui.setupUi(self.simplex_page,self)

        self.output_ui = OutputPage(self.output_page)
        self.output_ui.setupUi(self.output_page)

        self.goal_ui = GoalPage()
        self.goal_ui.setupUi(self.goal_page,self)
        
        self.addWidget(self.start_page)
        self.addWidget(self.method_selection_page)
        self.addWidget(self.simplex_page)
        self.addWidget(self.output_page)
        self.addWidget(self.goal_page)
        
        self.start_ui.pushButton.clicked.connect(self.go_to_method_selection)
        self.start_ui.pushButton_2.clicked.connect(QtWidgets.QApplication.instance().quit)  
        
        self.method_selection_ui.pushButton.clicked.connect(self.go_to_simplex)  
        self.method_selection_ui.pushButton_2.clicked.connect(self.go_to_goal)
        self.method_selection_ui.pushButton_3.clicked.connect(self.go_to_start)
        self.output_ui.pushButton.clicked.connect(self.go_to_method_selection)
        self.simplex_ui.pushButton_3.clicked.connect(self.go_to_method_selection)
        self.goal_ui.pushButton_3.clicked.connect(self.go_to_method_selection) 

        self.setCurrentWidget(self.start_page)

    
    def go_to_start(self):
        self.setCurrentWidget(self.start_page)

    def go_to_method_selection(self):
        self.setCurrentWidget(self.method_selection_page)

    def go_to_simplex(self):
        self.setCurrentWidget(self.simplex_page)

    def go_to_goal(self):
        self.setCurrentWidget(self.goal_page)

    def go_to_output(self, output_text):
        # print("wohooooooooooooooooooo"+ output_text)
        self.setCurrentWidget(self.output_page) 
        self.output_ui.set_output_text(output_text) 


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.setFixedSize(600, 600)
    main_app.show()
    sys.exit(app.exec())
