# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMdiArea, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1388, 796)
        mainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        mainWindow.setDockNestingEnabled(False)
        self.centralwidget_grid = QWidget(mainWindow)
        self.centralwidget_grid.setObjectName(u"centralwidget_grid")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget_grid)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RightContainer_widget = QWidget(self.centralwidget_grid)
        self.RightContainer_widget.setObjectName(u"RightContainer_widget")
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


        self.horizontalLayout_2.addWidget(self.RightContainer_widget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.centralwidget_pB_panels__hLayout = QHBoxLayout()
        self.centralwidget_pB_panels__hLayout.setObjectName(u"centralwidget_pB_panels__hLayout")
        self.centralwidget_pB_panels__hLayout.setContentsMargins(0, -1, -1, -1)
        self.left_panel_pB = QPushButton(self.centralwidget_grid)
        self.left_panel_pB.setObjectName(u"left_panel_pB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_panel_pB.sizePolicy().hasHeightForWidth())
        self.left_panel_pB.setSizePolicy(sizePolicy)
        self.left_panel_pB.setCheckable(True)

        self.centralwidget_pB_panels__hLayout.addWidget(self.left_panel_pB)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centralwidget_pB_panels__hLayout.addItem(self.horizontalSpacer)

        self.right_panel_pB = QPushButton(self.centralwidget_grid)
        self.right_panel_pB.setObjectName(u"right_panel_pB")
        sizePolicy.setHeightForWidth(self.right_panel_pB.sizePolicy().hasHeightForWidth())
        self.right_panel_pB.setSizePolicy(sizePolicy)
        self.right_panel_pB.setCheckable(True)

        self.centralwidget_pB_panels__hLayout.addWidget(self.right_panel_pB)


        self.verticalLayout_5.addLayout(self.centralwidget_pB_panels__hLayout)

        self.mdiArea = QMdiArea(self.centralwidget_grid)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy1)
        self.mdiArea.setMouseTracking(False)
        self.mdiArea.setTabletTracking(False)
        self.mdiArea.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.mdiArea.setToolTipDuration(8)
        self.mdiArea.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.mdiArea.setFrameShape(QFrame.Shape.NoFrame)
        self.mdiArea.setFrameShadow(QFrame.Shadow.Plain)
        self.mdiArea.setLineWidth(-1)
        self.mdiArea.setMidLineWidth(-1)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mdiArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.mdiArea.setViewMode(QMdiArea.ViewMode.TabbedView)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setTabShape(QTabWidget.TabShape.Rounded)
        self.mdiArea.setTabPosition(QTabWidget.TabPosition.North)
        self.writer_sw = QWidget()
        self.writer_sw.setObjectName(u"writer_sw")
        self.writer_sw.setEnabled(True)
        self.writer_sw.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.writer_sw.setLocale(QLocale(QLocale.English, QLocale.UnitedStatesVirginIslands))
        self.verticalLayout_3 = QVBoxLayout(self.writer_sw)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.writer_sw)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.copy_pB_5 = QPushButton(self.widget)
        self.copy_pB_5.setObjectName(u"copy_pB_5")
        sizePolicy.setHeightForWidth(self.copy_pB_5.sizePolicy().hasHeightForWidth())
        self.copy_pB_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.copy_pB_5)

        self.cut_pB_5 = QPushButton(self.widget)
        self.cut_pB_5.setObjectName(u"cut_pB_5")
        sizePolicy.setHeightForWidth(self.cut_pB_5.sizePolicy().hasHeightForWidth())
        self.cut_pB_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.cut_pB_5)

        self.paste_pB_5 = QPushButton(self.widget)
        self.paste_pB_5.setObjectName(u"paste_pB_5")
        sizePolicy.setHeightForWidth(self.paste_pB_5.sizePolicy().hasHeightForWidth())
        self.paste_pB_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.paste_pB_5)

        self.undo_pB_5 = QPushButton(self.widget)
        self.undo_pB_5.setObjectName(u"undo_pB_5")
        sizePolicy.setHeightForWidth(self.undo_pB_5.sizePolicy().hasHeightForWidth())
        self.undo_pB_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.undo_pB_5)

        self.redo_pB_5 = QPushButton(self.widget)
        self.redo_pB_5.setObjectName(u"redo_pB_5")
        self.redo_pB_5.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_19.addWidget(self.redo_pB_5)

        self.upload_pB_5 = QPushButton(self.widget)
        self.upload_pB_5.setObjectName(u"upload_pB_5")
        self.upload_pB_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.horizontalLayout_19.addWidget(self.upload_pB_5)

        self.clear_pB_5 = QPushButton(self.widget)
        self.clear_pB_5.setObjectName(u"clear_pB_5")
        sizePolicy.setHeightForWidth(self.clear_pB_5.sizePolicy().hasHeightForWidth())
        self.clear_pB_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.clear_pB_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.Reader_editText = QTextEdit(self.widget)
        self.Reader_editText.setObjectName(u"Reader_editText")
        sizePolicy1.setHeightForWidth(self.Reader_editText.sizePolicy().hasHeightForWidth())
        self.Reader_editText.setSizePolicy(sizePolicy1)
        self.Reader_editText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.verticalLayout_4.addWidget(self.Reader_editText)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_20.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_17 = QPushButton(self.widget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_21.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.widget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_21.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_21.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.widget)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_21.addWidget(self.pushButton_20)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.main_pB = QProgressBar(self.widget)
        self.main_pB.setObjectName(u"main_pB")
        self.main_pB.setValue(24)

        self.verticalLayout_4.addWidget(self.main_pB)


        self.verticalLayout_3.addWidget(self.widget)

        self.mdiArea.addSubWindow(self.writer_sw)
        self.Reader = QWidget()
        self.Reader.setObjectName(u"Reader")
        self.verticalLayout_2 = QVBoxLayout(self.Reader)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.webEngineView = QWebEngineView(self.Reader)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView)

        self.mdiArea.addSubWindow(self.Reader)
        self.Split = QWidget()
        self.Split.setObjectName(u"Split")
        self.Split.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(self.Split)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webEngineView_2 = QWebEngineView(self.Split)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.webEngineView_2)

        self.Panel_widget = QWidget(self.Split)
        self.Panel_widget.setObjectName(u"Panel_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Panel_widget.sizePolicy().hasHeightForWidth())
        self.Panel_widget.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.Panel_widget)

        self.mdiArea.addSubWindow(self.Split)

        self.verticalLayout_5.addWidget(self.mdiArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.tabWidget = QTabWidget(self.centralwidget_grid)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_12 = QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.engineLabel_2 = QLabel(self.tab_3)
        self.engineLabel_2.setObjectName(u"engineLabel_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.engineLabel_2.sizePolicy().hasHeightForWidth())
        self.engineLabel_2.setSizePolicy(sizePolicy3)
        self.engineLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.engineLabel_2.setAutoFillBackground(False)
        self.engineLabel_2.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_14.addWidget(self.engineLabel_2)

        self.engine_cB = QComboBox(self.tab_3)
        self.engine_cB.addItem("")
        self.engine_cB.addItem("")
        self.engine_cB.addItem("")
        self.engine_cB.addItem("")
        self.engine_cB.setObjectName(u"engine_cB")
        sizePolicy.setHeightForWidth(self.engine_cB.sizePolicy().hasHeightForWidth())
        self.engine_cB.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.engine_cB)

        self.about_engineButton_2 = QPushButton(self.tab_3)
        self.about_engineButton_2.setObjectName(u"about_engineButton_2")
        sizePolicy.setHeightForWidth(self.about_engineButton_2.sizePolicy().hasHeightForWidth())
        self.about_engineButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.about_engineButton_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.voiceLabel_2 = QLabel(self.tab_3)
        self.voiceLabel_2.setObjectName(u"voiceLabel_2")
        sizePolicy.setHeightForWidth(self.voiceLabel_2.sizePolicy().hasHeightForWidth())
        self.voiceLabel_2.setSizePolicy(sizePolicy)
        self.voiceLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_15.addWidget(self.voiceLabel_2)

        self.voice_cB = QComboBox(self.tab_3)
        self.voice_cB.addItem("")
        self.voice_cB.addItem("")
        self.voice_cB.addItem("")
        self.voice_cB.addItem("")
        self.voice_cB.setObjectName(u"voice_cB")

        self.horizontalLayout_15.addWidget(self.voice_cB)

        self.preview_pB = QPushButton(self.tab_3)
        self.preview_pB.setObjectName(u"preview_pB")
        sizePolicy3.setHeightForWidth(self.preview_pB.sizePolicy().hasHeightForWidth())
        self.preview_pB.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.preview_pB)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.reaload_engine_pB = QPushButton(self.tab_3)
        self.reaload_engine_pB.setObjectName(u"reaload_engine_pB")
        sizePolicy.setHeightForWidth(self.reaload_engine_pB.sizePolicy().hasHeightForWidth())
        self.reaload_engine_pB.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.reaload_engine_pB)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.speech_settings_gB = QGroupBox(self.tab_3)
        self.speech_settings_gB.setObjectName(u"speech_settings_gB")
        self.verticalLayout_9 = QVBoxLayout(self.speech_settings_gB)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.speed_speech_settingslabel = QLabel(self.speech_settings_gB)
        self.speed_speech_settingslabel.setObjectName(u"speed_speech_settingslabel")

        self.verticalLayout_6.addWidget(self.speed_speech_settingslabel)

        self.speed_speech_settings_hS = QSlider(self.speech_settings_gB)
        self.speed_speech_settings_hS.setObjectName(u"speed_speech_settings_hS")
        self.speed_speech_settings_hS.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.speed_speech_settings_hS)

        self.pitch_speech_settingslabel = QLabel(self.speech_settings_gB)
        self.pitch_speech_settingslabel.setObjectName(u"pitch_speech_settingslabel")

        self.verticalLayout_6.addWidget(self.pitch_speech_settingslabel)

        self.pitch_speech_hS_2 = QSlider(self.speech_settings_gB)
        self.pitch_speech_hS_2.setObjectName(u"pitch_speech_hS_2")
        self.pitch_speech_hS_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.pitch_speech_hS_2)

        self.volume_speech_settingslabel = QLabel(self.speech_settings_gB)
        self.volume_speech_settingslabel.setObjectName(u"volume_speech_settingslabel")

        self.verticalLayout_6.addWidget(self.volume_speech_settingslabel)

        self.volume_speed_speech_settings_hS_2 = QSlider(self.speech_settings_gB)
        self.volume_speed_speech_settings_hS_2.setObjectName(u"volume_speed_speech_settings_hS_2")
        self.volume_speed_speech_settings_hS_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.volume_speed_speech_settings_hS_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_12.addWidget(self.speech_settings_gB)

        self.animated_image_right_panelLabel = QLabel(self.tab_3)
        self.animated_image_right_panelLabel.setObjectName(u"animated_image_right_panelLabel")
        sizePolicy1.setHeightForWidth(self.animated_image_right_panelLabel.sizePolicy().hasHeightForWidth())
        self.animated_image_right_panelLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.animated_image_right_panelLabel)

        self.audio_settings_gB = QGroupBox(self.tab_3)
        self.audio_settings_gB.setObjectName(u"audio_settings_gB")
        self.verticalLayout_17 = QVBoxLayout(self.audio_settings_gB)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_20 = QLabel(self.audio_settings_gB)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.comboBox_6 = QComboBox(self.audio_settings_gB)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_11.addWidget(self.comboBox_6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_21 = QLabel(self.audio_settings_gB)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_12.addWidget(self.label_21)

        self.comboBox_7 = QComboBox(self.audio_settings_gB)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_12.addWidget(self.comboBox_7)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_3 = QCheckBox(self.audio_settings_gB)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_13.addWidget(self.checkBox_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)


        self.verticalLayout_12.addWidget(self.audio_settings_gB)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.left_container_widget = QWidget()
        self.left_container_widget.setObjectName(u"left_container_widget")
        self.vertru = QVBoxLayout(self.left_container_widget)
        self.vertru.setObjectName(u"vertru")
        self.audio_model_gB = QGroupBox(self.left_container_widget)
        self.audio_model_gB.setObjectName(u"audio_model_gB")
        self.audio_settingLabel = QLabel(self.audio_model_gB)
        self.audio_settingLabel.setObjectName(u"audio_settingLabel")
        self.audio_settingLabel.setGeometry(QRect(12, 90, 62, 20))
        self.layoutWidget = QWidget(self.audio_model_gB)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 35, 198, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.audio_model_cB = QComboBox(self.layoutWidget)
        self.audio_model_cB.addItem("")
        self.audio_model_cB.addItem("")
        self.audio_model_cB.addItem("")
        self.audio_model_cB.addItem("")
        self.audio_model_cB.setObjectName(u"audio_model_cB")

        self.horizontalLayout.addWidget(self.audio_model_cB)

        self.about_audio_model = QPushButton(self.layoutWidget)
        self.about_audio_model.setObjectName(u"about_audio_model")

        self.horizontalLayout.addWidget(self.about_audio_model)


        self.vertru.addWidget(self.audio_model_gB)

        self.tabWidget_2.addTab(self.left_container_widget, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.formLayout = QFormLayout(self.tab_4)
        self.formLayout.setObjectName(u"formLayout")
        self.meaning_searchLabel = QLabel(self.tab_4)
        self.meaning_searchLabel.setObjectName(u"meaning_searchLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.meaning_searchLabel)

        self.search_pB = QPushButton(self.tab_4)
        self.search_pB.setObjectName(u"search_pB")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.search_pB)

        self.search_lE = QLineEdit(self.tab_4)
        self.search_lE.setObjectName(u"search_lE")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.search_lE)

        self.search_wVE = QWebEngineView(self.tab_4)
        self.search_wVE.setObjectName(u"search_wVE")
        self.search_wVE.setUrl(QUrl(u"about:blank"))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.search_wVE)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.score_label = QLabel(self.tab_5)
        self.score_label.setObjectName(u"score_label")

        self.verticalLayout_7.addWidget(self.score_label)

        self.score_frame = QListView(self.tab_5)
        self.score_frame.setObjectName(u"score_frame")

        self.verticalLayout_7.addWidget(self.score_frame)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.space_rep_systemLabel = QLabel(self.tab_6)
        self.space_rep_systemLabel.setObjectName(u"space_rep_systemLabel")
        self.space_rep_systemLabel.setGeometry(QRect(50, 30, 131, 16))
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")

        self.verticalLayout_11.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.theme_pB = QPushButton(self.tab_8)
        self.theme_pB.setObjectName(u"theme_pB")
        self.theme_pB.setGeometry(QRect(80, 30, 93, 29))
        self.theme_pB.setCheckable(True)
        self.widget1 = QWidget(self.tab_8)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 160, 179, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget.addTab(self.tab_11, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        mainWindow.setCentralWidget(self.centralwidget_grid)

        self.retranslateUi(mainWindow)
        self.left_panel_pB.toggled.connect(self.RightContainer_widget.setHidden)
        self.right_panel_pB.toggled.connect(self.tabWidget.setHidden)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.Generated_audioLabel.setText(QCoreApplication.translate("mainWindow", u"Generated audios/Engine", None))
        self.yoursLabel.setText(QCoreApplication.translate("mainWindow", u"Yours/Qualification", None))
        self.OptiongBox.setTitle(QCoreApplication.translate("mainWindow", u"OPTIONS ", None))
        self.play_pB.setText(QCoreApplication.translate("mainWindow", u"PLAY", None))
        self.rename_pB.setText(QCoreApplication.translate("mainWindow", u"RENAME", None))
        self.delete_pB.setText(QCoreApplication.translate("mainWindow", u"DELATE", None))
        self.left_panel_pB.setText(QCoreApplication.translate("mainWindow", u"left settings", None))
        self.right_panel_pB.setText(QCoreApplication.translate("mainWindow", u"right settings", None))
        self.writer_sw.setWindowTitle(QCoreApplication.translate("mainWindow", u"WRITER", None))
        self.copy_pB_5.setText(QCoreApplication.translate("mainWindow", u"COPY", None))
        self.cut_pB_5.setText(QCoreApplication.translate("mainWindow", u"CUT", None))
        self.paste_pB_5.setText(QCoreApplication.translate("mainWindow", u"PASTE", None))
        self.undo_pB_5.setText(QCoreApplication.translate("mainWindow", u"UNDO", None))
        self.redo_pB_5.setText(QCoreApplication.translate("mainWindow", u"REDO", None))
        self.upload_pB_5.setText(QCoreApplication.translate("mainWindow", u"UPLOAD", None))
        self.clear_pB_5.setText(QCoreApplication.translate("mainWindow", u"CLEAR", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"0/1000", None))
        self.pushButton_17.setText(QCoreApplication.translate("mainWindow", u"READ", None))
        self.pushButton_18.setText(QCoreApplication.translate("mainWindow", u"READ ALL", None))
        self.pushButton_19.setText(QCoreApplication.translate("mainWindow", u"RECORD", None))
        self.pushButton_20.setText(QCoreApplication.translate("mainWindow", u"SAVE", None))
        self.Reader.setWindowTitle(QCoreApplication.translate("mainWindow", u"READER", None))
        self.Split.setWindowTitle(QCoreApplication.translate("mainWindow", u"SPLIT", None))
        self.engineLabel_2.setText(QCoreApplication.translate("mainWindow", u"Engine", None))
        self.engine_cB.setItemText(0, QCoreApplication.translate("mainWindow", u"Piper", None))
        self.engine_cB.setItemText(1, QCoreApplication.translate("mainWindow", u"Coquis", None))
        self.engine_cB.setItemText(2, QCoreApplication.translate("mainWindow", u"Kokoro", None))
        self.engine_cB.setItemText(3, QCoreApplication.translate("mainWindow", u"Orpheus", None))

        self.about_engineButton_2.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.voiceLabel_2.setText(QCoreApplication.translate("mainWindow", u"Voice", None))
        self.voice_cB.setItemText(0, QCoreApplication.translate("mainWindow", u"v1", None))
        self.voice_cB.setItemText(1, QCoreApplication.translate("mainWindow", u"v2", None))
        self.voice_cB.setItemText(2, QCoreApplication.translate("mainWindow", u"v3", None))
        self.voice_cB.setItemText(3, QCoreApplication.translate("mainWindow", u"v4", None))

        self.preview_pB.setText(QCoreApplication.translate("mainWindow", u"Preview", None))
        self.reaload_engine_pB.setText(QCoreApplication.translate("mainWindow", u"RELOAD ENGINES", None))
        self.speech_settings_gB.setTitle(QCoreApplication.translate("mainWindow", u"SPEECH SETTING", None))
        self.speed_speech_settingslabel.setText(QCoreApplication.translate("mainWindow", u"Speed", None))
        self.pitch_speech_settingslabel.setText(QCoreApplication.translate("mainWindow", u"Pitch", None))
        self.volume_speech_settingslabel.setText(QCoreApplication.translate("mainWindow", u"Volume", None))
        self.animated_image_right_panelLabel.setText("")
        self.audio_settings_gB.setTitle(QCoreApplication.translate("mainWindow", u"AUDIO SETTINGS", None))
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"Output format", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("mainWindow", u"mp3", None))

        self.label_21.setText(QCoreApplication.translate("mainWindow", u"Sample Rate", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("mainWindow", u"128", None))

        self.checkBox_3.setText(QCoreApplication.translate("mainWindow", u"Normalize Audio", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"Engines", None))
        self.audio_model_gB.setTitle(QCoreApplication.translate("mainWindow", u"Audio", None))
        self.audio_settingLabel.setText(QCoreApplication.translate("mainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Model", None))
        self.audio_model_cB.setItemText(0, QCoreApplication.translate("mainWindow", u"m1", None))
        self.audio_model_cB.setItemText(1, QCoreApplication.translate("mainWindow", u"m2", None))
        self.audio_model_cB.setItemText(2, QCoreApplication.translate("mainWindow", u"m3", None))
        self.audio_model_cB.setItemText(3, QCoreApplication.translate("mainWindow", u"m4", None))

        self.about_audio_model.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.left_container_widget), QCoreApplication.translate("mainWindow", u"Models", None))
        self.meaning_searchLabel.setText(QCoreApplication.translate("mainWindow", u"Look up meanings", None))
        self.search_pB.setText(QCoreApplication.translate("mainWindow", u"Search", None))
        self.search_lE.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Insert a word...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("mainWindow", u"Dict", None))
        self.score_label.setText(QCoreApplication.translate("mainWindow", u"Feedbacks", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("mainWindow", u"Score", None))
        self.space_rep_systemLabel.setText(QCoreApplication.translate("mainWindow", u"Space Repetition System", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("mainWindow", u"SRS", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("mainWindow", u"Library", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"User profile", None))
        self.theme_pB.setText(QCoreApplication.translate("mainWindow", u"theme", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Display language", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("mainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("mainWindow", u"Pluggins", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("mainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("mainWindow", u"Manual", None))
    # retranslateUi

