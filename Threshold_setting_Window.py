from PySide6.QtWidgets import QMainWindow, QMessageBox
from Threshold_setting import Ui_Form


class Threshold_setting_Window(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_reset.clicked.connect(self.reset)
        self.refresh()

    def save(self):
        reply = QMessageBox.question(self,
                                     "Confirmation",
                                     "Are you sure you want to save these settings?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        Steering_wheel_distance = self.Distance_Line.text()
        Dive_angle = self.Dive_Line.text()
        tilt_angle = self.Tilt_Line.text()
        with open('Resources/Threshold.txt', 'w', encoding='utf-8') as file:
            file.write(f"{Steering_wheel_distance}\n")
            file.write(f"{Dive_angle}\n")
            file.write(f"{tilt_angle}\n")
        self.refresh()

    def reset(self):
        reply = QMessageBox.question(self,
                                     "Confirmation",
                                     "Are you sure you want to reset to default values?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        with open('Resources/Threshold.txt', 'w', encoding='utf-8') as file:
            file.write(f"{0}\n")
            file.write(f"{15}\n")
            file.write(f"{15}\n")
        self.refresh()

    def refresh(self):
        with open('Resources/Threshold.txt', 'r', encoding='utf-8') as file:
            i = 0
            lines = file.readlines()
            for line in lines:
                if (i == 0):
                    wheel_Threshold = float(line.strip())
                elif (i == 1):
                    dive_value = float(line.strip())
                elif (i == 2):
                    tilt_value = float(line.strip())
                i = i + 1

        self.Distance_Line.setText(str(wheel_Threshold))
        self.Dive_Line.setText(str(dive_value))
        self.Tilt_Line.setText(str(tilt_value))