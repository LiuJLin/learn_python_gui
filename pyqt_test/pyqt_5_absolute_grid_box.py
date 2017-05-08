import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow,QAction,qApp,QTextEdit,QLabel, QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class adventure_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #反馈信息提交布局
        password = QLabel('Password')
        author = QLabel("Author")
        date = QLabel("Date")

        password_edit = QLineEdit()
        author_edit = QLineEdit()
        date_edit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(password, 1, 0)
        grid.addWidget(password_edit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)
        grid.addWidget(date, 3, 0)
        grid.addWidget(date_edit, 3, 1,5,1)
        self.setLayout(grid)

        #label
        QLabel.setFont(self, QFont('Comic Sans MS',10))
        lb1 = QLabel('Welcome',self)
        lb1.move(450, 10)

        lb2 = QLabel('Wanna go on your adventure?',self)
        lb2.move(450, 30)

        lb3 = QLabel('Please give me your password',self)
        lb3.move(450, 50)
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
        # #盒布局
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(btn)
        # hbox.addWidget(quit_btn)
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        # self.setLayout(vbox)
        # #栅格布局
        # grid = QGridLayout()
        # self.setLayout(grid)
        #
        # names = ['Cls', 'Bck', '', 'Close',
        #         '7', '8', '9', '/',
        #         '4', '5', '6', '+',
        #         '1', '2', '3', '-',
        #         '0', '.', '=', '+']
        # positions = [(i,j) for i in range(5) for j in range(4)]
        # for position, name in zip(positions, names):
        #     if name == "":
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)
        # 位置大小
        self.setGeometry(300, 300, 900, 520)
        self.setWindowTitle('Adventure')
        #图标
        self.setWindowIcon(QIcon("2.jpg"))
        self.center()
        self.show()

    # 将页面移到屏幕中心
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
    ex1 = adventure_widget()
    #ex2 = adventure_widget()

    sys.exit(app.exec_())
