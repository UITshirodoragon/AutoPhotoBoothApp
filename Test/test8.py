from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Interaction Example")
        self.setGeometry(100, 100, 500, 800)
        
        self.frame = QFrame(self)
        self.frame.setGeometry(50, 0, 400, 100)
        self.container = QWidget(self.frame)
        self.container.setGeometry(0, 0, 1000, 100)
        self.container.setStyleSheet("background-color: white; border: 1px solid black;")
        
        colors = ["lightblue", "lightgreen", "lightcoral", "lightgoldenrodyellow", "lightpink", 
                  "lightgray", "lightcyan", "lightsalmon", "lightseagreen", "lightskyblue"]
        
        self.widgets = []
        for i in range(10):
            widget = QWidget(self.container)
            widget.setGeometry(i * 100, 0, 100, 100)
            widget.setStyleSheet(f"background-color: {colors[i]}; border: 1px solid black;")
            self.widgets.append(widget)
        
        self.startPos = None
        
        # Add buttons to move the container left and right
        self.left_button = QPushButton("Left", self)
        self.left_button.setGeometry(10, 470, 50, 30)
        self.left_button.clicked.connect(self.move_left)
        
        self.right_button = QPushButton("Right", self)
        self.right_button.setGeometry(70, 470, 50, 30)
        self.right_button.clicked.connect(self.move_right)
        
        # Add widget to display the color of the touched widget
        self.info_widget = QWidget(self)
        self.info_widget.setGeometry(50, 100, 400, 400)
        self.info_widget.setStyleSheet("background-color: lightyellow; border: 1px solid black;")
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = event.pos()
    
    def mouseMoveEvent(self, event):
        if self.startPos:
            delta = event.pos() - self.startPos
            new_x = self.container.x() + delta.x()
            new_x = max(min(new_x, 0), -600)  # Ensure new_x is between -600 and 0
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
        new_x = max(new_x, -600)  # Ensure new_x is not less than -600
        self.container.move(new_x, self.container.y())
    
    def move_right(self):
        new_x = self.container.x() + 10
        new_x = min(new_x, 0)  # Ensure new_x is not greater than 0
        self.container.move(new_x, self.container.y())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())