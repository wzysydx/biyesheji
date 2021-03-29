import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPaintEvent, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from Function.main import Main
from View.ui_calmatrix import Ui_Cal_Matrix
from View.ui_main import Ui_MainWindow


class CalMatrix(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Cal_Matrix()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CalMatrix()
    form.show()
    sys.exit(app.exec_())
