import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt , QSize, pyqtSignal, QThread, QThreadPool
from PyQt5.QtGui import QImage, QPixmap, QMovie, QIcon

import cv2
import numpy as np
from rembg import remove, new_session
from Background_Remover_Model import BackgroundRemoverWorker
import logging


class BackgroundRemoverApp(QWidget):

    image_path_signal = pyqtSignal(str)
    start_remove_background_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.worker = BackgroundRemoverWorker(self.selected_image_path)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        
        self.worker_thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.worker_thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        self.worker.error.connect(self.worker_error)
        self.worker.finished.connect(self.done_remove_background)
        # self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.image_path_signal.connect(self.worker.receive_image_path)
        self.start_remove_background_signal.connect(self.worker.start_remove_background)
        self.worker_thread.start()
        

    def initUI(self):
        self.setWindowTitle('Background Remover App')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.imageList = QListWidget()
        self.imageList.itemClicked.connect(self.displayImage)
        layout.addWidget(self.imageList)

        imageLayout = QHBoxLayout()
        self.currentImageLabel = QLabel('Current Image')
        self.currentImageLabel.setFixedSize(400, 400)
        self.resultImageLabel = QLabel('Result Image')
        self.resultImageLabel.setFixedSize(400, 400)
        imageLayout.addWidget(self.currentImageLabel)
        imageLayout.addWidget(self.resultImageLabel)
        layout.addLayout(imageLayout)

        self.removeBgButton = QPushButton('Xóa Background')
        self.removeBgButton.clicked.connect(self.removeBackground)
        layout.addWidget(self.removeBgButton)
        
        self.selected_image_path = None

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("AI_Test\loading.gif")
        self.movie.setScaledSize(QSize(400, 400))
        
        self.resultImageLabel.setMovie(self.movie)
        self.resultImageLabel.setAlignment(Qt.AlignCenter)
        
        
        
        
        self.setLayout(layout)
        self.loadImages()

    def loadImages(self):
        imageDir = 'AI_Test\\test_images'
        for imageName in os.listdir(imageDir):
            if imageName.endswith(('.png', '.jpg', '.jpeg')):
                self.imageList.addItem(imageName)

    def displayImage(self, item):
        self.resultImageLabel.clear()
        imageDir = 'AI_Test\\test_images'
        imagePath = imageDir + '\\' + item.text()
        self.selected_image_path = imagePath
        pixmap = QPixmap(imagePath)
        if not pixmap.isNull():
            self.currentImageLabel.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.currentImageLabel.setAlignment(Qt.AlignCenter)
        else:
            self.currentImageLabel.setText('Image not found or unable to load')
            self.currentImageLabel.setAlignment(Qt.AlignCenter)

    def show_loading_gif(self):
        self.resultImageLabel.setMovie(self.movie)
        self.movie.start()
        
    def hide_loading_gif(self):
        self.movie.stop()
        self.resultImageLabel.clear()
        
    def displayResultImage(self, imagePath):
        pixmap = QPixmap(imagePath)
        if not pixmap.isNull():
            self.resultImageLabel.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.resultImageLabel.setAlignment(Qt.AlignCenter)
        else:
            self.resultImageLabel.setText('Image not found or unable to load')
            self.resultImageLabel.setAlignment(Qt.AlignCenter)
            
    def done_remove_background(self):
        self.hide_loading_gif()
        self.displayResultImage('AI_Test\\test_results\\' + os.path.basename(self.selected_image_path))

    def removeBackground(self):
        if self.selected_image_path:
            self.show_loading_gif()
            self.image_path_signal.emit(self.selected_image_path)   
            self.start_remove_background_signal.emit()
           
            
        else:
            print("No image selected")
            
    def worker_error(self, error):
        print(error)    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BackgroundRemoverApp()
    ex.show()
    sys.exit(app.exec_())