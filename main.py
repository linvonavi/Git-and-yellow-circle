import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from PyQt5.QtWidgets import QApplication, QMainWindow

is_button_clicked = False
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.b)

    def paintEvent(self, event):
        global is_button_clicked
        if is_button_clicked != False:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def b(self):
        global is_button_clicked
        is_button_clicked = True
        self.repaint()


    def draw(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 255))
        for i in range(5):
            s = randrange(100)
            qp.drawEllipse(randrange(800), randrange(600), s, s)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec())
