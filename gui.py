import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from organizer import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("./gui.ui", self)

        self.setFixedSize(self.size())
        self.undoBtn.setVisible(False)
        self.msgBox.hide()


    def button_actions(self):
        self.browseBtn.clicked.connect(self.get_folder_path)
        self.undoBtn.clicked.connect(self.undo_actions)

    def get_folder_path(self):
        self.folder_path = self.addressBar.text()
        if self.folder_path == "":
            return
        self.folder_path = Path(self.folder_path)
        valid_folder = True if self.folder_path.is_dir() and self.folder_path.exists() else False
        if valid_folder:
            main_logic(self.folder_path)
        self.msgBox.setVisible(True)
        self.msgBox.setText("Organizing successful!")
        self.undoBtn.setVisible(True)
    def undo_actions(self):
        undo_func(self.folder_path)
        self.msgBox.setText("Undo changes successful")
        self.undoBtn.setVisible(False)

def gui_main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.button_actions()

    sys.exit(app.exec_())




if __name__ == "__main__":
   gui_main()
