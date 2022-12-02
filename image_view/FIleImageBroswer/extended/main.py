# https://pastebin.com/Mes6cVZt
# https://www.pythonguis.com/faq/file-image-browser-app-with-thumbnails/
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from modUI import clsIconsGrid

appWidth = 800
appHeight = 600


class mainWindow(QMainWindow):
    def __init__(self, dirPath):
        super().__init__()
        self.setWindowTitle('File System Viewer')
        self.setGeometry(100, 100, appWidth, appHeight)

        self.ig = clsIconsGrid(dirPath)
        self.setCentralWidget(self.ig)


if __name__ == '__main__':
    dirPath = r'C:/waDump/'
    app = QApplication(sys.argv)

    mw = mainWindow(dirPath)
    mw.show()
    app.exec_()
