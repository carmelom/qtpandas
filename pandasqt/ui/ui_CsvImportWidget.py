# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pandasqt/ui/ui_CsvImportWidget.ui'
#
# Created: Wed Jan 14 16:08:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CsvImportWidget(object):
    def setupUi(self, CsvImportWidget):
        CsvImportWidget.setObjectName(_fromUtf8("CsvImportWidget"))
        CsvImportWidget.resize(672, 687)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CsvImportWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelFileName = QtGui.QLabel(CsvImportWidget)
        self.labelFileName.setObjectName(_fromUtf8("labelFileName"))
        self.verticalLayout.addWidget(self.labelFileName)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditFileName = QtGui.QLineEdit(CsvImportWidget)
        self.lineEditFileName.setReadOnly(True)
        self.lineEditFileName.setObjectName(_fromUtf8("lineEditFileName"))
        self.horizontalLayout.addWidget(self.lineEditFileName)
        self.toolButtonOpen = QtGui.QToolButton(CsvImportWidget)
        self.toolButtonOpen.setText(_fromUtf8("update"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonOpen.setIcon(icon)
        self.toolButtonOpen.setIconSize(QtCore.QSize(20, 20))
        self.toolButtonOpen.setObjectName(_fromUtf8("toolButtonOpen"))
        self.horizontalLayout.addWidget(self.toolButtonOpen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(CsvImportWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBoxDelimiterComma = QtGui.QCheckBox(CsvImportWidget)
        self.checkBoxDelimiterComma.setObjectName(_fromUtf8("checkBoxDelimiterComma"))
        self.buttonGroup = QtGui.QButtonGroup(CsvImportWidget)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.checkBoxDelimiterComma)
        self.gridLayout.addWidget(self.checkBoxDelimiterComma, 0, 2, 1, 1)
        self.lineEditDelimiterCustom = QtGui.QLineEdit(CsvImportWidget)
        self.lineEditDelimiterCustom.setEnabled(False)
        self.lineEditDelimiterCustom.setMinimumSize(QtCore.QSize(46, 23))
        self.lineEditDelimiterCustom.setMaximumSize(QtCore.QSize(46, 23))
        self.lineEditDelimiterCustom.setReadOnly(True)
        self.lineEditDelimiterCustom.setObjectName(_fromUtf8("lineEditDelimiterCustom"))
        self.gridLayout.addWidget(self.lineEditDelimiterCustom, 0, 4, 1, 1)
        self.labelDelimiter = QtGui.QLabel(CsvImportWidget)
        self.labelDelimiter.setObjectName(_fromUtf8("labelDelimiter"))
        self.gridLayout.addWidget(self.labelDelimiter, 0, 0, 1, 1)
        self.checkBoxDelimiterSemicolon = QtGui.QCheckBox(CsvImportWidget)
        self.checkBoxDelimiterSemicolon.setChecked(True)
        self.checkBoxDelimiterSemicolon.setObjectName(_fromUtf8("checkBoxDelimiterSemicolon"))
        self.buttonGroup.addButton(self.checkBoxDelimiterSemicolon)
        self.gridLayout.addWidget(self.checkBoxDelimiterSemicolon, 0, 1, 1, 1)
        self.checkBoxDelimiterCustom = QtGui.QCheckBox(CsvImportWidget)
        self.checkBoxDelimiterCustom.setObjectName(_fromUtf8("checkBoxDelimiterCustom"))
        self.buttonGroup.addButton(self.checkBoxDelimiterCustom)
        self.gridLayout.addWidget(self.checkBoxDelimiterCustom, 0, 3, 1, 1)
        self.labelDelimiter_2 = QtGui.QLabel(CsvImportWidget)
        self.labelDelimiter_2.setObjectName(_fromUtf8("labelDelimiter_2"))
        self.gridLayout.addWidget(self.labelDelimiter_2, 1, 0, 1, 1)
        self.checkBoxSkipFaultyLines = QtGui.QCheckBox(CsvImportWidget)
        self.checkBoxSkipFaultyLines.setChecked(False)
        self.checkBoxSkipFaultyLines.setObjectName(_fromUtf8("checkBoxSkipFaultyLines"))
        self.gridLayout.addWidget(self.checkBoxSkipFaultyLines, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtGui.QFrame(CsvImportWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.labelPreview = QtGui.QLabel(CsvImportWidget)
        self.labelPreview.setObjectName(_fromUtf8("labelPreview"))
        self.verticalLayout.addWidget(self.labelPreview)
        self.tableViewData = QtGui.QTableView(CsvImportWidget)
        self.tableViewData.setObjectName(_fromUtf8("tableViewData"))
        self.verticalLayout.addWidget(self.tableViewData)
        self.line_3 = QtGui.QFrame(CsvImportWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.labelColumns = QtGui.QLabel(CsvImportWidget)
        self.labelColumns.setObjectName(_fromUtf8("labelColumns"))
        self.verticalLayout.addWidget(self.labelColumns)
        self.tableViewColumns = QtGui.QTableView(CsvImportWidget)
        self.tableViewColumns.setObjectName(_fromUtf8("tableViewColumns"))
        self.verticalLayout.addWidget(self.tableViewColumns)
        self.line_4 = QtGui.QFrame(CsvImportWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayoutButtons = QtGui.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(_fromUtf8("horizontalLayoutButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem)
        self.toolButtonUpdate = QtGui.QToolButton(CsvImportWidget)
        self.toolButtonUpdate.setText(_fromUtf8("update"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonUpdate.setIcon(icon1)
        self.toolButtonUpdate.setIconSize(QtCore.QSize(20, 20))
        self.toolButtonUpdate.setObjectName(_fromUtf8("toolButtonUpdate"))
        self.horizontalLayoutButtons.addWidget(self.toolButtonUpdate)
        self.toolButtonCancel = QtGui.QToolButton(CsvImportWidget)
        self.toolButtonCancel.setText(_fromUtf8("cancel"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dialog-cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonCancel.setIcon(icon2)
        self.toolButtonCancel.setIconSize(QtCore.QSize(20, 20))
        self.toolButtonCancel.setObjectName(_fromUtf8("toolButtonCancel"))
        self.horizontalLayoutButtons.addWidget(self.toolButtonCancel)
        self.toolButtonImport = QtGui.QToolButton(CsvImportWidget)
        self.toolButtonImport.setText(_fromUtf8("import  file"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dialog-ok-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonImport.setIcon(icon3)
        self.toolButtonImport.setIconSize(QtCore.QSize(20, 20))
        self.toolButtonImport.setObjectName(_fromUtf8("toolButtonImport"))
        self.horizontalLayoutButtons.addWidget(self.toolButtonImport)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayoutButtons)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CsvImportWidget)
        QtCore.QObject.connect(self.checkBoxDelimiterCustom, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditDelimiterCustom.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(CsvImportWidget)

    def retranslateUi(self, CsvImportWidget):
        CsvImportWidget.setWindowTitle(_translate("CsvImportWidget", "Form", None))
        self.labelFileName.setText(_translate("CsvImportWidget", "file", None))
        self.toolButtonOpen.setToolTip(_translate("CsvImportWidget", "update", None))
        self.toolButtonOpen.setShortcut(_translate("CsvImportWidget", "Ctrl+O", None))
        self.checkBoxDelimiterComma.setText(_translate("CsvImportWidget", ",", None))
        self.lineEditDelimiterCustom.setText(_translate("CsvImportWidget", ";", None))
        self.labelDelimiter.setText(_translate("CsvImportWidget", "delimiter", None))
        self.checkBoxDelimiterSemicolon.setText(_translate("CsvImportWidget", ";", None))
        self.checkBoxDelimiterCustom.setText(_translate("CsvImportWidget", "custom delimiter:", None))
        self.labelDelimiter_2.setText(_translate("CsvImportWidget", "delimiter", None))
        self.checkBoxSkipFaultyLines.setToolTip(_translate("CsvImportWidget", "skip faulty lines", None))
        self.checkBoxSkipFaultyLines.setText(_translate("CsvImportWidget", "skip faulty lines", None))
        self.labelPreview.setText(_translate("CsvImportWidget", "preview", None))
        self.labelColumns.setText(_translate("CsvImportWidget", "columns", None))
        self.toolButtonUpdate.setToolTip(_translate("CsvImportWidget", "update", None))
        self.toolButtonUpdate.setShortcut(_translate("CsvImportWidget", "Ctrl+O", None))
        self.toolButtonCancel.setToolTip(_translate("CsvImportWidget", "cancel", None))
        self.toolButtonCancel.setShortcut(_translate("CsvImportWidget", "Ctrl+O", None))
        self.toolButtonImport.setToolTip(_translate("CsvImportWidget", "import file", None))
        self.toolButtonImport.setShortcut(_translate("CsvImportWidget", "Ctrl+O", None))

import icons_rc
