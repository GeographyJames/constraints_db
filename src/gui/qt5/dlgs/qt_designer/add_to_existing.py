# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jcampbell\OneDrive - EDF Renouvelables\Documents\python_projects\constraints_db\src\gui\qt5\dlgs\qt_designer\qt_files//add_to_existing.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


from qgis.gui import QgsFileWidget
class Ui_AddConstraintDlg(object):
    def setupUi(self, AddConstraintDlg):
        AddConstraintDlg.setObjectName("AddConstraintDlg")
        AddConstraintDlg.resize(640, 600)
        self.gridLayout = QtWidgets.QGridLayout(AddConstraintDlg)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.DevelopmentConstraintCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.DevelopmentConstraintCB.setObjectName("DevelopmentConstraintCB")
        self.gridLayout.addWidget(self.DevelopmentConstraintCB, 3, 1, 1, 2)
        self.SelectShapefileQgsFileWidget = QgsFileWidget(AddConstraintDlg)
        self.SelectShapefileQgsFileWidget.setObjectName("SelectShapefileQgsFileWidget")
        self.gridLayout.addWidget(self.SelectShapefileQgsFileWidget, 0, 1, 1, 2)
        self.FeatureStatusCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.FeatureStatusCB.setObjectName("FeatureStatusCB")
        self.gridLayout.addWidget(self.FeatureStatusCB, 5, 1, 1, 2)
        self.ShapefileInfoTE = QtWidgets.QTextEdit(AddConstraintDlg)
        self.ShapefileInfoTE.setReadOnly(True)
        self.ShapefileInfoTE.setObjectName("ShapefileInfoTE")
        self.gridLayout.addWidget(self.ShapefileInfoTE, 1, 1, 1, 2)
        self.FeatureNameCB = QtWidgets.QComboBox(AddConstraintDlg)
        self.FeatureNameCB.setObjectName("FeatureNameCB")
        self.gridLayout.addWidget(self.FeatureNameCB, 4, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(AddConstraintDlg)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddConstraintDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 3)

        self.retranslateUi(AddConstraintDlg)
        self.buttonBox.accepted.connect(AddConstraintDlg.accept) # type: ignore
        self.buttonBox.rejected.connect(AddConstraintDlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddConstraintDlg)

    def retranslateUi(self, AddConstraintDlg):
        _translate = QtCore.QCoreApplication.translate
        AddConstraintDlg.setWindowTitle(_translate("AddConstraintDlg", "Add Constraint"))
        self.FeatureStatusCB.setPlaceholderText(_translate("AddConstraintDlg", "Optional"))
        self.label_14.setText(_translate("AddConstraintDlg", "Select Shapefile"))
        self.label_15.setText(_translate("AddConstraintDlg", "Select column to use as feature name"))
        self.label_2.setText(_translate("AddConstraintDlg", "Layer"))
        self.label_16.setText(_translate("AddConstraintDlg", "Select column to use as feature status"))