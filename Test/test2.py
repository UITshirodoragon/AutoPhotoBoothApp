import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class SwipeLabels(QWidget):
    def __init__(self):
        super().__init__()
        self.current_index = 0
        self.start_pos = None
        self.total_width = 450  # Width of the visible area
        self.swipe_speed_factor = 0.005  # Adjust this factor to slow down swipe speed

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
        self.displayed_labels = self.labels[:10]
        for label in self.displayed_labels:
            self.labels_layout.addWidget(label)

        # Variable to track the current offset (relative position of the labels)
        self.offset = 0

    def mousePressEvent(self, event):
        """Capture the start position of the swipe"""
        self.start_pos = event.pos()

    def mouseMoveEvent(self, event):
        """Move the labels dynamically based on the swipe"""
        if self.start_pos:
            current_pos = event.pos()
            delta_x = (current_pos.x() - self.start_pos.x()) * self.swipe_speed_factor  # Slowed down

            # Move the labels according to delta_x
            self.move_labels(delta_x)

    def mouseReleaseEvent(self, event):
        """Handle the swipe end and update labels accordingly"""
        if self.start_pos:
            end_pos = event.pos()
            delta_x = (end_pos.x() - self.start_pos.x()) * self.swipe_speed_factor  # Slowed down

            # Update labels based on delta_x
            self.update_labels(delta_x)

        self.start_pos = None

    def move_labels(self, delta_x):
        """Move the labels according to the swipe distance"""
        for i in range(self.labels_layout.count()):
            widget = self.labels_layout.itemAt(i).widget()
            widget.move(int(widget.pos().x() + delta_x), int(widget.pos().y()))

    def update_labels(self, delta_x):
        """Update the visible labels based on the swipe distance"""
        threshold = self.total_width // 10  # Change labels after swiping one label's width
        if delta_x < -threshold:  # Swipe left
            if self.current_index + 10 < len(self.labels):
                self.current_index += 1  # Only increment if there are more labels to show
        elif delta_x > threshold:  # Swipe right
            if self.current_index > 0:
                self.current_index -= 1  # Only decrement if there are previous labels

        # Print index for debugging
        print(f"Current index: {self.current_index}")

        # Clear current layout
        for i in reversed(range(self.labels_layout.count())):
            self.labels_layout.itemAt(i).widget().setParent(None)

        # Add the new set of 4 labels
        self.displayed_labels = self.labels[self.current_index:self.current_index + 4]
        for label in self.displayed_labels:
            self.labels_layout.addWidget(label)

        # Reset positions after update and apply animation
        self.animate_labels()

    def animate_labels(self):
        """Animate the labels to slide into position smoothly"""
        for i in range(self.labels_layout.count()):
            widget = self.labels_layout.itemAt(i).widget()
            animation = QPropertyAnimation(widget, b"pos")
            animation.setDuration(500)  # Adjust the duration for smoothness
            animation.setStartValue(widget.pos())
            animation.setEndValue(QPoint(0 + i  , widget.pos().y()))  # Adjust horizontal positioning
            animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwipeLabels()
    window.setGeometry(100, 100, 450, 200)
    window.show()
    sys.exit(app.exec_())
