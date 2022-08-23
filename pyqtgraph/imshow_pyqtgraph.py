"""
安装依赖库：
1. Pillow
2. PySide2
3. PyQtGraph
from https://blog.csdn.net/zhy29563/article/details/119754910
"""

import sys

import numpy as np
import pyqtgraph as pg
from PIL import Image
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QFileDialog
from pyqtgraph import ImageView

# 设置 PyQtGraph 显示配置
########################################################################################################################
# 设置显示背景色为白色，默认为黑色
pg.setConfigOption('background', 'w')
# 设置显示前景色为黑色，默认为灰色
pg.setConfigOption('foreground', 'k')
# 设置图像显示以行为主，默认以列为主
pg.setConfigOption('imageAxisOrder', 'row-major')


class PyQtGraphicDemo(QWidget):
    def __init__(self, parent=None):
        super(PyQtGraphicDemo, self).__init__(parent)

        self.resize(600, 400)

        # 图像显示控件
        self.graphicsView = ImageView(self)
        # 隐藏直方图，菜单按钮，ROI
        self.graphicsView.ui.histogram.hide()
        self.graphicsView.ui.menuBtn.hide()
        self.graphicsView.ui.roiBtn.hide()

        # 按钮
        self.pushButton = QPushButton(self)
        self.pushButton.setText("PushButton")
        self.pushButton.clicked.connect(self.showImage)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addWidget(self.pushButton)

        # 设置窗口布局
        self.setLayout(self.verticalLayout)

    def showImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "请选择图像：", '.', "All Files(*);;*.jpg;;*.png;;*.bmp")
        if fileName != '':
            image = Image.open(fileName)
            if image is not None:
                # 如果之前未设置显示选项以行为主，这里需要对显示图像进行转置
                self.graphicsView.setImage(np.array(image))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PyQtGraphicDemo()
    window.show()
    sys.exit(app.exec_())
