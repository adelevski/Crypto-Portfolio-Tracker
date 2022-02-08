from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 300, 800, 450)
    win.setWindowTitle("Crypto-GUI")

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()