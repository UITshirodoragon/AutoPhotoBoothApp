import sys
from PyQt5.QtCore import QUrl, QThread, pyqtSignal, QObject
from PyQt5.QtMultimedia import QSoundEffect

class SoundWorker(QThread):
    finished = pyqtSignal()


    def __init__(self, sound_file_path: str = None):
        super().__init__()
        self.camera_sound = QSoundEffect()
        self.camera_sound.setSource(QUrl.fromLocalFile(sound_file_path))
        self.camera_sound.setVolume(1)
    
    
        
    def run(self):
        self.camera_sound.play()
        self.finished.emit()
        
