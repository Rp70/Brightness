# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Sep 17 11:56:47 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 333)
        MainWindow.setMinimumSize(QtCore.QSize(701, 333))
        MainWindow.setMaximumSize(QtCore.QSize(701, 333))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 511, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 231, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.primary_brightness = QtGui.QSlider(self.horizontalLayoutWidget_2)
        self.primary_brightness.setProperty("value", 99)
        self.primary_brightness.setOrientation(QtCore.Qt.Vertical)
        self.primary_brightness.setObjectName("primary_brightness")
        self.horizontalLayout_2.addWidget(self.primary_brightness)
        self.primary_red = QtGui.QSlider(self.horizontalLayoutWidget_2)
        self.primary_red.setProperty("value", 99)
        self.primary_red.setOrientation(QtCore.Qt.Vertical)
        self.primary_red.setObjectName("primary_red")
        self.horizontalLayout_2.addWidget(self.primary_red)
        self.primary_green = QtGui.QSlider(self.horizontalLayoutWidget_2)
        self.primary_green.setProperty("value", 99)
        self.primary_green.setOrientation(QtCore.Qt.Vertical)
        self.primary_green.setObjectName("primary_green")
        self.horizontalLayout_2.addWidget(self.primary_green)
        self.primary_blue = QtGui.QSlider(self.horizontalLayoutWidget_2)
        self.primary_blue.setProperty("value", 99)
        self.primary_blue.setOrientation(QtCore.Qt.Vertical)
        self.primary_blue.setObjectName("primary_blue")
        self.horizontalLayout_2.addWidget(self.primary_blue)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 40, 231, 211))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.secondary_brightness = QtGui.QSlider(self.horizontalLayoutWidget_3)
        self.secondary_brightness.setProperty("value", 99)
        self.secondary_brightness.setOrientation(QtCore.Qt.Vertical)
        self.secondary_brightness.setObjectName("secondary_brightness")
        self.horizontalLayout_3.addWidget(self.secondary_brightness)
        self.secondary_red = QtGui.QSlider(self.horizontalLayoutWidget_3)
        self.secondary_red.setProperty("value", 99)
        self.secondary_red.setOrientation(QtCore.Qt.Vertical)
        self.secondary_red.setObjectName("secondary_red")
        self.horizontalLayout_3.addWidget(self.secondary_red)
        self.secondary_green = QtGui.QSlider(self.horizontalLayoutWidget_3)
        self.secondary_green.setProperty("value", 99)
        self.secondary_green.setOrientation(QtCore.Qt.Vertical)
        self.secondary_green.setObjectName("secondary_green")
        self.horizontalLayout_3.addWidget(self.secondary_green)
        self.secondary_blue = QtGui.QSlider(self.horizontalLayoutWidget_3)
        self.secondary_blue.setProperty("value", 99)
        self.secondary_blue.setOrientation(QtCore.Qt.Vertical)
        self.secondary_blue.setObjectName("secondary_blue")
        self.horizontalLayout_3.addWidget(self.secondary_blue)
        self.horizontalLayout.addWidget(self.groupBox)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(100, 260, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(150, 260, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(200, 260, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(290, 260, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(370, 260, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(420, 260, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(470, 260, 16, 16))
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(529, 0, 173, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 701, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionCheck_for_update = QtGui.QAction(MainWindow)
        self.actionCheck_for_update.setObjectName("actionCheck_for_update")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionCheck_for_update)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Brightness Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Primary", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Secondary", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", " R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", " G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", " B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", " R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", " G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", " B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Reverse Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Color Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "1900K Candle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "2600K 40W Tungsten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "2850K 100W Tungsten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "3200K Halogen", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "5200K Carbon Arc", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "5400K High Noon", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "6000K Direct Sun", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "7000K Overcast Sky", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "20000K Clear Blue Sky", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("MainWindow", "&License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "&Load settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_update.setText(QtGui.QApplication.translate("MainWindow", "&Check for Update", None, QtGui.QApplication.UnicodeUTF8))

