# https://blog.csdn.net/jinggege_7758521/article/details/122505224
import sys

import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QApplication
from pyqtgraph.Qt import QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyqtgraph example"))


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.showLineChart()

    def showLineChart(self):
        # 创建一个GraphicsWidget
        win = pg.GraphicsLayoutWidget(self, show=True)
        # 设置widget大小
        win.resize(600, 300)
        # 创建画笔
        chartPen1 = pg.mkPen(color=(107, 200, 224), width=3)
        # 创建一个Plot画板
        plot = win.addPlot(title="随机数据对比")
        # 加入随机的点数据
        plot.plot(y=np.random.normal(size=30), pen=chartPen1, title="随机数据1")

        # 创建画笔
        chartPen2 = pg.mkPen(color=(192, 80, 77), width=3)
        plot.plot(y=np.random.normal(size=30) + 5, pen=chartPen2, title="随机数据2", symbolPen='w')


if __name__ == '__main__':
    # 设置背景色
    pg.setConfigOption('background', 'w')
    # 设置平滑绘制
    pg.setConfigOptions(antialias=True)
    # 创建Application
    app = QApplication(sys.argv)
    # 创建对话框
    mainWidget = MainWindow()
    # 对话框显示
    mainWidget.show()
    # 执行app
    sys.exit(app.exec_())
