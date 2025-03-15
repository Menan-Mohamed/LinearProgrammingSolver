from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: rgba(240, 255, 240, 0.5);")
        
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 560, 560))
        self.widget.setObjectName("widget")
        
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(130, 100, 300, 40))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 250, 300, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border-radius: 10px; background-color: #4CAF50; color: white;")
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 300, 300, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-radius: 10px; background-color: #008CBA; color: white;")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Optimization Methods"))
        self.label.setText(_translate("Dialog", "Choose the starting Method approach:"))
        self.pushButton.setText(_translate("Dialog", "Simplex Method"))
        self.pushButton_2.setText(_translate("Dialog", "Goal Programming"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
