import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        #用initUI创建一个gui
        self.initUI()
    def initUI(self):
        #窗口位置和大小
        self.setGeometry(300,300,900,520)
        self.setWindowTitle("Adventure")
        #添加图标
        self.setWindowIcon(QIcon("2.jpg"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # w = QWidget()
    # w.resize(530,520)
    # w.move(300,300)
    # w.setWindowTitle('Happy Birthday!')
    # w.show()

    sys.exit(app.exec_())
