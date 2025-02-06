from __future__ import annotations
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow, QPushButton, QHBoxLayout, QSizePolicy, QFrame, QGraphicsOpacityEffect, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt, QSize, QRect, QPropertyAnimation, QTimer, QSequentialAnimationGroup
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPalette, QColor, QMovie
from PyQt5.uic import loadUi
from typing import Protocol
from cv2.typing import MatLike

from View.ui_Image_Capture_View import Ui_Image_Capture_View
from View.Alert_Box_View import AlertBoxView


class ImageCaptureView(QWidget, Ui_Image_Capture_View ):
    ICV_back_button_signal = pyqtSignal()
    ICV_next_button_signal = pyqtSignal()
    ICV_capture_button_signal = pyqtSignal()
    ICV_export_template_button_clicked_signal = pyqtSignal()
    ICV_remove_background_button_clicked_signal = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setupUi(self)
        
        self.image_gallery_container_widget = QWidget(self.image_gallery_frame)       
        self.image_gallery_container_widget.setGeometry(0, 0, 30, 200)
        self.image_gallery_container_layout = QHBoxLayout()
        self.image_gallery_container_widget.setLayout(self.image_gallery_container_layout)
       
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        self.next_button.clicked.connect(self.emit_next_button_clicked_signal)
        self.capture_button.clicked.connect(self.emit_capture_button_clicked_signal)

        self.next_button.hide()
        
        self.export_template_button = QPushButton(self)
        self.export_template_button.setGeometry(25,1595,200,50)
        self.export_template_button.setText("Export Template")
        self.export_template_button.clicked.connect(self.emit_export_template_button_clicked_signal)
        self.export_template_button.hide()
        
        
        self.remove_background_button = QPushButton(self)
        self.remove_background_button.setGeometry(250,1595,200,50)
        self.remove_background_button.setCheckable(True)
        self.remove_background_button.clicked.connect(self.emit_remove_background_button_clicked_signal)
        self.remove_background_button.setText("Remove Background")
        self.remove_background_button.hide()
        
        self.loading_remove_background_label = QLabel(self)
        self.loading_remove_background_label.setGeometry(250,1595,50,50)
        self.loading_remove_background_label.hide()
        
        self.loading_remove_background_gif = QMovie("View/Gif/loading.gif")
        self.loading_remove_background_gif.setScaledSize(QSize(50,50))
        self.loading_remove_background_label.setMovie(self.loading_remove_background_gif)
        self.loading_remove_background_label.setAlignment(Qt.AlignCenter)
        
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.ICV_back_button_signal.emit()
        
    def emit_next_button_clicked_signal(self) -> None:
        self.ICV_next_button_signal.emit() 
        
    def emit_capture_button_clicked_signal(self) -> None:
        self.ICV_capture_button_signal.emit() 
        
    def emit_export_template_button_clicked_signal(self) -> None:
        self.ICV_export_template_button_clicked_signal.emit()
        
    def emit_remove_background_button_clicked_signal(self) -> None:
        self.ICV_remove_background_button_clicked_signal.emit()
        
    def hide_remove_background_button(self):
        self.remove_background_button.hide()
        
    def show_remove_background_button(self):  
        self.remove_background_button.show()
        
    def hide_loading_remove_background_label(self):
        self.loading_remove_background_label.hide()
        self.loading_remove_background_gif.stop()
        
    def show_loading_remove_background_label(self):
        self.loading_remove_background_label.show()
        self.loading_remove_background_gif.start()



    def update_preview_image_gui(self, frame: MatLike) -> None:
        height, width, channel = frame.shape
        bytesPerLine = channel * width
        image = QImage(frame.data.tobytes(), width, height, bytesPerLine, QImage.Format_BGR888)
        # self.preview_reigion.setPixmap(QPixmap.fromImage(image))
        self.preview_image_label.setPixmap(QPixmap.fromImage(image).scaled(1080,1440, Qt.KeepAspectRatio))


    def update_preview_fps_gui(self, fps: float) -> None:
        # self.fps.setText(f"FPS: {fps}")
        self.preview_fps_label.setText(f"FPS: {fps}")
        
    def update_number_of_captured_images_gui(self, number_of_captured_images: int, number_of_images_in_template: int) -> None:
        if(number_of_images_in_template != 0):
            if(number_of_captured_images == number_of_images_in_template):
                self.number_of_captured_images_label.setStyleSheet("color: green")
            else:
                self.number_of_captured_images_label.setStyleSheet("color: red")
            self.number_of_captured_images_label.setText(f"{number_of_captured_images}/{number_of_images_in_template}")
        else:
            self.number_of_captured_images_label.setStyleSheet("color: red")
            self.number_of_captured_images_label.setText("NA/NA")
            
    def update_countdown_number_label_gui(self, countdown_number_icon_path: str) -> None:
        self.countdown_number_label.setPixmap(QPixmap(countdown_number_icon_path).scaled(360,360, Qt.KeepAspectRatio))
        
    def animate_countdown_number_label_gui(self):
        
        # # Animate the size
        # self.size_animation = QPropertyAnimation(self.label, b"geometry")
        # self.size_animation.setDuration(1000)
        # self.size_animation.setStartValue(QRect(self.label.x(), self.label.y(), self.label.width(), self.label.height()))
        # self.size_animation.setEndValue(QRect(self.label.x() - 50, self.label.y() - 50, self.label.width() + 100, self.label.height() + 100))
        
        # Animate the opacity
        self.opacity_effect = QGraphicsOpacityEffect(self.countdown_number_label)
        self.countdown_number_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(1000)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        
        # # Group animations
        self.animation_group = QSequentialAnimationGroup()
        # self.animation_group.addAnimation(self.size_animation)
        self.animation_group.addAnimation(self.opacity_animation)
        
        # # Start animations
        self.animation_group.start()
    
    def clear_countdown_number_label_gui(self):
        self.countdown_number_label.clear()
        self.capture_button.setEnabled(True)
        
    def show_export_tempate_button(self):
        self.export_template_button.show()
        
        
    def hide_export_tempate_button(self):
        self.export_template_button.hide()
    
    
    def show_dialog_alert_to_clear_image_gallery(self):
        # alert_go_back_box = QMessageBox(self)
        # alert_go_back_box.setWindowTitle('ALERT!')
        
        # alert_go_back_box.setText('Your images will be deleted.\nAre you sure to go to the Template Menu?')
        # alert_go_back_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # alert_go_back_box.setDefaultButton(QMessageBox.No)
        # yes_button = alert_go_back_box.button(QMessageBox.Yes)
        # no_button = alert_go_back_box.button(QMessageBox.No)
        # yes_button.setObjectName("Yes")
        # no_button.setObjectName("No")

        # alert_go_back_box.setStyleSheet("""
        
        # QPushButton {
        #     color: white;
        #     border-radius: 5px;
        #     padding: 20px 40px; /* Increase padding for larger buttons */
        #     font-size: 30px;    /* Increase font size */
        # }
        # QPushButton#No {
        #     background-color: green;
        # }
        # QPushButton#No:hover {
        #     background-color: darkgreen;
        # }
        # QPushButton#Yes {
        #     background-color: red;
        # }
        # QPushButton#Yes:hover {
        #     background-color: darkred;
        # }
        # QLabel {
        #     color: red;
        #     font-size: 25px;
        # }
        # """)

        alert_go_back_box = AlertBoxView(self)
        alert_go_back_box.setGeometry(340, 860, 400, 200)
        alert_go_back_box.set_alert_title_label('ALERT!')
        alert_go_back_box.set_alert_content_label('Your images will be deleted.\nAre you sure to go to the Template Menu?')
        
        reply = alert_go_back_box.exec_()

        return reply