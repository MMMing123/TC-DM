# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Threshold_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(509, 414)
        icon = QIcon()
        icon.addFile(u"images/Set.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 120, 394, 166))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Distance_Line = QLineEdit(self.widget)
        self.Distance_Line.setObjectName(u"Distance_Line")
        self.Distance_Line.setMinimumSize(QSize(0, 30))
        self.Distance_Line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Distance_Line, 0, 1, 1, 1)

        self.Tilt_Line = QLineEdit(self.widget)
        self.Tilt_Line.setObjectName(u"Tilt_Line")
        self.Tilt_Line.setMinimumSize(QSize(0, 30))
        self.Tilt_Line.setMaximumSize(QSize(16777215, 16777215))
        self.Tilt_Line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Tilt_Line, 2, 1, 1, 1)

        self.Dive_Line = QLineEdit(self.widget)
        self.Dive_Line.setObjectName(u"Dive_Line")
        self.Dive_Line.setMinimumSize(QSize(0, 30))
        self.Dive_Line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Dive_Line, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_save = QPushButton(self.widget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 30))
        self.pushButton_save.setIconSize(QSize(10, 16))

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_reset = QPushButton(self.widget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.pushButton_reset)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Threshold setting", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Angle of leaning forward:</span></p></body></html>", None))
        self.Distance_Line.setText(QCoreApplication.translate("Form", u"0", None))
        self.Distance_Line.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.Tilt_Line.setText(QCoreApplication.translate("Form", u"15", None))
        self.Tilt_Line.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.Dive_Line.setText(QCoreApplication.translate("Form", u"15", None))
        self.Dive_Line.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">\u00b0</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Angle of leaning back:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">\u00b0</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Steering wheel distance\uff1a</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">pixel</span></p></body></html>", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"save", None))
        self.pushButton_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

