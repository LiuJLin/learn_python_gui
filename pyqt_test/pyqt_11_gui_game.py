import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer,QCoreApplication, QBasicTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QToolTip, QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QAction,qApp,QTextEdit, QLineEdit, QInputDialog,QHBoxLayout,QVBoxLayout,QGridLayout,QDialog)
from PyQt5.QtGui import QFont, QIcon, QColor, QFontMetrics, QPainter, QPalette
import pygame, sys, time, random
from pygame.locals import *
class Wiggly_Widget(QWidget):
    def __init__(self, parent=None):
        super(Wiggly_Widget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        #wiggly
        self.setBackgroundRole(QPalette.Midlight)
        self.setAutoFillBackground(True)

        newFont = self.font()
        newFont.setPointSize(newFont.pointSize() +50)
        self.setFont(newFont)

        self.timer = QBasicTimer()
        self.text = ''
        self.step = 0;
        self.timer.start(60, self)

    def paintEvent(self, event):
        sineTable = (0, 38, 71, 92, 100, 92, 71, 38, 0 , -38, -71, -92, -100, -92, -71, -38)
        metrics = QFontMetrics(self.font())
        x = (self.width() - metrics.width(self.text)) / 2
        y = (self.height() + metrics.ascent() - metrics.descent()) / 2
        color = QColor()

        painter = QPainter(self)
        for i, ch in enumerate(self.text):
            index = (self.step + i) %16
            color.setHsv((15-index) *16, 255, 191)
            painter.setPen(color)
            painter.drawText(x, y - ((sineTable[index] * metrics.height())/ 400), ch)
            x += metrics.width(ch)
    def setText(self, newText):
        self.text = newText

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            self.update()
        else:
            super(wiggly_widg, self).timerEvent(event)

class WidgetGift(QDialog):
    def __init__(self, parent=None):
        super(WidgetGift, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        QApplication.setPalette(QApplication.style().standardPalette()) #配色方案

        styleLabel = QLabel("526:")
        #styleLabel.setBuddy(styleComboBox)

        self.createBottomGroupBox()
        self.createMiddleGroupBox()
        # self.createProgressBar()

        #最上方top主题选择模块
        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        #topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        # topLayout.addWidget(self.useStylePaletteCheckBox)
        # topLayout.addWidget(disableWidgetsCheckBox)

        # 中间模块middle
        # wiggly_widget = Wiggly_Widget()
        # lineEdit = QLineEdit()
        #
        # middleLayout = QVBoxLayout()
        # middleLayout.addWidget(wiggly_widget)
        # middleLayout.addWidget(lineEdit)
        # #self.setLayout(middleLayout)
        #
        #
        # lineEdit.textChanged.connect(wiggly_widget.setText)
        # lineEdit.setText("Happy")
        # #self.setWindowTitle("Happy (wiggly)")
        # self.resize(900,520)

        # 主
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, )
        mainLayout.addWidget(self.middleGroupBox, 1, 0,)
        #mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomGroupBox, 2, 0)
        #mainLayout.addWidget(self.bottomGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        mainLayout.sizeHint()
        self.setLayout(mainLayout)

        self.setWindowTitle("Happy")
        #self.resize(1000,800)
        #self.changeStyle("Windows")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())


    def createMiddleGroupBox(self):
        self.middleGroupBox = QGroupBox("happy")
        self.middleGroupBox.setCheckable(True)
        self.middleGroupBox.setChecked(True)
        self.middleGroupBox.setFixedSize(800,200)
        wiggly_widget = Wiggly_Widget()
        lineEdit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(wiggly_widget)
        #layout.addWidget(lineEdit)
        self.middleGroupBox.setLayout(layout)


        lineEdit.textChanged.connect(wiggly_widget.setText)
        lineEdit.setText("Happy")
        # self.setWindowTitle("Happy (wiggly)")
        #self.middleGroupBox.sizePolicy()

    def createBottomGroupBox(self):
        self.bottomGroupBox = QGroupBox("Welcome")
        self.bottomGroupBox.setCheckable(True)
        self.bottomGroupBox.setChecked(True)

        lb1 = QLabel('Welcome',self)
        lb1.move(450, 30)
        lb1.setFont(QFont('Comic Sans MS',20))
        lb2 = QLabel('Wanna go on your adventure?',self)
        lb2.move(450, 70)
        lb2.setFont(QFont('Comic Sans MS',20))
        lb3 = QLabel('Please give me your password:',self)
        lb3.move(450, 110)
        lb3.setFont(QFont('Comic Sans MS',15))

        lineEditPassword = QLineEdit('')
        lineEditPassword.setEchoMode(QLineEdit.Password)

        okBtn = QPushButton('OK', self)
        #okBtn.setToolTip('Click me to <b>enter</b> the game!')
        okBtn.clicked.connect(self.check_password)
        okBtn.resize(okBtn.sizeHint())
        #okBtn.move(50,50)
        #clicked 点击触发事件
        quitBtn = QPushButton('Quit', self)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        #quitBtn.setToolTip('Click me to <b>Quit</b>')
        quitBtn.resize(quitBtn.sizeHint())

        layout = QGridLayout()
        layout.addWidget(lb1, 0, 0, 1, 3)
        layout.addWidget(lb2, 1, 0, 1, 3)
        layout.addWidget(lb3, 2, 0, 1, 3)
        layout.addWidget(lineEditPassword, 3, 0, 1, 3)
        layout.addWidget(okBtn, 4, 0, 2, 1)
        layout.addWidget(quitBtn, 4, 2, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomGroupBox.setLayout(layout)

    def check_password(self):
        password = "526"
        enteredPassword = lineEditPassword.text()
        #entered_password, ok = QInputDialog.getText(self, 'Give me your password', 'Password:')
        if enteredPassword == password:
            self.lb1.setText('Wonderful!')
            self.lb2.setText('Happy ')
            self.lb3.setText('love u!')
        else:
            self.lb1.setText('Welcome')
            self.lb2.setText('Wanna go on your adventure?')
            self.lb3.setText('Please give me your password:')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gift = WidgetGift()
    gift.show()
    sys.exit(app.exec_())
