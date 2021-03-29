from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cal_Matrix(object):
    def setupUi(self, Cal_Matrix):
        Cal_Matrix.setObjectName("Cal_Matrix")
        Cal_Matrix.resize(757, 524)
        self.tableWidget = QtWidgets.QTableWidget(Cal_Matrix)
        self.tableWidget.setGeometry(QtCore.QRect(380, 20, 321, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.btnRes = QtWidgets.QPushButton(Cal_Matrix)
        self.btnRes.setGeometry(QtCore.QRect(130, 210, 111, 51))
        self.btnRes.setObjectName("btnRes")
        self.btnAppendRow = QtWidgets.QPushButton(Cal_Matrix)
        self.btnAppendRow.setGeometry(QtCore.QRect(130, 70, 111, 51))
        self.btnAppendRow.setObjectName("btnAppendRow")
        self.btnDelRow = QtWidgets.QPushButton(Cal_Matrix)
        self.btnDelRow.setGeometry(QtCore.QRect(130, 140, 111, 51))
        self.btnDelRow.setObjectName("btnDelRow")

        self.retranslateUi(Cal_Matrix)
        QtCore.QMetaObject.connectSlotsByName(Cal_Matrix)

    def retranslateUi(self, Cal_Matrix):
        _translate = QtCore.QCoreApplication.translate
        Cal_Matrix.setWindowTitle(_translate("Cal_Matrix", "可压性矩阵计算"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Cal_Matrix", "参数名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Cal_Matrix", "等级"))
        self.btnRes.setText(_translate("Cal_Matrix", "计算可压性矩阵"))
        self.btnAppendRow.setText(_translate("Cal_Matrix", "添加参数"))
        self.btnDelRow.setText(_translate("Cal_Matrix", "删除参数"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cal_Matrix = QtWidgets.QWidget()
    ui = Ui_Cal_Matrix()
    ui.setupUi(Cal_Matrix)
    Cal_Matrix.show()
    sys.exit(app.exec_())
