# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_sample.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_3.addWidget(self.listWidget_var)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_selected_add_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/arrow_right_hover.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add_2.setIcon(icon)
        self.pushButton_selected_add_2.setObjectName("pushButton_selected_add_2")
        self.verticalLayout_4.addWidget(self.pushButton_selected_add_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_weight_add_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_weight_add_2.setText("")
        self.pushButton_weight_add_2.setIcon(icon)
        self.pushButton_weight_add_2.setObjectName("pushButton_weight_add_2")
        self.verticalLayout_16.addWidget(self.pushButton_weight_add_2)
        self.verticalLayout.addLayout(self.verticalLayout_16)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget_selected = QtWidgets.QListWidget(self.tab)
        self.listWidget_selected.setObjectName("listWidget_selected")
        self.horizontalLayout_6.addWidget(self.listWidget_selected)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_selected_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pyqt/source/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add.setIcon(icon1)
        self.pushButton_selected_add.setObjectName("pushButton_selected_add")
        self.verticalLayout_6.addWidget(self.pushButton_selected_add)
        self.pushButton_selected_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_up.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pyqt/source/images/up1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_up.setIcon(icon2)
        self.pushButton_selected_up.setObjectName("pushButton_selected_up")
        self.verticalLayout_6.addWidget(self.pushButton_selected_up)
        self.pushButton_selected_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_down.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pyqt/source/images/down1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_down.setIcon(icon3)
        self.pushButton_selected_down.setObjectName("pushButton_selected_down")
        self.verticalLayout_6.addWidget(self.pushButton_selected_down)
        self.pushButton_selected_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_del.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_del.setIcon(icon4)
        self.pushButton_selected_del.setObjectName("pushButton_selected_del")
        self.verticalLayout_6.addWidget(self.pushButton_selected_del)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget_weight = QtWidgets.QListWidget(self.tab)
        self.listWidget_weight.setObjectName("listWidget_weight")
        self.horizontalLayout_7.addWidget(self.listWidget_weight)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_weight_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_weight_add.setText("")
        self.pushButton_weight_add.setIcon(icon1)
        self.pushButton_weight_add.setObjectName("pushButton_weight_add")
        self.verticalLayout_7.addWidget(self.pushButton_weight_add)
        self.pushButton_weight_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_weight_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_weight_up.setText("")
        self.pushButton_weight_up.setIcon(icon2)
        self.pushButton_weight_up.setObjectName("pushButton_weight_up")
        self.verticalLayout_7.addWidget(self.pushButton_weight_up)
        self.pushButton_weight_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_weight_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_weight_down.setText("")
        self.pushButton_weight_down.setIcon(icon3)
        self.pushButton_weight_down.setObjectName("pushButton_weight_down")
        self.verticalLayout_7.addWidget(self.pushButton_weight_down)
        self.pushButton_weight_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_weight_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_weight_del.setText("")
        self.pushButton_weight_del.setIcon(icon4)
        self.pushButton_weight_del.setObjectName("pushButton_weight_del")
        self.verticalLayout_7.addWidget(self.pushButton_weight_del)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_dataset_name = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_dataset_name.setText("")
        self.lineEdit_dataset_name.setObjectName("lineEdit_dataset_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dataset_name)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.comboBox_replace = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_replace.setObjectName("comboBox_replace")
        self.comboBox_replace.addItem("")
        self.comboBox_replace.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_replace)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.spinBox_random_state = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_random_state.setMaximum(999999999)
        self.spinBox_random_state.setProperty("value", 12345)
        self.spinBox_random_state.setObjectName("spinBox_random_state")
        self.horizontalLayout_15.addWidget(self.spinBox_random_state)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton_size = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_size.setChecked(True)
        self.radioButton_size.setObjectName("radioButton_size")
        self.horizontalLayout_16.addWidget(self.radioButton_size)
        self.spinBox_size = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_size.setMaximum(999999999)
        self.spinBox_size.setProperty("value", 100)
        self.spinBox_size.setObjectName("spinBox_size")
        self.horizontalLayout_16.addWidget(self.spinBox_size)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.radioButton_ratio = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_ratio.setObjectName("radioButton_ratio")
        self.horizontalLayout_17.addWidget(self.radioButton_ratio)
        self.doubleSpinBox_ratio = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_ratio.setMinimumSize(QtCore.QSize(104, 0))
        self.doubleSpinBox_ratio.setMaximum(100.0)
        self.doubleSpinBox_ratio.setObjectName("doubleSpinBox_ratio")
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_ratio)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_17.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_11)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.comboBox_axis = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_axis.setObjectName("comboBox_axis")
        self.comboBox_axis.addItem("")
        self.comboBox_axis.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_axis)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_code = QtWidgets.QPushButton(self.widget)
        self.pushButton_code.setObjectName("pushButton_code")
        self.horizontalLayout.addWidget(self.pushButton_code)
        self.pushButton_help = QtWidgets.QPushButton(self.widget)
        self.pushButton_help.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_helpindex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon5)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout.addWidget(self.pushButton_help)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_save = QtWidgets.QPushButton(self.widget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "随机抽样"))
        self.label_3.setText(_translate("Form", "全部变量:"))
        self.label_2.setText(_translate("Form", "已选变量:"))
        self.label_4.setText(_translate("Form", "权重变量:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "变量"))
        self.label_12.setText(_translate("Form", "数据集："))
        self.label_7.setText(_translate("Form", "抽样方法:"))
        self.comboBox_replace.setItemText(0, _translate("Form", "无放回抽样"))
        self.comboBox_replace.setItemText(1, _translate("Form", "有放回抽样"))
        self.label_14.setText(_translate("Form", "随机种子:"))
        self.label_15.setText(_translate("Form", "样本方法:"))
        self.radioButton_size.setText(_translate("Form", "样本大小"))
        self.label_5.setText(_translate("Form", "行"))
        self.radioButton_ratio.setText(_translate("Form", "样本比例"))
        self.label.setText(_translate("Form", "%"))
        self.label_16.setText(_translate("Form", "抽取行/列:"))
        self.comboBox_axis.setItemText(0, _translate("Form", "行"))
        self.comboBox_axis.setItemText(1, _translate("Form", "列"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "抽样"))
        self.pushButton_code.setText(_translate("Form", "代码"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc