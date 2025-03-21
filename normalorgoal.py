from PyQt6 import QtCore, QtWidgets

class Ui_Dialog(object):
    
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: rgba(220 220, 220, 0.5);")
        
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 560, 560))
        self.widget.setStyleSheet("""
            background-color: rgba(245, 245, 245, 0.7);  /* Semi-transparent gray */
        """)
        self.widget.setObjectName("widget")
        
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(130, 100, 300, 40))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 250, 300, 40))
        self.pushButton.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 300, 300, 40))
        self.pushButton_2.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 350, 300, 40))
        self.pushButton_3.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Optimization Methods"))
        self.label.setText(_translate("Dialog", "Choose the starting Method approach:"))
        self.pushButton.setText(_translate("Dialog", "Simplex Method"))
        self.pushButton_2.setText(_translate("Dialog", "Goal Programming"))
        self.pushButton_3.setText(_translate("Dialog", "Back"))

