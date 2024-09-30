import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PhotoViewer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Photo Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # QStackedWidget để chứa các ảnh
        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        # Tạo các QLabel cho mỗi ảnh
        self.labels = []
        self.image_paths = [f"Data/Template/template{i}.png" for i in range(1, 9)]  # Giả sử bạn có 10 ảnh từ image_1.png đến image_10.png
        self.current_index = 0

        for i in range(len(self.image_paths) // 4 + 1):
            widget = QWidget()
            widget_layout = QVBoxLayout()
            for j in range(4):
                if self.current_index < len(self.image_paths):
                    label = QLabel()
                    pixmap = QPixmap(self.image_paths[self.current_index])
                    label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))  # Kích thước nhỏ hơn
                    label.mousePressEvent = self.create_click_handler(self.current_index)  # Thiết lập sự kiện click
                    widget_layout.addWidget(label)
                    self.labels.append(label)
                    self.current_index += 1
            widget.setLayout(widget_layout)
            self.stacked_widget.addWidget(widget)

        # Thêm nút để vuốt trái, phải
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.show_previous)
        self.layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.show_next)
        self.layout.addWidget(self.next_button)

        self.large_label = QLabel(self)
        self.layout.addWidget(self.large_label)

    def create_click_handler(self, index):
        def handler(event):
            pixmap = QPixmap(self.image_paths[index])
            self.large_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))  # Kích thước lớn hơn
        return handler

    def show_previous(self):
        if self.stacked_widget.currentIndex() > 0:
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)

    def show_next(self):
        if self.stacked_widget.currentIndex() < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PhotoViewer()
    viewer.show()
    sys.exit(app.exec_())
