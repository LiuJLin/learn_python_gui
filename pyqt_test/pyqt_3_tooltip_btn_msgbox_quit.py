import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # tooltip消息框
        QToolTip.setFont(QFont('Comic Sans MS',10))
        self.setToolTip("This is a <b>QWidget</b> widget. Wanna go on your adventure?")
        #button按钮
        btn = QPushButton('OK', self)
        btn.setToolTip('Click me to <b>enter</b> the game!')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        #clicked 点击触发事件
        quit_btn = QPushButton('Quit', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.setToolTip('Click me to <b>Quit</b>')
        quit_btn.resize(btn.sizeHint())
        quit_btn.move(250,50)
        # 位置大小
        self.setGeometry(300, 300, 900, 520)
        self.setWindowTitle('Adventure')
        #图标
        self.setWindowIcon(QIcon("2.jpg"))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    # 消息提示
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
