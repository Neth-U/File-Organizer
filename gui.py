import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
from organizer import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("./gui.ui", self)

        self.setFixedSize(self.size())
        self.undoBtn.setVisible(False)

    def button_actions(self):
        self.browseBtn.clicked.connect(self.get_folder)
        self.organizeBtn.clicked.connect(self.organize_folder)
        self.undoBtn.clicked.connect(self.undo_actions)

    def get_folder(self):
        self.msgBox.setText("")
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_path = Path(folder)
        self.addressBar.setText(folder)

    def organize_folder(self):
        self.folder_path = self.addressBar.text()
        if self.folder_path == "":
            return
        self.folder_path = Path(self.folder_path)

        valid_folder = True if self.folder_path.is_dir() and self.folder_path.exists() else False
        if valid_folder:
            main_logic(self.folder_path)
            self.msgBox.setText("Organizing successful!")
            self.undoBtn.setVisible(True)
        else:
            self.msgBox.setText("Invalid folder")

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
