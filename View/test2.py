import sys
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QGestureEvent, QSwipeGesture, QGesture

class SwipeRainbowWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Các màu của cầu vồng
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
        
        # Vị trí bắt đầu của 2 nhãn đầu tiên
        self.current_index = 0
        
        # Tạo layout và nhãn
        self.layout = QVBoxLayout()
        self.labels = [QLabel(self.colors[i]) for i in range(7)]
        for label, color in zip(self.labels, self.colors):
            label.setStyleSheet(f"background-color: {color}; color: white; font-size: 24px; text-align: center;")
            label.setAlignment(Qt.AlignCenter)

        # Chỉ hiển thị 2 nhãn đầu tiên
        self.layout.addWidget(self.labels[self.current_index])
        self.layout.addWidget(self.labels[self.current_index + 1])
        self.setLayout(self.layout)

        # Đăng ký Swipe Gesture cho widget này
        self.grabGesture(Qt.SwipeGesture)

    def event(self, event):
        # Xử lý gesture event
        if event.type() == QEvent.Gesture:
            return self.gestureEvent(event)
        return super().event(event)

    def gestureEvent(self, event):
        if event.type() == QEvent.Gesture:
            swipe = event.gesture(Qt.SwipeGesture)
            if swipe:
                return self.handleSwipeGesture(swipe)
        return False


    def handleSwipeGesture(self, gesture):
        if gesture.state() == QGesture.Finished:
            if gesture.horizontalDirection() == QSwipeGesture.Left:
                print("Vuốt trái")
                self.updateLabels(1)
            elif gesture.horizontalDirection() == QSwipeGesture.Right:
                print("Vuốt phải")
                self.updateLabels(-1)
            return True
        return False


    def updateLabels(self, direction):
        # Tính toán vị trí mới của các nhãn
        new_index = self.current_index + 2 * direction
        if new_index < 0 or new_index + 1 >= len(self.colors):
            return  # Không di chuyển nếu đã tới đầu hoặc cuối danh sách

        # Cập nhật chỉ số hiện tại
        self.current_index = new_index

        # Xóa các nhãn hiện tại trong layout
        while self.layout.count():
            widget = self.layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        # Hiển thị nhãn mới
        self.layout.addWidget(self.labels[self.current_index])
        self.layout.addWidget(self.labels[self.current_index + 1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SwipeRainbowWidget()
    w.resize(300, 200)
    w.show()
    sys.exit(app.exec_())
