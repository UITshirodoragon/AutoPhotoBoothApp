import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea, QHBoxLayout, QStackedWidget, QSizePolicy
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QPalette, QColor

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(558, 978)
        Form.setMaximumSize(QSize(1038, 1938))
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(540, 960))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-572, -992, 1098, 1938))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1080, 1920))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        widget1 = QWidget()
        layout1 = QVBoxLayout(widget1)
        button1 = QPushButton("Go to Widget 2", widget1)
        button1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        label1 = QLabel("Widget 1", widget1)
        label1.setFixedSize(400, 400)
        label1.setAutoFillBackground(True)
        palette1 = label1.palette()
        palette1.setColor(QPalette.Window, QColor("lightblue"))
        label1.setPalette(palette1)
        layout1.addWidget(button1)
        layout1.addWidget(label1)

        widget2 = QWidget()
        layout2 = QVBoxLayout(widget2)
        button2 = QPushButton("Go to Widget 1", widget2)
        button2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        label2 = QLabel("Widget 2", widget2)
        label2.setFixedSize(400, 400)
        label2.setAutoFillBackground(True)
        palette2 = label2.palette()
        palette2.setColor(QPalette.Window, QColor("lightgreen"))
        label2.setPalette(palette2)
        layout2.addWidget(button2)
        layout2.addWidget(label2)

        self.ui.stackedWidget.addWidget(widget1)
        self.ui.stackedWidget.addWidget(widget2)

        # Set the scroll area to expand with the main window
        self.ui.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())