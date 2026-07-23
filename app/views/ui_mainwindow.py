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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1342, 617)
        mainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        mainWindow.setDockNestingEnabled(False)
        self.actionAbout = QAction(mainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionManualIntegrated = QAction(mainWindow)
        self.actionManualIntegrated.setObjectName(u"actionManualIntegrated")
        self.actionGuide = QAction(mainWindow)
        self.actionGuide.setObjectName(u"actionGuide")
        self.actionAboutSofware = QAction(mainWindow)
        self.actionAboutSofware.setObjectName(u"actionAboutSofware")
        self.actionPreferences = QAction(mainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionTools = QAction(mainWindow)
        self.actionTools.setObjectName(u"actionTools")
        self.centralwidget_grid = QWidget(mainWindow)
        self.centralwidget_grid.setObjectName(u"centralwidget_grid")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget_grid)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RightContainer_widget = QWidget(self.centralwidget_grid)
        self.RightContainer_widget.setObjectName(u"RightContainer_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightContainer_widget.sizePolicy().hasHeightForWidth())
        self.RightContainer_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.RightContainer_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 9, -1)
        self.audioLabel = QLabel(self.RightContainer_widget)
        self.audioLabel.setObjectName(u"audioLabel")

        self.verticalLayout_10.addWidget(self.audioLabel)

        self.audioListWidget = QListWidget(self.RightContainer_widget)
        self.audioListWidget.setObjectName(u"audioListWidget")

        self.verticalLayout_10.addWidget(self.audioListWidget)

        self.rep_timeLabel = QLabel(self.RightContainer_widget)
        self.rep_timeLabel.setObjectName(u"rep_timeLabel")
        self.rep_timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.rep_timeLabel)

        self.OptiongBox = QGroupBox(self.RightContainer_widget)
        self.OptiongBox.setObjectName(u"OptiongBox")
        self.verticalLayout_8 = QVBoxLayout(self.OptiongBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.reload_audio_pB = QPushButton(self.OptiongBox)
        self.reload_audio_pB.setObjectName(u"reload_audio_pB")

        self.horizontalLayout_7.addWidget(self.reload_audio_pB)

        self.check_pronounce_pB = QPushButton(self.OptiongBox)
        self.check_pronounce_pB.setObjectName(u"check_pronounce_pB")

        self.horizontalLayout_7.addWidget(self.check_pronounce_pB)

        self.play_pause_pB = QPushButton(self.OptiongBox)
        self.play_pause_pB.setObjectName(u"play_pause_pB")

        self.horizontalLayout_7.addWidget(self.play_pause_pB)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.rename_pB = QPushButton(self.OptiongBox)
        self.rename_pB.setObjectName(u"rename_pB")

        self.horizontalLayout_9.addWidget(self.rename_pB)

        self.delete_pB = QPushButton(self.OptiongBox)
        self.delete_pB.setObjectName(u"delete_pB")

        self.horizontalLayout_9.addWidget(self.delete_pB)

        self.transcibe_pB = QPushButton(self.OptiongBox)
        self.transcibe_pB.setObjectName(u"transcibe_pB")
        self.transcibe_pB.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.transcibe_pB)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addWidget(self.OptiongBox)


        self.horizontalLayout_2.addWidget(self.RightContainer_widget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_panel_pB = QPushButton(self.centralwidget_grid)
        self.left_panel_pB.setObjectName(u"left_panel_pB")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_panel_pB.sizePolicy().hasHeightForWidth())
        self.left_panel_pB.setSizePolicy(sizePolicy1)
        self.left_panel_pB.setCheckable(True)

        self.horizontalLayout.addWidget(self.left_panel_pB)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.theme_pB = QPushButton(self.centralwidget_grid)
        self.theme_pB.setObjectName(u"theme_pB")
        sizePolicy1.setHeightForWidth(self.theme_pB.sizePolicy().hasHeightForWidth())
        self.theme_pB.setSizePolicy(sizePolicy1)
        self.theme_pB.setCheckable(False)

        self.horizontalLayout.addWidget(self.theme_pB)

        self.right_panel_pB = QPushButton(self.centralwidget_grid)
        self.right_panel_pB.setObjectName(u"right_panel_pB")
        sizePolicy1.setHeightForWidth(self.right_panel_pB.sizePolicy().hasHeightForWidth())
        self.right_panel_pB.setSizePolicy(sizePolicy1)
        self.right_panel_pB.setCheckable(True)

        self.horizontalLayout.addWidget(self.right_panel_pB)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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
        self.mdiArea.setTabShape(QTabWidget.TabShape.Rounded)
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

        self.writer_editText = QTextEdit(self.writerwidget)
        self.writer_editText.setObjectName(u"writer_editText")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.writer_editText.sizePolicy().hasHeightForWidth())
        self.writer_editText.setSizePolicy(sizePolicy5)
        self.writer_editText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.verticalLayout_4.addWidget(self.writer_editText)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.counterLabel = QLabel(self.writerwidget)
        self.counterLabel.setObjectName(u"counterLabel")
        self.counterLabel.setStyleSheet(u"font: 600 10.5pt \"Inter\";")

        self.horizontalLayout_20.addWidget(self.counterLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.Check_grammar_pB = QPushButton(self.writerwidget)
        self.Check_grammar_pB.setObjectName(u"Check_grammar_pB")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Check_grammar_pB.sizePolicy().hasHeightForWidth())
        self.Check_grammar_pB.setSizePolicy(sizePolicy6)

        self.horizontalLayout_21.addWidget(self.Check_grammar_pB)

        self.translate_pB = QPushButton(self.writerwidget)
        self.translate_pB.setObjectName(u"translate_pB")
        sizePolicy6.setHeightForWidth(self.translate_pB.sizePolicy().hasHeightForWidth())
        self.translate_pB.setSizePolicy(sizePolicy6)

        self.horizontalLayout_21.addWidget(self.translate_pB)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.read_pB = QPushButton(self.writerwidget)
        self.read_pB.setObjectName(u"read_pB")
        sizePolicy6.setHeightForWidth(self.read_pB.sizePolicy().hasHeightForWidth())
        self.read_pB.setSizePolicy(sizePolicy6)
        self.read_pB.setCheckable(True)
        self.read_pB.setChecked(False)

        self.horizontalLayout_21.addWidget(self.read_pB)

        self.record_pause_pB = QPushButton(self.writerwidget)
        self.record_pause_pB.setObjectName(u"record_pause_pB")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.record_pause_pB.sizePolicy().hasHeightForWidth())
        self.record_pause_pB.setSizePolicy(sizePolicy7)
        self.record_pause_pB.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.record_pause_pB)

        self.stop_pB = QPushButton(self.writerwidget)
        self.stop_pB.setObjectName(u"stop_pB")
        sizePolicy7.setHeightForWidth(self.stop_pB.sizePolicy().hasHeightForWidth())
        self.stop_pB.setSizePolicy(sizePolicy7)

        self.horizontalLayout_21.addWidget(self.stop_pB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)


        self.verticalLayout_3.addWidget(self.writerwidget)

        self.mdiArea.addSubWindow(self.writer_sw)
        self.Reader = QWidget()
        self.Reader.setObjectName(u"Reader")
        self.gridLayout_7 = QGridLayout(self.Reader)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.open_book_pB = QPushButton(self.Reader)
        self.open_book_pB.setObjectName(u"open_book_pB")

        self.gridLayout_7.addWidget(self.open_book_pB, 0, 0, 1, 1)

        self.book_webEngineView = QWebEngineView(self.Reader)
        self.book_webEngineView.setObjectName(u"book_webEngineView")
        sizePolicy5.setHeightForWidth(self.book_webEngineView.sizePolicy().hasHeightForWidth())
        self.book_webEngineView.setSizePolicy(sizePolicy5)
        self.book_webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout_7.addWidget(self.book_webEngineView, 1, 0, 1, 3)

        self.toggle_reader_mode_pB = QPushButton(self.Reader)
        self.toggle_reader_mode_pB.setObjectName(u"toggle_reader_mode_pB")

        self.gridLayout_7.addWidget(self.toggle_reader_mode_pB, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(462, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.mdiArea.addSubWindow(self.Reader)

        self.verticalLayout_2.addWidget(self.mdiArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.contentLayout = QTabWidget(self.centralwidget_grid)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.contentLayout.sizePolicy().hasHeightForWidth())
        self.contentLayout.setSizePolicy(sizePolicy8)
        self.contentLayout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.contentLayout.setAutoFillBackground(False)
        self.contentLayout.setTabPosition(QTabWidget.TabPosition.North)
        self.contentLayout.setTabShape(QTabWidget.TabShape.Rounded)
        self.contentLayout.setDocumentMode(False)
        self.contentLayout.setTabsClosable(False)
        self.engine_tab = QWidget()
        self.engine_tab.setObjectName(u"engine_tab")
        self.verticalLayout = QVBoxLayout(self.engine_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.audio_settings_gB = QGroupBox(self.engine_tab)
        self.audio_settings_gB.setObjectName(u"audio_settings_gB")
        sizePolicy7.setHeightForWidth(self.audio_settings_gB.sizePolicy().hasHeightForWidth())
        self.audio_settings_gB.setSizePolicy(sizePolicy7)
        self.gridLayout = QGridLayout(self.audio_settings_gB)
        self.gridLayout.setObjectName(u"gridLayout")
        self.voiceLabel = QLabel(self.audio_settings_gB)
        self.voiceLabel.setObjectName(u"voiceLabel")
        sizePolicy8.setHeightForWidth(self.voiceLabel.sizePolicy().hasHeightForWidth())
        self.voiceLabel.setSizePolicy(sizePolicy8)
        self.voiceLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.voiceLabel, 2, 0, 1, 1)

        self.about_engines_pB = QPushButton(self.audio_settings_gB)
        self.about_engines_pB.setObjectName(u"about_engines_pB")
        sizePolicy1.setHeightForWidth(self.about_engines_pB.sizePolicy().hasHeightForWidth())
        self.about_engines_pB.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.about_engines_pB, 1, 4, 1, 1)

        self.engine_lang_cB = QComboBox(self.audio_settings_gB)
        self.engine_lang_cB.setObjectName(u"engine_lang_cB")
        sizePolicy7.setHeightForWidth(self.engine_lang_cB.sizePolicy().hasHeightForWidth())
        self.engine_lang_cB.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.engine_lang_cB, 1, 2, 1, 2)

        self.label = QLabel(self.audio_settings_gB)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)

        self.preview_pB = QPushButton(self.audio_settings_gB)
        self.preview_pB.setObjectName(u"preview_pB")
        sizePolicy8.setHeightForWidth(self.preview_pB.sizePolicy().hasHeightForWidth())
        self.preview_pB.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.preview_pB, 2, 3, 1, 1)

        self.languageLabel = QLabel(self.audio_settings_gB)
        self.languageLabel.setObjectName(u"languageLabel")
        sizePolicy8.setHeightForWidth(self.languageLabel.sizePolicy().hasHeightForWidth())
        self.languageLabel.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.languageLabel, 0, 2, 1, 2)

        self.engineLabel = QLabel(self.audio_settings_gB)
        self.engineLabel.setObjectName(u"engineLabel")
        sizePolicy8.setHeightForWidth(self.engineLabel.sizePolicy().hasHeightForWidth())
        self.engineLabel.setSizePolicy(sizePolicy8)
        self.engineLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.engineLabel.setAutoFillBackground(False)
        self.engineLabel.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout.addWidget(self.engineLabel, 0, 0, 1, 1)

        self.engine_cB = QComboBox(self.audio_settings_gB)
        self.engine_cB.setObjectName(u"engine_cB")

        self.gridLayout.addWidget(self.engine_cB, 1, 0, 1, 2)

        self.engine_voice_cB = QComboBox(self.audio_settings_gB)
        self.engine_voice_cB.setObjectName(u"engine_voice_cB")
        sizePolicy7.setHeightForWidth(self.engine_voice_cB.sizePolicy().hasHeightForWidth())
        self.engine_voice_cB.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.engine_voice_cB, 2, 1, 1, 2)


        self.verticalLayout.addWidget(self.audio_settings_gB)

        self.groupBox_4 = QGroupBox(self.engine_tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy7.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy7)
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.volumeLabel = QLabel(self.groupBox_4)
        self.volumeLabel.setObjectName(u"volumeLabel")
        sizePolicy8.setHeightForWidth(self.volumeLabel.sizePolicy().hasHeightForWidth())
        self.volumeLabel.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.volumeLabel, 0, 0, 1, 1)

        self.volume_HSlider = QSlider(self.groupBox_4)
        self.volume_HSlider.setObjectName(u"volume_HSlider")
        sizePolicy7.setHeightForWidth(self.volume_HSlider.sizePolicy().hasHeightForWidth())
        self.volume_HSlider.setSizePolicy(sizePolicy7)
        self.volume_HSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.volume_HSlider, 0, 1, 1, 1)

        self.speedLabel = QLabel(self.groupBox_4)
        self.speedLabel.setObjectName(u"speedLabel")
        sizePolicy8.setHeightForWidth(self.speedLabel.sizePolicy().hasHeightForWidth())
        self.speedLabel.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.speedLabel, 1, 0, 1, 1)

        self.speed_HSlider = QSlider(self.groupBox_4)
        self.speed_HSlider.setObjectName(u"speed_HSlider")
        sizePolicy7.setHeightForWidth(self.speed_HSlider.sizePolicy().hasHeightForWidth())
        self.speed_HSlider.setSizePolicy(sizePolicy7)
        self.speed_HSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.speed_HSlider, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.image1Label_2 = QLabel(self.engine_tab)
        self.image1Label_2.setObjectName(u"image1Label_2")
        sizePolicy2.setHeightForWidth(self.image1Label_2.sizePolicy().hasHeightForWidth())
        self.image1Label_2.setSizePolicy(sizePolicy2)
        self.image1Label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.image1Label_2)

        self.groupBox = QGroupBox(self.engine_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.save_pB = QPushButton(self.groupBox)
        self.save_pB.setObjectName(u"save_pB")
        sizePolicy1.setHeightForWidth(self.save_pB.sizePolicy().hasHeightForWidth())
        self.save_pB.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.save_pB, 3, 0, 1, 1)

        self.normalize_audio_checkbox = QCheckBox(self.groupBox)
        self.normalize_audio_checkbox.setObjectName(u"normalize_audio_checkbox")

        self.gridLayout_3.addWidget(self.normalize_audio_checkbox, 2, 0, 1, 3)

        self.choice_formatLabel = QLabel(self.groupBox)
        self.choice_formatLabel.setObjectName(u"choice_formatLabel")

        self.gridLayout_3.addWidget(self.choice_formatLabel, 1, 0, 1, 2)

        self.choice_format_cB = QComboBox(self.groupBox)
        self.choice_format_cB.setObjectName(u"choice_format_cB")

        self.gridLayout_3.addWidget(self.choice_format_cB, 1, 2, 1, 1)

        self.sample_rate_cB = QComboBox(self.groupBox)
        self.sample_rate_cB.setObjectName(u"sample_rate_cB")

        self.gridLayout_3.addWidget(self.sample_rate_cB, 0, 2, 1, 1)

        self.sample_ratetLabel = QLabel(self.groupBox)
        self.sample_ratetLabel.setObjectName(u"sample_ratetLabel")

        self.gridLayout_3.addWidget(self.sample_ratetLabel, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupBox)

        self.contentLayout.addTab(self.engine_tab, "")
        self.feedback_tab = QWidget()
        self.feedback_tab.setObjectName(u"feedback_tab")
        self.gridLayout_4 = QGridLayout(self.feedback_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.grammarLabel = QLabel(self.feedback_tab)
        self.grammarLabel.setObjectName(u"grammarLabel")
        self.grammarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.grammarLabel, 0, 0, 1, 1)

        self.lang_cb = QComboBox(self.feedback_tab)
        self.lang_cb.setObjectName(u"lang_cb")

        self.gridLayout_4.addWidget(self.lang_cb, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.feedback_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.feedback_grammar_textBrowser = QTextBrowser(self.groupBox_2)
        self.feedback_grammar_textBrowser.setObjectName(u"feedback_grammar_textBrowser")
        sizePolicy3.setHeightForWidth(self.feedback_grammar_textBrowser.sizePolicy().hasHeightForWidth())
        self.feedback_grammar_textBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_14.addWidget(self.feedback_grammar_textBrowser)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.feedback_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.feedback_speaking_textBrowser = QTextBrowser(self.groupBox_3)
        self.feedback_speaking_textBrowser.setObjectName(u"feedback_speaking_textBrowser")
        sizePolicy3.setHeightForWidth(self.feedback_speaking_textBrowser.sizePolicy().hasHeightForWidth())
        self.feedback_speaking_textBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_13.addWidget(self.feedback_speaking_textBrowser)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.contentLayout.addTab(self.feedback_tab, "")
        self.translation_tab = QWidget()
        self.translation_tab.setObjectName(u"translation_tab")
        self.gridLayout_5 = QGridLayout(self.translation_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.translation_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 1, 2, 1, 1)

        self.trans_to_cB = QComboBox(self.translation_tab)
        self.trans_to_cB.setObjectName(u"trans_to_cB")

        self.gridLayout_5.addWidget(self.trans_to_cB, 1, 3, 1, 1)

        self.translator_textBrowser = QTextBrowser(self.translation_tab)
        self.translator_textBrowser.setObjectName(u"translator_textBrowser")

        self.gridLayout_5.addWidget(self.translator_textBrowser, 2, 0, 1, 4)

        self.score_label = QLabel(self.translation_tab)
        self.score_label.setObjectName(u"score_label")

        self.gridLayout_5.addWidget(self.score_label, 0, 0, 1, 2)

        self.label_3 = QLabel(self.translation_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)

        self.trans_from_cB = QComboBox(self.translation_tab)
        self.trans_from_cB.setObjectName(u"trans_from_cB")

        self.gridLayout_5.addWidget(self.trans_from_cB, 1, 1, 1, 1)

        self.contentLayout.addTab(self.translation_tab, "")

        self.horizontalLayout_2.addWidget(self.contentLayout)

        mainWindow.setCentralWidget(self.centralwidget_grid)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1342, 25))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        mainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionGuide)
        self.menuHelp.addAction(self.actionAboutSofware)
        self.menuSettings.addAction(self.actionPreferences)

        self.retranslateUi(mainWindow)
        self.left_panel_pB.toggled.connect(self.RightContainer_widget.setHidden)
        self.right_panel_pB.toggled.connect(self.contentLayout.setHidden)

        self.contentLayout.setCurrentIndex(0)
        self.engine_lang_cB.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.actionManualIntegrated.setText(QCoreApplication.translate("mainWindow", u"ManGuideual", None))
        self.actionGuide.setText(QCoreApplication.translate("mainWindow", u"Guide", None))
        self.actionAboutSofware.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.actionPreferences.setText(QCoreApplication.translate("mainWindow", u"Prefereneces...", None))
        self.actionTools.setText(QCoreApplication.translate("mainWindow", u"Tools", None))
        self.audioLabel.setText(QCoreApplication.translate("mainWindow", u"Historial records", None))
        self.rep_timeLabel.setText(QCoreApplication.translate("mainWindow", u"00:00", None))
        self.OptiongBox.setTitle(QCoreApplication.translate("mainWindow", u"OPTIONS ", None))
#if QT_CONFIG(tooltip)
        self.reload_audio_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Reload list", None))
#endif // QT_CONFIG(tooltip)
        self.reload_audio_pB.setText("")
#if QT_CONFIG(tooltip)
        self.check_pronounce_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Check pronuciation", None))
#endif // QT_CONFIG(tooltip)
        self.check_pronounce_pB.setText("")
#if QT_CONFIG(tooltip)
        self.play_pause_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Play & pause", None))
#endif // QT_CONFIG(tooltip)
        self.play_pause_pB.setText("")
#if QT_CONFIG(tooltip)
        self.rename_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Rename", None))
#endif // QT_CONFIG(tooltip)
        self.rename_pB.setText("")
#if QT_CONFIG(tooltip)
        self.delete_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.delete_pB.setText("")
#if QT_CONFIG(tooltip)
        self.transcibe_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Transcribe", None))
#endif // QT_CONFIG(tooltip)
        self.transcibe_pB.setText("")
#if QT_CONFIG(tooltip)
        self.left_panel_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Audio section", None))
#endif // QT_CONFIG(tooltip)
        self.left_panel_pB.setText("")
#if QT_CONFIG(tooltip)
        self.theme_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Switch themes", None))
#endif // QT_CONFIG(tooltip)
        self.theme_pB.setText("")
#if QT_CONFIG(tooltip)
        self.right_panel_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Engine & model settings", None))
#endif // QT_CONFIG(tooltip)
        self.right_panel_pB.setText("")
        self.writer_sw.setWindowTitle(QCoreApplication.translate("mainWindow", u"Writer", None))
#if QT_CONFIG(tooltip)
        self.copy_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.copy_pB.setText("")
#if QT_CONFIG(tooltip)
        self.cut_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Cut", None))
#endif // QT_CONFIG(tooltip)
        self.cut_pB.setText("")
#if QT_CONFIG(tooltip)
        self.paste_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Paste", None))
#endif // QT_CONFIG(tooltip)
        self.paste_pB.setText("")
#if QT_CONFIG(tooltip)
        self.undo_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Undo", None))
#endif // QT_CONFIG(tooltip)
        self.undo_pB.setText("")
#if QT_CONFIG(tooltip)
        self.redo_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Redo", None))
#endif // QT_CONFIG(tooltip)
        self.redo_pB.setText("")
#if QT_CONFIG(tooltip)
        self.export_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Export .txt", None))
#endif // QT_CONFIG(tooltip)
        self.export_pB.setText("")
#if QT_CONFIG(tooltip)
        self.upload_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Load .txt", None))
#endif // QT_CONFIG(tooltip)
        self.upload_pB.setText("")
#if QT_CONFIG(tooltip)
        self.clear_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Backspace", None))
#endif // QT_CONFIG(tooltip)
        self.clear_pB.setText("")
        self.writer_editText.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.counterLabel.setText(QCoreApplication.translate("mainWindow", u"0/5000", None))
#if QT_CONFIG(tooltip)
        self.Check_grammar_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Check grammar", None))
#endif // QT_CONFIG(tooltip)
        self.Check_grammar_pB.setText("")
#if QT_CONFIG(tooltip)
        self.translate_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Translate", None))
#endif // QT_CONFIG(tooltip)
        self.translate_pB.setText("")
#if QT_CONFIG(tooltip)
        self.read_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Read with TTS", None))
#endif // QT_CONFIG(tooltip)
        self.read_pB.setText("")
#if QT_CONFIG(tooltip)
        self.record_pause_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Start & pause recording", None))
#endif // QT_CONFIG(tooltip)
        self.record_pause_pB.setText("")
#if QT_CONFIG(tooltip)
        self.stop_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Stop recording", None))
#endif // QT_CONFIG(tooltip)
        self.stop_pB.setText("")
        self.Reader.setWindowTitle(QCoreApplication.translate("mainWindow", u"Reader", None))
        self.open_book_pB.setText(QCoreApplication.translate("mainWindow", u"Open a book (PDF)", None))
        self.toggle_reader_mode_pB.setText("")
        self.audio_settings_gB.setTitle(QCoreApplication.translate("mainWindow", u"Choice a TSS engine and a voice", None))
        self.voiceLabel.setText(QCoreApplication.translate("mainWindow", u"Voice ", None))
#if QT_CONFIG(tooltip)
        self.about_engines_pB.setToolTip(QCoreApplication.translate("mainWindow", u"About the engine", None))
#endif // QT_CONFIG(tooltip)
        self.about_engines_pB.setText("")
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.preview_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Voice preview", None))
#endif // QT_CONFIG(tooltip)
        self.preview_pB.setText("")
        self.languageLabel.setText(QCoreApplication.translate("mainWindow", u"Language", None))
        self.engineLabel.setText(QCoreApplication.translate("mainWindow", u"Engine", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("mainWindow", u"Settings", None))
        self.volumeLabel.setText(QCoreApplication.translate("mainWindow", u"Volume", None))
        self.speedLabel.setText(QCoreApplication.translate("mainWindow", u"Speed", None))
        self.image1Label_2.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Output", None))
#if QT_CONFIG(tooltip)
        self.save_pB.setToolTip(QCoreApplication.translate("mainWindow", u"Save TTS audio", None))
#endif // QT_CONFIG(tooltip)
        self.save_pB.setText("")
        self.normalize_audio_checkbox.setText(QCoreApplication.translate("mainWindow", u"Normalize Audio", None))
        self.choice_formatLabel.setText(QCoreApplication.translate("mainWindow", u"Output format", None))
        self.sample_ratetLabel.setText(QCoreApplication.translate("mainWindow", u"Sample Rate", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.engine_tab), QCoreApplication.translate("mainWindow", u"Engines", None))
        self.grammarLabel.setText(QCoreApplication.translate("mainWindow", u"Language", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Grammar Checker", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"QUALIFICATION:", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.feedback_tab), QCoreApplication.translate("mainWindow", u"Feedbacks", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"to", None))
        self.score_label.setText(QCoreApplication.translate("mainWindow", u"Translation", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"From", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.translation_tab), QCoreApplication.translate("mainWindow", u"Translations", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("mainWindow", u"Settings", None))
    # retranslateUi

