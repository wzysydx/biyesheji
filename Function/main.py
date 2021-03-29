import sys

from PyQt5.QtGui import QPainter, QPixmap, QPaintEvent
from PyQt5.QtWidgets import QMainWindow, QApplication
from View.ui_main import Ui_MainWindow
from View import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def paintEvent(self, a0: QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("../UI/image/img.png")
        painter.drawPixmap(0, 0, self.width(), self.height()-self.statusBar().height(), pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
