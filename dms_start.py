import os
import shutil
import time
import pandas as pd
from PIL.ImageQt import QPixmap
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QCloseEvent, Qt
from PySide6.QtWidgets import QApplication, QMainWindow,  QTableWidgetItem, QAbstractItemView, \
    QButtonGroup, QMessageBox, QFileDialog
from pyk4a import K4AException, PyK4A

from Threshold_setting_Window import Threshold_setting_Window
from Wheel_windows import Wheel_Window
from excel import update_Excel, read_Excel
from model_perdict import update,  draw_wheel, k4a
from DMS_mainwindows_copy import Ui_MainWindow


classification = ["Calling","Back","Drinking","Eating","Get","Operate","Phone","Pick","Smoking",
                  "Take","Forward", "Normal", "No Person Detected"]

# Last displayed and saved to Excel index
red_index = 0
excel_index = 77
kinect_isopen = 0

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## Create child windows
        self.subwindows_wheel = Wheel_Window()
        self.Threshold_setting = Threshold_setting_Window()

        self.pushButton_8.clicked.connect(self.closec)

        # Excel timer
        self.excel_timer = QTimer()
        self.excel_timer.timeout.connect(self.excel_reset)
        self.excel_timer.start(10000) # Clear last saved to Excel every 10s

        # Initialize table settings
        self.tableSet()
        # Initialize status bar settings
        self.statusBarSet()
        # RadioButton group settings
        self.RadioButtonSet()
        ## Camera internal parameter display settings
        with open('Resources/Camera_internal_reference.txt', 'r') as file:
            i = 0
            lines = file.readlines()
            for line in lines:
                if (i == 0):
                    cx = float(line.strip())
                elif (i == 1):
                    cy = float(line.strip())
                elif (i == 2):
                    fx = float(line.strip())
                elif (i == 3):
                    fy = float(line.strip())
                i = i + 1
            self.cx.setText(str(cx))
            self.cy.setText(str(cy))
            self.fx.setText(str(fx))
            self.fy.setText(str(fy))

        self.wheel_button.clicked.connect(lambda : self.subwindows_wheel.show())

        ## Create timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.loadModel)
        self.pushButton_camera.clicked.connect(self.Start_tof)

        ## Camera parameter modification
        self.Camera_Save.clicked.connect(self.Camera_Internal_Save)
        self.Camera_Reset.clicked.connect(self.Camera_Internal_reset)

        # Export Excel settings
        self.source_excel = "Resources/dms.xlsx"
        self.pushButton_5.clicked.connect(self.export_excel)

    def tableSet(self):
        # 0. Read Excel table
        df = read_Excel()
        # Add serial number column (starting from 1, as the first column)
        df.insert(0, "序号", range(1, len(df) + 1))

        # 1. Set number of rows/columns
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        # 2. Set column headers
        self.tableWidget.setHorizontalHeaderLabels(['Number', 'Type', 'Confidence', 'Time', '3D camera coordinates'])
        # 3. Set table items by traversing
        for i in range(df.shape[0]):  # Rows
            for j in range(df.shape[1]):  # Columns
                # Get cell data and convert to string, handle empty values
                cell_value = df.iloc[i, j]
                display_text = str(cell_value) if not pd.isna(cell_value) else ""
                item = QTableWidgetItem(display_text)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.setAlternatingRowColors(True)  # Alternate row colors
        self.tableWidget.verticalHeader().setVisible(False)  # Hide vertical headers
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # Last column auto-fills container
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # Disable cell editing
        self.tableWidget.setColumnWidth(0, 60)  # Set first column width
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)

    def statusBarSet(self):
        self.action_2.triggered.connect(lambda : self.Threshold_setting.show())

    def excel_reset(self):
        global excel_index
        excel_index = 77

    def RadioButtonSet(self):
        group1 = QButtonGroup(self)
        group1.addButton(self.radioButton)
        group1.addButton(self.radioButton_2)

        group2 = QButtonGroup(self)
        group2.addButton(self.radioButton_3)
        group2.addButton(self.radioButton_4)

        self.radioButton.setChecked(True)
        self.radioButton_4.setChecked(True)

    def Camera_Internal_Save(self):
        reply = QMessageBox.question(
            self,
            'Confirm Save',
            'Are you sure you want to save the camera parameters?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        with open('Resources/Camera_internal_reference.txt', 'w', encoding='utf-8') as file:
            cx = self.cx.text()
            cy = self.cy.text()
            fx = self.fx.text()
            fy = self.fy.text()
            file.write(f"{cx}\n")
            file.write(f"{cy}\n")
            file.write(f"{fx}\n")
            file.write(f"{fy}\n")

        self.cx.setText(str(cx))
        self.cy.setText(str(cy))
        self.fx.setText(str(fx))
        self.fy.setText(str(fy))

    ## Reset camera parameters: reset to defaults without saving
    def Camera_Internal_reset(self):
        reply = QMessageBox.question(
            self,
            'Confirm Reset',
            'Are you sure you want to reset the camera parameters?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return
        ## 1. Read default camera parameters from txt
        with open('Resources/Camera_internal_reference.txt', 'r', encoding='utf-8') as file:
            i = 0
            lines = file.readlines()
            for line in lines:
                if (i == 0):
                    cx = float(line.strip())
                elif (i == 1):
                    cy = float(line.strip())
                elif (i == 2):
                    fx = float(line.strip())
                elif (i == 3):
                    fy = float(line.strip())
                i = i + 1

        ## 2. Update text display
        self.cx.setText(str(cx))
        self.cy.setText(str(cy))
        self.fx.setText(str(fx))
        self.fy.setText(str(fy))

    def loadModel(self):
        ## Start timer
        self.timer.start()

        global excel_index,red_index
        ## Initialize related variables
        QLabel_Confidence = [self.call, self.dive, self.drinking, self.eating,
                             self.get, self.operate, self.mobile_use,self.pick,
                             self.smoking, self.take, self.tilt,self.Normal_driving]

        # NOTE: When importing functions from other files, global variables will only initialize once and enter the buffer

        try:
            if self.radioButton.isChecked():
                numpy_img, Confidence, Sort_Confidence, world_coords = update(Display=0)  # Get image and confidence values
            else:
                numpy_img, Confidence, Sort_Confidence, world_coords = update(Display=1)
        except K4AException as e:
            raise e

        numpy_img = draw_wheel(numpy_img) # Draw steering wheel

        if len(Confidence) != 0:  # Takes time to get confidence
            ## No person detected
            if Confidence[-1][1] == 1:
                print("Driver not detected")
            else:
                for i in range(len(Confidence)-1):
                    QLabel_Confidence[i].setText(f"{Confidence[i][1]:.2f}")
                    QLabel_Confidence[red_index].setStyleSheet("color: black;")  # Revert last red label to black

                    QLabel_Confidence[int(Sort_Confidence[0][0])].setStyleSheet("color: red;")  # Highlight highest confidence in red
                    red_index = int(Sort_Confidence[0][0])  # Remember this red index
                    self.model_result.setText(f"{classification[red_index]}" + f"({Confidence[red_index][1]:.2f})")  # Set final result
                    font = self.model_result.font()
                    font.setPointSize(20)
                    self.model_result.setFont(font)
                    if Sort_Confidence[0][0] == 11:
                        self.model_result.setStyleSheet("color: black;")
                        pixmap = QPixmap("images/Safe.png")
                        self.label_2.setPixmap(pixmap)

                    else:
                        self.model_result.setStyleSheet("color: red;")  # Set final result in red
                        pixmap = QPixmap("images/Dangerous.png")
                        self.label_2.setPixmap(pixmap)

            ## Excel operations
            if(Sort_Confidence[0][0] != 6 and self.radioButton_3.isChecked()):
                if(excel_index != Sort_Confidence[0][0] and Sort_Confidence[0][0] != 11
                    and Sort_Confidence[0][0] != 12): # Prevent duplicate updates
                    Cur_Classification =  str(classification[Sort_Confidence[0][0]]) # Classification string

                    # Confidence value
                    Sort_Confidence = [list(item) for item in Sort_Confidence] # Convert each tuple to list
                    Sort_Confidence[0][1] = round(Sort_Confidence[0][1], 2) # Keep two decimals
                    Cur_Confidence = str(Sort_Confidence[0][1])

                    # Time
                    timestamp = time.time()
                    local_time = time.localtime(timestamp)
                    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time) # Format as string
                    Cur_Time = formatted_time

                    rounded_list = [[round(num, 2) for num in sublist] for sublist in world_coords]
                    Cur_World_coords = str(rounded_list)
                    data = [Cur_Classification,Cur_Confidence,Cur_Time,Cur_World_coords]
                    update_Excel(data)
                    excel_index = Sort_Confidence[0][0]  # Update last saved index
                    self.tableSet()

        height, width, channel = numpy_img.shape
        bytes_per_line = channel * width
        pixmap = QImage(numpy_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap(pixmap)  # Convert QImage to QPixmap
        scaled_pixmap = pixmap.scaled(
            self.Depth.size(),
            Qt.AspectRatioMode.KeepAspectRatio,  # Maintain aspect ratio
            Qt.TransformationMode.FastTransformation  # Disable smoothing to reduce blur
        )
       # self.Depth.setScaledContents(True) # Enable image scaling to fit label
        self.Depth.setPixmap(scaled_pixmap)

    # Override window close method
    def closeEvent(self, event: QCloseEvent):
        # Create confirmation dialog
        reply = QMessageBox.question(
            self,
            'Confirm exit',
            'Are you sure you want to exit the program?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Execute custom operations before closing (e.g. save data)
            print("Closing program...")
            # Call parent method to ensure normal shutdown
            super().closeEvent(event)
        else:
            # Ignore close event to keep window open
            event.ignore()

    # Export Excel
    def export_excel(self):
        # Check if source file exists
        if not os.path.exists(self.source_excel):
            QMessageBox.critical(self, "Error", "The original Excel file does not exist!")
            return

        # Get save path
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Excel file",
            os.path.basename(self.source_excel),  # Use original filename by default
            "Excel Files (*.xlsx *.xls);;All Files (*)"
        )

        if not file_path:
            return

        try:
            # Copy file
            shutil.copyfile(self.source_excel, file_path)
            QMessageBox.information(self, "Success", f"File exported to:\n{file_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Export failed:\n{str(e)}")

    def Start_tof(self):
        global  kinect_isopen
        if kinect_isopen == 0:
            if not self.is_kinect_connected():
                # Create error dialog
                error_dialog = QMessageBox(parent=self)
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Device not connected")
                error_dialog.setText("Kinect not detected")
                error_dialog.setInformativeText("Please check device connection and try again")
                # Add OK button
                error_dialog.addButton(QMessageBox.StandardButton.Ok)
                # Show dialog modally (blocking)
                error_dialog.exec()
            else:
                self.loadModel()
                kinect_isopen = 1

    def is_kinect_connected(self):
        try:
            k4a = PyK4A(device_id=0)
            k4a.start()  # Manually start device
            k4a.stop()  # Manually stop device
            return True
        except Exception as e:
            return False

    def closec(self):
        global kinect_isopen
        if kinect_isopen == 1:
            kinect_isopen = 0
            self.timer.stop()
            pixmap = QPixmap("images/TOF.png")
            self.Depth.setScaledContents(True)  # Enable image scaling to fit label
            self.Depth.setPixmap(pixmap)
            k4a.stop()


if __name__ == '__main__':
    app = QApplication([])
    windows = MyWindow()
    windows.show()
    app.exec()