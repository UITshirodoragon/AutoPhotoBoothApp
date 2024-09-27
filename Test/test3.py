import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class SwipeLabels(QWidget):
    def __init__(self):
        super().__init__()
        self.current_index = 0

        # List of colors for labels
        self.colors = [
            'red', 'green', 'blue', 'yellow', 'purple', 
            'orange', 'pink', 'cyan', 'brown', 'gray'
        ]

        # Create list of labels with different background colors
        self.labels = []
        for i in range(10):
            label = QLabel(f"Label {i + 1}")
            label.setStyleSheet(f"background-color: {self.colors[i]}; color: white; font-size: 20px; padding: 20px;")
            self.labels.append(label)

        # Main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create a widget to hold the labels and add it to the layout
        self.labels_widget = QWidget()
        self.labels_layout = QHBoxLayout()
        self.labels_widget.setLayout(self.labels_layout)
        self.main_layout.addWidget(self.labels_widget)

        # Only show 4 labels at a time
        self.displayed_labels = self.labels[:4]
        for label in self.displayed_labels:
            self.labels_layout.addWidget(label)

        # Enable swipe gesture
        self.setMouseTracking(True)
        self.start_pos = None

    def update_labels(self, direction):
        """Update the visible labels based on the swipe direction"""
        if direction == 'left' and self.current_index + 4 < len(self.labels):
            self.current_index += 1
        elif direction == 'right' and self.current_index > 0:
            self.current_index -= 1

        # Clear current layout
        for i in reversed(range(self.labels_layout.count())):
            self.labels_layout.itemAt(i).widget().setParent(None)

        # Add the new set of 4 labels with updated colors
        self.displayed_labels = self.labels[self.current_index:self.current_index + 4]
        for label in self.displayed_labels:
            self.labels_layout.addWidget(label)

    def mousePressEvent(self, event):
        """Capture the start position of the swipe"""
        self.start_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """Handle the swipe detection and animate the label update"""
        if self.start_pos:
            end_pos = event.pos()
            delta_x = end_pos.x() - self.start_pos.x()

            if delta_x < -50:  # Swipe left
                self.update_labels('left')
            elif delta_x > 50:  # Swipe right
                self.update_labels('right')

        self.start_pos = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwipeLabels()
    window.setGeometry(100, 100, 450, 200)
    window.show()
    sys.exit(app.exec_())
