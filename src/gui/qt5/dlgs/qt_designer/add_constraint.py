# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jcampbell\OneDrive - EDF Renouvelables\Documents\python_projects\constraints_db\src\gui\qt5\dlgs\qt_designer\qt_files//add_constraint.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddConstraintDlg(object):
    def setupUi(self, AddConstraintDlg):
        AddConstraintDlg.setObjectName("AddConstraintDlg")
        AddConstraintDlg.resize(640, 480)
        self.formLayout = QtWidgets.QFormLayout(AddConstraintDlg)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(AddConstraintDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.LayerNameLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.LayerNameLE.setObjectName("LayerNameLE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LayerNameLE)
        self.label_2 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.DevelopmentConstraintCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.DevelopmentConstraintCB.setObjectName("DevelopmentConstraintCB")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DevelopmentConstraintCB)
        self.label_3 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.AdministrativeAreaCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.AdministrativeAreaCB.setObjectName("AdministrativeAreaCB")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AdministrativeAreaCB)
        self.label_4 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.DataPublisherCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.DataPublisherCB.setObjectName("DataPublisherCB")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DataPublisherCB)
        self.line = QtWidgets.QFrame(AddConstraintDlg)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_5 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.LicenseCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.LicenseCB.setObjectName("LicenseCB")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.LicenseCB)
        self.label_6 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.SourceLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.SourceLE.setObjectName("SourceLE")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.SourceLE)
        self.label_7 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.UpdateCycleLE = QtWidgets.QLineEdit(AddConstraintDlg)
        self.UpdateCycleLE.setObjectName("UpdateCycleLE")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.UpdateCycleLE)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddConstraintDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.label_8 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.AccessedCreatedDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.AccessedCreatedDE.setObjectName("AccessedCreatedDE")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.AccessedCreatedDE)
        self.label_9 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.LastUpdatedDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.LastUpdatedDE.setObjectName("LastUpdatedDE")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.LastUpdatedDE)
        self.label_10 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.NextUpdateDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.NextUpdateDE.setObjectName("NextUpdateDE")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.NextUpdateDE)
        self.label_11 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ExpiresDE = QtWidgets.QDateEdit(AddConstraintDlg)
        self.ExpiresDE.setObjectName("ExpiresDE")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ExpiresDE)
        self.NotesTE = QtWidgets.QTextEdit(AddConstraintDlg)
        self.NotesTE.setObjectName("NotesTE")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.NotesTE)
        self.label_12 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.retranslateUi(AddConstraintDlg)
        self.buttonBox.accepted.connect(AddConstraintDlg.accept) # type: ignore
        self.buttonBox.rejected.connect(AddConstraintDlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddConstraintDlg)

    def retranslateUi(self, AddConstraintDlg):
        _translate = QtCore.QCoreApplication.translate
        AddConstraintDlg.setWindowTitle(_translate("AddConstraintDlg", "Add Constraint"))
        self.label.setText(_translate("AddConstraintDlg", "Layer name"))
        self.label_2.setText(_translate("AddConstraintDlg", "Development Constraint"))
        self.label_3.setText(_translate("AddConstraintDlg", "Administrative Area"))
        self.label_4.setText(_translate("AddConstraintDlg", "Data Publisher"))
        self.label_5.setText(_translate("AddConstraintDlg", "License"))
        self.LicenseCB.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_6.setText(_translate("AddConstraintDlg", "Source"))
        self.SourceLE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_7.setText(_translate("AddConstraintDlg", "Update Cycle"))
        self.UpdateCycleLE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_8.setText(_translate("AddConstraintDlg", "Date data accessed or created"))
        self.label_9.setText(_translate("AddConstraintDlg", "Date data last updated"))
        self.label_10.setText(_translate("AddConstraintDlg", "Date data next updated"))
        self.label_11.setText(_translate("AddConstraintDlg", "Data data expires"))
        self.NotesTE.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_12.setText(_translate("AddConstraintDlg", "Notes"))
