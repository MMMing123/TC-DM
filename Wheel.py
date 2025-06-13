# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wheel.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 680)
        icon = QIcon()
        icon.addFile(u"images/Wheel.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, 0, -1)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.widget_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.radioButton_1 = QRadioButton(self.widget_2)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setFont(font1)
        self.radioButton_1.setIconSize(QSize(16, 20))

        self.horizontalLayout_2.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.widget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.g1 = QGroupBox(self.widget_2)
        self.g1.setObjectName(u"g1")
        self.g1.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.g1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.g1)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pre_x = QLabel(self.g1)
        self.pre_x.setObjectName(u"pre_x")
        font3 = QFont()
        font3.setPointSize(16)
        self.pre_x.setFont(font3)
        self.pre_x.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_4.addWidget(self.pre_x)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.g1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.pre_y = QLabel(self.g1)
        self.pre_y.setObjectName(u"pre_y")
        self.pre_y.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pre_y)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addWidget(self.g1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.now_x = QLabel(self.groupBox)
        self.now_x.setObjectName(u"now_x")
        self.now_x.setFont(font3)

        self.horizontalLayout_8.addWidget(self.now_x)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.now_y = QLabel(self.groupBox)
        self.now_y.setObjectName(u"now_y")
        self.now_y.setFont(font3)

        self.horizontalLayout_7.addWidget(self.now_y)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 5, 0, 10)
        self.save_button = QPushButton(self.groupBox)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(0, 45))
        self.save_button.setMaximumSize(QSize(100, 16777215))
        self.save_button.setIconSize(QSize(20, 200))

        self.horizontalLayout_10.addWidget(self.save_button)

        self.Cancel_button = QPushButton(self.groupBox)
        self.Cancel_button.setObjectName(u"Cancel_button")
        self.Cancel_button.setMinimumSize(QSize(50, 45))
        self.Cancel_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.Cancel_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_7.setStretch(0, 3)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 3)
        self.verticalLayout_7.setStretch(3, 3)
        self.verticalLayout_7.setStretch(4, 3)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 5)

        self.horizontalLayout_11.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Steering wheel calibration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">drive vehicles\uff1a</span></p></body></html>", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"left-hand", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"right-hand", None))
        self.g1.setTitle(QCoreApplication.translate("MainWindow", u"Current steering wheel coordinates", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.pre_x.setText(QCoreApplication.translate("MainWindow", u"224", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.pre_y.setText(QCoreApplication.translate("MainWindow", u"226", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Recalibrate steering wheel coordinates", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.now_x.setText(QCoreApplication.translate("MainWindow", u"none", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.now_y.setText(QCoreApplication.translate("MainWindow", u"none", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

