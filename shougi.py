import sys
from PyQt4 import QtCore, QtGui

class Ban(QtGui.QWidget):
    def __init__(self):
        super(Ban, self).__init__()
        # grid layout setting
        self.grid = QtGui.QGridLayout(self)
        for i in range(9):
            for j in range(9):
                self.grid.addWidget(QtGui.QLabel(), i, j)

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # window setting
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('HeppokoShougi')
        # central widget setting
        self.widget = QtGui.QWidget()
        self.vbox = QtGui.QVBoxLayout(self.widget)
        self.ban = Ban()
        self.vbox.addWidget(self.ban)
        self.setCentralWidget(self.widget)

def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
