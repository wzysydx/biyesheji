# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 646)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_P = QtWidgets.QMenu(self.menubar)
        self.menu_P.setObjectName("menu_P")
        self.menu_I = QtWidgets.QMenu(self.menubar)
        self.menu_I.setObjectName("menu_I")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actFile_wellinfo = QtWidgets.QAction(MainWindow)
        self.actFile_wellinfo.setObjectName("actFile_wellinfo")
        self.actFile_loadlogdata = QtWidgets.QAction(MainWindow)
        self.actFile_loadlogdata.setObjectName("actFile_loadlogdata")
        self.actCal_property = QtWidgets.QAction(MainWindow)
        self.actCal_property.setObjectName("actCal_property")
        self.actCal_brit = QtWidgets.QAction(MainWindow)
        self.actCal_brit.setCheckable(False)
        self.actCal_brit.setEnabled(True)
        self.actCal_brit.setObjectName("actCal_brit")
        self.actCal_fi = QtWidgets.QAction(MainWindow)
        self.actCal_fi.setObjectName("actCal_fi")
        self.actCal_cor = QtWidgets.QAction(MainWindow)
        self.actCal_cor.setEnabled(False)
        self.actCal_cor.setObjectName("actCal_cor")
        self.actPaint_property = QtWidgets.QAction(MainWindow)
        self.actPaint_property.setObjectName("actPaint_property")
        self.actPaint_fi = QtWidgets.QAction(MainWindow)
        self.actPaint_fi.setObjectName("actPaint_fi")
        self.actExport_excel = QtWidgets.QAction(MainWindow)
        self.actExport_excel.setObjectName("actExport_excel")
        self.actExport_txt = QtWidgets.QAction(MainWindow)
        self.actExport_txt.setObjectName("actExport_txt")
        self.actHelp_instruction = QtWidgets.QAction(MainWindow)
        self.actHelp_instruction.setObjectName("actHelp_instruction")
        self.actFile_exit = QtWidgets.QAction(MainWindow)
        self.actFile_exit.setObjectName("actFile_exit")
        self.menu.addAction(self.actFile_wellinfo)
        self.menu.addAction(self.actFile_loadlogdata)
        self.menu.addSeparator()
        self.menu.addAction(self.actFile_exit)
        self.menu_2.addAction(self.actCal_brit)
        self.menu_2.addAction(self.actCal_property)
        self.menu_2.addAction(self.actCal_fi)
        self.menu_2.addAction(self.actCal_cor)
        self.menu_P.addAction(self.actPaint_property)
        self.menu_P.addAction(self.actPaint_fi)
        self.menu_I.addAction(self.actExport_excel)
        self.menu_I.addAction(self.actExport_txt)
        self.menu_H.addAction(self.actHelp_instruction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_P.menuAction())
        self.menubar.addAction(self.menu_I.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.actFile_exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "陆相页岩可压性评价软件-version1.0"))
        self.menu.setTitle(_translate("MainWindow", "文件（&F）"))
        self.menu_2.setTitle(_translate("MainWindow", "计算（&C）"))
        self.menu_P.setTitle(_translate("MainWindow", "曲线（&P）"))
        self.menu_I.setTitle(_translate("MainWindow", "成果导出（&E）"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助（&H）"))
        self.actFile_wellinfo.setText(_translate("MainWindow", "输入井段参数"))
        self.actFile_loadlogdata.setText(_translate("MainWindow", "导入测井数据"))
        self.actFile_loadlogdata.setToolTip(_translate("MainWindow", "导入测井数据"))
        self.actCal_property.setText(_translate("MainWindow", "岩石力学参数计算"))
        self.actCal_property.setToolTip(_translate("MainWindow", "岩石力学参数计算"))
        self.actCal_brit.setText(_translate("MainWindow", "脆性计算方法"))
        self.actCal_fi.setText(_translate("MainWindow", "可压性计算"))
        self.actCal_cor.setText(_translate("MainWindow", "压裂施工校正"))
        self.actPaint_property.setText(_translate("MainWindow", "岩石力学参数曲线"))
        self.actPaint_property.setToolTip(_translate("MainWindow", "岩石力学参数曲线"))
        self.actPaint_fi.setText(_translate("MainWindow", "可压性曲线"))
        self.actExport_excel.setText(_translate("MainWindow", "导出为excel文件"))
        self.actExport_txt.setText(_translate("MainWindow", "导出为txt文件"))
        self.actHelp_instruction.setText(_translate("MainWindow", "说明"))
        self.actFile_exit.setText(_translate("MainWindow", "退出"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
