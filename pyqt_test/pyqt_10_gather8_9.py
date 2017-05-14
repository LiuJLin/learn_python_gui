import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer,QCoreApplication, QBasicTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QToolTip, QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QAction,qApp,QTextEdit, QLineEdit, QInputDialog,QHBoxLayout,QVBoxLayout,QGridLayout,QDialog)
from PyQt5.QtGui import QFont, QIcon, QColor, QFontMetrics, QPainter, QPalette

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

        #选择风格的下拉菜单
        # styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())


        styleLabel = QLabel("526:")
        #styleLabel.setBuddy(styleComboBox)

        #多选项，
        #self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        #设置默认选择
        #self.useStylePaletteCheckBox.setChecked(True)
        #
        #disableWidgetsCheckBox = QCheckBox("&Disable widgets")
        # 布局设置
        # self.createTopLeftGroupBox()
        # self.createTopRightGroupBox()
        # self.createBottomLeftTabWidget()
        self.createBottomGroupBox()
        # self.createProgressBar()

        #styleComboBox.activated[str].connect(self.changeStyle)
        # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        # disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.bottomGroupBox.setDisabled)

        #最上方top主题选择模块
        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        #topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        # topLayout.addWidget(self.useStylePaletteCheckBox)
        # topLayout.addWidget(disableWidgetsCheckBox)

        # 中间模块middle
        wiggly_widget = Wiggly_Widget()
        lineEdit = QLineEdit()
        middleLayout = QVBoxLayout()
        middleLayout.addWidget(wiggly_widget)
        #middleLayout.addWidget(lineEdit)
        #self.setLayout(layout)
        lineEdit.textChanged.connect(wiggly_widget.setText)
        lineEdit.setText("Happy")
        #self.setWindowTitle("Happy (wiggly)")
        wiggly_widget.resize(600,520)
        # 主
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, )
        mainLayout.addWidget(wiggly_widget, 1, 0,)
        #mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomGroupBox, 2, 0)
        #mainLayout.addWidget(self.bottomGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Happy")
        #self.changeStyle("Windows")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

    # def changeStyle(self, styleName):
    #     QApplication.setStyle(QStyleFactory.create(styleName))
    #     self.changePalette()

    # def changePalette(self):
    #     if (self.useStylePaletteCheckBox.isChecked()):
    #         QApplication.setPalette(QApplication.style().standardPalette())
    #     else:
    #         QApplication.setPalette(self.originalPalette)

    #def advanceProgressBar(self):
    #     curVal = self.progressBar.value()
    #     maxVal = self.progressBar.maximum()
    #     self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    # def createMiddleGroupBox(self):
    #     self.topLeftGroupBox = QGroupBox("Group 1")
    #
    #     radioButton1 = QRadioButton("Radio button 1")
    #     radioButton2 = QRadioButton("Radio button 2")
    #     radioButton3 = QRadioButton("Radio button 3")
    #     radioButton1.setChecked(True)
    #
    #     checkBox = QCheckBox("Tri-state check box")
    #     checkBox.setTristate(True)
    #     checkBox.setCheckState(Qt.PartiallyChecked)
    #
    #     layout = QVBoxLayout()
    #     layout.addWidget(radioButton1)
    #     layout.addWidget(radioButton2)
    #     layout.addWidget(radioButton3)
    #     layout.addWidget(checkBox)
    #     layout.addStretch(1)
    #     self.topLeftGroupBox.setLayout(layout)
    #
    # def createTopRightGroupBox(self):
    #     self.topRightGroupBox = QGroupBox("Group 2")
    #
    #     defaultPushButton = QPushButton("Default Push Button")
    #     defaultPushButton.setDefault(True)
    #
    #     togglePushButton = QPushButton("Toggle Push Button")
    #     togglePushButton.setCheckable(True)
    #     togglePushButton.setChecked(True)
    #
    #     flatPushButton = QPushButton("Flat Push Button")
    #     flatPushButton.setFlat(True)
    #
    #     layout = QVBoxLayout()
    #     layout.addWidget(defaultPushButton)
    #     layout.addWidget(togglePushButton)
    #     layout.addWidget(flatPushButton)
    #     layout.addStretch(1)
    #     self.topRightGroupBox.setLayout(layout)
    #
    # def createBottomLeftTabWidget(self):
    #     self.bottomLeftTabWidget = QTabWidget()
    #     self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
    #             QSizePolicy.Ignored)
    #
    #     tab1 = QWidget()
    #     tableWidget = QTableWidget(10, 10)
    #
    #     tab1hbox = QHBoxLayout()
    #     tab1hbox.setContentsMargins(5, 5, 5, 5)
    #     tab1hbox.addWidget(tableWidget)
    #     tab1.setLayout(tab1hbox)
    #
    #     tab2 = QWidget()
    #     textEdit = QTextEdit()
    #
    #     textEdit.setPlainText("Twinkle, twinkle, little star,\n"
    #                           "How I wonder what you are.\n"
    #                           "Up above the world so high,\n"
    #                           "Like a diamond in the sky.\n"
    #                           "Twinkle, twinkle, little star,\n"
    #                           "How I wonder what you are!\n")
    #
    #     tab2hbox = QHBoxLayout()
    #     tab2hbox.setContentsMargins(5, 5, 5, 5)
    #     tab2hbox.addWidget(textEdit)
    #     tab2.setLayout(tab2hbox)
    #
    #     self.bottomLeftTabWidget.addTab(tab1, "&Table")
    #     self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

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

        lineEdit = QLineEdit('')
        lineEdit.setEchoMode(QLineEdit.Password)

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
        #quit_btn.move(250,50)
        # spinBox = QSpinBox(self.bottomGroupBox)
        # spinBox.setValue(50)

        # dateTimeEdit = QDateTimeEdit(self.bottomGroupBox)
        # dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # slider = QSlider(Qt.Horizontal, self.bottomGroupBox)
        # slider.setValue(40)
        #
        # scrollBar = QScrollBar(Qt.Horizontal, self.bottomGroupBox)
        # scrollBar.setValue(60)

        # dial = QDial(self.bottomGroupBox)
        # dial.setValue(30)
        # dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lb1, 0, 0, 1, 2)
        layout.addWidget(lb2, 1, 0, 1, 2)
        layout.addWidget(lb3, 2, 0, 1, 2)
        layout.addWidget(lineEdit, 3, 0, 1, 2)
        layout.addWidget(okBtn, 4, 0, 1, 1)
        layout.addWidget(quitBtn, 4, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomGroupBox.setLayout(layout)

    def check_password(self):
        password = "526"
        enteredPassword = lineEdit.text()
        #entered_password, ok = QInputDialog.getText(self, 'Give me your password', 'Password:')
        if enteredPassword == password:
            self.lb1.setText('Wonderful!')
            self.lb2.setText('Happy ')
            self.lb3.setText('love u!')
        else:
            self.lb1.setText('Welcome')
            self.lb2.setText('Wanna go on your adventure?')
            self.lb3.setText('Please give me your password:')
    # def createProgressBar(self):
    #     self.progressBar = QProgressBar()
    #     self.progressBar.setRange(0, 10000)
    #     self.progressBar.setValue(0)
    #
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.advanceProgressBar)
    #     timer.start(1000)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gift = WidgetGift()
    gift.show()
    sys.exit(app.exec_())
