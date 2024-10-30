import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QPropertyAnimation, QRect, QSequentialAnimationGroup, Qt
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Parent label
        self.background_label = QLabel(self)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setFont(QFont('Arial', 50))
        self.background_label.setStyleSheet("background-color: yellow")
        self.background_label.setGeometry(50, 50, 300, 300)
        
        # Child label
        self.label = QLabel("Press the button to start countdown", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 50))
        self.label.setStyleSheet("color: red")
        self.label.setGeometry(50, 50, 300, 300)
        
        # Button
        self.button = QPushButton("Start Countdown", self)
        self.button.setGeometry(150, 400, 150, 50)
        self.button.clicked.connect(self.startCountdown)
        
        self.setWindowTitle('Countdown App')
        self.setGeometry(100, 100, 400, 500)
        self.show()
        
    def startCountdown(self):
        self.time_left = 10
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.timer.start(1000)
        self.button.setEnabled(False)  # Disable the button
        
    def updateCountdown(self):
        if self.time_left > 0:
            self.label.setText(f"{self.time_left}")
            self.animateLabel()
            self.time_left -= 1
        else:
            self.timer.stop()
            self.label.setText("Done!")
            self.button.setEnabled(True)  # Enable the button

    def animateLabel(self):
        # Animate the size
        self.size_animation = QPropertyAnimation(self.label, b"geometry")
        self.size_animation.setDuration(1000)
        self.size_animation.setStartValue(QRect(self.label.x(), self.label.y(), self.label.width(), self.label.height()))
        self.size_animation.setEndValue(QRect(self.label.x() - 50, self.label.y() - 50, self.label.width() + 100, self.label.height() + 100))
        
        # Animate the opacity
        self.opacity_effect = QGraphicsOpacityEffect(self.label)
        self.label.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(1000)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        
        # Group animations
        self.animation_group = QSequentialAnimationGroup()
        self.animation_group.addAnimation(self.size_animation)
        self.animation_group.addAnimation(self.opacity_animation)
        
        # Start animations
        self.animation_group.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownApp()
    sys.exit(app.exec_())