import sys
from PyQt4 import QtCore, QtGui

class Mochi(QtGui.QWidget):
    def __init__(self, ban, player):
        super(Mochi, self).__init__()
        self.ban = ban
        self.select = Koma.Nothing
        self.player = player
        if player == Turn.Sente:
            self.koma = {Koma.Sente_Fu: 0,
                         Koma.Sente_Kyou: 0,
                         Koma.Sente_Kei: 0,
                         Koma.Sente_Gin: 0,
                         Koma.Sente_Kin: 0,
                         Koma.Sente_Hisha: 0,
                         Koma.Sente_Kaku: 0}
            self.location1 = {'player': 0,
                             Koma.Sente_Fu: 2,
                             Koma.Sente_Kyou: 3,
                             Koma.Sente_Kei: 4,
                             Koma.Sente_Gin: 5,
                             Koma.Sente_Kin: 6,
                             Koma.Sente_Hisha: 7,
                             Koma.Sente_Kaku: 8}
            self.location2 = {2: Koma.Sente_Fu,
                              3: Koma.Sente_Kyou,
                              4: Koma.Sente_Kei,
                              5: Koma.Sente_Gin,
                              6: Koma.Sente_Kin,
                              7: Koma.Sente_Hisha,
                              8: Koma.Sente_Kaku}
        elif player == Turn.Gote:
            self.koma = {Koma.Gote_Fu: 0,
                         Koma.Gote_Kyou: 0,
                         Koma.Gote_Kei: 0,
                         Koma.Gote_Gin: 0,
                         Koma.Gote_Kin: 0,
                         Koma.Gote_Hisha: 0,
                         Koma.Gote_Kaku: 0}
            self.location1 = {'player': 7,
                              Koma.Gote_Fu: 6,
                              Koma.Gote_Kyou: 5,
                              Koma.Gote_Kei: 4,
                              Koma.Gote_Gin: 3,
                              Koma.Gote_Kin: 2,
                              Koma.Gote_Hisha: 1,
                              Koma.Gote_Kaku: 0}
            self.location2 = {6: Koma.Gote_Fu,
                              5: Koma.Gote_Kyou,
                              4: Koma.Gote_Kei,
                              3: Koma.Gote_Gin,
                              2: Koma.Gote_Kin,
                              1: Koma.Gote_Hisha,
                              0: Koma.Gote_Kaku}
    
    def paintEvent(self, e):
        width = self.width()-1
        height = self.height()-1
        self.w = width/9.0
        qp = QtGui.QPainter()
        qp.begin(self)
        # draw select
        if self.select != Koma.Nothing:
            qp.setBrush(QtGui.QColor(204,255,255))
            qp.drawRect(self.location1[self.select]*self.w, 0,
                        self.w, height)
        # draw lines
        qp.setPen(QtCore.Qt.black)
        qp.drawLine(0, 0, width, 0)
        qp.drawLine(0, 0, 0, height)
        qp.drawLine(0, height, width, height)
        qp.drawLine(width, 0, width, height)
        # draw images
        qp.drawImage(QtCore.QRect(self.location1['player']*self.w, 0,
                                  2*self.w, height),
                     QtGui.QImage(Pictures.Path[self.player]))
        for kind in self.koma.keys():
            if self.koma[kind] > 0:
                qp.drawImage(QtCore.QRect(self.location1[kind]*self.w, 0,
                                          self.w, height),
                             QtGui.QImage(Pictures.Path[kind]))
                if self.koma[kind] > 1:
                    qp.drawText(QtCore.QRectF(self.location1[kind]*self.w, 0,
                                              self.w,height),
                                str(self.koma[kind]))
        qp.end()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x = int(e.x()//self.w)
            # select mochi koma
            if self.select == Koma.Nothing and \
                    self.ban.checkTurn(self.player):
                if x in range(min(self.location2.keys()),
                              max(self.location2.keys())+1) and \
                        self.koma[self.location2[x]] > 0:
                    self.select = self.location2[x]
                    self.update()
                    self.ban.calcCandidates(self.select, True)
            else:
                self.ban.cancelSelect()

    def resetSelect(self):
        self.select = Koma.Nothing
        self.update()

    def addKoma(self, koma):
        self.koma[koma] += 1
        self.update()

    def subKoma(self, koma):
        self.koma[koma] -= 1
        self.select = Koma.Nothing
        self.update()

class Ban(QtGui.QWidget):
    def __init__(self):
        super(Ban, self).__init__()
        self.state = {}
        for i in range(9):
            for j in range(9):
                if i in range(3, 6) or \
                        (i == 1 or i == 7) and \
                        (j == 0 or j in range(2, 7) or j == 8):
                    self.state[(j, i)] = Koma.Nothing
                elif i == 2:
                    self.state[(j, i)] = Koma.Gote_Fu
                elif i == 6:
                    self.state[(j, i)] = Koma.Sente_Fu
                elif i == 0:
                    if j == 0 or j == 8:
                        self.state[(j, i)] = Koma.Gote_Kyou
                    elif j == 1 or j == 7:
                        self.state[(j, i)] = Koma.Gote_Kei
                    elif j == 2 or j == 6:
                        self.state[(j, i)] = Koma.Gote_Gin
                    elif j == 3 or j == 5:
                        self.state[(j, i)] = Koma.Gote_Kin
                    elif j == 4:
                        self.state[(j, i)] = Koma.Gote_Gyoku
                elif i == 8:
                    if j == 0 or j == 8:
                        self.state[(j, i)] = Koma.Sente_Kyou
                    elif j == 1 or j == 7:
                        self.state[(j, i)] = Koma.Sente_Kei
                    elif j == 2 or j == 6:
                        self.state[(j, i)] = Koma.Sente_Gin
                    elif j == 3 or j == 5:
                        self.state[(j, i)] = Koma.Sente_Kin
                    elif j == 4:
                        self.state[(j, i)] = Koma.Sente_Gyoku
                elif i == 1 and j == 1:
                    self.state[(j, i)] = Koma.Gote_Hisha
                elif i == 1 and j == 7:
                    self.state[(j, i)] = Koma.Gote_Kaku
                elif i == 7 and j == 1:
                    self.state[(j, i)] = Koma.Sente_Kaku
                elif i == 7 and j == 7:
                    self.state[(j, i)] = Koma.Sente_Hisha
        self.turn = Turn.Sente
        self.select = ()
        self.mochi_select = Koma.Nothing
        self.candidates = []

    def paintEvent(self, e):
        width = self.width()-1
        height = self.height()-1
        self.w = width/9.0
        self.h = height/9.0
        qp = QtGui.QPainter()
        qp.begin(self)
        # draw select
        if self.select != ():
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
                if self.state[(i, j)] != Koma.Nothing:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage(Pictures.Path[self.state[(i, j)]]))
        qp.end()
        
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x = int(e.x()//self.w)
            y = int(e.y()//self.h)
            # select koma on ban
            if self.select == () and \
                    self.state[(x, y)] in Koma.jigoma(self.turn):
                self.select = (x, y)
                self.calcCandidates(self.state[(x, y)], False, x, y)
                self.update()
            # move or put koma
            elif (x, y) in self.candidates:
                # move
                if self.select != ():
                    if self.state[(x, y)] in Koma.Gote_Koma:
                        self.sente_mochi.addKoma(
                            Koma.changePlayer(self.state[(x, y)]))
                    elif self.state[(x, y)] in Koma.Sente_Koma:
                        self.gote_mochi.addKoma(
                            Koma.changePlayer(self.state[(x, y)]))
                    if self.state[self.select] in Koma.Nareru \
                            and y in Jin.tekijin(self.turn):
                        if Jin.naru(self.state[self.select], y) or \
                                self.askNari():
                            self.state[(x, y)] = Koma.naru(
                                self.state[self.select], self.turn)
                        else:
                            self.state[(x, y)] = self.state[self.select]
                    else:
                        self.state[(x, y)] = self.state[self.select]
                    self.state[self.select] = Koma.Nothing
                    self.select = ()
                # put
                else:
                    self.state[(x, y)] = self.mochi_select
                    if self.turn == Turn.Sente:
                        self.sente_mochi.subKoma(self.mochi_select)
                    else:
                        self.gote_mochi.subKoma(self.mochi_select)
                    self.mochi_select = Koma.Nothing
                # common
                self.candidates = []
                self.turn = Turn.changeTurn(self.turn)
                self.update()
            # cancel
            else:
                self.cancelSelect()

    def calcCandidates(self, koma, mochi, x=0, y=0):
        # koma on ban
        if mochi == False:
            movable = self.calcMovable(koma, self.turn, x, y)
            if koma in Koma.Hashiri:
                for direction in movable:
                    for masu in direction:
                        if masu[0] in range(9) and masu[1] in range(9):
                            if self.state[masu] == Koma.Nothing:
                                self.candidates.append(masu)
                            elif self.state[masu] in Koma.teki(koma):
                                self.candidates.append(masu)
                                break
                            else:
                                break
            else:
                for masu in movable:
                    if masu[0] in range(9) and masu[1] in range(9):
                        if self.state[masu] in Koma.available(koma):
                            self.candidates.append(masu)
        # mochi koma
        else:
            if koma in Koma.Sente_Koma:
                if koma == Koma.Sente_Fu:
                    for i in range(9):
                        row = []
                        for j in range(1, 9):
                            if self.state[(i, j)] == Koma.Nothing:
                                row.append((i, j))
                            elif self.state[(i, j)] == Koma.Sente_Fu:
                                row = []
                                break
                        self.candidates.extend(row)
                else:
                    if koma == Koma.Sente_Kyou:
                        start = 1
                    elif koma == Koma.Sente_Kei:
                        start = 2
                    else:
                        start = 0
                    for i in range(9):
                        for j in range(start, 9):
                            if self.state[(i, j)] == Koma.Nothing:
                                self.candidates.append((i, j))
            else:
                if koma == Koma.Gote_Fu:
                    for i in range(9):
                        row = []
                        for j in range(0, 8):
                            if self.state[(i, j)] == Koma.Nothing:
                                row.append((i, j))
                            elif self.state[(i, j)] == Koma.Gote_Fu:
                                row = []
                                break
                        self.candidates.extend(row)
                else:
                    if koma == Koma.Gote_Kyou:
                        end = 8
                    elif koma == Koma.Gote_Kei:
                        end = 7
                    else:
                        end = 9
                    for i in range(9):
                        for j in range(0, end):
                            if self.state[(i, j)] == Koma.Nothing:
                                self.candidates.append((i, j))
            self.mochi_select = koma
            self.update()

    def calcMovable(self, koma, turn, x, y):
        movable = []
        if abs(koma) == Koma.Sente_Fu:
            movable.append((x, y-1*turn))
        elif koma == Koma.Sente_Kyou:
            direction = []
            for i in range(1, y+1):
                direction.append((x, y-i))
            movable.append(direction)
        elif koma == Koma.Gote_Kyou:
            direction = []
            for i in range(1, 9-y):
                direction.append((x, y+i))
            movable.append(direction)
        elif abs(koma) == Koma.Sente_Kei:
            movable.extend([(x+1, y-2*turn), (x-1, y-2*turn)])
        elif abs(koma) == Koma.Sente_Gin:
            movable.extend([(x, y-1*turn), (x-1, y-1*turn), (x+1, y-1*turn),
                            (x-1, y+1*turn), (x+1, y+1*turn)])
        elif abs(koma) in Koma.Sente_KinFamily:
            movable.extend[(x, y-1*turn), (x-1, y-1*turn), (x+1, y-1*turn),
                           (x-1, y), (x+1, y), (x, y+1*turn)]
        elif koma in Koma.HishaGroup:
            direction = []
            for i in range(1, y+1):
                direction.append((x, y-i))
            movable.append(direction)
            direction = []
            for i in range(1, 9-y):
                direction.append((x, y+i))
            movable.append(direction)
            direction = []
            for i in range(1, x+1):
                direction.append((x-i, y))
            movable.append(direction)
            direction = []
            for i in range(1, 9-x):
                direction.append((x+i, y))
            movable.append(direction)
            if koma == Koma.Sente_NariHisha or koma == Koma.Gote_NariHisha:
                movable.extend([[(x-1, y-1)], [(x+1, y-1)],
                                [(x-1, y+1)], [(x+1, y+1)]])
        elif koma in Koma.KakuGroup:
            direction = []
            for i in range(1, min(x+1, y+1)):
                direction.append((x-i, y-i))
            movable.append(direction)
            direction = []
            for i in range(1, min(x+1, 9-y)):
                direction.append((x-i, y+i))
            movable.append(direction)
            direction = []
            for i in range(1, min(9-x, y+1)):
                direction.append((x+i, y-i))
            movable.append(direction)
            direction = []
            for i in range(1, min(9-x, 9-y)):
                direction.append((x+i, y+i))
            movable.append(direction)
            if koma == Koma.Sente_NariKaku or koma == Koma.Gote_NariKaku:
                    movable.extend([[(x, y-1)], [(x, y+1)],
                                    [(x-1, y)], [(x+1, y)]])
        elif koma == Koma.Sente_Gyoku or koma == Koma.Gote_Gyoku:
                movable.extend([(x, y-1), (x, y+1), (x-1, y), (x+1, y)
                                (x-1, y-1), (x+1, y-1),
                                (x-1, y+1), (x+1, y+1)])
        return movable

    def setMochi(self, sente, gote):
        self.sente_mochi = sente
        self.gote_mochi = gote

    def checkTurn(self, turn):
        if turn == self.turn:
            return True
        else:
            return False

    def cancelSelect(self):
        if self.select != ():
            self.select = ()
            self.candidates = []
            self.update()
        elif self.turn == Turn.Sente and self.mochi_select != Koma.Nothing:
            self.sente_mochi.resetSelect()
            self.candidates = []
            self.update()
        elif self.turn == Turn.Gote and self.mochi_select != Koma.Nothing:
            self.gote_mochi.resetSelect()
            self.candidates = []
            self.update()

    def askNari(self):
        reply = QtGui.QMessageBox.question(self,
                                           'Nari',
                                           "Narimasuka??",
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

class Koma:
    Nothing = 0
    Sente_Fu = 2
    Sente_Kyou = 3
    Sente_Kei = 4
    Sente_Gin = 5
    Sente_Hisha = 6
    Sente_Kaku = 7
    Sente_Kin = 8
    Sente_NariFu = 9
    Sente_NariKyou = 10
    Sente_NariKei = 11
    Sente_NariGin = 12
    Sente_NariHisha = 13
    Sente_NariKaku = 14
    Sente_Gyoku = 15
    Gote_Fu = -2
    Gote_Kyou = -3
    Gote_Kei = -4
    Gote_Gin = -5
    Gote_Hisha = -6
    Gote_Kaku = -7
    Gote_Kin = -8
    Gote_NariFu = -9
    Gote_NariKyou = -10
    Gote_NariKei = -11
    Gote_NariGin = -12
    Gote_NariHisha = -13
    Gote_NariKaku = -14
    Gote_Gyoku = -15
    Sente_Koma = range(Sente_Fu, Sente_Gyoku+1)
    Gote_Koma = range(Gote_Fu, Gote_Gyoku-1, -1)
    All = Sente_Koma + Gote_Koma
    Sente_FuKyou = [Sente_Fu] + [Sente_Kyou]
    Gote_FuKyou = [Gote_Fu] + [Gote_Kyou]
    Sente_Nareru = range(Sente_Fu, Sente_Kaku+1)
    Gote_Nareru = range(Gote_Fu, Gote_Kaku-1, -1)
    Nareru = Sente_Nareru + Gote_Nareru
    Sente_KinFamily = range(Sente_NariFu, Sente_NariGin+1) + [Sente_Kin]
    Gote_KinFamily = range(Gote_NariFu, Gote_NariGin-1, -1) + [Gote_Kin]
    HishaGroup = [Sente_Hisha, Sente_NariHisha, Gote_Hisha, Gote_NariHisha]
    KakuGroup = [Sente_Kaku, Sente_NariKaku, Gote_Kaku, Gote_NariKaku]
    Sente_Hashiri = [Sente_Kyou, Sente_Hisha, Sente_NariHisha, 
                     Sente_Kaku, Sente_NariKaku]
    Gote_Hashiri = [Gote_Kyou, Gote_Hisha, Gote_NariHisha,
                    Gote_Kaku, Gote_NariKaku]
    Hashiri = Sente_Hashiri + Gote_Hashiri
    Sente_Available = Gote_Koma + [Nothing]
    Gote_Available = Sente_Koma + [Nothing]

    @classmethod
    def changePlayer(self, koma):
        if abs(koma) > 8:
            return -koma - 7
        else:
            return -koma

    @classmethod
    def naru(self, koma, turn):
        return koma + 7*turn

    @classmethod
    def teki(self, koma):
        if koma > 0:
            return self.Gote_Koma
        elif koma < 0:
            return self.Sente_Koma

    @classmethod
    def available(self, koma):
        if koma > 0:
            return self.Sente_Available
        elif koma < 0:
            return self.Gote_Available

    @classmethod
    def jigoma(self, turn):
        if turn == Turn.Sente:
            return self.Sente_Koma
        elif turn == Turn.Gote:
            return self.Gote_Koma

class Turn:
    Sente = 1
    Gote = -1

    @classmethod
    def changeTurn(self, turn):
        return turn * -1

class Jin:
    Sente_Tekijin = range(0, 3)
    Gote_Tekijin = range(6, 9)
    Sente_FuKyouNaru = 0
    Gote_FuKyouNaru = 8
    Sente_KeiNaru = range(0, 2)
    Gote_KeiNaru = range(7, 9)

    @classmethod
    def tekijin(self, turn):
        if turn == Turn.Sente:
            return self.Sente_Tekijin
        elif turn == Turn.Gote:
            return self.Gote_Tekijin

    @classmethod
    def naru(self, koma, y):
        if koma in Koma.Sente_FuKyou and y == self.Sente_FuKyouNaru or \
                koma in Koma.Gote_FuKyou and y == self.Gote_FuKyouNaru or \
                koma == Koma.Sente_Kei and y in self.Sente_KeiNaru or \
                koma == Koma.Gote_Kei and y in self.Gote_KeiNaru:
            return True
        else:
            return False
        

class Pictures:
    Path = {
        Koma.Sente_Fu: './Pictures/Sente_Fu.png',
        Koma.Sente_Kyou: './Pictures/Sente_Kyou.png',
        Koma.Sente_Kei: './Pictures/Sente_Kei.png',
        Koma.Sente_Gin: './Pictures/Sente_Gin.png',
        Koma.Sente_Hisha: './Pictures/Sente_Hisha.png',
        Koma.Sente_Kaku: './Pictures/Sente_Kaku.png',
        Koma.Sente_Kin: './Pictures/Sente_Kin.png',
        Koma.Sente_NariFu: './Pictures/Sente_NariFu.png',
        Koma.Sente_NariKyou: './Pictures/Sente_NariKyou.png',
        Koma.Sente_NariKei: './Pictures/Sente_NariKei.png',
        Koma.Sente_NariGin: './Pictures/Sente_NariGin.png',
        Koma.Sente_NariHisha: './Pictures/Sente_NariHisha.png',
        Koma.Sente_NariKaku: './Pictures/Sente_NariKaku.png',
        Koma.Sente_Gyoku: './Pictures/Sente_Gyoku.png',
        Koma.Gote_Fu: './Pictures/Gote_Fu.png',
        Koma.Gote_Kyou: './Pictures/Gote_Kyou.png',
        Koma.Gote_Kei: './Pictures/Gote_Kei.png',
        Koma.Gote_Gin: './Pictures/Gote_Gin.png',
        Koma.Gote_Hisha: './Pictures/Gote_Hisha.png',
        Koma.Gote_Kaku: './Pictures/Gote_Kaku.png',
        Koma.Gote_Kin: './Pictures/Gote_Kin.png',
        Koma.Gote_NariFu: './Pictures/Gote_NariFu.png',
        Koma.Gote_NariKyou: './Pictures/Gote_NariKyou.png',
        Koma.Gote_NariKei: './Pictures/Gote_NariKei.png',
        Koma.Gote_NariGin: './Pictures/Gote_NariGin.png',
        Koma.Gote_NariHisha: './Pictures/Gote_NariHisha.png',
        Koma.Gote_NariKaku: './Pictures/Gote_NariKaku.png',
        Koma.Gote_Gyoku: './Pictures/Gote_Gyoku.png',
        Turn.Sente: './Pictures/Sente.png',
        Turn.Gote: './Pictures/Gote.png' }

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # window setting
        self.setGeometry(0, 0, 800, 1000)
        self.setWindowTitle('HeppokoShougi')
        # central widget setting
        self.widget = QtGui.QWidget()
        self.grid = QtGui.QGridLayout(self.widget)
        self.ban = Ban()
        self.sente_mochi = Mochi(self.ban, Turn.Sente)
        self.gote_mochi = Mochi(self.ban, Turn.Gote)
        self.ban.setMochi(self.sente_mochi, self.gote_mochi)
        self.grid.addWidget(self.gote_mochi, 0, 0, 1, 1)
        self.grid.addWidget(self.ban, 1, 0, 9, 1)
        self.grid.addWidget(self.sente_mochi, 11, 0, 1, 1)
        self.setCentralWidget(self.widget)

def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
