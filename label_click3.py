# from https://blog.csdn.net/weixin_46185214/article/details/105918454

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class MyLabel(QLabel):
    mylabelSig = pyqtSignal(str)
    mylabelDoubleClickSig = pyqtSignal(str)

    def __int__(self):
        super(MyLabel, self).__init__()

    def mouseDoubleClickEvent(self, e):  # 双击
        sigContent = self.objectName()
        self.mylabelDoubleClickSig.emit(sigContent)

    def mousePressEvent(self, e):  # 单击
        sigContent = self.objectName()
        self.mylabelSig.emit(sigContent)

    def leaveEvent(self, e):  # 鼠标离开label
        print("leaveEvent")

    def enterEvent(self, e):  # 鼠标移入label
        print("enterEvent")
