#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Додаток має бути симулятором фортепіано, на цьому етапі це прототип лише з білими нединамічними клавішами,
які просто відтворюють файли формату .wav. Спершу cтворивши клас Piano, перекинув його виконання на UI_Form,
створений за допомогою QT Desighner. Після цього я хотів перетворити кнопки на зображення, що би змінювались
під наведенням мишки та натиском (чого приховувати, мені було б достатньо, щоб вони просто відтворювались як зображення).
Хоч в інеті є мало матеріалів щодо створення інтерфейсів QT в Python, я вс-таки знайшов на StackOverflow готовий клас
PicButton, що спадкує по класу QAbstractButton (він є окремо збережений, як файл PicButton).
Основні проблеми почались, коли я намагався додати об'єкт цього класу до Ui_Form. В даному варівнті коду пробував
змінювати лише "клавішу" c_note.
'''


import winsound, sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.resize(600, 600)
        ###
        self.c_note = PicButton(QtGui.QPixmap("images/C.png"), QtGui.QPixmap("images/C_mouse.png"), QtGui.QPixmap("images/C_on.png"))
        ###
        self.d_note = QtGui.QPushButton(Form)
        self.d_note.setGeometry(QtCore.QRect(90, 20, 75, 441))
        self.e_note = QtGui.QPushButton(Form)
        self.e_note.setGeometry(QtCore.QRect(170, 20, 75, 441))
        self.f_note = QtGui.QPushButton(Form)
        self.f_note.setGeometry(QtCore.QRect(250, 20, 75, 441))
        self.g_note = QtGui.QPushButton(Form)
        self.g_note.setGeometry(QtCore.QRect(330, 20, 75, 441))
        self.a_note = QtGui.QPushButton(Form)
        self.a_note.setGeometry(QtCore.QRect(410, 20, 75, 441))
        self.h_note = QtGui.QPushButton(Form)
        self.h_note.setGeometry(QtCore.QRect(490, 20, 75, 441))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Piano Simulator", None))
        self.c_note.clicked.connect(self.play_c)
        self.d_note.clicked.connect(self.play_d)
        self.e_note.clicked.connect(self.play_e)
        self.f_note.clicked.connect(self.play_f)
        self.g_note.clicked.connect(self.play_g)
        self.a_note.clicked.connect(self.play_a)
        self.h_note.clicked.connect(self.play_h)

    def play_c(self):
        x.play("C")

    def play_d(self):
        x.play("D")

    def play_e(self):
        x.play("E")

    def play_f(self):
        x.play("F")

    def play_g(self):
        x.play("G")

    def play_a(self):
        x.play("A")

    def play_h(self):
        x.play("H")

class PicButton(QAbstractButton):
    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(100, 400)

class Piano(object):
    def play(self, note):
        if note == "C":
            return winsound.PlaySound('sounds/028.wav', winsound.SND_ALIAS)
        if note == "D":
            return winsound.PlaySound('sounds/030.wav', winsound.SND_ALIAS)
        if note == "E":
            return winsound.PlaySound('sounds/032.wav', winsound.SND_ALIAS)
        if note == "F":
            return winsound.PlaySound('sounds/033.wav', winsound.SND_ALIAS)
        if note == "G":
            return winsound.PlaySound('sounds/035.wav', winsound.SND_ALIAS)
        if note == "A":
            return winsound.PlaySound('sounds/037.wav', winsound.SND_ALIAS)
        if note == "H":
            return winsound.PlaySound('sounds/039.wav', winsound.SND_ALIAS)

x = Piano()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
