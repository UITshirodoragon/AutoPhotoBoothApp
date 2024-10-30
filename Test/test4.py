import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox

class FirstWidget(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel('This is the first widget', self)
        self.label.setStyleSheet("background-color: lightblue;")
        layout.addWidget(self.label)

        self.button = QPushButton('Go to Second Widget', self)
        self.button.clicked.connect(self.showDialog)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def showDialog(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to go to the second widget?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.stack.setCurrentIndex(1)

class SecondWidget(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel('This is the second widget', self)
        self.label.setStyleSheet("background-color: lightgreen;")
        layout.addWidget(self.label)

        self.button = QPushButton('Go to First Widget', self)
        self.button.clicked.connect(self.showDialog)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def showDialog(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to go to the first widget?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.stack.setCurrentIndex(0)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackedWidget Example')
        self.setGeometry(100, 100, 300, 200)

        self.stack = QStackedWidget(self)
        self.firstWidget = FirstWidget(self.stack)
        self.secondWidget = SecondWidget(self.stack)

        self.stack.addWidget(self.firstWidget)
        self.stack.addWidget(self.secondWidget)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())