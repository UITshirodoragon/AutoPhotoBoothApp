
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys
import time


class Worker(QObject):
    # Slot nhận tín hiệu từ main thread
    @pyqtSlot(str)
    def process_data(self, data):
        print(f"Worker received data: {data}")
        # Mô phỏng xử lý trong worker thread
        time.sleep(2)
        print("Worker finished processing")


class MainApp(QWidget):
    send_data = pyqtSignal(str)  # Tín hiệu gửi từ main thread đến worker

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initWorker()

    def initUI(self):
        self.setWindowTitle("PyQt5 Signal to Worker Thread")
        layout = QVBoxLayout()
        
        self.button = QPushButton("Send to Worker")
        self.button.clicked.connect(self.sendToWorker)
        
        layout.addWidget(self.button)
        self.setLayout(layout)

    def initWorker(self):
        self.thread = QThread()  # Tạo một thread riêng
        self.worker = Worker()  # Tạo worker
        
        # Di chuyển worker vào thread
        self.worker.moveToThread(self.thread)
        
        # Kết nối tín hiệu từ main thread đến slot trong worker
        self.send_data.connect(self.worker.process_data)
        
        # Bắt đầu thread
        self.thread.start()

    def sendToWorker(self):
        # Gửi tín hiệu với dữ liệu là một chuỗi
        self.send_data.emit("Hello from Khoa")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
