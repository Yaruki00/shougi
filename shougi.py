import sys
from PyQt4 import QtCore, QtGui

class Ban(QtGui.QWidget):
    def __init__(self, parent):
        super(Ban, self).__init__()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtCore.Qt.black)
        w = self.width()-1
        h = self.height()-1
        for i in range(10):
            qp.drawLine(0, i*h/9, w, i*h/9)
            qp.drawLine(i*w/9, 0, i*w/9, h)

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # window setting
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('HeppokoShougi')
        # central widget setting
        self.widget = QtGui.QWidget()
        self.vbox = QtGui.QVBoxLayout(self.widget)
        self.ban = Ban(self)
        self.vbox.addWidget(self.ban)
        self.setCentralWidget(self.widget)

def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
