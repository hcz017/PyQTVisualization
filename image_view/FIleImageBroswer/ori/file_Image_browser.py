# https://www.pythonguis.com/faq/file-image-browser-app-with-thumbnails/
# File Image Browser App with thumbnails
import glob
import math
import sys
import time
from collections import namedtuple

from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate

# Create a custom namedtuple class to hold our data.
preview = namedtuple("preview", "id title image")

NUMBER_OF_COLUMNS = 4
CELL_PADDING = 20  # all sides


class PreviewDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        # data is our preview object
        data = index.model().data(index, Qt.DisplayRole)
        if data is None:
            return

        width = option.rect.width() - CELL_PADDING * 2
        height = option.rect.height() - CELL_PADDING * 2

        # option.rect holds the area we are painting on the widget (our table cell)
        # scale our pixmap to fit
        scaled = data.image.scaled(
            width,
            height,
            aspectRatioMode=Qt.KeepAspectRatio,
        )
        # Position in the middle of the area.
        x = CELL_PADDING + (width - scaled.width()) / 2
        y = CELL_PADDING + (height - scaled.height()) / 2

        painter.drawImage(option.rect.x() + x, option.rect.y() + y, scaled)

    def sizeHint(self, option, index):
        # All items the same size.
        return QSize(200, 150)


class PreviewModel(QAbstractTableModel):
    def __init__(self, todos=None):
        super().__init__()
        # .data holds our data for display, as a list of Preview objects.
        self.previews = []

    def data(self, index, role):
        try:
            data = self.previews[index.row() * 4 + index.column()]
        except IndexError:
            # Incomplete last row.
            return

        if role == Qt.DisplayRole:
            return data  # Pass the data to our delegate to draw.

        if role == Qt.ToolTipRole:
            return data.title

    def columnCount(self, index):
        return NUMBER_OF_COLUMNS

    def rowCount(self, index):
        n_items = len(self.previews)
        return math.ceil(n_items / NUMBER_OF_COLUMNS)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print('main windows init')
        self.resize(800, 600)
        self.view = QTableView()
        self.view.horizontalHeader().hide()
        self.view.verticalHeader().hide()
        self.view.setGridStyle(Qt.NoPen)

        delegate = PreviewDelegate()
        self.view.setItemDelegate(delegate)
        self.model = PreviewModel()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)

        print('adding images')
        # Add a bunch of images.
        for n, fn in enumerate(glob.glob(r"C:\waDump\*.jpg")):
            image = QImage(fn)
            item = preview(n, fn, image)
            self.model.previews.append(item)
        print('adding images done')
        self.model.layoutChanged.emit()

        self.view.resizeRowsToContents()
        self.view.resizeColumnsToContents()


start_time = time.time()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
print("耗时: {:.3f}秒".format(time.time() - start_time))
app.exec_()
