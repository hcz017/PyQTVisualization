import sys
from typing import Dict, Any

import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class RotateAxisItem(pg.AxisItem):
    def drawPicture(self, p, axisSpec, tickSpecs, textSpecs):
        p.setRenderHint(p.Antialiasing, False)
        p.setRenderHint(p.TextAntialiasing, True)
        # draw long line along axis
        pen, p1, p2 = axisSpec
        p.setPen(pen)
        p.drawLine(p1, p2)
        p.translate(0.5, 0)  # resolves some damn pixel ambiguity
        # draw ticks
        for pen, p1, p2 in tickSpecs:
            p.setPen(pen)
            p.drawLine(p1, p2)
        # draw all text
        # if self.tickFont is not None:
        #     p.setFont(self.tickFont)
        p.setPen(self.pen())
        for rect, flags, text in textSpecs:
            # this is the important part
            p.save()
            p.translate(rect.x(), rect.y())
            p.rotate(-30)
            p.drawText(-rect.width(), rect.height(), rect.width(), rect.height(), flags, text)
            # restoring the painter is *required*!!!
            p.restore()


# 散点图
class PyQtGraphScatterWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.pw = None
        self.title_label = None
        self.temp_mark = 0
        self.init_data()
        self.init_ui()

    def init_data(self):
        # https://www.sioe.cn/yingyong/yanse-rgb-16/
        pass

    def init_ui(self):
        self.title_label = QtWidgets.QLabel('散点图')
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        xax = RotateAxisItem(orientation='bottom')
        xax.setHeight(h=50)
        self.pw = pg.PlotWidget(axisItems={'bottom': xax})
        # self.pw = pg.plot()
        self.pw.setMouseEnabled(x=True, y=False)
        self.pw.setAutoVisible(x=False, y=True)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.pw)
        self.setLayout(layout)
        pass

    def set_data(self, data: Dict[str, Any]):
        scatters = pg.ScatterPlotItem(
            brush=pg.mkBrush(255, 255, 255, 120),
            hoverable=True,
            # 把默认的hover 值取消掉
            # tip=None,
            hoverPen=pg.mkPen('w')
        )
        spots3 = []

        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12]
        self.y = [3] * 10

        for x0, y0 in zip(x, self.y):
            if x0 % 4 == 0:
                spots3.append({
                    'pos': (x0, y0 + 4),
                    'size': 15,
                    # 'pen': pg.mkPen(color=(0, 0, 255), width=3),
                    # 'brush': pg.mkBrush(color=(0, 255, 0)),
                    # 'symbol': 's',
                    'data': 'only symbol'
                })
                spots3.append({
                    'pos': (x0, y0 + 3),
                    'size': 15,
                    'pen': pg.mkPen(color='b', width=3),
                    # 'brush': pg.mkBrush(color=(0, 255, 0)),
                    # 'symbol': 's',
                    'data': 'blue pen'
                })
                spots3.append({
                    'pos': (x0, y0 + 2),
                    'size': 15,
                    # 'pen': pg.mkPen(color=(0, 0, 255), width=3),
                    'brush': pg.mkBrush(color='g'),
                    # 'symbol': 's',
                    'data': 'green brush'
                })
                spots3.append({
                    'pos': (x0, y0 + 1),
                    'size': 15,
                    'pen': pg.mkPen(color=(0, 0, 255), width=3),
                    'brush': pg.mkBrush(color=(0, 255, 0)),
                    # 'symbol': 's',
                    'data': 'blue pen + green brush'
                })
            else:
                spots3.append({
                    'pos': (x0, y0),
                    'size': 10,
                    'pen': pg.mkPen(color=(255, 0, 0), width=3),
                    'brush': pg.mkBrush(color=(0, 255, 0)),
                    'data': 'scrasfd'
                })

        pass
        # temp end

        scatters.addPoints(spots3)
        self.pw.addItem(scatters)
        # self.pw.setYRange(2, 10)
        # self.pw.autoRange()
        self.pw.showGrid(x=True, y=True)
        self.label = pg.TextItem()
        self.pw.addItem(self.label)

        scatters.sigClicked.connect(self.scatter_clicked)
        # 自定义hover 响应行为
        # scatters.sigHovered.connect(self.scatter_hovered)
        pass

    def scatter_clicked(self, plot, points):
        if len(points) <= 0:
            return
        cur_x = points[0].pos()[0]
        cur_y = points[0].pos()[1]

        index_val = points[0].index()
        y_val = self.y[index_val]
        print(index_val)

        label = pg.TextItem()
        html_str = '<p style="color:black;font-size:12px;">' + '&nbsp;' + str(y_val) + '</p>'
        # label.setHtml(html_str)
        label.setPlainText('asdasd')
        # label.setColor(color='r')
        label.setPos(cur_x, cur_y)
        self.pw.addItem(label)
        pass

    def scatter_hovered(self, plot, points):
        if len(points) <= 0:
            return
        cur_x = points[0].pos()[0]
        cur_y = points[0].pos()[1]

        index_val = points[0].index()

        # x_str = self.x_ticks[index_val][1]
        y_val = self.y[index_val]

        html_str = '<p style="color:black;font-size:12px;">' + '&nbsp;' + str(y_val) + '</p>'
        self.label.setHtml(html_str)
        self.label.setPos(cur_x, cur_y)
        print('hovered::', points[0].index(), points[0].pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    t_win = PyQtGraphScatterWidget()
    t_win.show()
    t_win.set_data(None)
    sys.exit(app.exec_())
    pass
