import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


class FontAdjusterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("adjuster.ui", self)

        self.setup_ui()
        self.setup_connections()
        self.set_default_values()

    def setup_ui(self):
        self.labelDisplay = self.findChild(QtWidgets.QLabel, "nim")
        self.labelFooter = self.findChild(QtWidgets.QLabel, "nama")

        self.sliderFontSize = self.findChild(QtWidgets.QSlider, "size")
        self.sliderFontColor = self.findChild(QtWidgets.QSlider, "color")
        self.sliderBackgroundColor = self.findChild(QtWidgets.QSlider, "bg")

        self.labelSizeValue = self.findChild(QtWidgets.QLabel, "sizeVal")
        self.labelColorValue = self.findChild(QtWidgets.QLabel, "colorVal")
        self.labelBgValue = self.findChild(QtWidgets.QLabel, "bgVal")

        self.btnReset = self.findChild(QtWidgets.QPushButton, "reset")

        self.labelDisplay.setAlignment(Qt.AlignCenter)
        self.labelDisplay.setAutoFillBackground(True)

        self.sliderFontSize.setRange(20, 60)
        self.sliderFontColor.setRange(0, 255)
        self.sliderBackgroundColor.setRange(0, 255)

    def setup_connections(self):
        self.sliderFontSize.valueChanged.connect(self.update_font_size)
        self.sliderFontColor.valueChanged.connect(self.update_colors)
        self.sliderBackgroundColor.valueChanged.connect(self.update_colors)
        self.btnReset.clicked.connect(self.reset_values)

    def set_default_values(self):
        self.sliderFontSize.setValue(40)
        self.sliderFontColor.setValue(0)
        self.sliderBackgroundColor.setValue(255)
        self.update_font_size()
        self.update_colors()

    def update_font_size(self):
        size = self.sliderFontSize.value()
        self.labelDisplay.setFont(QFont("Arial", size))
        self.labelSizeValue.setText(f"{size} pt")

    def update_colors(self):
        font_gray = self.sliderFontColor.value()
        bg_gray = self.sliderBackgroundColor.value()

        palette = self.labelDisplay.palette()
        palette.setColor(QPalette.WindowText, QColor(font_gray, font_gray, font_gray))
        palette.setColor(QPalette.Window, QColor(bg_gray, bg_gray, bg_gray))

        self.labelDisplay.setPalette(palette)

        self.labelColorValue.setText(str(font_gray))
        self.labelBgValue.setText(str(bg_gray))

    def reset_values(self):
        self.set_default_values()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FontAdjusterApp()
    window.setWindowTitle("Font Size and Color Adjuster")
    window.show()
    sys.exit(app.exec_())
