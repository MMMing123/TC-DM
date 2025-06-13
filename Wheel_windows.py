import gc
import sys
import matplotlib
import numpy as np
from Wheel import Ui_MainWindow
from model_perdict import org_depth, draw_wheel

matplotlib.use('QtAgg')

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PySide6.QtCore import Signal, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt


class MplCanvas(FigureCanvasQTAgg):

    mouse_moved = Signal(float, float, np.ndarray)
    mouse_click = Signal(float, float, np.ndarray)

    def __init__(self):
        # Adjust figure size and DPI
        super().__init__(plt.Figure(figsize=(5, 4), dpi=100))
        self.axes = self.figure.add_subplot(111)
        self.axes.set_aspect('auto')  # Prevent aspect ratio calculation issues

        # Initialize image
        img, self.org_img = org_depth()
        self.image = self.axes.imshow(img, aspect='auto')  # Fixed image aspect ratio

        # Timer settings
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateImg)
        self.timer.start(100)

        ## Connect mouse events
        self.mpl_connect('motion_notify_event', self.on_mouse_move)  # Mouse movement
        self.mpl_connect('button_press_event', self.on_mouse_click)  # Mouse click


    def on_mouse_move(self, event):
        if event.inaxes:
            self.mouse_moved.emit(event.xdata, event.ydata, self.org_img)
        else:
            self.mouse_moved.emit(None, None, None)

    def on_mouse_click(self, event):
        if event.inaxes:
            self.mouse_click.emit(event.xdata, event.ydata, self.org_img)
        else:
            self.mouse_click.emit(None, None, None)


    def updateImg(self):
        try:
            img, self.org_img = org_depth()
            img = draw_wheel(img)
            self.image.set_data(img)
            self.image.autoscale()
            self.draw_idle()  # Use non-blocking drawing
        except ValueError as e:
            print(f"Drawing error handled: {e}")


class Wheel_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.original_x = None
        self.original_y = None
        self.original_position = None
        self.setupUi(self)


    def update_status_bar(self, x, y, org_img):
        if x is not None and y is not None and x != 0 and y != 0:
            int_x = int(x)
            int_y = int(y)
            depth = org_img[int_y][int_x]
            self.statusBar().showMessage(f"X: {x:.2f}, Y: {y:.2f}, D:{depth}")
        else:
            self.statusBar().clearMessage()

    def update_xyz(self, x, y, org_img):
        if x is not None and y is not None and x != 0 and y != 0:
            int_x = int(x)
            int_y = int(y)
            x = round(x, 2)
            y = round(y, 2)
            depth = org_img[int_y][int_x]
            self.now_x.setText(str(x))
            self.now_y.setText(str(y))
            # self.now_z.setText(str(depth))

    def wheel_xyz_Driving_position(self):
        with open('Resources/wheel.txt', 'r') as file:
            ## 0 is a left-hand drive vehicle and 1 is a right-hand drive vehicle
            self.x, self.y, self.Driving_position = 0, 0, 0
            i = 0
            lines = file.readlines()
            for line in lines:
                if (i == 0):
                    self.x = float(line.strip())
                elif (i == 1):
                    self.y = float(line.strip())
                elif (i == 2):
                    self.Driving_position = float(line.strip())
                i = i + 1

    # Save XYZ coordinates
    def save_xyz(self):
        with open('Resources/wheel.txt', 'w', encoding='utf-8') as file:
            save_x = self.now_x.text()
            save_y = self.now_y.text()
            if save_x == "none" or save_y == "none":
                file.write(f"{self.x}\n")
                file.write(f"{self.y}\n")
            else:
                file.write(f"{save_x}\n")
                file.write(f"{save_y}\n")
            if self.radioButton_1.isChecked():
                file.write(f"0")
                self.radioButton_1.setChecked(True)
            else:
                file.write(f"1")
        self.pre_x.setText(str(save_x))
        self.pre_y.setText(str(save_y))

    def bind(self):
        self.pre_x.setText(str(self.x))
        self.pre_y.setText(str(self.y))
        if self.Driving_position == 0:
            self.radioButton_1.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)


        try:
            self.save_button.clicked.disconnect()
        except RuntimeError:
            pass

        self.save_button.clicked.connect(self.confirm_save)

        # 绑定重置按钮
        try:
            self.Cancel_button.clicked.disconnect()
        except RuntimeError:
            pass
        self.Cancel_button.clicked.connect(self.reset_xyz)

    def confirm_save(self):
        confirm_box = QMessageBox(self)
        confirm_box.setWindowTitle("Confirm and save")
        confirm_box.setText("Are you sure you want to overwrite the original coordinate data?")
        confirm_box.setIcon(QMessageBox.Question)
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        answer = confirm_box.exec()

        if answer == QMessageBox.Yes:

            self.save_xyz()

            QMessageBox.information(self, "Save successful", "Coordinate data updated!")

    def reset_xyz(self):

        self.now_x.setText(str(self.original_x))
        self.now_y.setText(str(self.original_y))


        if self.original_position == 0:
            self.radioButton_1.setChecked(True)
        else:
            self.radioButton_2.setChecked(False)


        self.pre_x.setText(str(self.original_x))
        self.pre_y.setText(str(self.original_y))

        QMessageBox.information(self, "Reset successful", "Coordinates have been reset to their original saved values!")

    def showEvent(self, event):
        super().showEvent(event)
        self.canvas = MplCanvas()
        ## Connect signals to window functions
        self.canvas.mouse_moved.connect(self.update_status_bar)  # Bind to status bar update
        self.canvas.mouse_click.connect(self.update_xyz)  # Bind to coordinate update

        self.verticalLayout_5.addWidget(self.canvas)
        self.statusBar().show()

        # Load stored steering wheel coordinates
        self.wheel_xyz_Driving_position()


        self.original_x = self.x
        self.original_y = self.y
        self.original_position = self.Driving_position

        # Setup event bindings
        self.bind()

    def closeEvent(self, event):
        super().closeEvent(event)
        # Stop timer
        self.canvas.timer.stop()
        # Clear canvas content
        self.canvas.axes.clear()
        self.canvas.figure.clf()
        plt.close(self.canvas.figure)
        # Remove and delete canvas from layout
        self.verticalLayout_5.removeWidget(self.canvas)
        self.canvas.deleteLater()
        # Release related resources
        del self.canvas
        gc.collect()