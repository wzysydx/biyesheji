import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from View.ui_calmatrix import Ui_Cal_Matrix


class CalMatrix(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Cal_Matrix()
        self.ui.setupUi(self)

    @pyqtSlot()    ##设置行数，即参数个数
    def on_btnSetRows_clicked(self):
        self.ui.tableWidget.setRowCount(self.ui.spinBox.value())

    @pyqtSlot()  ##添加一行
    def on_btnAppendRow_clicked(self):
        curRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(curRow)

    @pyqtSlot()  ##删除指定行
    def on_btnDelRow_clicked(self):
        curRow = self.ui.tableWidget.currentRow()  # 当前行号
        self.ui.tableWidget.removeRow(curRow)

    @pyqtSlot()  ##自动行高
    def on_btnAutoHeight_clicked(self):
        self.ui.tableWidget.resizeRowsToContents()

    @pyqtSlot()  ##自动列宽
    def on_btnAutoWidth_clicked(self):
        self.ui.tableWidget.resizeColumnsToContents()

    @pyqtSlot()
    def on_btnRes_clicked(self):
        rowCount = self.ui.tableWidget.rowCount() # 获取总行数，即参数个数
        if rowCount==0:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CalMatrix()
    form.show()
    sys.exit(app.exec_())