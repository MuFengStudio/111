# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 523)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_front = QtWidgets.QLabel(self.centralwidget)
        self.image_front.setGeometry(QtCore.QRect(490, 10, 360, 200))
        self.image_front.setMinimumSize(QtCore.QSize(360, 200))
        self.image_front.setMouseTracking(False)
        self.image_front.setFrameShape(QtWidgets.QFrame.Box)
        self.image_front.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_front.setText("")
        self.image_front.setObjectName("image_front")
        self.sequence_list = QtWidgets.QListView(self.centralwidget)
        self.sequence_list.setGeometry(QtCore.QRect(10, 10, 200, 241))
        self.sequence_list.setMinimumSize(QtCore.QSize(200, 200))
        self.sequence_list.setMaximumSize(QtCore.QSize(16777215, 300))
        self.sequence_list.setObjectName("sequence_list")
        self.e_country = QtWidgets.QLineEdit(self.centralwidget)
        self.e_country.setGeometry(QtCore.QRect(220, 30, 110, 32))
        self.e_country.setObjectName("e_country")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 66, 20))
        self.label.setObjectName("label")
        self.cb_roadtype = QtWidgets.QComboBox(self.centralwidget)
        self.cb_roadtype.setGeometry(QtCore.QRect(220, 90, 110, 28))
        self.cb_roadtype.setObjectName("cb_roadtype")
        self.cb_roadtype.addItem("")
        self.cb_roadtype.addItem("")
        self.cb_roadtype.addItem("")
        self.cb_roadtype.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 71, 20))
        self.label_2.setObjectName("label_2")
        self.steering_wheel = QtWidgets.QLabel(self.centralwidget)
        self.steering_wheel.setGeometry(QtCore.QRect(380, 110, 100, 100))
        self.steering_wheel.setMinimumSize(QtCore.QSize(100, 100))
        self.steering_wheel.setMouseTracking(False)
        self.steering_wheel.setFrameShape(QtWidgets.QFrame.Box)
        self.steering_wheel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.steering_wheel.setText("")
        self.steering_wheel.setObjectName("steering_wheel")
        self.b_sequenceApply = QtWidgets.QPushButton(self.centralwidget)
        self.b_sequenceApply.setGeometry(QtCore.QRect(220, 130, 110, 30))
        self.b_sequenceApply.setObjectName("b_sequenceApply")
        self.b_sequenceDelete = QtWidgets.QPushButton(self.centralwidget)
        self.b_sequenceDelete.setGeometry(QtCore.QRect(110, 260, 95, 30))
        self.b_sequenceDelete.setObjectName("b_sequenceDelete")
        self.b_sequenceDetails = QtWidgets.QPushButton(self.centralwidget)
        self.b_sequenceDetails.setGeometry(QtCore.QRect(10, 260, 95, 30))
        self.b_sequenceDetails.setObjectName("b_sequenceDetails")
        self.gb_modes = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_modes.setGeometry(QtCore.QRect(10, 300, 111, 171))
        self.gb_modes.setFlat(False)
        self.gb_modes.setCheckable(False)
        self.gb_modes.setObjectName("gb_modes")
        self.mode_recording = QtWidgets.QRadioButton(self.gb_modes)
        self.mode_recording.setGeometry(QtCore.QRect(10, 30, 111, 25))
        self.mode_recording.setChecked(True)
        self.mode_recording.setObjectName("mode_recording")
        self.mode_autopilot = QtWidgets.QRadioButton(self.gb_modes)
        self.mode_autopilot.setGeometry(QtCore.QRect(10, 90, 111, 25))
        self.mode_autopilot.setObjectName("mode_autopilot")
        self.mode_training = QtWidgets.QRadioButton(self.gb_modes)
        self.mode_training.setGeometry(QtCore.QRect(10, 60, 111, 25))
        self.mode_training.setObjectName("mode_training")
        self.b_mode = QtWidgets.QPushButton(self.gb_modes)
        self.b_mode.setGeometry(QtCore.QRect(10, 130, 95, 30))
        self.b_mode.setObjectName("b_mode")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(0, 20))
        self.statusbar.setBaseSize(QtCore.QSize(0, 20))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setCheckable(False)
        self.actionSettings.setChecked(False)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdater = QtWidgets.QAction(MainWindow)
        self.actionUpdater.setObjectName("actionUpdater")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionUpdater)
        self.menuInfo.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ETS2 Autopilot"))
        self.label.setText(_translate("MainWindow", "Country:"))
        self.cb_roadtype.setItemText(0, _translate("MainWindow", "Not set"))
        self.cb_roadtype.setItemText(1, _translate("MainWindow", "Freeway"))
        self.cb_roadtype.setItemText(2, _translate("MainWindow", "Highway"))
        self.cb_roadtype.setItemText(3, _translate("MainWindow", "City"))
        self.label_2.setText(_translate("MainWindow", "Road type:"))
        self.b_sequenceApply.setText(_translate("MainWindow", "Apply"))
        self.b_sequenceDelete.setText(_translate("MainWindow", "Delete"))
        self.b_sequenceDetails.setText(_translate("MainWindow", "Details"))
        self.gb_modes.setTitle(_translate("MainWindow", "Mode"))
        self.mode_recording.setText(_translate("MainWindow", "Recording"))
        self.mode_autopilot.setText(_translate("MainWindow", "Autopilot"))
        self.mode_training.setText(_translate("MainWindow", "Training"))
        self.b_mode.setText(_translate("MainWindow", "Start"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdater.setText(_translate("MainWindow", "Updater"))

