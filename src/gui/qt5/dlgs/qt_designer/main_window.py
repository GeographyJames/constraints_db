# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jcampbell\OneDrive - EDF Renouvelables\Documents\python_projects\constraints_db\src\gui\qt5\dlgs\qt_designer\qt_files//main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConstraintsTW = QtWidgets.QTableWidget(self.centralwidget)
        self.ConstraintsTW.setObjectName("ConstraintsTW")
        self.ConstraintsTW.setColumnCount(0)
        self.ConstraintsTW.setRowCount(0)
        self.verticalLayout.addWidget(self.ConstraintsTW)
        self.RefreshPB = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshPB.setObjectName("RefreshPB")
        self.verticalLayout.addWidget(self.RefreshPB)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuConstraints = QtWidgets.QMenu(self.menubar)
        self.menuConstraints.setObjectName("menuConstraints")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New = QtWidgets.QAction(mainWindow)
        self.actionAdd_New.setObjectName("actionAdd_New")
        self.menuConstraints.addAction(self.actionAdd_New)
        self.menubar.addAction(self.menuConstraints.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Constraints Database"))
        self.RefreshPB.setText(_translate("mainWindow", "Refresh"))
        self.menuConstraints.setTitle(_translate("mainWindow", "Constraints"))
        self.actionAdd_New.setText(_translate("mainWindow", "Add New"))
