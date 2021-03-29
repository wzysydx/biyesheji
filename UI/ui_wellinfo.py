# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wellinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wellinfo(object):
    def setupUi(self, wellinfo):
        wellinfo.setObjectName("wellinfo")
        wellinfo.resize(222, 365)
        self.verticalLayout = QtWidgets.QVBoxLayout(wellinfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.well_description = QtWidgets.QGroupBox(wellinfo)
        self.well_description.setObjectName("well_description")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.well_description)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_block = QtWidgets.QLineEdit(self.well_description)
        self.le_block.setObjectName("le_block")
        self.gridLayout.addWidget(self.le_block, 0, 1, 1, 2)
        self.lb_layer = QtWidgets.QLabel(self.well_description)
        self.lb_layer.setObjectName("lb_layer")
        self.gridLayout.addWidget(self.lb_layer, 2, 0, 1, 2)
        self.lb_wellnum = QtWidgets.QLabel(self.well_description)
        self.lb_wellnum.setObjectName("lb_wellnum")
        self.gridLayout.addWidget(self.lb_wellnum, 1, 0, 1, 1)
        self.lb_bolck = QtWidgets.QLabel(self.well_description)
        self.lb_bolck.setObjectName("lb_bolck")
        self.gridLayout.addWidget(self.lb_bolck, 0, 0, 1, 1)
        self.le_wellnum = QtWidgets.QLineEdit(self.well_description)
        self.le_wellnum.setObjectName("le_wellnum")
        self.gridLayout.addWidget(self.le_wellnum, 1, 1, 1, 2)
        self.le_layer = QtWidgets.QLineEdit(self.well_description)
        self.le_layer.setObjectName("le_layer")
        self.gridLayout.addWidget(self.le_layer, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.well_description)
        self.layer_description = QtWidgets.QGroupBox(wellinfo)
        self.layer_description.setObjectName("layer_description")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layer_description)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_top = QtWidgets.QLabel(self.layer_description)
        self.lb_top.setMinimumSize(QtCore.QSize(50, 0))
        self.lb_top.setObjectName("lb_top")
        self.horizontalLayout.addWidget(self.lb_top)
        self.sb_top = QtWidgets.QDoubleSpinBox(self.layer_description)
        self.sb_top.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_top.setDecimals(3)
        self.sb_top.setMaximum(5000.0)
        self.sb_top.setObjectName("sb_top")
        self.horizontalLayout.addWidget(self.sb_top)
        self.label_5 = QtWidgets.QLabel(self.layer_description)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_bottom = QtWidgets.QLabel(self.layer_description)
        self.lb_bottom.setMinimumSize(QtCore.QSize(50, 0))
        self.lb_bottom.setObjectName("lb_bottom")
        self.horizontalLayout_2.addWidget(self.lb_bottom)
        self.sb_bottom = QtWidgets.QDoubleSpinBox(self.layer_description)
        self.sb_bottom.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_bottom.setDecimals(3)
        self.sb_bottom.setMaximum(5000.0)
        self.sb_bottom.setObjectName("sb_bottom")
        self.horizontalLayout_2.addWidget(self.sb_bottom)
        self.label_6 = QtWidgets.QLabel(self.layer_description)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_layertype = QtWidgets.QLabel(self.layer_description)
        self.lb_layertype.setMinimumSize(QtCore.QSize(80, 0))
        self.lb_layertype.setObjectName("lb_layertype")
        self.horizontalLayout_3.addWidget(self.lb_layertype)
        self.cb_layertype = QtWidgets.QComboBox(self.layer_description)
        self.cb_layertype.setObjectName("cb_layertype")
        self.cb_layertype.addItem("")
        self.cb_layertype.addItem("")
        self.horizontalLayout_3.addWidget(self.cb_layertype)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layer_description)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.layer_description)
        self.pb_confirm = QtWidgets.QPushButton(wellinfo)
        self.pb_confirm.setObjectName("pb_confirm")
        self.verticalLayout.addWidget(self.pb_confirm)

        self.retranslateUi(wellinfo)
        QtCore.QMetaObject.connectSlotsByName(wellinfo)

    def retranslateUi(self, wellinfo):
        _translate = QtCore.QCoreApplication.translate
        wellinfo.setWindowTitle(_translate("wellinfo", "目标井参数录入"))
        self.well_description.setTitle(_translate("wellinfo", "可压性评价井描述："))
        self.lb_layer.setText(_translate("wellinfo", "所在层位："))
        self.lb_wellnum.setText(_translate("wellinfo", "井号："))
        self.lb_bolck.setText(_translate("wellinfo", "区块："))
        self.layer_description.setTitle(_translate("wellinfo", "评价层段描述："))
        self.lb_top.setText(_translate("wellinfo", "顶深："))
        self.label_5.setText(_translate("wellinfo", "m"))
        self.lb_bottom.setText(_translate("wellinfo", "底深："))
        self.label_6.setText(_translate("wellinfo", "m"))
        self.lb_layertype.setText(_translate("wellinfo", "层段类型："))
        self.cb_layertype.setItemText(0, _translate("wellinfo", "页岩储层"))
        self.cb_layertype.setItemText(1, _translate("wellinfo", "砂岩储层"))
        self.plainTextEdit.setPlainText(_translate("wellinfo", "默认为由测井资料导入的全井段\n"
""))
        self.pb_confirm.setText(_translate("wellinfo", "确定选择"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wellinfo = QtWidgets.QWidget()
    ui = Ui_wellinfo()
    ui.setupUi(wellinfo)
    wellinfo.show()
    sys.exit(app.exec_())