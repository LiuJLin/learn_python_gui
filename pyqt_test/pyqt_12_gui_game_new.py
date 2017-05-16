import sys
from PyQt5.QtCore import QDir,QDateTime, Qt,qAbs, QLineF, QPointF, qrand, QRectF, QSizeF, qsrand, QTime, QTimer,QCoreApplication, QBasicTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,QGraphicsItem, QGraphicsScene,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,QGraphicsView, QStyle,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QToolTip, QPushButton,QMessageBox, QDesktopWidget,QMainWindow,QAction,qApp,QTextEdit, QLineEdit, QInputDialog,QHBoxLayout,QVBoxLayout,QGridLayout,QDialog, QScrollArea, QSizePolicy,QMenu)
from PyQt5.QtGui import QFont, QIcon, QColor, QFontMetrics, QPainter, QPalette,QBrush, QColor, QLinearGradient, QPainter, QPainterPath, QPen, QPolygonF, QRadialGradient, QImage, QPainter, QPalette, QPixmap
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
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

class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.printer = QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Image Viewer")
        self.resize(500, 400)

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                QDir.currentPath())
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer",
                        "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def print_(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def about(self):
        QMessageBox.about(self, "About Image Viewer",
                "<p>The <b>Image Viewer</b> example shows how to combine "
                "QLabel and QScrollArea to display an image. QLabel is "
                "typically used for displaying text, but it can also display "
                "an image. QScrollArea provides a scrolling view around "
                "another widget. If the child widget exceeds the size of the "
                "frame, QScrollArea automatically provides scroll bars.</p>"
                "<p>The example demonstrates how QLabel's ability to scale "
                "its contents (QLabel.scaledContents), and QScrollArea's "
                "ability to automatically resize its contents "
                "(QScrollArea.widgetResizable), can be used to implement "
                "zooming and scaling features.</p>"
                "<p>In addition the example shows how to use QPainter to "
                "print an image.</p>")

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O",
                triggered=self.open)

        self.printAct = QAction("&Print...", self, shortcut="Ctrl+P",
                enabled=False, triggered=self.print_)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++",
                enabled=False, triggered=self.zoomIn)

        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-",
                enabled=False, triggered=self.zoomOut)

        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S",
                enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QAction("&Fit to Window", self, enabled=False,
                checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)

        self.aboutAct = QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))

class WidgetGift(QDialog):
    def __init__(self, parent=None):
        super(WidgetGift, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        QApplication.setPalette(QApplication.style().standardPalette()) #配色方案

        styleLabel = QLabel("526:")
        #styleLabel.setBuddy(styleComboBox)

        self.createBottomGroupBox()
        self.createMiddleGroupBox()
        self.createRightWidget()
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
        mainLayout.addLayout(topLayout, 0, 0, 1, 1 )
        mainLayout.addWidget(self.middleGroupBox, 1, 0, 1, 1)
        #mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomGroupBox, 2, 0, 1, 1)
        #mainLayout.addWidget(self.bottomGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.addWidget(self.rightWidget, 1,0,3,1)
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

        self.lb1 = QLabel('Welcome',self)
        self.lb1.move(450, 30)
        self.lb1.setFont(QFont('Comic Sans MS',20))
        self.lb2 = QLabel('Wanna go on your adventure?',self)
        self.lb2.move(450, 70)
        self.lb2.setFont(QFont('Comic Sans MS',20))
        self.lb3 = QLabel('Please give me your password:',self)
        self.lb3.move(450, 110)
        self.lb3.setFont(QFont('Comic Sans MS',15))

        self.lineEditPassword = QLineEdit('')
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

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
        layout.addWidget(self.lb1, 0, 0, 1, 3)
        layout.addWidget(self.lb2, 1, 0, 1, 3)
        layout.addWidget(self.lb3, 2, 0, 1, 3)
        layout.addWidget(self.lineEditPassword, 3, 0, 1, 3)
        layout.addWidget(okBtn, 4, 0, 2, 1)
        layout.addWidget(quitBtn, 4, 2, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomGroupBox.setLayout(layout)

    def createRightWidget(self):
        self.rightWidget = QWidget()
        journal_show = ImageViewer()
        fileName = ('Day'+str(4) +'.JPG')#journalnum

        # fileName, _ = QFileDialog.getOpenFileName(journal_show, "Open File",
        #         QDir.currentPath())
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(journal_show, "Image Viewer",
                        "Cannot load %s." % fileName)
                return

            journal_show.imageLabel.setPixmap(QPixmap.fromImage(image))
            journal_show.scaleFactor = 1.0

            journal_show.printAct.setEnabled(True)
            journal_show.fitToWindowAct.setEnabled(True)
            journal_show.updateActions()

            if not journal_show.fitToWindowAct.isChecked():
                journal_show.imageLabel.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(journal_show)
        #layout.addWidget(lineEdit)
        self.rightWidget.setLayout(layout)

    def check_password(self):
        password = "526"
        enteredPassword = self.lineEditPassword.text()
        #entered_password, ok = QInputDialog.getText(self, 'Give me your password', 'Password:')
        if enteredPassword == password:
            self.lb1.setText('Wonderful!')
            self.lb2.setText('Happy ')
            self.lb3.setText('love u!')
            self.game()
        else:
            self.lb1.setText('Welcome')
            self.lb2.setText('Wanna go on your adventure?')
            self.lb3.setText('Please give me your password:')

    def game(self):
        pygame.init()
        main_clock = pygame.time.Clock()
        #set up the window
        window_width = 800
        window_height = 600
        window_surface = pygame.display.set_mode((window_width, window_height), 0 , 32)
        pygame.display.set_caption("Sounds and images")

        food_counter = 0
        NEWFOOD = 40
        FOODSIZE = 26

        #set up the colors
        BLACK = (0, 0, 0)
        #set up the block data structures
        player = pygame.Rect(300, 100, 31, 54)
        player_image = pygame.image.load('boy.png')
        player_stretched_image_flip = pygame.transform.scale(player_image, (31, 54))
        player_stretched_image = pygame.transform.scale(player_image, (31, 54))
        food_image = pygame.image.load('heart2.png')
        food_stretched_image = pygame.transform.scale(food_image,(26, 24))
        foods = []
        for i in range(20):
            foods.append(pygame.Rect(random.randint(0, window_width - FOODSIZE), random.randint(0, window_height - FOODSIZE), FOODSIZE, FOODSIZE))

        pos_images = []
        pos_image = []
        pos_stretched_image = []
        # pos_image[0] = pygame.image.load("1.png")
        # pos_image[1] = pygame.image.load("2.png")
        # pos_image[2] = pygame.image.load("3.png")
        # pos_image[3] = pygame.image.load("4.png")
        # pos_image[4] = pygame.image.load("5.png")
        for j in range(5):
            pos_image.append(pygame.image.load(str(j+1)+'.png'))
            pos_stretched_image.append(pygame.transform.scale(pos_image[j],(25,30)))
            pos_images.append(pygame.Rect(random.randint(0, window_width - FOODSIZE), random.randint(0, window_height - FOODSIZE), FOODSIZE, FOODSIZE))


        #set up keyboard variables
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        MOVESPEED = 6

        #set up flip flag
        flip_flag = False

        #set up music
        pick_up_sound = pygame.mixer.Sound('pickup.wav')
        pygame.mixer.music.load('belief.mp3')
        pygame.mixer.music.play(-1, 0.0)
        music_playing = True

        #run the game loop
        while True:
            #check for the QUIT event
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    #sys.exit()


                if event.type == KEYDOWN:
                    #change the keyboard variables
                    if event.key == K_LEFT or event.key == ord('a'):
                        move_right = False
                        move_left = True
                        flip_flag = True
                        player_stretched_image = pygame.transform.flip(player_stretched_image_flip, flip_flag, 0)
                    if event.key == K_RIGHT or event.key == ord('d'):
                        move_right = True
                        move_left = False
                        flip_flag = False
                        player_stretched_image = pygame.transform.flip(player_stretched_image_flip, flip_flag, 0)
                    if event.key == K_UP or event.key == ord('w'):
                        move_down = False
                        move_up = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        move_down = True
                        move_up = False
                if event.type == KEYUP:
                    #change the keyboard variables
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT or event.key == ord('a'):
                        move_left = False
                        #flip_flag = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        move_right = False
                        #flip_flag = False
                    if event.key == K_UP or event.key == ord('w'):
                        move_up = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        move_down = False
                    if event.key == ord('x'):
                        player.top = random.randint(0, window_height - player.height)
                        player.left = random.randint(0, window_width - player.width)
                    if event.key == ord('m'):
                        if music_playing:
                            pygame.mixer.music.stop()
                        else:
                            pygame.mixer.music.play(-1, 0, 0)
                        music_playing = not music_playing

                if event.type == MOUSEBUTTONUP:
                    foods.append(pygame.Rect(event.pos[0] - 13 , event.pos[1] - 12, FOODSIZE, FOODSIZE))

            food_counter += 1
            if food_counter >= NEWFOOD:
                #add new food
                food_counter = 0
                foods.append(pygame.Rect(random.randint(0, window_width - FOODSIZE),random.randint(0, window_height - FOODSIZE),FOODSIZE, FOODSIZE))
            #draw the black background onto the surface
            window_surface.fill(BLACK)

            #move the player
            if move_down and player.bottom < window_height:
                player.top += MOVESPEED
            if move_up and player.top > 0:
                player.top -= MOVESPEED
            if move_left and player.left > 0:
                player.left -= MOVESPEED
            if move_right and player.right < window_width:
                player.right += MOVESPEED

            #draw the block onto the surface
            window_surface.blit(player_stretched_image, player)

            #check if the block has intersected with any food squares
            for food in foods[:]:
                if player.colliderect(food):
                    foods.remove(food)
                    player = pygame.Rect(player.left, player.top, player.width + 1, player.height + 2)
                    #player_stretched_image = pygame.transform.scale(player_image, (player.width, player.height))
                    player_stretched_image_flip = pygame.transform.scale(player_image, (player.width, player.height))
                    player_stretched_image = pygame.transform.flip(player_stretched_image_flip, flip_flag, 0)
                    if music_playing:
                        pick_up_sound.play()

            #draw the food
            for food in foods:
                window_surface.blit(food_stretched_image, food)
                #window_surface.blit(food_image, food)

            # notes = []

            for k in range(5):
                    window_surface.blit(pos_stretched_image[k], pos_images[k])
                    if player.colliderect(pos_images[k]):
                        self.journalnum = k
                        #notes.append(pygame.image.load('Day'+str(4) +'.JPG'))
                        #journal_window.deiconify()
                        #journal_window.blit(pos_image[k])
            #draw the window onto the screen
            pygame.display.update()
            main_clock.tick(40)
# class gameWidget(QWidget):
#     def __init__(self, parent=None):
#         super(gameWidget, self).__init__(parent)
#         self.initUI()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gift = WidgetGift()
    gift.show()
    sys.exit(app.exec_())
