import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot

class CounterApp(QWidget):
   
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Counter Application")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        layout = QVBoxLayout()

        # Increment Button
        self.button_increment = QPushButton("Click me to increment", self)
        self.button_increment.clicked.connect(self.increment_and_print)
        layout.addWidget(self.button_increment)

        # Decrement Button
        self.button_decrement = QPushButton("Click me to decrement", self)
        self.button_decrement.clicked.connect(self.decrement_and_print)
        layout.addWidget(self.button_decrement)

        # Set layout
        self.setLayout(layout)

    @pyqtSlot()
    def increment_and_print(self):
  
        self.counter += 1
        print(f"Clicked increment. Value = {self.counter}")

    @pyqtSlot()
    def decrement_and_print(self):
 
        self.counter -= 1
        print(f"Clicked decrement. Value = {self.counter}")


def run_app():

    app = QApplication(sys.argv)
    counter_app = CounterApp()
    counter_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()
