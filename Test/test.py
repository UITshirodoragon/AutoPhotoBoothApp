import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor


class DraggableSquare(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draggable Square")
        self.square_rect = QRect(50, 50, 100, 100)  # Vị trí và kích thước của ô vuông
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(100, 200, 150))
        painter.drawRect(self.square_rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.square_rect.contains(event.pos()):
            self.dragging = True
            # Lưu trữ offset khi nhấn để biết vị trí tương đối của ngón tay/chuột so với ô vuông
            self.offset_x = event.pos().x() - self.square_rect.x()
            self.offset_y = event.pos().y() - self.square_rect.y()

    def mouseMoveEvent(self, event):
        if self.dragging:
            # Cập nhật vị trí của ô vuông khi di chuyển chuột/ngón tay
            new_x = event.pos().x() - self.offset_x
            new_y = event.pos().y() - self.offset_y
            self.square_rect.moveTo(new_x, new_y)
            self.update()  # Vẽ lại giao diện để cập nhật vị trí ô vuông

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DraggableSquare()
    window.show()
    sys.exit(app.exec_())
