import sys
from PyQt4 import QtCore, QtGui

class Ban(QtGui.QWidget):
    def __init__(self, parent):
        super(Ban, self).__init__()
        self.state = [[Koma.Gote_Kyou,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Kyou],
                      [Koma.Gote_Kei,
                       Koma.Gote_Hisha,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Sente_Kaku,
                       Koma.Sente_Kei],
                      [Koma.Gote_Gin,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Gin],
                      [Koma.Gote_Kin,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Kin],
                      [Koma.Gote_Gyoku,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Gyoku],
                      [Koma.Gote_Kin,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Kin],
                      [Koma.Gote_Gin,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Gin],
                      [Koma.Gote_Kei,
                       Koma.Gote_Kaku,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Sente_Hisha,
                       Koma.Sente_Kei],
                      [Koma.Gote_Kyou,
                       Koma.Nothing,
                       Koma.Gote_Fu,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Nothing,
                       Koma.Sente_Fu,
                       Koma.Nothing,
                       Koma.Sente_Kyou]]

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        # draw lines
        qp.setPen(QtCore.Qt.black)
        width = self.width()-1
        height = self.height()-1
        w = width/9.0
        h = height/9.0
        for i in range(10):
            qp.drawLine(0, i*h, width, i*h)
            qp.drawLine(i*w, 0, i*w, height)
        # draw images
        for i in range(9):
            for j in range(9):
                if self.state[i][j] == Koma.Sente_Fu:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Fu.png'))
                elif self.state[i][j] == Koma.Sente_Kyou:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Kyou.png'))
                elif self.state[i][j] == Koma.Sente_Kei:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Kei.png'))
                elif self.state[i][j] == Koma.Sente_Gin:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Gin.png'))
                elif self.state[i][j] == Koma.Sente_Kin:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Kin.png'))
                elif self.state[i][j] == Koma.Sente_Hisha:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Hisha.png'))
                elif self.state[i][j] == Koma.Sente_Kaku:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Kaku.png'))
                elif self.state[i][j] == Koma.Sente_Gyoku:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Sente_Gyoku.png'))
                elif self.state[i][j] == Koma.Gote_Fu:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Fu.png'))
                elif self.state[i][j] == Koma.Gote_Kyou:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Kyou.png'))
                elif self.state[i][j] == Koma.Gote_Kei:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Kei.png'))
                elif self.state[i][j] == Koma.Gote_Gin:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Gin.png'))
                elif self.state[i][j] == Koma.Gote_Kin:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Kin.png'))
                elif self.state[i][j] == Koma.Gote_Hisha:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Hisha.png'))
                elif self.state[i][j] == Koma.Gote_Kaku:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Kaku.png'))
                elif self.state[i][j] == Koma.Gote_Gyoku:
                    qp.drawImage(QtCore.QRect(i*w, j*h, w, h),
                                 QtGui.QImage('./Pictures/Gote_Gyoku.png'))
        qp.end()

        
class Koma:
    Nothing = 0
    Sente_Fu = 1
    Sente_Kyou = 2
    Sente_Kei = 3
    Sente_Gin = 4
    Sente_Kin = 5
    Sente_Hisha = 6
    Sente_Kaku = 7
    Sente_Gyoku = 8
    Gote_Fu = 9
    Gote_Kyou = 10
    Gote_Kei = 11
    Gote_Gin = 12
    Gote_Kin = 13
    Gote_Hisha = 14
    Gote_Kaku = 15
    Gote_Gyoku = 16

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # window setting
        self.setGeometry(0, 0, 800, 1000)
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
