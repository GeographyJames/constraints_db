# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Owner\Documents\constraints_db\src\gui\qt5\dlgs\qt_designer\qt_files//add_constraint.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddConstraintDlg(object):
    def setupUi(self, AddConstraintDlg):
        AddConstraintDlg.setObjectName("AddConstraintDlg")
        AddConstraintDlg.resize(640, 600)
        self.gridLayout = QtWidgets.QGridLayout(AddConstraintDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.LastUpdatedDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.LastUpdatedDE.setObjectName("LastUpdatedDE")
        self.gridLayout.addWidget(self.LastUpdatedDE, 11, 1, 1, 1)
        self.DataPublisherCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.DataPublisherCB.setObjectName("DataPublisherCB")
        self.gridLayout.addWidget(self.DataPublisherCB, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.NotesTE = QtWidgets.QTextEdit(AddConstraintDlg)
        self.NotesTE.setObjectName("NotesTE")
        self.gridLayout.addWidget(self.NotesTE, 14, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddConstraintDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 16, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.ExpiresDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.ExpiresDE.setObjectName("ExpiresDE")
        self.gridLayout.addWidget(self.ExpiresDE, 13, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.SourceLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.SourceLE.setObjectName("SourceLE")
        self.gridLayout.addWidget(self.SourceLE, 9, 1, 1, 2)
        self.DevelopmentConstraintCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.DevelopmentConstraintCB.setObjectName("DevelopmentConstraintCB")
        self.gridLayout.addWidget(self.DevelopmentConstraintCB, 2, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 14, 0, 1, 1)
        self.UpdateCycleLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.UpdateCycleLE.setObjectName("UpdateCycleLE")
        self.gridLayout.addWidget(self.UpdateCycleLE, 10, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)
        self.LastUpdatedCB = QtWidgets.QCheckBox(AddConstraintDlg)
        self.LastUpdatedCB.setObjectName("LastUpdatedCB")
        self.gridLayout.addWidget(self.LastUpdatedCB, 11, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.LayerNameLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.LayerNameLE.setReadOnly(True)
        self.LayerNameLE.setObjectName("LayerNameLE")
        self.gridLayout.addWidget(self.LayerNameLE, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(AddConstraintDlg)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.NextUpdateCB = QtWidgets.QCheckBox(AddConstraintDlg)
        self.NextUpdateCB.setObjectName("NextUpdateCB")
        self.gridLayout.addWidget(self.NextUpdateCB, 12, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.LicenseCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.LicenseCB.setObjectName("LicenseCB")
        self.gridLayout.addWidget(self.LicenseCB, 8, 1, 1, 2)
        self.NextUpdateDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.NextUpdateDE.setObjectName("NextUpdateDE")
        self.gridLayout.addWidget(self.NextUpdateDE, 12, 1, 1, 1)
        self.AdministrativeAreaCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.AdministrativeAreaCB.setObjectName("AdministrativeAreaCB")
        self.gridLayout.addWidget(self.AdministrativeAreaCB, 3, 1, 1, 2)
        self.ExpiresCB = QtWidgets.QCheckBox(AddConstraintDlg)
        self.ExpiresCB.setObjectName("ExpiresCB")
        self.gridLayout.addWidget(self.ExpiresCB, 13, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(AddConstraintDlg)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 3)
        self.GeomTypeCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.GeomTypeCB.setObjectName("GeomTypeCB")
        self.gridLayout.addWidget(self.GeomTypeCB, 5, 1, 1, 2)
        self.AccessedCreatedDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.AccessedCreatedDE.setObjectName("AccessedCreatedDE")
        self.gridLayout.addWidget(self.AccessedCreatedDE, 6, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.retranslateUi(AddConstraintDlg)
        self.buttonBox.accepted.connect(AddConstraintDlg.accept) # type: ignore
        self.buttonBox.rejected.connect(AddConstraintDlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddConstraintDlg)

    def retranslateUi(self, AddConstraintDlg):
        _translate = QtCore.QCoreApplication.translate
        AddConstraintDlg.setWindowTitle(_translate("AddConstraintDlg", "Add Constraint"))
        self.label_6.setText(_translate("AddConstraintDlg", "Source"))
        self.NotesTE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_9.setText(_translate("AddConstraintDlg", "Date data last updated"))
        self.label_8.setText(_translate("AddConstraintDlg", "Date data accessed or created"))
        self.label_4.setText(_translate("AddConstraintDlg", "Data Publisher"))
        self.SourceLE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_12.setText(_translate("AddConstraintDlg", "Notes"))
        self.UpdateCycleLE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_7.setText(_translate("AddConstraintDlg", "Update Cycle"))
        self.label_11.setText(_translate("AddConstraintDlg", "Data data expires"))
        self.LastUpdatedCB.setText(_translate("AddConstraintDlg", "Include"))
        self.label_2.setText(_translate("AddConstraintDlg", "Development Constraint"))
        self.label_3.setText(_translate("AddConstraintDlg", "Administrative Area"))
        self.LayerNameLE.setPlaceholderText(_translate("AddConstraintDlg", "Autogenerated from selections"))
        self.label.setText(_translate("AddConstraintDlg", "Layer name"))
        self.NextUpdateCB.setText(_translate("AddConstraintDlg", "Include"))
        self.label_10.setText(_translate("AddConstraintDlg", "Date data next updated"))
        self.LicenseCB.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.ExpiresCB.setText(_translate("AddConstraintDlg", "Include"))
        self.label_5.setText(_translate("AddConstraintDlg", "License"))
        self.label_13.setText(_translate("AddConstraintDlg", "Geometry Type"))
