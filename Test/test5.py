import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)

    def run(self):
        total = 100000
        for i in range(1, total + 1):
            time.sleep(0.0001)  # Simulate a long process
            percent_complete = int((i / total) * 100)
            self.progress.emit(percent_complete)

class LoadingScreen(QMainWindow):
    progress = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(50, 50, 200, 25)
        self.progressBar.setMaximum(100)

        self.label = QLabel("Processing...", self)
        self.label.setGeometry(50, 80, 200, 25)
        self.label.setAlignment(Qt.AlignCenter)

        self.completionLabel = QLabel(self)
        self.completionLabel.setGeometry(0, 0, 0, 0)  # Initially hidden

        self.worker = QThread()
        self.worker.run = self.run
        self.progress.connect(self.update_progress)
        
        self.worker.start()
        
        
        



    def update_progress(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            self.label.setText("Completed")
            self.completionLabel.setGeometry(50, 50, 400, 400)
            self.completionLabel.setStyleSheet("background-color: green;")
            self.completionLabel.setText("Task Completed")
            self.completionLabel.setAlignment(Qt.AlignCenter)
            
    def run(self):
        total = 100000
        for i in range(1, total + 1):
            time.sleep(0.0001)  # Simulate a long process
            percent_complete = int((i / total) * 100)
            self.progress.emit(percent_complete)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    sys.exit(app.exec_())