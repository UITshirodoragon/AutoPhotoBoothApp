from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

class GifViewer(QWidget):
    def __init__(self, gif_path, svg_path):
        super().__init__()
        
        self.setWindowTitle("GIF and SVG Viewer")
        self.setGeometry(100, 100, 400, 300)
        
        # Background widget
        self.background_widget = QWidget(self)
        self.background_widget.setStyleSheet("background-color: yellow;")
        
        # GIF
        self.gif_label = QLabel(self.background_widget)
        self.gif_movie = QMovie(gif_path)
        self.gif_label.setMovie(self.gif_movie)
        
        # SVG
        self.svg_widget = QSvgWidget(svg_path, self.background_widget)
        
        layout = QVBoxLayout()
        layout.addWidget(self.gif_label)
        layout.addWidget(self.svg_widget)
        self.background_widget.setLayout(layout)
        
        self.gif_movie.start()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    viewer = GifViewer("path_to_your_gif.gif", "path_to_your_svg.svg")
    viewer.show()
    sys.exit(app.exec_())