from PyQt5.QtWidgets import QApplication
from .dlgs.main_window import MainWindow
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    exitcode = app.exec()
