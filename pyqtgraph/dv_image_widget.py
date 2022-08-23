# -*- coding: utf-8 -*-
import sys

import numpy as np
import pyqtgraph as pg
from PIL import Image
from PyQt5 import QtWidgets


class ImageViewWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewWidget, self).__init__(parent)
        # 按钮
        self.path2 = None
        self.path1 = None
        self.cmp_button = QtWidgets.QPushButton()
        self.cmp_button.setText("compare")
        self.cmp_button.clicked.connect(self.cmp_image)

        self.pg_widget = pg.GraphicsLayoutWidget(show=True)
        self.pg_widget.setBackground('w')
        self.viewBox1 = self.pg_widget.addViewBox()

        ## lock the aspect ratio so pixels are always square
        self.viewBox1.setAspectLocked(True)
        self.pg_widget.nextColumn()
        self.viewBox2 = self.pg_widget.addViewBox()
        self.viewBox2.setAspectLocked(True)

        self.image_item1 = pg.ImageItem()
        self.viewBox1.addItem(self.image_item1)
        self.image_item2 = pg.ImageItem()
        self.viewBox2.addItem(self.image_item2)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.pg_widget)
        layout.addWidget(self.cmp_button)
        self.setLayout(layout)

    def mousePressEvent(self, ev):
        print('event mouse pressed')

    def mouseReleaseEvent(self, ev):
        print('event mouse released')

    def cmp_image(self):
        print('cmp image')
        if self.path2 is not None:
            # image1 = Image.open(self.path2)
            # self.image_item1.setImage(np.array(image1))
            self.viewBox1.addItem(self.image_item2)
            self.viewBox2.addItem(self.image_item2)
            print('view 1 show path2 image')
            import time
            time.sleep(0.1)
            if self.path1 is not None:
                # image1 = Image.open(self.path1)
                # self.image_item1.setImage(np.array(image1))
                self.viewBox1.addItem(self.image_item1)
                print('view 1 show path1 image')

    def set_image(self, path):
        self.path1 = self.path2
        self.path2 = path
        if self.path1 is not None:
            image1 = Image.open(self.path1)
            self.image_item1.setImage(np.array(image1))
            self.viewBox1.addItem(self.image_item1)
        if self.path2 is not None:
            image2 = Image.open(self.path2)
            self.image_item2.setImage(np.array(image2))
            self.viewBox2.addItem(self.image_item2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ImageViewWidget()
    win.set_image('../waDump/OPTZOOM_FUSION_20220810142751_r0_l0.600_m1.000_a1.000_aux.jpg')
    win.set_image('../waDump/OPTZOOM_FUSION_20220810142751_r0_l0.600_m1.000_a1.000_main.jpg')

    win.show()
    sys.exit(app.exec_())
