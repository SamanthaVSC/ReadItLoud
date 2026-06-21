"""
ReadItLoud — Desktop application for language learning through
reading documents with speech synthesis (TTS), pronunciation feedback
and integrated grammar correction.

Copyright (C) 2026 Samantha Alvarez Hechevarría

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Author: Samantha Alvarez Hechevarria
Contact: samanthadesktop324@gmail.com
GitHub: https://github.com/SamanthaVSC/ReadItLoud
"""

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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

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
        self.check_pronounce_pB = QPushButton(self.OptiongBox)
        self.check_pronounce_pB.setObjectName(u"check_pronounce_pB")

        self.verticalLayout_8.addWidget(self.check_pronounce_pB)

        self.reload_audio_pB = QPushButton(self.OptiongBox)
        self.reload_audio_pB.setObjectName(u"reload_audio_pB")

        self.verticalLayout_8.addWidget(self.reload_audio_pB)

        self.transcibe_pB = QPushButton(self.OptiongBox)
        self.transcibe_pB.setObjectName(u"transcibe_pB")

        self.verticalLayout_8.addWidget(self.transcibe_pB)

        self.play_pause_pB = QPushButton(self.OptiongBox)
        self.play_pause_pB.setObjectName(u"play_pause_pB")

        self.verticalLayout_8.addWidget(self.play_pause_pB)

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

        self.image1Label = QLabel(self.centralwidget_grid)
        self.image1Label.setObjectName(u"image1Label")

        self.centralwidget_pB_panels__hLayout.addWidget(self.image1Label)

        self.theme_pB = QPushButton(self.centralwidget_grid)
        self.theme_pB.setObjectName(u"theme_pB")
        sizePolicy1.setHeightForWidth(self.theme_pB.sizePolicy().hasHeightForWidth())
        self.theme_pB.setSizePolicy(sizePolicy1)
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

        self.counterLabel = QLabel(self.writerwidget)
        self.counterLabel.setObjectName(u"counterLabel")

        self.horizontalLayout_20.addWidget(self.counterLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_5)

        self.read_pB = QPushButton(self.writerwidget)
        self.read_pB.setObjectName(u"read_pB")

        self.horizontalLayout_21.addWidget(self.read_pB)

        self.Check_grammar_pB = QPushButton(self.writerwidget)
        self.Check_grammar_pB.setObjectName(u"Check_grammar_pB")

        self.horizontalLayout_21.addWidget(self.Check_grammar_pB)

        self.translate_pB = QPushButton(self.writerwidget)
        self.translate_pB.setObjectName(u"translate_pB")

        self.horizontalLayout_21.addWidget(self.translate_pB)

        self.record_pause_pB = QPushButton(self.writerwidget)
        self.record_pause_pB.setObjectName(u"record_pause_pB")
        sizePolicy1.setHeightForWidth(self.record_pause_pB.sizePolicy().hasHeightForWidth())
        self.record_pause_pB.setSizePolicy(sizePolicy1)
        self.record_pause_pB.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.record_pause_pB)

        self.stop_pB = QPushButton(self.writerwidget)
        self.stop_pB.setObjectName(u"stop_pB")

        self.horizontalLayout_21.addWidget(self.stop_pB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)


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

        self.verticalLayout_11.addWidget(self.mdiArea)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.contentLayout = QTabWidget(self.centralwidget_grid)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.contentLayout.sizePolicy().hasHeightForWidth())
        self.contentLayout.setSizePolicy(sizePolicy2)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.audio_settings_gB.sizePolicy().hasHeightForWidth())
        self.audio_settings_gB.setSizePolicy(sizePolicy6)
        self.verticalLayout_9 = QVBoxLayout(self.audio_settings_gB)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.engineLabel = QLabel(self.audio_settings_gB)
        self.engineLabel.setObjectName(u"engineLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.engineLabel.sizePolicy().hasHeightForWidth())
        self.engineLabel.setSizePolicy(sizePolicy7)
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
        self.voiceLabel = QLabel(self.audio_settings_gB)
        self.voiceLabel.setObjectName(u"voiceLabel")
        sizePolicy7.setHeightForWidth(self.voiceLabel.sizePolicy().hasHeightForWidth())
        self.voiceLabel.setSizePolicy(sizePolicy7)
        self.voiceLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_15.addWidget(self.voiceLabel)

        self.voice_cB = QComboBox(self.audio_settings_gB)
        self.voice_cB.setObjectName(u"voice_cB")
        sizePolicy1.setHeightForWidth(self.voice_cB.sizePolicy().hasHeightForWidth())
        self.voice_cB.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.voice_cB)

        self.preview_pB = QPushButton(self.audio_settings_gB)
        self.preview_pB.setObjectName(u"preview_pB")
        sizePolicy1.setHeightForWidth(self.preview_pB.sizePolicy().hasHeightForWidth())
        self.preview_pB.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.preview_pB)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addWidget(self.audio_settings_gB)

        self.image1Label_2 = QLabel(self.engine_tab)
        self.image1Label_2.setObjectName(u"image1Label_2")
        sizePolicy3.setHeightForWidth(self.image1Label_2.sizePolicy().hasHeightForWidth())
        self.image1Label_2.setSizePolicy(sizePolicy3)
        self.image1Label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.image1Label_2)

        self.groupBox = QGroupBox(self.engine_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sample_ratetLabel = QLabel(self.groupBox)
        self.sample_ratetLabel.setObjectName(u"sample_ratetLabel")

        self.horizontalLayout_12.addWidget(self.sample_ratetLabel)

        self.sample_rate_cb = QComboBox(self.groupBox)
        self.sample_rate_cb.setObjectName(u"sample_rate_cb")

        self.horizontalLayout_12.addWidget(self.sample_rate_cb)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.choice_formatLabel = QLabel(self.groupBox)
        self.choice_formatLabel.setObjectName(u"choice_formatLabel")

        self.horizontalLayout_11.addWidget(self.choice_formatLabel)

        self.choice_format_cb = QComboBox(self.groupBox)
        self.choice_format_cb.setObjectName(u"choice_format_cb")

        self.horizontalLayout_11.addWidget(self.choice_format_cb)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.normalize_audio_checkbox = QCheckBox(self.groupBox)
        self.normalize_audio_checkbox.setObjectName(u"normalize_audio_checkbox")

        self.verticalLayout_5.addWidget(self.normalize_audio_checkbox)


        self.verticalLayout.addWidget(self.groupBox)

        self.contentLayout.addTab(self.engine_tab, "")
        self.feedback_tab = QWidget()
        self.feedback_tab.setObjectName(u"feedback_tab")
        self.verticalLayout_7 = QVBoxLayout(self.feedback_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.feedback_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.grammarLabel = QLabel(self.groupBox_2)
        self.grammarLabel.setObjectName(u"grammarLabel")
        self.grammarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.grammarLabel)

        self.grammar_cb = QComboBox(self.groupBox_2)
        self.grammar_cb.setObjectName(u"grammar_cb")

        self.horizontalLayout_5.addWidget(self.grammar_cb)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_14.addWidget(self.textBrowser)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.label = QLabel(self.feedback_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.groupBox_3 = QGroupBox(self.feedback_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_checker_pB = QPushButton(self.groupBox_3)
        self.clear_checker_pB.setObjectName(u"clear_checker_pB")

        self.horizontalLayout_3.addWidget(self.clear_checker_pB)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.textEdit = QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_13.addWidget(self.textEdit)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.contentLayout.addTab(self.feedback_tab, "")
        self.translation_tab = QWidget()
        self.translation_tab.setObjectName(u"translation_tab")
        self.verticalLayout_6 = QVBoxLayout(self.translation_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.score_label = QLabel(self.translation_tab)
        self.score_label.setObjectName(u"score_label")

        self.verticalLayout_6.addWidget(self.score_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.translation_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.translation_tab)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_4 = QLabel(self.translation_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.translation_tab)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.textBrowser_2 = QTextBrowser(self.translation_tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_6.addWidget(self.textBrowser_2)

        self.contentLayout.addTab(self.translation_tab, "")

        self.horizontalLayout_8.addWidget(self.contentLayout)

        mainWindow.setCentralWidget(self.centralwidget_grid)

        self.retranslateUi(mainWindow)
        self.left_panel_pB.toggled.connect(self.RightContainer_widget.setHidden)
        self.right_panel_pB.toggled.connect(self.contentLayout.setHidden)

        self.contentLayout.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.audioLabel.setText(QCoreApplication.translate("mainWindow", u"Historial records", None))
        self.rep_timeLabel.setText(QCoreApplication.translate("mainWindow", u"00:00", None))
        self.OptiongBox.setTitle(QCoreApplication.translate("mainWindow", u"OPTIONS ", None))
        self.check_pronounce_pB.setText(QCoreApplication.translate("mainWindow", u"CHECK PRONOUNCE", None))
        self.reload_audio_pB.setText(QCoreApplication.translate("mainWindow", u"RELOAD", None))
        self.transcibe_pB.setText(QCoreApplication.translate("mainWindow", u"TRANCRIBE", None))
        self.play_pause_pB.setText(QCoreApplication.translate("mainWindow", u"PLAY/STOP", None))
        self.rename_pB.setText(QCoreApplication.translate("mainWindow", u"RENAME", None))
        self.delete_pB.setText(QCoreApplication.translate("mainWindow", u"DELETE", None))
        self.left_panel_pB.setText(QCoreApplication.translate("mainWindow", u"Audio", None))
        self.image1Label.setText("")
        self.theme_pB.setText(QCoreApplication.translate("mainWindow", u"theme", None))
        self.right_panel_pB.setText(QCoreApplication.translate("mainWindow", u"Tools", None))
        self.writer_sw.setWindowTitle(QCoreApplication.translate("mainWindow", u"WRITER", None))
        self.copy_pB.setText(QCoreApplication.translate("mainWindow", u"COPY", None))
        self.cut_pB.setText(QCoreApplication.translate("mainWindow", u"CUT", None))
        self.paste_pB.setText(QCoreApplication.translate("mainWindow", u"PASTE", None))
        self.undo_pB.setText(QCoreApplication.translate("mainWindow", u"UNDO", None))
        self.redo_pB.setText(QCoreApplication.translate("mainWindow", u"REDO", None))
        self.export_pB.setText(QCoreApplication.translate("mainWindow", u"EXPORT", None))
        self.upload_pB.setText(QCoreApplication.translate("mainWindow", u"UPLOAD", None))
        self.clear_pB.setText(QCoreApplication.translate("mainWindow", u"CLEAR", None))
        self.counterLabel.setText(QCoreApplication.translate("mainWindow", u"0/5000", None))
        self.read_pB.setText(QCoreApplication.translate("mainWindow", u"READ", None))
        self.Check_grammar_pB.setText(QCoreApplication.translate("mainWindow", u"CHECK GRAMMAR", None))
        self.translate_pB.setText(QCoreApplication.translate("mainWindow", u"TRANSLATE", None))
        self.record_pause_pB.setText(QCoreApplication.translate("mainWindow", u"RECORD/PAUSE", None))
        self.stop_pB.setText(QCoreApplication.translate("mainWindow", u"STOP", None))
        self.Reader.setWindowTitle(QCoreApplication.translate("mainWindow", u"READER", None))
        self.open_book_bP.setText(QCoreApplication.translate("mainWindow", u"Open a book (PDF)", None))
        self.audio_settings_gB.setTitle(QCoreApplication.translate("mainWindow", u"Choice a TSS engine and a voice", None))
        self.engineLabel.setText(QCoreApplication.translate("mainWindow", u"Engine", None))
        self.about_engineButton.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.voiceLabel.setText(QCoreApplication.translate("mainWindow", u"Voice", None))
        self.preview_pB.setText(QCoreApplication.translate("mainWindow", u"Preview", None))
        self.image1Label_2.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Output", None))
        self.sample_ratetLabel.setText(QCoreApplication.translate("mainWindow", u"Sample Rate", None))
        self.choice_formatLabel.setText(QCoreApplication.translate("mainWindow", u"Output format", None))
        self.normalize_audio_checkbox.setText(QCoreApplication.translate("mainWindow", u"Normalize Audio", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.engine_tab), QCoreApplication.translate("mainWindow", u"Engines", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Grammar Checker", None))
        self.grammarLabel.setText(QCoreApplication.translate("mainWindow", u"Language", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"QUALIFICATION:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"Expected text to ponunciation", None))
        self.clear_checker_pB.setText(QCoreApplication.translate("mainWindow", u"CLEAR", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"PASTE", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.feedback_tab), QCoreApplication.translate("mainWindow", u"Feedbacks", None))
        self.score_label.setText(QCoreApplication.translate("mainWindow", u"Translation", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"From", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"to", None))
        self.contentLayout.setTabText(self.contentLayout.indexOf(self.translation_tab), QCoreApplication.translate("mainWindow", u"Translations", None))
    # retranslateUi

