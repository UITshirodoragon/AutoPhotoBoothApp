import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Press the button to start countdown", self)
        self.layout.addWidget(self.label)
        
        self.button = QPushButton("Start Countdown", self)
        self.button.clicked.connect(self.startCountdown)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        self.setWindowTitle('Countdown App')
        self.show()
        
    def startCountdown(self):
        self.time_left = 10
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.timer.start(1000)
        self.button.setEnabled(False)  # Disable the button
        
    def updateCountdown(self):
        if self.time_left > 0:
            self.label.setText(f"{self.time_left} seconds remaining")
            self.time_left -= 1
        else:
            self.timer.stop()
            self.label.setText("Done!")
            self.button.setEnabled(True)  # Enable the button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownApp()
    sys.exit(app.exec_())