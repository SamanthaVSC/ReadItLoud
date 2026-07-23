# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogsettingmenu.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFontComboBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(470, 558)
        self.verticalLayout_5 = QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.font_tab = QWidget()
        self.font_tab.setObjectName(u"font_tab")
        self.verticalLayout_4 = QVBoxLayout(self.font_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.font_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.groupBox = QGroupBox(self.font_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fontComboBox = QFontComboBox(self.groupBox)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.verticalLayout_2.addWidget(self.fontComboBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.font_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fontComboBox_2 = QFontComboBox(self.groupBox_2)
        self.fontComboBox_2.setObjectName(u"fontComboBox_2")

        self.verticalLayout_3.addWidget(self.fontComboBox_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_5.addWidget(self.spinBox_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.font_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fontComboBox_3 = QFontComboBox(self.groupBox_3)
        self.fontComboBox_3.setObjectName(u"fontComboBox_3")

        self.verticalLayout.addWidget(self.fontComboBox_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinBox_3 = QSpinBox(self.groupBox_3)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_7.addWidget(self.spinBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.font_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.font_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.font_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.font_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.font_tab, "")
        self.tools_tab = QWidget()
        self.tools_tab.setObjectName(u"tools_tab")
        self.verticalLayout_6 = QVBoxLayout(self.tools_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.tools_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.tools_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.tabWidget.addTab(self.tools_tab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Font (Style & Size)", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Primary", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Secondary", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Text Editor", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Restart", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.font_tab), QCoreApplication.translate("Dialog", u"Fonts", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Dictionary", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Space Repetition System", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab), QCoreApplication.translate("Dialog", u"Tools", None))
    # retranslateUi

