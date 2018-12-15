import sys

from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl, QObject


class MapQml(QQuickView):
    def __init__(self):
        super().__init__()
        CUR_POINT = dict()
        CUR_POINT['lat'] = 59.9390430
        CUR_POINT['lon'] = 30.3157135

        self.setSource(QUrl('map.qml'))
        map = self.findChild(QObject, 'map')
        map.setProperty('lat', CUR_POINT['lat'])
        map.setProperty('lon', CUR_POINT['lon'])
        map.setProperty('zoom', 14)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 640, 480)
        self.setWindowTitle('OSM')

        map_qml = MapQml()
        self.container = QWidget.createWindowContainer(map_qml, self)
        self.container.move(0, 0)
        # self.container.resize(640, 480)
        self.show()

    def resizeEvent(self, event):
        self.container.resize(self.width(), self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
