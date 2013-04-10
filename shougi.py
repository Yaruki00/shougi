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
                if self.state[i][j] != Koma.Nothing:
                    qp.drawImage(QtCore.QRect(i*self.w, j*self.h,
                                              self.w, self.h),
                                 QtGui.QImage(Pictures.Path[self.state[i][j]]))
        qp.end()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x = int(e.x()//self.w)
            y = int(e.y()//self.h)
            # select koma on ban
            if self.select == [] and \
                    (self.state[x][y] in Koma.Sente_Koma and \
                         self.turn == Turn.Sente or \
                         self.state[x][y] in Koma.Gote_Koma and \
                         self.turn == Turn.Gote):
                self.select = [x, y]
                self.calcCandidates(
                    self.state[x][y],
                    False,
                    x,
                    y)
                self.update()
            # move or put koma
            elif [x, y] in self.candidates:
                # move
                if self.select != []:
                    if self.state[x][y] in Koma.Sente_Koma:
                        if self.state[x][y] in Koma.Sente_Nareru + [Koma.Sente_Kin]:
                            self.gote_mochi.addKoma(self.state[x][y]+14)
                        else:
                            self.gote_mochi.addKoma(self.state[x][y]+7)
                    elif self.state[x][y] in Koma.Gote_Koma:
                        if self.state[x][y] in Koma.Gote_Nareru + [Koma.Gote_Kin]:
                            self.sente_mochi.addKoma(self.state[x][y]-14)
                        else:
                            self.sente_mochi.addKoma(self.state[x][y]-21)
                    if self.state[self.select[0]][self.select[1]] in Koma.Nareru \
                            and (self.turn == Turn.Sente and y < 3 or \
                                     self.turn == Turn.Gote and y > 5):
                        if y == 0 and (self.state[self.select[0]][self.select[1]] == Koma.Sente_Fu or self.state[self.select[0]][self.select[1]] == Koma.Sente_Kyou) or \
                                y < 2 and self.state[self.select[0]][self.select[1]] == Koma.Sente_Kei or \
                                y == 8 and (self.state[self.select[0]][self.select[1]] == Koma.Gote_Fu or self.state[self.select[0]][self.select[1]] == Koma.Gote_Kyou) or \
                                y > 6 and self.state[self.select[0]][self.select[1]] == Koma.Gote_Kei:
                                
                            self.state[x][y] = self.state[self.select[0]][self.select[1]] + 7
                        elif self.askNari():
                            self.state[x][y] = self.state[self.select[0]][self.select[1]] + 7
                        else:
                            self.state[x][y] = self.state[self.select[0]][self.select[1]]
                    else:
                        self.state[x][y] = self.state[self.select[0]][self.select[1]]
                    self.state[self.select[0]][self.select[1]] = Koma.Nothing
                    self.select = []
                # put
                else:
                    self.state[x][y] = self.mochi_select
                    if self.turn == Turn.Sente:
                        self.sente_mochi.subKoma(self.mochi_select)
                    else:
                        self.gote_mochi.subKoma(self.mochi_select)
                    self.mochi_select = Koma.Nothing
                # common
                self.candidates = []
                self.turn = self.turn ^ 1
                self.update()
            # cancel
            else:
                self.cancelSelect()

    def calcCandidates(self, koma, mochi, x=0, y=0):
        # koma on ban
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
        # mochi koma
        else:
            if koma in Koma.Sente_Koma:
                if koma == Koma.Sente_Fu:
                    for i in range(9):
                        row = []
                        for j in range(1, 9):
                            if self.state[i][j] == Koma.Nothing:
                                row.append([i, j])
                            elif self.state[i][j] == Koma.Sente_Fu:
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
                            if self.state[i][j] == Koma.Nothing:
                                self.candidates.append([i, j])
            else:
                if koma == Koma.Gote_Fu:
                    for i in range(9):
                        row = []
                        for j in range(0, 8):
                            if self.state[i][j] == Koma.Nothing:
                                row.append([i, j])
                            elif self.state[i][j] == Koma.Gote_Fu:
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
                            if self.state[i][j] == Koma.Nothing:
                                self.candidates.append([i, j])
            self.mochi_select = koma
            self.update()

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
            for i in range(1, 9-y):
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

    def setMochi(self, sente, gote):
        self.sente_mochi = sente
        self.gote_mochi = gote

    def checkTurn(self, turn):
        if turn == self.turn:
            return True
        else:
            return False

    def cancelSelect(self):
        if self.select != []:
            self.select = []
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
    Sente_Fu = 1
    Sente_Kyou = 2
    Sente_Kei = 3
    Sente_Gin = 4
    Sente_Hisha = 5
    Sente_Kaku = 6
    Sente_Kin = 7
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
    Gote_Hisha = 19
    Gote_Kaku = 20
    Gote_Kin = 21
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
    Nareru = Sente_Nareru + Gote_Nareru
    Sente_KinFamily = range(Sente_NariFu, Sente_NariGin+1) + [Sente_Kin]
    Gote_KinFamily = range(Gote_NariFu, Gote_NariGin+1) + [Gote_Kin]
    HishaGroup = [Sente_Hisha, Sente_NariHisha, Gote_Hisha, Gote_NariHisha]
    KakuGroup = [Sente_Kaku, Sente_NariKaku, Gote_Kaku, Gote_NariKaku]
    Sente_Hashiri = [Sente_Kyou, Sente_Hisha, Sente_NariHisha, 
                     Sente_Kaku, Sente_NariKaku]
    Gote_Hashiri = [Gote_Kyou, Gote_Hisha, Gote_NariHisha,
                    Gote_Kaku, Gote_NariKaku]
    Sente_Available = Gote_Koma + [Nothing]
    Gote_Available = Sente_Koma + [Nothing]

class Turn:
    Sente = 30
    Gote = 31

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
