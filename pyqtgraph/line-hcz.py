import sys

import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 400)
        self.setWindowTitle("pyqtgraph line")
        self.setStyleSheet("background-color:rgb(255,255,255)")

        # 创建一个GraphicsWidget
        self.win = pg.GraphicsLayoutWidget(self, show=True)

        # 创建布局显示line chart
        layout = QVBoxLayout()
        layout.addWidget(self.win)
        self.setLayout(layout)
        self.showLineChart()

    def showLineChart(self):
        # 创建一个Plot画板
        plot = self.win.addPlot(title="随机数据对比")

        # 显示网格
        plot.showGrid(x=True, y=True)

        # 显示图例， 需要在绘制点的时候添加name 属性，如 name='blue'
        plot.addLegend()

        # 添加 x 轴和 y 轴标签
        plot.setLabel('left', 'thread ids', units='y')
        plot.setLabel('bottom', 'Horizontal Values', units='s')

        # 设置 X 坐标轴范围
        # plot.setXRange(0, 10)

        # 设置 Y 坐标轴范围
        # plot.setYRange(1, 4)

        # 创建画笔
        chartPen1 = pg.mkPen(color=(107, 200, 224), width=3)

        # 加入随机的点数据
        plot.plot(y=np.random.normal(size=30), pen=chartPen1, title="随机数据1", symbol='x', symbolPen='d', name='blue')

        # 创建画笔
        chartPen2 = pg.mkPen(color=(192, 80, 77), width=3)
        plot.plot(y=np.random.normal(size=30) + 5, pen=chartPen2, title="随机数据2", symbol='t1', symbolPen='w',
                  name='green')


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
