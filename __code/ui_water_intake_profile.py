# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_water_intake_profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 910)
        MainWindow.setMinimumSize(QtCore.QSize(0, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMidLineWidth(5)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(22)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.add_radioButton.setChecked(True)
        self.add_radioButton.setObjectName("add_radioButton")
        self.verticalLayout_2.addWidget(self.add_radioButton)
        self.mean_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.mean_radioButton.setObjectName("mean_radioButton")
        self.verticalLayout_2.addWidget(self.mean_radioButton)
        self.median_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.median_radioButton.setObjectName("median_radioButton")
        self.verticalLayout_2.addWidget(self.median_radioButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.x_axis_integration_radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.x_axis_integration_radioButton.setChecked(True)
        self.x_axis_integration_radioButton.setObjectName("x_axis_integration_radioButton")
        self.verticalLayout_5.addWidget(self.x_axis_integration_radioButton)
        self.y_axis_integration_radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.y_axis_integration_radioButton.setObjectName("y_axis_integration_radioButton")
        self.verticalLayout_5.addWidget(self.y_axis_integration_radioButton)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sliding_average_checkBox = QtWidgets.QRadioButton(self.groupBox_5)
        self.sliding_average_checkBox.setChecked(True)
        self.sliding_average_checkBox.setObjectName("sliding_average_checkBox")
        self.verticalLayout_6.addWidget(self.sliding_average_checkBox)
        self.error_function_checkBox = QtWidgets.QRadioButton(self.groupBox_5)
        self.error_function_checkBox.setObjectName("error_function_checkBox")
        self.verticalLayout_6.addWidget(self.error_function_checkBox)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.ignore_first_image_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.ignore_first_image_checkbox.setChecked(True)
        self.ignore_first_image_checkbox.setObjectName("ignore_first_image_checkbox")
        self.verticalLayout_3.addWidget(self.ignore_first_image_checkbox)
        self.export_table_button = QtWidgets.QPushButton(self.layoutWidget)
        self.export_table_button.setObjectName("export_table_button")
        self.verticalLayout_3.addWidget(self.export_table_button)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sort_files_by_time_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.sort_files_by_time_radioButton.setChecked(True)
        self.sort_files_by_time_radioButton.setObjectName("sort_files_by_time_radioButton")
        self.horizontalLayout_7.addWidget(self.sort_files_by_time_radioButton)
        self.sort_files_by_name_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.sort_files_by_name_radioButton.setObjectName("sort_files_by_name_radioButton")
        self.horizontalLayout_7.addWidget(self.sort_files_by_name_radioButton)
        self.time_between_runs_label = QtWidgets.QLabel(self.groupBox_3)
        self.time_between_runs_label.setEnabled(False)
        self.time_between_runs_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.time_between_runs_label.setObjectName("time_between_runs_label")
        self.horizontalLayout_7.addWidget(self.time_between_runs_label)
        self.time_between_runs_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.time_between_runs_spinBox.setEnabled(False)
        self.time_between_runs_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.time_between_runs_spinBox.setDecimals(2)
        self.time_between_runs_spinBox.setMinimum(0.1)
        self.time_between_runs_spinBox.setMaximum(500.0)
        self.time_between_runs_spinBox.setSingleStep(0.1)
        self.time_between_runs_spinBox.setProperty("value", 30.0)
        self.time_between_runs_spinBox.setObjectName("time_between_runs_spinBox")
        self.horizontalLayout_7.addWidget(self.time_between_runs_spinBox)
        self.time_between_runs_units_label = QtWidgets.QLabel(self.groupBox_3)
        self.time_between_runs_units_label.setEnabled(False)
        self.time_between_runs_units_label.setMinimumSize(QtCore.QSize(20, 0))
        self.time_between_runs_units_label.setMaximumSize(QtCore.QSize(20, 16777215))
        self.time_between_runs_units_label.setObjectName("time_between_runs_units_label")
        self.horizontalLayout_7.addWidget(self.time_between_runs_units_label)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pixel_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.pixel_radioButton.setChecked(True)
        self.pixel_radioButton.setObjectName("pixel_radioButton")
        self.horizontalLayout_5.addWidget(self.pixel_radioButton)
        self.distance_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.distance_radioButton.setObjectName("distance_radioButton")
        self.horizontalLayout_5.addWidget(self.distance_radioButton)
        self.water_intake_distance_label = QtWidgets.QLabel(self.groupBox)
        self.water_intake_distance_label.setEnabled(False)
        self.water_intake_distance_label.setObjectName("water_intake_distance_label")
        self.horizontalLayout_5.addWidget(self.water_intake_distance_label)
        self.pixel_size_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.pixel_size_spinBox.setEnabled(False)
        self.pixel_size_spinBox.setDecimals(3)
        self.pixel_size_spinBox.setMinimum(0.001)
        self.pixel_size_spinBox.setMaximum(10.0)
        self.pixel_size_spinBox.setSingleStep(0.001)
        self.pixel_size_spinBox.setProperty("value", 0.05)
        self.pixel_size_spinBox.setObjectName("pixel_size_spinBox")
        self.horizontalLayout_5.addWidget(self.pixel_size_spinBox)
        self.pixel_size_units = QtWidgets.QLabel(self.groupBox)
        self.pixel_size_units.setEnabled(False)
        self.pixel_size_units.setObjectName("pixel_size_units")
        self.horizontalLayout_5.addWidget(self.pixel_size_units)
        self.horizontalLayout_6.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 30))
        self.cancel_button.setMaximumSize(QtCore.QSize(100, 30))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem2 = QtWidgets.QSpacerItem(408, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setMinimumSize(QtCore.QSize(100, 30))
        self.help_button.setMaximumSize(QtCore.QSize(100, 30))
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setMinimumSize(QtCore.QSize(100, 30))
        self.ok_button.setMaximumSize(QtCore.QSize(100, 30))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile_2 = QtWidgets.QMenu(self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")
        self.menuImport_2 = QtWidgets.QMenu(self.menuFile_2)
        self.menuImport_2.setObjectName("menuImport_2")
        self.menuExport = QtWidgets.QMenu(self.menuFile_2)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.actionWater_Intake = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake.setObjectName("actionWater_Intake")
        self.actionImportedFilesMetadata = QtWidgets.QAction(MainWindow)
        self.actionImportedFilesMetadata.setObjectName("actionImportedFilesMetadata")
        self.actionBy_Time_Stamp = QtWidgets.QAction(MainWindow)
        self.actionBy_Time_Stamp.setObjectName("actionBy_Time_Stamp")
        self.actionBy_File_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_File_Name.setObjectName("actionBy_File_Name")
        self.actionDsc_files = QtWidgets.QAction(MainWindow)
        self.actionDsc_files.setObjectName("actionDsc_files")
        self.actionDsc = QtWidgets.QAction(MainWindow)
        self.actionDsc.setObjectName("actionDsc")
        self.actionWater_Intake_2 = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake_2.setObjectName("actionWater_Intake_2")
        self.actionProfiles = QtWidgets.QAction(MainWindow)
        self.actionProfiles.setObjectName("actionProfiles")
        self.menuImport_2.addAction(self.actionDsc)
        self.menuExport.addAction(self.actionProfiles)
        self.menuExport.addAction(self.actionWater_Intake_2)
        self.menuFile_2.addAction(self.menuImport_2.menuAction())
        self.menuFile_2.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFile_2.menuAction())

        self.retranslateUi(MainWindow)
        self.ok_button.clicked.connect(MainWindow.ok_button_clicked)
        self.cancel_button.clicked.connect(MainWindow.cancel_button_clicked)
        self.help_button.clicked.connect(MainWindow.help_button_clicked)
        self.actionExport_Profile.triggered.connect(MainWindow.export_profile_clicked)
        self.actionWater_Intake.triggered.connect(MainWindow.export_water_intake_clicked)
        self.add_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.mean_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.median_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.sort_files_by_time_radioButton.clicked.connect(MainWindow.sorting_files_checkbox_clicked)
        self.sort_files_by_name_radioButton.clicked.connect(MainWindow.sorting_files_checkbox_clicked)
        self.time_between_runs_spinBox.editingFinished.connect(MainWindow.time_between_runs_spinBox_changed)
        self.pixel_radioButton.clicked.connect(MainWindow._water_intake_yaxis_checkbox_changed)
        self.distance_radioButton.clicked.connect(MainWindow._water_intake_yaxis_checkbox_changed)
        self.pixel_size_spinBox.editingFinished.connect(MainWindow._pixel_size_spinBox_changed)
        self.actionDsc_files.triggered.connect(MainWindow.import_dsc_clicked)
        self.export_table_button.pressed.connect(MainWindow.export_table_button_clicked)
        self.actionProfiles.triggered.connect(MainWindow.export_profile_clicked)
        self.actionWater_Intake_2.triggered.connect(MainWindow.export_water_intake_clicked)
        self.actionDsc.triggered.connect(MainWindow.import_dsc_clicked)
        self.x_axis_integration_radioButton.clicked.connect(MainWindow.integration_direction_changed)
        self.y_axis_integration_radioButton.clicked.connect(MainWindow.integration_direction_changed)
        self.ignore_first_image_checkbox.clicked.connect(MainWindow.ignore_first_image_checkbox_clicked)
        self.sliding_average_checkBox.clicked.connect(MainWindow.algorithm_changed)
        self.error_function_checkBox.clicked.connect(MainWindow.algorithm_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time Stamp (unix format)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time Stamp (user format)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Profile Algorithms"))
        self.add_radioButton.setText(_translate("MainWindow", "Add"))
        self.mean_radioButton.setText(_translate("MainWindow", "Mean"))
        self.median_radioButton.setText(_translate("MainWindow", "Median"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Integration Direction"))
        self.x_axis_integration_radioButton.setText(_translate("MainWindow", "along x-axis"))
        self.y_axis_integration_radioButton.setText(_translate("MainWindow", "along y-axis"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Algorithm"))
        self.sliding_average_checkBox.setText(_translate("MainWindow", "Sliding Average"))
        self.error_function_checkBox.setText(_translate("MainWindow", "Error Function"))
        self.ignore_first_image_checkbox.setText(_translate("MainWindow", "Ignore first image"))
        self.export_table_button.setText(_translate("MainWindow", "Export Table ..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sorting Files"))
        self.sort_files_by_time_radioButton.setText(_translate("MainWindow", "by Time Stamp"))
        self.sort_files_by_name_radioButton.setText(_translate("MainWindow", "by Name"))
        self.time_between_runs_label.setText(_translate("MainWindow", "-> Time Between Runs"))
        self.time_between_runs_units_label.setText(_translate("MainWindow", "s"))
        self.groupBox.setTitle(_translate("MainWindow", "Water Intake Y Axis"))
        self.pixel_radioButton.setText(_translate("MainWindow", "Pixel"))
        self.distance_radioButton.setText(_translate("MainWindow", "Distance"))
        self.water_intake_distance_label.setText(_translate("MainWindow", "-> 1 pixel = "))
        self.pixel_size_units.setText(_translate("MainWindow", "mm"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.help_button.setText(_translate("MainWindow", "HELP"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.menuFile_2.setTitle(_translate("MainWindow", "File"))
        self.menuImport_2.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))

