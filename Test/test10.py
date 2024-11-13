import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class WarningDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Warning")
        self.setGeometry(50, 50, 300, 300)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        self.title_label = QLabel("Alert Title", self)
        self.title_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        self.content_label = QLabel("Are you sure kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\nkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", self)
        
        self.yes_button = QPushButton("Yes", self)
        self.yes_button.clicked.connect(self.on_yes)
        
        self.no_button = QPushButton("No", self)
        self.no_button.clicked.connect(self.on_no)
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.yes_button)
        h_layout.addWidget(self.no_button)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.title_label)
        v_layout.addWidget(self.content_label)
        v_layout.addLayout(h_layout)
        
        self.setLayout(v_layout)
        
    def on_yes(self):
        print("Yes clicked")
        self.close()
        
    def on_no(self):
        print("No clicked")
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 500, 500)
        
        self.button = QPushButton("Show Warning", self)
        self.button.setGeometry(150, 130, 100, 30)
        self.button.clicked.connect(self.show_warning)
        
    def show_warning(self):
        self.warning_dialog = WarningDialog(self)
        self.warning_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())