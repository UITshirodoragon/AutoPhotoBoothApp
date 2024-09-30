import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap


class SwipeableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 800)
        self.template_path_list = []
        for i in range(1, 9):
            self.template_path_list.append(f"Data/Template/template{i}.png")
        # Colors for 10 different labels
        self.colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3', '#00FFFF', '#FF00FF', '#808080']
        self.label_widgets = []
        self.current_labels = [0, 1, 2, 3, 4]  # Always show 4 labels

        # Create a large display area
        self.large_label = QLabel("Select a Label")
        self.large_label.setStyleSheet("background-color: #FFFFFF; font-size: 30px; border: 1px solid black;")
        self.large_label.setFixedSize(400, 300)
        self.large_label.setAlignment(Qt.AlignCenter)

        # Create a layout for the small labels (100x100)
        self.small_labels_layout = QHBoxLayout()
        self.createSmallLabels()

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.large_label, 0)
        main_layout.addLayout(self.small_labels_layout, 1)

        self.startPos = None

    def createSmallLabels(self):
        for i in range(5):
            label = QLabel(f"Label {self.current_labels[i]}")
            # label.setStyleSheet(f"background-color: {self.colors[self.current_labels[i]]}; color: white; font-size: 16px;")
            label
            template_pixmap = QPixmap(f"Data/Template/template{i}.png")
            scaled_template_pixmap = template_pixmap.scaled(75,75)
            label.setPixmap(scaled_template_pixmap)
            if i == 2: label.setFixedSize(100, 100)
            else: label.setFixedSize(75, 75)
            label.setAlignment(Qt.AlignCenter)
            label.mousePressEvent = lambda event, idx=i: self.onSmallLabelClicked(idx)
            self.small_labels_layout.addWidget(label)
            self.label_widgets.append(label)

    def onSmallLabelClicked(self, idx):
        # Update the large label based on the small label clicked
        selected_label_index = self.current_labels[idx]
        self.large_label.setText(f"Label {selected_label_index}")
        template_pixmap = QPixmap(f"Data/Template/template{idx}.png")
        scaled_template_pixmap = template_pixmap.scaled(400, 400)
        self.large_label.setPixmap(scaled_template_pixmap)

    def mousePressEvent(self, event):
        self.startPos = event.pos()

    def mouseReleaseEvent(self, event):
        endPos = event.pos()
        delta = endPos.x() - self.startPos.x()

        if abs(delta) > 50:  # Vuốt đủ dài mới tính
            steps = int(delta / 150)  # Tính số bước di chuyển dựa trên khoảng vuốt
            self.updateLabels(steps)

    def updateLabels(self, steps):
        # Cập nhật label dựa vào số bước tính được
        self.current_labels = [(x + steps) % len(self.template_path_list) for x in self.current_labels]
        self.animateFadeOutIn()

    def animateFadeOutIn(self):
        # Fade out animation for current labels
        for label in self.label_widgets:
            self.fadeAnimation(label, 1.0, 0.0)

        # After fade out completes, update labels
        QTimer.singleShot(500, self.updateLabelTexts)

        # Fade in animation for new labels
        QTimer.singleShot(500, lambda: [self.fadeAnimation(label, 0.0, 1.0) for label in self.label_widgets])

    def updateLabelTexts(self):
        for i, label in enumerate(self.label_widgets):
            label.setText(f"Label {self.current_labels[i]}")
            template_pixmap = QPixmap(f"Data/Template/template{i}.png")
            scaled_template_pixmap = template_pixmap.scaled(75,75)
            label.setPixmap(scaled_template_pixmap)
            
    def fadeAnimation(self, widget, start_opacity, end_opacity):
        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(500)
        animation.setStartValue(start_opacity)
        animation.setEndValue(end_opacity)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwipeableWidget()
    window.show()
    sys.exit(app.exec_())
