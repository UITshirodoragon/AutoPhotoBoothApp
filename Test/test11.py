import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime

class CountdownTimer(QWidget):
    def __init__(self, minutes, seconds):
        super().__init__()
        self.initUI(minutes, seconds)

    def initUI(self, minutes, seconds):
        self.layout = QVBoxLayout()

        self.time_label = QLabel(self)
        self.layout.addWidget(self.time_label)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

        self.initial_time = QTime(0, minutes, seconds)
        self.time = QTime(0, minutes, seconds)
        self.update_time_label()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.setWindowTitle('Countdown Timer')
        self.show()

    def start_timer(self):
        self.timer.start(1000)

    def update_timer(self):
        self.time = self.time.addSecs(-1)
        self.update_time_label()
        if self.time == QTime(0, 0, 0):
            self.timer.stop()
            self.reset_timer()

    def reset_timer(self):
        self.time = self.initial_time
        self.update_time_label()

    def update_time_label(self):
        self.time_label.setText(self.time.toString('mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownTimer(1, 30)  # Đếm ngược từ 1 phút 30 giây
    sys.exit(app.exec_())