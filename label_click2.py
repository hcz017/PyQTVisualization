# https://blog.csdn.net/weixin_44429308/article/details/106315778
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class MyQLabel(QLabel):

    # 自定义单击信号
    clicked = pyqtSignal()
    # 自定义双击信号
    DoubleClicked = pyqtSignal()

    def __int__(self):
        super().__init__()

    # 重写鼠标单击事件
    def mousePressEvent(self, QMouseEvent):  # 单击
        self.clicked.emit()

    # 重写鼠标双击事件
    def mouseDoubleClickEvent(self, e):  # 双击
        self.DoubleClicked.emit()
