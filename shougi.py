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
        self.turn = Turn.Sente
        self.select = []
        self.candidates = []

    def paintEvent(self, e):
        width = self.width()-1
        height = self.height()-1
        self.w = width/9.0
        self.h = height/9.0
        qp = QtGui.QPainter()
        qp.begin(self)
        # draw select
        if self.select != []:
            qp.setBrush(QtGui.QColor(204,255,255))
            qp.drawRect(self.select[0]*self.w, self.select[1]*self.h,
                        self.w, self.h)
        # draw candidates
        if self.candidates != []:
            qp.setBrush(QtGui.QColor(204,255,204))
            for candidate in self.candidates:
                qp.drawRect(candidate[0]*self.w, candidate[1]*self.h,
                        self.w, self.h)
        # draw lines
        qp.setPen(QtCore.Qt.black)
        for i in range(10):
            qp.drawLine(0, i*self.h, width, i*self.h)
            qp.drawLine(i*self.w, 0, i*self.w, height)
        # draw images
        for i in range(9):
            for j in range(9):
                if self.state[i][j] == Koma.Sente_Fu:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Fu.png'))
                elif self.state[i][j] == Koma.Sente_Kyou:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Kyou.png'))
                elif self.state[i][j] == Koma.Sente_Kei:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Kei.png'))
                elif self.state[i][j] == Koma.Sente_Gin:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Gin.png'))
                elif self.state[i][j] == Koma.Sente_Kin:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Kin.png'))
                elif self.state[i][j] == Koma.Sente_Hisha:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Hisha.png'))
                elif self.state[i][j] == Koma.Sente_Kaku:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Kaku.png'))
                elif self.state[i][j] == Koma.Sente_Gyoku:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Sente_Gyoku.png'))
                elif self.state[i][j] == Koma.Gote_Fu:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Fu.png'))
                elif self.state[i][j] == Koma.Gote_Kyou:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Kyou.png'))
                elif self.state[i][j] == Koma.Gote_Kei:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Kei.png'))
                elif self.state[i][j] == Koma.Gote_Gin:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Gin.png'))
                elif self.state[i][j] == Koma.Gote_Kin:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Kin.png'))
                elif self.state[i][j] == Koma.Gote_Hisha:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Hisha.png'))
                elif self.state[i][j] == Koma.Gote_Kaku:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Kaku.png'))
                elif self.state[i][j] == Koma.Gote_Gyoku:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage('./Pictures/Gote_Gyoku.png'))
        qp.end()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x = int(e.x()//self.w)
            y = int(e.y()//self.h)
            # select koma on ban
            if self.select == [] and self.state[x][y]-self.turn*(Koma.Gote_Fu-Koma.Sente_Fu) in Koma.Sente_Koma:
                self.select = [x, y]
                self.calcCandidates(
                    self.state[x][y],
                    False,
                    x,
                    y)
                self.update()
            elif [x, y] in self.candidates:
                if self.select != []:
                    self.state[x][y] = self.state[self.select[0]][self.select[1]]
                    self.state[self.select[0]][self.select[1]] = Koma.Nothing
                    self.select = []
                self.candidates = []
                self.turn = self.turn ^ 1
                self.update()
            else:
                self.select = []
                self.candidates = []
                self.update()

    def calcCandidates(self, koma, mochi, x, y):
        if mochi == False:
            movable = self.calcMovable(koma, x, y)
            if koma in Koma.Sente_Koma:
                if koma in Koma.Sente_Hashiri:
                    for direction in movable:
                        for masu in direction:
                            if self.state[masu[0]][masu[1]] == Koma.Nothing:
                                self.candidates.append(masu)
                            elif self.state[masu[0]][masu[1]] in Koma.Gote_Koma:
                                self.candidates.append(masu)
                                break
                            else:
                                break
                else:
                    for masu in movable:
                        if self.state[masu[0]][masu[1]] in Koma.Sente_Available:
                            self.candidates.append(masu)
            elif koma in Koma.Gote_Koma:
                if koma in Koma.Gote_Hashiri:
                    for direction in movable:
                        for masu in direction:
                            if self.state[masu[0]][masu[1]] == Koma.Nothing:
                                self.candidates.append(masu)
                            elif self.state[masu[0]][masu[1]] in Koma.Sente_Koma:
                                self.candidates.append(masu)
                                break
                            else:
                                break
                else:
                    for masu in movable:
                        if self.state[masu[0]][masu[1]] in Koma.Gote_Available:
                            self.candidates.append(masu)
        elif mochi == True:
            '''not implemented'''
        else:
            return

    def calcMovable(self, koma, x, y):
        movable = []
        if koma == Koma.Sente_Fu:
            movable.append([x, y-1])
        elif koma == Koma.Gote_Fu:
            movable.append([x, y+1])
        elif koma == Koma.Sente_Kyou:
            direction = []
            for i in range(1, y+1):
                direction.append([x, y-i])
            movable.append(direction)
        elif koma == Koma.Gote_Kyou:
            direction = []
            for i in range(1, 8-y):
                direction.append([x, y+i])
            movable.append(direction)
        elif koma == Koma.Sente_Kei:
            if x > 0:
                movable.append([x-1, y-2])
            if x < 8:
                movable.append([x+1, y-2])
        elif koma == Koma.Gote_Kei:
            if x > 0:
                movable.append([x-1, y+2])
            if x < 8:
                movable.append([x+1, y+2])
        elif koma == Koma.Sente_Gin:
            if y > 0:
                movable.append([x, y-1])
            if y > 0 and x > 0:
                movable.append([x-1, y-1])
            if y > 0 and x < 8:
                movable.append([x+1, y-1])
            if y < 8 and x > 0:
                movable.append([x-1, y+1])
            if y < 8 and x < 8:
                movable.append([x+1, y+1])
        elif koma == Koma.Gote_Gin:
            if y < 8:
                movable.append([x, y+1])
            if y < 8 and x > 0:
                movable.append([x-1, y+1])
            if y < 8 and x < 8:
                movable.append([x+1, y+1])
            if y > 0 and x > 0:
                movable.append([x-1, y-1])
            if y > 0 and x < 8:
                movable.append([x+1, y-1])
        elif koma in Koma.Sente_KinFamily:
            if y > 0:
                movable.append([x, y-1])
            if y > 0 and x > 0:
                movable.append([x-1, y-1])
            if y > 0 and x < 8:
                movable.append([x+1, y-1])
            if x > 0:
                movable.append([x-1, y])
            if x < 8:
                movable.append([x+1, y])
            if y < 8:
                movable.append([x, y+1])
        elif koma in Koma.Gote_KinFamily:
            if y < 8:
                movable.append([x, y+1])
            if y < 8 and x > 0:
                movable.append([x-1, y+1])
            if y < 8 and x < 8:
                movable.append([x+1, y+1])
            if x > 0:
                movable.append([x-1, y])
            if x < 8:
                movable.append([x+1, y])
            if y > 0:
                movable.append([x, y-1])
        elif koma in Koma.HishaGroup:
            direction = []
            for i in range(1, y+1):
                direction.append([x, y-i])
            movable.append(direction)
            direction = []
            for i in range(1, 9-y):
                direction.append([x, y+i])
            movable.append(direction)
            direction = []
            for i in range(1, x+1):
                direction.append([x-i, y])
            movable.append(direction)
            direction = []
            for i in range(1, 9-x):
                direction.append([x+i, y])
            movable.append(direction)
            if koma == Koma.Sente_NariHisha or koma == Koma.Gote_NariHisha:
                if y > 0 and x > 0:
                    movable.append([[x-1, y-1]])
                if y > 0 and x < 8:
                    movable.append([[x+1, y-1]])
                if y < 8 and x > 0:
                    movable.append([[x-1, y+1]])
                if y < 8 and x < 8:
                    movable.append([[x+1, y+1]])
        elif koma in Koma.KakuGroup:
            direction = []
            for i in range(1, min(x+1, y+1)):
                direction.append([x-i, y-i])
            movable.append(direction)
            direction = []
            for i in range(1, min(x+1, 9-y)):
                direction.append([x-i, y+i])
            movable.append(direction)
            direction = []
            for i in range(1, min(9-x, y+1)):
                direction.append([x+i, y-i])
            movable.append(direction)
            direction = []
            for i in range(1, min(9-x, 9-y)):
                direction.append([x+i, y+i])
            movable.append(direction)
            if koma == Koma.Sente_NariKaku or koma == Koma.Gote_NariKaku:
                if y > 0:
                    movable.append([[x, y-1]])
                if y < 8:
                    movable.append([[x, y+1]])
                if x > 0:
                    movable.append([[x-1, y]])
                if x < 8:
                    movable.append([[x+1, y]])
        elif koma == Koma.Sente_Gyoku or koma == Koma.Gote_Gyoku:
            if y > 0:
                movable.append([x, y-1])
            if y < 8:
                movable.append([x, y+1])
            if x > 0:
                movable.append([x-1, y])
            if x < 8:
                movable.append([x+1, y])
            if y > 0 and x > 0:
                movable.append([x-1, y-1])
            if y > 0 and x < 8:
                movable.append([x+1, y-1])
            if y < 8 and x > 0:
                movable.append([x-1, y+1])
            if y < 8 and x < 8:
                movable.append([x+1, y+1])
        return movable

class Koma:
    Nothing = 0
    Sente_Fu = 1
    Sente_Kyou = 2
    Sente_Kei = 3
    Sente_Gin = 4
    Sente_Kin = 5
    Sente_Hisha = 6
    Sente_Kaku = 7
    Sente_NariFu = 8
    Sente_NariKyou = 9
    Sente_NariKei = 10
    Sente_NariGin = 11
    Sente_NariHisha = 12
    Sente_NariKaku = 13
    Sente_Gyoku = 14
    Gote_Fu = 15
    Gote_Kyou = 16
    Gote_Kei = 17
    Gote_Gin = 18
    Gote_Kin = 19
    Gote_Hisha = 20
    Gote_Kaku = 21
    Gote_NariFu = 22
    Gote_NariKyou = 23
    Gote_NariKei = 24
    Gote_NariGin = 25
    Gote_NariHisha = 26
    Gote_NariKaku = 27
    Gote_Gyoku = 28
    Sente_Koma = range(Sente_Fu, Sente_Gyoku+1)
    Gote_Koma = range(Gote_Fu, Gote_Gyoku+1)
    Sente_Nareru = range(Sente_Fu, Sente_Kaku+1)
    Gote_Nareru = range(Gote_Fu, Gote_Kaku+1)
    Sente_KinFamily = range(Sente_NariFu, Sente_NariGin+1) + [Sente_Kin]
    Gote_KinFamily = range(Gote_NariFu, Gote_NariGin+1) + [Gote_Kin]
    HishaGroup = [Sente_Hisha, Sente_NariHisha, Gote_Hisha, Gote_NariHisha]
    KakuGroup = [Sente_Kaku, Sente_NariKaku, Gote_Kaku, Gote_NariKaku]
    Sente_Hashiri = [Sente_Kyou, Sente_Hisha, Sente_NariHisha, 
                     Sente_Kaku, Sente_NariKaku]
    Gote_Hashiri = [Gote_Kyou, Gote_Hisha, Gote_NariKaku,
                    Gote_Kaku, Gote_NariKaku]
    Sente_Available = Gote_Koma + [Nothing]
    Gote_Available = Sente_Koma + [Nothing]

class Turn:
    Sente = 0
    Gote = 1

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
