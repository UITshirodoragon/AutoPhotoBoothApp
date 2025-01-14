import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl, QThread, pyqtSignal, QObject
from PyQt5.QtMultimedia import QSoundEffect

# class SoundWorker(QObject):
#     finished = pyqtSignal()

#     def __init__(self):
#         super().__init__()
#         self.camera_sound = QSoundEffect()
#         self.camera_sound.setSource(QUrl.fromLocalFile('Test/camera_shutter.wav'))
#         self.camera_sound.setVolume(1)

#     def play_sound(self):
#         self.camera_sound.play()
#         self.finished.emit()
        
class SoundWorker(QThread):
    finished = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.camera_sound = QSoundEffect()
        self.camera_sound.setSource(QUrl.fromLocalFile('Test/camera_shutter.wav'))
        self.camera_sound.setVolume(1)
        
    def run(self):
        self.camera_sound.play()
        self.finished.emit()
        
    
    

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.initUI()

        
        

    def initUI(self):
        self.setWindowTitle('Camera App')

        # Create a button
        self.button = QPushButton('Capture', self)
        self.button.clicked.connect(self.play_camera_sound)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def play_camera_sound(self):
        # Set up the sound worker and thread
        self.sound_worker = SoundWorker()
        self.sound_worker.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CameraApp()
    ex.show()
    sys.exit(app.exec_())