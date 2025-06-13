# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DMS_mainwindows_copy.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 892)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"images/Driver.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Depth = QLabel(self.groupBox_3)
        self.Depth.setObjectName(u"Depth")
        self.Depth.setPixmap(QPixmap(u"images/TOF.png"))
        self.Depth.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.Depth)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_12 = QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(20)
        self.label_7.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_7)

        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.verticalLayout_3.setStretch(0, 13)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 10)

        self.verticalLayout_9.addWidget(self.widget_3)

        self.verticalLayout_9.setStretch(0, 10)

        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, -1, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 9)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"images/Safe.png"))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(24)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.model_result = QLabel(self.groupBox)
        self.model_result.setObjectName(u"model_result")
        self.model_result.setMinimumSize(QSize(190, 0))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.model_result.setFont(font3)
        self.model_result.setScaledContents(True)

        self.horizontalLayout.addWidget(self.model_result)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_53 = QLabel(self.groupBox)
        self.label_53.setObjectName(u"label_53")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(18)
        self.label_53.setFont(font4)
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_53, 2, 0, 1, 1)

        self.pick = QLabel(self.groupBox)
        self.pick.setObjectName(u"pick")
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(26)
        self.pick.setFont(font5)

        self.gridLayout_5.addWidget(self.pick, 5, 3, 1, 1)

        self.label_42 = QLabel(self.groupBox)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font4)
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_42, 3, 0, 1, 1)

        self.eating = QLabel(self.groupBox)
        self.eating.setObjectName(u"eating")
        self.eating.setFont(font5)

        self.gridLayout_5.addWidget(self.eating, 4, 3, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font4)
        self.label2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label2, 1, 2, 1, 1)

        self.operate = QLabel(self.groupBox)
        self.operate.setObjectName(u"operate")
        self.operate.setFont(font5)

        self.gridLayout_5.addWidget(self.operate, 1, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font4)
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_35, 3, 2, 1, 1)

        self.take = QLabel(self.groupBox)
        self.take.setObjectName(u"take")
        self.take.setFont(font5)

        self.gridLayout_5.addWidget(self.take, 3, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font4)
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_40, 0, 2, 1, 1)

        self.smoking = QLabel(self.groupBox)
        self.smoking.setObjectName(u"smoking")
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(28)
        self.smoking.setFont(font6)

        self.gridLayout_5.addWidget(self.smoking, 4, 1, 1, 1)

        self.label_54 = QLabel(self.groupBox)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font4)
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_54, 4, 2, 1, 1)

        self.get = QLabel(self.groupBox)
        self.get.setObjectName(u"get")
        self.get.setFont(font5)

        self.gridLayout_5.addWidget(self.get, 3, 3, 1, 1)

        self.call = QLabel(self.groupBox)
        self.call.setObjectName(u"call")
        self.call.setFont(font5)

        self.gridLayout_5.addWidget(self.call, 5, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font4)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_43, 5, 0, 1, 1)

        self.dive = QLabel(self.groupBox)
        self.dive.setObjectName(u"dive")
        self.dive.setFont(font5)

        self.gridLayout_5.addWidget(self.dive, 1, 3, 1, 1)

        self.tilt = QLabel(self.groupBox)
        self.tilt.setObjectName(u"tilt")
        self.tilt.setFont(font5)

        self.gridLayout_5.addWidget(self.tilt, 2, 1, 1, 1)

        self.mobile_use = QLabel(self.groupBox)
        self.mobile_use.setObjectName(u"mobile_use")
        self.mobile_use.setFont(font5)

        self.gridLayout_5.addWidget(self.mobile_use, 0, 3, 1, 1)

        self.drinking = QLabel(self.groupBox)
        self.drinking.setObjectName(u"drinking")
        self.drinking.setFont(font5)

        self.gridLayout_5.addWidget(self.drinking, 2, 3, 1, 1)

        self.Normal_driving = QLabel(self.groupBox)
        self.Normal_driving.setObjectName(u"Normal_driving")
        self.Normal_driving.setFont(font5)

        self.gridLayout_5.addWidget(self.Normal_driving, 0, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font4)
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_41, 4, 0, 1, 1)

        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font4)
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_52, 5, 2, 1, 1)

        self.label_39 = QLabel(self.groupBox)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font4)
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_39, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font7 = QFont()
        font7.setPointSize(14)
        self.groupBox_2.setFont(font7)
        self.groupBox_2.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, -1, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, -1, -1, -1)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        font8 = QFont()
        font8.setPointSize(16)
        self.label_9.setFont(font8)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font8)
        self.radioButton.setChecked(False)

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font8)

        self.horizontalLayout_5.addWidget(self.radioButton_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font8)
        self.radioButton_3.setChecked(False)

        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font8)
        self.radioButton_4.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_4.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButton_4)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_7 = QWidget(self.groupBox_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(25, -1, -1, 0)
        self.pushButton_8 = QPushButton(self.widget_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(180, 100))
        icon1 = QIcon()
        icon1.addFile(u"images/Camera_Off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.widget_7, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.groupBox_2)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(35, -1, 50, 0)
        self.pushButton_5 = QPushButton(self.widget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(140, 100))
        icon2 = QIcon()
        icon2.addFile(u"images/EXCEL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon2)

        self.horizontalLayout_15.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.widget_8, 1, 1, 1, 1)

        self.widget_5 = QWidget(self.groupBox_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, 5, -1, 0)
        self.pushButton_camera = QPushButton(self.widget_5)
        self.pushButton_camera.setObjectName(u"pushButton_camera")
        self.pushButton_camera.setMinimumSize(QSize(0, 50))
        self.pushButton_camera.setMaximumSize(QSize(180, 100))
        icon3 = QIcon()
        icon3.addFile(u"images/Camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_camera.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.pushButton_camera)


        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.groupBox_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(35, 9, 50, 0)
        self.wheel_button = QPushButton(self.widget_6)
        self.wheel_button.setObjectName(u"wheel_button")
        self.wheel_button.setMaximumSize(QSize(140, 100))
        icon4 = QIcon()
        icon4.addFile(u"images/Wheel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wheel_button.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.wheel_button)


        self.gridLayout.addWidget(self.widget_6, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.cx = QLineEdit(self.groupBox_2)
        self.cx.setObjectName(u"cx")
        font9 = QFont()
        font9.setPointSize(10)
        self.cx.setFont(font9)

        self.horizontalLayout_7.addWidget(self.cx)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font9)
        self.label.setTextFormat(Qt.PlainText)

        self.horizontalLayout_7.addWidget(self.label)

        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.cy = QLineEdit(self.groupBox_2)
        self.cy.setObjectName(u"cy")
        self.cy.setFont(font9)

        self.horizontalLayout_8.addWidget(self.cy)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.fx = QLineEdit(self.groupBox_2)
        self.fx.setObjectName(u"fx")
        self.fx.setFont(font9)

        self.horizontalLayout_9.addWidget(self.fx)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font9)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.fy = QLineEdit(self.groupBox_2)
        self.fy.setObjectName(u"fy")
        self.fy.setFont(font9)

        self.horizontalLayout_10.addWidget(self.fy)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font9)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 15, -1, 15)
        self.Camera_Save = QPushButton(self.widget)
        self.Camera_Save.setObjectName(u"Camera_Save")
        self.Camera_Save.setMaximumSize(QSize(80, 70))
        icon5 = QIcon()
        icon5.addFile(u"images/Save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_Save.setIcon(icon5)

        self.verticalLayout_10.addWidget(self.Camera_Save)


        self.verticalLayout_8.addWidget(self.widget)

        self.widget_4 = QWidget(self.groupBox_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 15, -1, 15)
        self.Camera_Reset = QPushButton(self.widget_4)
        self.Camera_Reset.setObjectName(u"Camera_Reset")
        self.Camera_Reset.setMaximumSize(QSize(80, 100))
        icon6 = QIcon()
        icon6.addFile(u"images/Reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_Reset.setIcon(icon6)

        self.verticalLayout_11.addWidget(self.Camera_Reset)


        self.verticalLayout_8.addWidget(self.widget_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_8)

        self.horizontalLayout_12.setStretch(0, 6)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 6)
        self.verticalLayout_7.setStretch(3, 6)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 30)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 2)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1008, 22))
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.action_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TC-DMS", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u6a21\u578b", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"Backward tilt and forward tilt threshold Settings", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Display window:", None))
        self.Depth.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">Depth</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Store information:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Detection results:", None))
        self.label_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Current type\uff1a</span></p></body></html>", None))
        self.model_result.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Normal(1.00)</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Forward\uff1a</p></body></html>", None))
        self.pick.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Take\uff1a</p></body></html>", None))
        self.eating.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Back\uff1a</p></body></html>", None))
        self.operate.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Get\uff1a</p></body></html>", None))
        self.take.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Phone\uff1a</p></body></html>", None))
        self.smoking.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eating\uff1a</p></body></html>", None))
        self.get.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.call.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Operate\uff1a</p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calling\uff1a</p></body></html>", None))
        self.dive.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.tilt.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.mobile_use.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.drinking.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.Normal_driving.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Smoking\uff1a</p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Normal\uff1a</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pick\uff1a</p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Drinking\uff1a</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Related operations:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Display form:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Depth+Skeleton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Skeleton", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Store information:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u200b\u200bTurn off camera\u200b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Export EXCEL", None))
        self.pushButton_camera.setText(QCoreApplication.translate("MainWindow", u"Open camera", None))
        self.wheel_button.setText(QCoreApplication.translate("MainWindow", u"SWC ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cx:", None))
        self.cx.setText(QCoreApplication.translate("MainWindow", u"318.5131530761719", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cy:", None))
        self.cy.setText(QCoreApplication.translate("MainWindow", u"338.0367431640625", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fx:", None))
        self.fx.setText(QCoreApplication.translate("MainWindow", u"504.7893371582031", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Fy:", None))
        self.fy.setText(QCoreApplication.translate("MainWindow", u"504.9712829589844", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))
        self.Camera_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Camera_Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

