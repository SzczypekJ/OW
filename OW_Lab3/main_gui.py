from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from gui_main_window import Ui_MainWindow  # Import the generated UI class

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the UI from the generated class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Populate the main window with the UI elements

        # Access UI elements
        # self.ui.myButton.clicked.connect(self.on_button_click)

    # def on_button_click(self):
    #     print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())