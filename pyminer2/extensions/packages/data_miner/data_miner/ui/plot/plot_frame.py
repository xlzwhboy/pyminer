# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_dataset_name = QtWidgets.QLineEdit(self.page)
        self.lineEdit_dataset_name.setObjectName("lineEdit_dataset_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_dataset_name)
        self.toolButton_dataset_name = QtWidgets.QToolButton(self.page)
        self.toolButton_dataset_name.setObjectName("toolButton_dataset_name")
        self.horizontalLayout_4.addWidget(self.toolButton_dataset_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.widget_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "选择可视化类型")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.page)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.splitter_2)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.splitter_2)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitter_2)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.splitter_3 = QtWidgets.QSplitter(self.page_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.widget_4 = QtWidgets.QWidget(self.splitter_3)
        self.widget_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_var.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_5.addWidget(self.listWidget_var)
        self.widget_5 = QtWidgets.QWidget(self.splitter_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.pushButton_selected_del = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_selected_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_del.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_del.setIcon(icon)
        self.pushButton_selected_del.setObjectName("pushButton_selected_del")
        self.horizontalLayout_12.addWidget(self.pushButton_selected_del)
        self.pushButton_selected_down = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_selected_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_down.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pyqt/source/images/down1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_down.setIcon(icon1)
        self.pushButton_selected_down.setObjectName("pushButton_selected_down")
        self.horizontalLayout_12.addWidget(self.pushButton_selected_down)
        self.pushButton_selected_up = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_selected_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_up.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pyqt/source/images/up1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_up.setIcon(icon2)
        self.pushButton_selected_up.setObjectName("pushButton_selected_up")
        self.horizontalLayout_12.addWidget(self.pushButton_selected_up)
        self.pushButton_selected_add = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_selected_add.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pyqt/source/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add.setIcon(icon3)
        self.pushButton_selected_add.setObjectName("pushButton_selected_add")
        self.horizontalLayout_12.addWidget(self.pushButton_selected_add)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.listWidget_selected = QtWidgets.QListWidget(self.widget_5)
        self.listWidget_selected.setObjectName("listWidget_selected")
        self.horizontalLayout_13.addWidget(self.listWidget_selected)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addLayout(self.verticalLayout_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pushButton_group_del = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_group_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_del.setText("")
        self.pushButton_group_del.setIcon(icon)
        self.pushButton_group_del.setObjectName("pushButton_group_del")
        self.horizontalLayout_8.addWidget(self.pushButton_group_del)
        self.pushButton_group_down = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_group_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_down.setText("")
        self.pushButton_group_down.setIcon(icon1)
        self.pushButton_group_down.setObjectName("pushButton_group_down")
        self.horizontalLayout_8.addWidget(self.pushButton_group_down)
        self.pushButton_group_up = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_group_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_up.setText("")
        self.pushButton_group_up.setIcon(icon2)
        self.pushButton_group_up.setObjectName("pushButton_group_up")
        self.horizontalLayout_8.addWidget(self.pushButton_group_up)
        self.pushButton_group_add = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_group_add.setText("")
        self.pushButton_group_add.setIcon(icon3)
        self.pushButton_group_add.setObjectName("pushButton_group_add")
        self.horizontalLayout_8.addWidget(self.pushButton_group_add)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.listWidget_group = QtWidgets.QListWidget(self.widget_5)
        self.listWidget_group.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_group.setObjectName("listWidget_group")
        self.horizontalLayout_9.addWidget(self.listWidget_group)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.setStretch(1, 9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBox_type = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_type)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_title = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_title)
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_xlabel = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_xlabel.setObjectName("lineEdit_xlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_xlabel)
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_ylabel = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_ylabel.setObjectName("lineEdit_ylabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ylabel)
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget_6)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.verticalLayout_10.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.verticalLayout_9.addWidget(self.splitter_3)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_help_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_help_2.setObjectName("pushButton_help_2")
        self.horizontalLayout.addWidget(self.pushButton_help_2)
        self.pushButton_help = QtWidgets.QPushButton(self.widget)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout.addWidget(self.pushButton_help)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_last = QtWidgets.QPushButton(self.widget)
        self.pushButton_last.setObjectName("pushButton_last")
        self.horizontalLayout.addWidget(self.pushButton_last)
        self.pushButton_next = QtWidgets.QPushButton(self.widget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_preview = QtWidgets.QPushButton(self.widget)
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout.addWidget(self.pushButton_preview)
        self.pushButton_save = QtWidgets.QPushButton(self.widget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新建数据可视化"))
        self.label.setText(_translate("Form", "选择数据集："))
        self.toolButton_dataset_name.setText(_translate("Form", "..."))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("Form", "直方图"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("Form", "条形图"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("Form", "折线图"))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("Form", "散点图"))
        self.treeWidget_2.topLevelItem(4).setText(0, _translate("Form", "饼图"))
        self.treeWidget_2.topLevelItem(5).setText(0, _translate("Form", "箱线图"))
        self.treeWidget_2.topLevelItem(6).setText(0, _translate("Form", "热力图"))
        self.treeWidget_2.topLevelItem(7).setText(0, _translate("Form", "面积图"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("Form", "选择可视化技术"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "简单"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "按分组"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "包含拟合"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Form", "包含拟合和分组"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">直方图适合检查单个变量的数据分布。</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/pyqt/source/image/hist_simple.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">直接对单一变量进行直方图可视化。</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "变量列表:"))
        self.label_12.setText(_translate("Form", "已选变量"))
        self.pushButton_selected_del.setProperty("level", _translate("Form", "tool"))
        self.pushButton_selected_down.setProperty("level", _translate("Form", "tool"))
        self.pushButton_selected_up.setProperty("level", _translate("Form", "tool"))
        self.pushButton_selected_add.setProperty("level", _translate("Form", "tool"))
        self.label_4.setText(_translate("Form", "分组变量"))
        self.pushButton_group_del.setProperty("level", _translate("Form", "tool"))
        self.pushButton_group_down.setProperty("level", _translate("Form", "tool"))
        self.pushButton_group_up.setProperty("level", _translate("Form", "tool"))
        self.pushButton_group_add.setProperty("level", _translate("Form", "tool"))
        self.label_10.setText(_translate("Form", "类型:"))
        self.comboBox_type.setItemText(0, _translate("Form", "简单条形图"))
        self.comboBox_type.setItemText(1, _translate("Form", "分组条形图"))
        self.comboBox_type.setItemText(2, _translate("Form", "堆积条形图"))
        self.label_7.setText(_translate("Form", "标题:"))
        self.label_6.setText(_translate("Form", "X轴标题:"))
        self.label_9.setText(_translate("Form", "Y轴标题:"))
        self.label_8.setText(_translate("Form", "字体:"))
        self.fontComboBox.setCurrentText(_translate("Form", "黑体"))
        self.pushButton_help_2.setText(_translate("Form", "代码"))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_last.setText(_translate("Form", "后退"))
        self.pushButton_next.setText(_translate("Form", "前进"))
        self.pushButton_preview.setText(_translate("Form", "预览"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc
