# -*- coding: utf-8 -*-
# from https://blog.csdn.net/weixin_39888010/article/details/121456724

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph import ImageView
from PIL import Image

# 创建一个图形布局小部件
win = pg.GraphicsLayoutWidget(show=True, size=(800, 600), title="布局小部件标题")
# 上面已经初始化过size，还可以通过以下方式修改size
# win.resize(1000,600)
# 设置窗口标题
# win.setWindowTitle('布局小部件标题')

# 添加Plot显示窗体
p1 = win.addPlot(title="Plot标题1", y=np.random.normal(size=100))
# 在下一列显示窗体
win.nextColumn()
p2 = win.addPlot(title="Plot标题2", y=np.random.normal(size=100))
# 在下一行显示窗体
win.nextRow()
p3 = win.addPlot(title="Plot标题3", y=np.random.normal(size=100))
p4 = win.addPlot(title="Plot标题4", y=np.random.normal(size=100))
# 显示label
win.addLabel(text="我是一个Label")

if __name__ == '__main__':
    pg.exec()
