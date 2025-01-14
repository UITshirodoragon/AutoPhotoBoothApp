from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Interaction Example")
        self.setGeometry(100, 100, 800, 600)
        
        self.frame = QFrame(self)
        self.frame.setGeometry(50, 0, 700, 100)
        self.frame.setObjectName("main_frame")
        
        self.container = QWidget(self.frame)
        self.container.setGeometry(0, 0, 2000, 100)
        self.container.setObjectName("container")
        
        colors = ["lightblue", "lightgreen", "lightcoral", "lightgoldenrodyellow", "lightpink", 
                  "lightgray", "lightcyan", "lightsalmon", "lightseagreen", "lightskyblue"]
        
        self.widgets = []
        for i in range(10):
            widget = QWidget(self.container)
            widget.setGeometry(i * 200, 0, 200, 100)
            widget.setObjectName(f"widget_{i}")
            self.widgets.append(widget)
        
        self.startPos = None
        
        # Add buttons to move the container left and right
        self.left_button = QPushButton("Left", self)
        self.left_button.setGeometry(10, 500, 50, 30)
        self.left_button.clicked.connect(self.move_left)
        
        self.right_button = QPushButton("Right", self)
        self.right_button.setGeometry(70, 500, 50, 30)
        self.right_button.clicked.connect(self.move_right)
        
        self.info_widget = QFrame(self)
        self.info_widget.setGeometry(50, 100, 700, 400)
        self.info_widget.setObjectName("info_widget")
        
        # Load and apply QSS file
        self.load_stylesheet("Test/styles.qss")
    
    def load_stylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = event.pos()
    
    def mouseMoveEvent(self, event):
        if self.startPos:
            delta = event.pos() - self.startPos
            new_x = self.container.x() + delta.x()
            new_x = max(min(new_x, 0), -1300)  # Ensure new_x is between -1300 and 0
            self.container.move(new_x, self.container.y())
            self.startPos = event.pos()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.startPos and (event.pos() - self.startPos).manhattanLength() <= 10:
                self.handle_touch(event.pos())
            self.startPos = None
    
    def handle_touch(self, pos):
        for widget in self.widgets:
            if widget.geometry().contains(self.container.mapFromParent(pos)):
                self.info_widget.setStyleSheet(widget.styleSheet())
                break
    
    def move_left(self):
        new_x = self.container.x() - 10
        new_x = max(new_x, -1300)  # Ensure new_x is not less than -1300
        self.container.move(new_x, self.container.y())
    
    def move_right(self):
        new_x = self.container.x() + 10
        new_x = min(new_x, 0)  # Ensure new_x is not more than 0
        self.container.move(new_x, self.container.y())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()