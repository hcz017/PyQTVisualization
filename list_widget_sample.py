# code reference https://blog.csdn.net/qq_17246289/article/details/115135699
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QAbstractItemView, QApplication, QListWidgetItem, QListView


class MyListWidget(QtWidgets.QListWidget):
    signal = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(400, 300)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 创建QMenu信号事件
        self.customContextMenuRequested.connect(self.showMenu)
        self.contextMenu = QMenu(self)
        self.CP = self.contextMenu.addAction('复制')
        self.DL = self.contextMenu.addAction('删除')
        self.CP.triggered.connect(self.copy)
        self.DL.triggered.connect(self.del_text)

        # 设置每个item size
        self.setGridSize(QtCore.QSize(50, 50))
        # 设置横向list
        self.setFlow(QListView.LeftToRight)
        # 设置换行
        self.setWrapping(True)
        # 窗口size 变化后重新计算列数
        self.setResizeMode(QtWidgets.QListView.Adjust)
        # 设置选择模式
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    # 显示右键菜单
    def showMenu(self, pos):
        # pos 鼠标位置
        # 菜单显示前,将它移动到鼠标点击的位置
        self.contextMenu.exec_(QCursor.pos())  # 在鼠标位置显示

    # 获取选择行的内容
    def selected_text(self):
        try:
            selected = self.selectedItems()
            texts = ''
            for item in selected:
                if texts:
                    texts = texts + '\n' + item.text()
                else:
                    texts = item.text()
        except BaseException as e:
            print(e)
            return
        return texts

    def copy(self):
        text = self.selected_text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)

    def del_text(self):
        try:
            index = self.selectedIndexes()
            row = []

            for i in index:
                r = i.row()
                row.append(r)
            for i in sorted(row, reverse=True):
                self.takeItem(i)
        except BaseException as e:
            print(e)
            return
        self.signal.emit(row)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MyListWidget()
    for i in range(100):
        item = QListWidgetItem(str(i))
        main_window.addItem(item)

    main_window.show()
    import sys

    sys.exit(app.exec_())
