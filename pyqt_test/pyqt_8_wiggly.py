import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget,QLabel, QMainWindow,QAction,qApp,QTextEdit, QLineEdit, QInputDialog,QHBoxLayout,QVBoxLayout,QGridLayout,QDialog
from PyQt5.QtGui import QFont, QIcon, QColor, QFontMetrics, QPainter, QPalette
from PyQt5.QtCore import QCoreApplication, QBasicTimer

class Wiggly_Widget(QWidget):
    def __init__(self, parent=None):
        super(Wiggly_Widget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        #wiggly
        #self.setBackgroundRole(QPalette)
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
class Dialog(QDialog):
    def __init__(self,parent = None):
        super(Dialog,self).__init__(parent)
    #     self.initUI()
    # def initUI(self):
        wiggly_widget = Wiggly_Widget()
        lineEdit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(wiggly_widget)
        layout.addWidget(lineEdit)
        self.setLayout(layout)


        lineEdit.textChanged.connect(wiggly_widget.setText)
        lineEdit.setText("Happy")
        self.setWindowTitle("Happy (wiggly)")
        self.resize(900,520)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
