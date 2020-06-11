# Importing modules
import pyshorteners
from PyQt5 import QtCore, QtGui, QtWidgets

# Initialization
s = pyshorteners.Shortener()
shortener_list = ['chilpit', 'clckru', 'dagd', 'isgd', 'nullpointer', 'osdb', 'qpsru', 'tinyurl']


# Making Gui Interface

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 222)
        Form.setMaximumSize(QtCore.QSize(392, 222))
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 371, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 15, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 80, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 371, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 80, 111, 31))
        self.comboBox.setObjectName("comboBox")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        """gui changes"""

        self.pushButton.clicked.connect(self.shorten)
        self.comboBox.addItems(shortener_list)
        self.comboBox.setCurrentIndex(shortener_list.index('tinyurl'))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Url_shortener"))
        self.label.setText(_translate("Form", "Enter the Url Below :"))
        self.pushButton.setText(_translate("Form", "Process"))
        self.label_2.setText(_translate("Form", "Select Shortner:"))

    # Making Logic to shorten Urls

    def shorten(self):
        index = self.comboBox.currentIndex()
        shorten = shortener_list[index]
        print(shorten)
        url = self.lineEdit.text()
        print(url)
        self.textEdit.clear()
        shortened_url = {'chilpit': s.chilpit.short(url),
                         'clckru': s.clckru.short(url),
                         'dagd': s.dagd.short(url),
                         'isgd': s.isgd.short(url),
                         'nullpointer': s.nullpointer.short(url),
                         'osdb': s.osdb.short(url),
                         'qpsru': s.qpsru.short(url),
                         'tinyurl': s.tinyurl.short(url)}
        print(shortened_url[shorten])
        self.textEdit.setText(shortened_url[shorten])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
