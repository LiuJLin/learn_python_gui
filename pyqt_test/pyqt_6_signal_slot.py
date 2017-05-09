import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout,QApplication
from PyQt5.QtGui import QIcon


class adventure_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 900, 520)
        self.setWindowTitle('Adventure')
        self.setWindowIcon(QIcon("2.jpg"))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex1 = adventure_widget()
    #ex2 = adventure_widget()

    sys.exit(app.exec_())
