# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtask.ui'
#
# Created: Sun Jan  1 21:42:02 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        EditDialog.setObjectName(_fromUtf8("EditDialog"))
        EditDialog.resize(638, 404)
        EditDialog.setWindowTitle(QtGui.QApplication.translate("EditDialog", "Create new task", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_4 = QtGui.QVBoxLayout(EditDialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(EditDialog)
        self.label.setText(QtGui.QApplication.translate("EditDialog", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.task_name = QtGui.QLineEdit(EditDialog)
        self.task_name.setObjectName(_fromUtf8("task_name"))
        self.horizontalLayout.addWidget(self.task_name)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(EditDialog)
        self.label_3.setText(QtGui.QApplication.translate("EditDialog", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(31, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.statusLabel = QtGui.QLabel(EditDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setText(QtGui.QApplication.translate("EditDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_4.addWidget(self.statusLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(EditDialog)
        self.label_2.setText(QtGui.QApplication.translate("EditDialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(31, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.textEdit = QtGui.QTextEdit(EditDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.groupBox = QtGui.QGroupBox(EditDialog)
        self.groupBox.setTitle(QtGui.QApplication.translate("EditDialog", "Date/Time", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setText(QtGui.QApplication.translate("EditDialog", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.dateEdit = QtGui.QDateEdit(self.groupBox)
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("EditDialog", "ddd dd MMM, yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.timeCheckBox = QtGui.QCheckBox(self.groupBox)
        self.timeCheckBox.setText(QtGui.QApplication.translate("EditDialog", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.timeCheckBox.setObjectName(_fromUtf8("timeCheckBox"))
        self.horizontalLayout_6.addWidget(self.timeCheckBox)
        self.timeEdit = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayout_6.addWidget(self.timeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setText(QtGui.QApplication.translate("EditDialog", "Today", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setText(QtGui.QApplication.translate("EditDialog", "Tomorrow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setText(QtGui.QApplication.translate("EditDialog", "Next Week", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setText(QtGui.QApplication.translate("EditDialog", "Next Month", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setText(QtGui.QApplication.translate("EditDialog", "Remainder /* UI to be implemented */", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(EditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(EditDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditDialog.reject)
        QtCore.QObject.connect(self.timeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.timeEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(EditDialog)

    def retranslateUi(self, EditDialog):
        pass

