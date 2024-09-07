import sys
from multiprocessing import Process, Queue
import cv2
import time
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap


def capture_frames(queue):
    cvcam = cv2.VideoCapture(0)

    while True:
        _, frame = cvcam.read()
        queue.put(frame)

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Camera App with Multiprocessing")
        
        # Layout và các thành phần GUI
        self.label = QLabel(self)
        self.fps_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.fps_label)
        self.setLayout(layout)

        # Khởi tạo queue và process
        self.queue = Queue()
        self.process = Process(target=capture_frames, args=(self.queue,))
        self.process.start()

        # FPS tính toán
        self.last_time = time.time()
        self.frame_count = 0

        # Timer để cập nhật frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        if not self.queue.empty():
            frame = self.queue.get()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(qt_image))

            # FPS calculation
            self.frame_count += 1
            current_time = time.time()
            if current_time - self.last_time >= 1.0:
                fps = self.frame_count
                self.fps_label.setText(f"FPS: {fps}")
                self.frame_count = 0
                self.last_time = current_time

    def closeEvent(self, event):
        self.process.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
