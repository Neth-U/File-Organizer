import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from organizer import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("./gui.ui", self)

        self.undoBtn.setVisible(False)
        self.keepBtn.setVisible(False)
        self.msgBox.hide()


    def button_actions(self):
        self.browseBtn.clicked.connect(self.get_folder_path)
        self.undoBtn.clicked.connect(self.undo_actions)

    def get_folder_path(self):
        folder_path = self.addressBar.text()
        folder_path = Path(folder_path)
        valid_folder = True if folder_path.is_dir() and folder_path.exists() else False
        if valid_folder:
            main_logic(folder_path)

    def undo_actions(self):
        self.msgBox.setVisible(True)
        self.msgBox.setText("Undo changes successful")

def gui_main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.button_actions()

    sys.exit(app.exec_())




if __name__ == "__main__":
   gui_main()
