# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMdiArea,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1932, 797)
        mainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        mainWindow.setDockNestingEnabled(False)
        self.centralwidget_grid = QWidget(mainWindow)
        self.centralwidget_grid.setObjectName(u"centralwidget_grid")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget_grid)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.RightContainer_widget = QWidget(self.centralwidget_grid)
        self.RightContainer_widget.setObjectName(u"RightContainer_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightContainer_widget.sizePolicy().hasHeightForWidth())
        self.RightContainer_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.RightContainer_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 9, -1)
        self.Generated_audioLabel = QLabel(self.RightContainer_widget)
        self.Generated_audioLabel.setObjectName(u"Generated_audioLabel")

        self.verticalLayout_10.addWidget(self.Generated_audioLabel)

        self.Generated_audioListWidget = QListWidget(self.RightContainer_widget)
        self.Generated_audioListWidget.setObjectName(u"Generated_audioListWidget")

        self.verticalLayout_10.addWidget(self.Generated_audioListWidget)

        self.yoursLabel = QLabel(self.RightContainer_widget)
        self.yoursLabel.setObjectName(u"yoursLabel")

        self.verticalLayout_10.addWidget(self.yoursLabel)

        self.yoursListWidget = QListWidget(self.RightContainer_widget)
        self.yoursListWidget.setObjectName(u"yoursListWidget")

        self.verticalLayout_10.addWidget(self.yoursListWidget)

        self.OptiongBox = QGroupBox(self.RightContainer_widget)
        self.OptiongBox.setObjectName(u"OptiongBox")
        self.verticalLayout_8 = QVBoxLayout(self.OptiongBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.check_pronounce_pB = QPushButton(self.OptiongBox)
        self.check_pronounce_pB.setObjectName(u"check_pronounce_pB")

        self.verticalLayout_8.addWidget(self.check_pronounce_pB)

        self.reload_audio_pB = QPushButton(self.OptiongBox)
        self.reload_audio_pB.setObjectName(u"reload_audio_pB")

        self.verticalLayout_8.addWidget(self.reload_audio_pB)

        self.transcibe_pB = QPushButton(self.OptiongBox)
        self.transcibe_pB.setObjectName(u"transcibe_pB")

        self.verticalLayout_8.addWidget(self.transcibe_pB)

        self.play_pB = QPushButton(self.OptiongBox)
        self.play_pB.setObjectName(u"play_pB")

        self.verticalLayout_8.addWidget(self.play_pB)

        self.rename_pB = QPushButton(self.OptiongBox)
        self.rename_pB.setObjectName(u"rename_pB")

        self.verticalLayout_8.addWidget(self.rename_pB)

        self.delete_pB = QPushButton(self.OptiongBox)
        self.delete_pB.setObjectName(u"delete_pB")

        self.verticalLayout_8.addWidget(self.delete_pB)


        self.verticalLayout_10.addWidget(self.OptiongBox)


        self.horizontalLayout_8.addWidget(self.RightContainer_widget)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.centralwidget_pB_panels__hLayout = QHBoxLayout()
        self.centralwidget_pB_panels__hLayout.setObjectName(u"centralwidget_pB_panels__hLayout")
        self.centralwidget_pB_panels__hLayout.setContentsMargins(0, -1, -1, -1)
        self.left_panel_pB = QPushButton(self.centralwidget_grid)
        self.left_panel_pB.setObjectName(u"left_panel_pB")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_panel_pB.sizePolicy().hasHeightForWidth())
        self.left_panel_pB.setSizePolicy(sizePolicy1)
        self.left_panel_pB.setCheckable(True)

        self.centralwidget_pB_panels__hLayout.addWidget(self.left_panel_pB)

        self.theme_pB = QPushButton(self.centralwidget_grid)
        self.theme_pB.setObjectName(u"theme_pB")
        self.theme_pB.setCheckable(False)

        self.centralwidget_pB_panels__hLayout.addWidget(self.theme_pB)

        self.right_panel_pB = QPushButton(self.centralwidget_grid)
        self.right_panel_pB.setObjectName(u"right_panel_pB")
        sizePolicy1.setHeightForWidth(self.right_panel_pB.sizePolicy().hasHeightForWidth())
        self.right_panel_pB.setSizePolicy(sizePolicy1)
        self.right_panel_pB.setCheckable(True)

        self.centralwidget_pB_panels__hLayout.addWidget(self.right_panel_pB)


        self.verticalLayout_11.addLayout(self.centralwidget_pB_panels__hLayout)

        self.mdiArea = QMdiArea(self.centralwidget_grid)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy2)
        self.mdiArea.setMaximumSize(QSize(16777215, 16777212))
        self.mdiArea.setMouseTracking(True)
        self.mdiArea.setTabletTracking(False)
        self.mdiArea.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.mdiArea.setToolTipDuration(8)
        self.mdiArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mdiArea.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.mdiArea.setFrameShape(QFrame.Shape.NoFrame)
        self.mdiArea.setFrameShadow(QFrame.Shadow.Plain)
        self.mdiArea.setLineWidth(-1)
        self.mdiArea.setMidLineWidth(-1)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mdiArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.mdiArea.setViewMode(QMdiArea.ViewMode.TabbedView)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setTabShape(QTabWidget.TabShape.Triangular)
        self.mdiArea.setTabPosition(QTabWidget.TabPosition.North)
        self.writer_sw = QWidget()
        self.writer_sw.setObjectName(u"writer_sw")
        self.writer_sw.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.writer_sw.sizePolicy().hasHeightForWidth())
        self.writer_sw.setSizePolicy(sizePolicy3)
        self.writer_sw.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.writer_sw.setLocale(QLocale(QLocale.English, QLocale.UnitedStatesVirginIslands))
        self.verticalLayout_3 = QVBoxLayout(self.writer_sw)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.writerwidget = QWidget(self.writer_sw)
        self.writerwidget.setObjectName(u"writerwidget")
        self.verticalLayout_4 = QVBoxLayout(self.writerwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.copy_pB = QPushButton(self.writerwidget)
        self.copy_pB.setObjectName(u"copy_pB")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.copy_pB.sizePolicy().hasHeightForWidth())
        self.copy_pB.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.copy_pB)

        self.cut_pB = QPushButton(self.writerwidget)
        self.cut_pB.setObjectName(u"cut_pB")
        sizePolicy4.setHeightForWidth(self.cut_pB.sizePolicy().hasHeightForWidth())
        self.cut_pB.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.cut_pB)

        self.paste_pB = QPushButton(self.writerwidget)
        self.paste_pB.setObjectName(u"paste_pB")
        sizePolicy4.setHeightForWidth(self.paste_pB.sizePolicy().hasHeightForWidth())
        self.paste_pB.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.paste_pB)

        self.undo_pB = QPushButton(self.writerwidget)
        self.undo_pB.setObjectName(u"undo_pB")
        sizePolicy4.setHeightForWidth(self.undo_pB.sizePolicy().hasHeightForWidth())
        self.undo_pB.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.undo_pB)

        self.redo_pB = QPushButton(self.writerwidget)
        self.redo_pB.setObjectName(u"redo_pB")
        sizePolicy4.setHeightForWidth(self.redo_pB.sizePolicy().hasHeightForWidth())
        self.redo_pB.setSizePolicy(sizePolicy4)
        self.redo_pB.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_19.addWidget(self.redo_pB)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.export_pB = QPushButton(self.writerwidget)
        self.export_pB.setObjectName(u"export_pB")

        self.horizontalLayout_19.addWidget(self.export_pB)

        self.upload_pB = QPushButton(self.writerwidget)
        self.upload_pB.setObjectName(u"upload_pB")
        sizePolicy1.setHeightForWidth(self.upload_pB.sizePolicy().hasHeightForWidth())
        self.upload_pB.setSizePolicy(sizePolicy1)
        self.upload_pB.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.horizontalLayout_19.addWidget(self.upload_pB)

        self.clear_pB = QPushButton(self.writerwidget)
        self.clear_pB.setObjectName(u"clear_pB")
        sizePolicy4.setHeightForWidth(self.clear_pB.sizePolicy().hasHeightForWidth())
        self.clear_pB.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.clear_pB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.Reader_editText = QTextEdit(self.writerwidget)
        self.Reader_editText.setObjectName(u"Reader_editText")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Reader_editText.sizePolicy().hasHeightForWidth())
        self.Reader_editText.setSizePolicy(sizePolicy5)
        self.Reader_editText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.verticalLayout_4.addWidget(self.Reader_editText)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.label_7 = QLabel(self.writerwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_20.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.read_pB = QPushButton(self.writerwidget)
        self.read_pB.setObjectName(u"read_pB")

        self.horizontalLayout_21.addWidget(self.read_pB)

        self.Check_grammar_pB = QPushButton(self.writerwidget)
        self.Check_grammar_pB.setObjectName(u"Check_grammar_pB")

        self.horizontalLayout_21.addWidget(self.Check_grammar_pB)

        self.translate_pB = QPushButton(self.writerwidget)
        self.translate_pB.setObjectName(u"translate_pB")

        self.horizontalLayout_21.addWidget(self.translate_pB)

        self.record_pB = QPushButton(self.writerwidget)
        self.record_pB.setObjectName(u"record_pB")

        self.horizontalLayout_21.addWidget(self.record_pB)

        self.save_pB = QPushButton(self.writerwidget)
        self.save_pB.setObjectName(u"save_pB")

        self.horizontalLayout_21.addWidget(self.save_pB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.ar = QProgressBar(self.writerwidget)
        self.ar.setObjectName(u"ar")
        self.ar.setValue(24)

        self.verticalLayout_4.addWidget(self.ar)


        self.verticalLayout_3.addWidget(self.writerwidget)

        self.mdiArea.addSubWindow(self.writer_sw)
        self.Reader = QWidget()
        self.Reader.setObjectName(u"Reader")
        self.verticalLayout_2 = QVBoxLayout(self.Reader)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.open_book_bP = QPushButton(self.Reader)
        self.open_book_bP.setObjectName(u"open_book_bP")

        self.horizontalLayout_4.addWidget(self.open_book_bP)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.book_webEngineView = QWebEngineView(self.Reader)
        self.book_webEngineView.setObjectName(u"book_webEngineView")
        sizePolicy2.setHeightForWidth(self.book_webEngineView.sizePolicy().hasHeightForWidth())
        self.book_webEngineView.setSizePolicy(sizePolicy2)
        self.book_webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.book_webEngineView)

        self.mdiArea.addSubWindow(self.Reader)
        self.Split = QWidget()
        self.Split.setObjectName(u"Split")
        self.Split.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(self.Split)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webEngineView_2 = QWebEngineView(self.Split)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.webEngineView_2.sizePolicy().hasHeightForWidth())
        self.webEngineView_2.setSizePolicy(sizePolicy6)
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.webEngineView_2)

        self.Panel_widget = QWidget(self.Split)
        self.Panel_widget.setObjectName(u"Panel_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Panel_widget.sizePolicy().hasHeightForWidth())
        self.Panel_widget.setSizePolicy(sizePolicy7)

        self.verticalLayout.addWidget(self.Panel_widget)

        self.mdiArea.addSubWindow(self.Split)

        self.verticalLayout_11.addWidget(self.mdiArea)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.contentLayout = QTabWidget(self.centralwidget_grid)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.contentLayout.sizePolicy().hasHeightForWidth())
        self.contentLayout.setSizePolicy(sizePolicy8)
        self.contentLayout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.contentLayout.setAutoFillBackground(False)
        self.contentLayout.setTabPosition(QTabWidget.TabPosition.West)
        self.contentLayout.setTabShape(QTabWidget.TabShape.Rounded)
        self.contentLayout.setDocumentMode(False)
        self.contentLayout.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.topBarLayout = QTabWidget(self.tab)
        self.topBarLayout.setObjectName(u"topBarLayout")
        sizePolicy8.setHeightForWidth(self.topBarLayout.sizePolicy().hasHeightForWidth())
        self.topBarLayout.setSizePolicy(sizePolicy8)
        self.topBarLayout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_16 = QVBoxLayout(self.tab_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.audio_settings_gB = QGroupBox(self.tab_3)
        self.audio_settings_gB.setObjectName(u"audio_settings_gB")
        sizePolicy.setHeightForWidth(self.audio_settings_gB.sizePolicy().hasHeightForWidth())
        self.audio_settings_gB.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.audio_settings_gB)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.engineLabel = QLabel(self.audio_settings_gB)
        self.engineLabel.setObjectName(u"engineLabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.engineLabel.sizePolicy().hasHeightForWidth())
        self.engineLabel.setSizePolicy(sizePolicy9)
        self.engineLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.engineLabel.setAutoFillBackground(False)
        self.engineLabel.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_2.addWidget(self.engineLabel)

        self.engine_cB = QComboBox(self.audio_settings_gB)
        self.engine_cB.setObjectName(u"engine_cB")
        sizePolicy1.setHeightForWidth(self.engine_cB.sizePolicy().hasHeightForWidth())
        self.engine_cB.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.engine_cB)

        self.about_engineButton = QPushButton(self.audio_settings_gB)
        self.about_engineButton.setObjectName(u"about_engineButton")
        sizePolicy1.setHeightForWidth(self.about_engineButton.sizePolicy().hasHeightForWidth())
        self.about_engineButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.about_engineButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.voiceLabel_2 = QLabel(self.audio_settings_gB)
        self.voiceLabel_2.setObjectName(u"voiceLabel_2")
        sizePolicy1.setHeightForWidth(self.voiceLabel_2.sizePolicy().hasHeightForWidth())
        self.voiceLabel_2.setSizePolicy(sizePolicy1)
        self.voiceLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_15.addWidget(self.voiceLabel_2)

        self.voice_cB = QComboBox(self.audio_settings_gB)
        self.voice_cB.setObjectName(u"voice_cB")

        self.horizontalLayout_15.addWidget(self.voice_cB)

        self.preview_pB = QPushButton(self.audio_settings_gB)
        self.preview_pB.setObjectName(u"preview_pB")
        sizePolicy9.setHeightForWidth(self.preview_pB.sizePolicy().hasHeightForWidth())
        self.preview_pB.setSizePolicy(sizePolicy9)

        self.horizontalLayout_15.addWidget(self.preview_pB)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.pushButton_2 = QPushButton(self.audio_settings_gB)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_16.addWidget(self.audio_settings_gB)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.verticalLayout_16.addWidget(self.label)

        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_12.addWidget(self.label_21)

        self.comboBox_7 = QComboBox(self.groupBox)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_12.addWidget(self.comboBox_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.comboBox_6 = QComboBox(self.groupBox)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_11.addWidget(self.comboBox_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_5.addWidget(self.checkBox_3)


        self.verticalLayout_16.addWidget(self.groupBox)

        self.topBarLayout.addTab(self.tab_3, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.topBarLayout.addTab(self.tab_7, "")

        self.verticalLayout_12.addWidget(self.topBarLayout)

        self.contentLayout.addTab(self.tab, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_6 = QVBoxLayout(self.tab_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.score_label = QLabel(self.tab_12)
        self.score_label.setObjectName(u"score_label")

        self.verticalLayout_6.addWidget(self.score_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.tab_12)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.tab_12)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_4 = QLabel(self.tab_12)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.tab_12)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.pushButton_3 = QPushButton(self.tab_12)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.textBrowser_2 = QTextBrowser(self.tab_12)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_6.addWidget(self.textBrowser_2)

        self.contentLayout.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.verticalLayout_7 = QVBoxLayout(self.tab_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.tab_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_13.addWidget(self.pushButton_4)

        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_13.addWidget(self.textBrowser)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.contentLayout.addTab(self.tab_13, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.contentLayout.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.layoutWidget2 = QWidget(self.tab_8)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 20, 231, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.comboBox_4 = QComboBox(self.tab_8)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(166, 90, 93, 28))
        self.label_5 = QLabel(self.tab_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 90, 130, 28))
        self.contentLayout.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.contentLayout.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.contentLayout.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.contentLayout.addTab(self.tab_11, "")

        self.horizontalLayout_8.addWidget(self.contentLayout)

        mainWindow.setCentralWidget(self.centralwidget_grid)

        self.retranslateUi(mainWindow)
        self.left_panel_pB.toggled.connect(self.RightContainer_widget.setHidden)
        self.right_panel_pB.toggled.connect(self.contentLayout.setHidden)

        self.contentLayout.setCurrentIndex(0)
        self.topBarLayout.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.Generated_audioLabel.setText(QCoreApplication.translate("mainWindow", u"Generated audios/Engine", None))
        self.yoursLabel.setText(QCoreApplication.translate("mainWindow", u"Yours/Qualification", None))
        self.OptiongBox.setTitle(QCoreApplication.translate("mainWindow", u"OPTIONS ", None))
        self.check_pronounce_pB.setText(QCoreApplication.translate("mainWindow", u"CHECK PRONOUNCE", None))
        self.reload_audio_pB.setText(QCoreApplication.translate("mainWindow", u"RELOAD", None))
        self.transcibe_pB.setText(QCoreApplication.translate("mainWindow", u"TRANCRIBE", None))
        self.play_pB.setText(QCoreApplication.translate("mainWindow", u"PLAY", None))
        self.rename_pB.setText(QCoreApplication.translate("mainWindow", u"RENAME", None))
        self.delete_pB.setText(QCoreApplication.translate("mainWindow", u"DELATE", None))
        self.left_panel_pB.setText(QCoreApplication.translate("mainWindow", u"left settings", None))
        self.theme_pB.setText(QCoreApplication.translate("mainWindow", u"theme", None))
        self.right_panel_pB.setText(QCoreApplication.translate("mainWindow", u"right settings", None))
        self.writer_sw.setWindowTitle(QCoreApplication.translate("mainWindow", u"WRITER", None))
        self.copy_pB.setText(QCoreApplication.translate("mainWindow", u"COPY", None))
        self.cut_pB.setText(QCoreApplication.translate("mainWindow", u"CUT", None))
        self.paste_pB.setText(QCoreApplication.translate("mainWindow", u"PASTE", None))
        self.undo_pB.setText(QCoreApplication.translate("mainWindow", u"UNDO", None))
        self.redo_pB.setText(QCoreApplication.translate("mainWindow", u"REDO", None))
        self.export_pB.setText(QCoreApplication.translate("mainWindow", u"EXPORT", None))
        self.upload_pB.setText(QCoreApplication.translate("mainWindow", u"UPLOAD FILE", None))
        self.clear_pB.setText(QCoreApplication.translate("mainWindow", u"CLEAR", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"0/1000", None))
        self.read_pB.setText(QCoreApplication.translate("mainWindow", u"READ", None))
        self.Check_grammar_pB.setText(QCoreApplication.translate("mainWindow", u"CHECK GRAMMAR", None))
        self.translate_pB.setText(QCoreApplication.translate("mainWindow", u"TRANSLATE", None))
        self.record_pB.setText(QCoreApplication.translate("mainWindow", u"RECORD", None))
        self.save_pB.setText(QCoreApplication.translate("mainWindow", u"SAVE", None))
        self.Reader.setWindowTitle(QCoreApplication.translate("mainWindow", u"READER", None))
        self.open_book_bP.setText(QCoreApplication.translate("mainWindow", u"Open a book (PDF)", None))
        self.Split.setWindowTitle(QCoreApplication.translate("mainWindow", u"SPLIT", None))
        self.audio_settings_gB.setTitle(QCoreApplication.translate("mainWindow", u"Engine TSS", None))
        self.engineLabel.setText(QCoreApplication.translate("mainWindow", u"Engine", None))
        self.about_engineButton.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.voiceLabel_2.setText(QCoreApplication.translate("mainWindow", u"Voice", None))
        self.preview_pB.setText(QCoreApplication.translate("mainWindow", u"Preview", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"Reload", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Output", None))
        self.label_21.setText(QCoreApplication.translate("mainWindow", u"Sample Rate", None))
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"Output format", None))
        self.checkBox_3.setText(QCoreApplication.translate("mainWindow", u"Normalize Audio", None))
        self.topBarLayout.setTabText(self.topBarLayout.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"Models Settings", None))
        self.topBarLayout.setTabText(self.topBarLayout.indexOf(self.tab_7), QCoreApplication.translate("mainWindow", u"Library", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"main", None))
        self.score_label.setText(QCoreApplication.translate("mainWindow", u"Translation", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"From", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"to", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"Clear", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_12), QCoreApplication.translate("mainWindow", u"Translation", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Grammar Checker", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"Clear", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_13), QCoreApplication.translate("mainWindow", u"Score/feedback", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"User profile", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Display language", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"Divice cpu/gpu", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_8), QCoreApplication.translate("mainWindow", u"Settings", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_9), QCoreApplication.translate("mainWindow", u"Pluggins", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_10), QCoreApplication.translate("mainWindow", u"About", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.tab_11), QCoreApplication.translate("mainWindow", u"Manual", None))
    # retranslateUi

