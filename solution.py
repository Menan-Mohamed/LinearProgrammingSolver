from PyQt6 import QtCore,  QtWidgets

from PyQt6 import QtWidgets, QtCore

class Ui_Dialog(QtWidgets.QDialog):
    
    def __init__(self, Dialog):
        super().__init__(Dialog)  
        self.setupUi(Dialog) 

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: rgba(220, 220, 220, 0.5);")

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 560, 560))
        self.widget.setStyleSheet("background-color: rgba(245, 245, 245, 0.7);")
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 20, 300, 40))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        # scrollable
        self.scroll_area = QtWidgets.QScrollArea(self.widget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 100, 520, 350))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        self.output_label = QtWidgets.QLabel(self.scroll_widget)
        self.output_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.output_label.setWordWrap(True)
        self.output_label.setStyleSheet("padding: 10px; background-color: white; border-radius: 5px; font-size: 14px;")

        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.scroll_layout.addWidget(self.output_label)

        self.pushButton = QtWidgets.QPushButton("Back",self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 490, 300, 40))
        self.pushButton.setStyleSheet("border-radius: 2px; background-color: #008CBA; color: white;")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simplex Solution Output"))


    def set_output_text(self, output_text):
        self.output_label.setText(output_text)

