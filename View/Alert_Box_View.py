from PyQt5.QtWidgets import QWidget

from View.ui_Alert_Box_View import Ui_AlertBoxView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
import sys

class AlertBoxView(QWidget, Ui_AlertBoxView):
    def __init__(self, parent=None):
        super(AlertBoxView, self).__init__(parent)
        self.result = None
        self.setupUi(self)
        
        self.yes_button.clicked.connect(self.on_yes)
        self.no_button.clicked.connect(self.on_no)
        
    def set_alert_title_label(self, alert_title: str):
        self.alert_title_label.setText(alert_title)
        
    def set_alert_content_label(self, alert_content: str):
        self.alert_content_label.setText(alert_content)
        
    def exec_(self):
        self.show()
        while self.result is None:
            QApplication.processEvents()
        return self.result

    def on_yes(self):
        self.result = True
        self.close()

    def on_no(self):
        self.result = False
        self.close()
        

# class MainApp(QMainWindow):
#     def __init__(self):
#         super(MainApp, self).__init__()
#         self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle('Countdown Timer with AlertBox')
#         self.setGeometry(100, 100, 500, 500)
#         self.timer_label = QLabel('10', self)
#         self.timer_label.setAlignment(Qt.AlignCenter)
        
#         self.alert_button = QPushButton('Show AlertBox', self)
#         self.alert_button.clicked.connect(self.show_alert_box)
        
#         layout = QVBoxLayout()
#         layout.addWidget(self.timer_label)
#         layout.addWidget(self.alert_button)
        
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
        
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_timer)
#         self.time_left = 10
#         self.timer.start(1000)
        
#     def update_timer(self):
#         self.time_left -= 1
#         self.timer_label.setText(str(self.time_left))
#         if self.time_left == 0:
#             self.timer.stop()
        
#     def show_alert_box(self):
#         self.alert_box = AlertBoxView(self)
#         self.alert_box.set_alert_title_label('Alert')
#         self.alert_box.set_alert_content_label('Do you want to reset the timer?')
#         if self.alert_box.exec_():
#             self.time_left = 10
#             self.timer_label.setText(str(self.time_left))
#             self.timer.start(1000)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_app = MainApp()
#     main_app.show()
#     sys.exit(app.exec_())