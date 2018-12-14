import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QApplication, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter


class MyWidget(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi('Виселица.ui', self)
        self.setWindowTitle('Виселица')
        self.run()
        self.btn1.clicked.connect(self.run_btn1)
        self.btn2.clicked.connect(self.run_btn2)
        self.btna.clicked.connect(self.run_btna)
        self.btnb.clicked.connect(self.run_btnb)
        self.btnv.clicked.connect(self.run_btnv)
        self.btng.clicked.connect(self.run_btng)
        self.btnd.clicked.connect(self.run_btnd)
        self.btne.clicked.connect(self.run_btne)
        self.btne2.clicked.connect(self.run_btne2)
        self.btnzh.clicked.connect(self.run_btnzh)
        self.btnz.clicked.connect(self.run_btnz)
        self.btni.clicked.connect(self.run_btni)
        self.btny.clicked.connect(self.run_btny)
        self.btnk.clicked.connect(self.run_btnk)
        self.btnl.clicked.connect(self.run_btnl)
        self.btnm.clicked.connect(self.run_btnm)
        self.btnn.clicked.connect(self.run_btnn)
        self.btno.clicked.connect(self.run_btno)
        self.btnp.clicked.connect(self.run_btnp)
        self.btnr.clicked.connect(self.run_btnr)
        self.btns.clicked.connect(self.run_btns)
        self.btnt.clicked.connect(self.run_btnt)
        self.btnu.clicked.connect(self.run_btnu)
        self.btnf.clicked.connect(self.run_btnf)
        self.btnh.clicked.connect(self.run_btnh)
        self.btnc.clicked.connect(self.run_btnc)
        self.btnch.clicked.connect(self.run_btnch)
        self.btnsh.clicked.connect(self.run_btnsh)
        self.btnsch.clicked.connect(self.run_btnsch)
        self.btni2.clicked.connect(self.run_btni2)
        self.btna2.clicked.connect(self.run_btna2)
        self.btnyu.clicked.connect(self.run_btnyu)
        self.btnya.clicked.connect(self.run_btnya)
        self.btnagain.clicked.connect(self.run)

    def run_btn1(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btn1.setDisabled(True)

    def run_btn2(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btn2.setDisabled(True)

    def run_btna(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btna.setDisabled(True)

    def run_btnb(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnb.setDisabled(True)

    def run_btnv(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnv.setDisabled(True)

    def run_btng(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btng.setDisabled(True)

    def run_btnd(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnd.setDisabled(True)

    def run_btne(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btne.setDisabled(True)

    def run_btne2(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btne2.setDisabled(True)

    def run_btnzh(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnzh.setDisabled(True)

    def run_btnz(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnz.setDisabled(True)

    def run_btni(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btni.setDisabled(True)

    def run_btny(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btny.setDisabled(True)

    def run_btnk(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnk.setDisabled(True)

    def run_btnl(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnl.setDisabled(True)

    def run_btnm(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnm.setDisabled(True)

    def run_btnn(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnn.setDisabled(True)

    def run_btno(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btno.setDisabled(True)

    def run_btnp(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnp.setDisabled(True)

    def run_btnr(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnr.setDisabled(True)

    def run_btns(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btns.setDisabled(True)

    def run_btnt(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnt.setDisabled(True)

    def run_btnu(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnu.setDisabled(True)

    def run_btnf(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnf.setDisabled(True)

    def run_btnh(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnh.setDisabled(True)

    def run_btnc(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnc.setDisabled(True)

    def run_btnch(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnch.setDisabled(True)

    def run_btnsh(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnsh.setDisabled(True)

    def run_btnsch(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnsch.setDisabled(True)

    def run_btni2(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btni2.setDisabled(True)

    def run_btna2(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btna2.setDisabled(True)

    def run_btnyu(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnyu.setDisabled(True)

    def run_btnya(self):

        sender = self.sender()
        if sender.text().lower() in self.word:
            a = list(self.label.text())
            for i in range(len(self.word)):
                if self.word[i] == sender.text().lower():
                    a[i] = self.word[i]
            self.label.setText("".join(a))
        else:
            self.wr += 1
            self.wrons()
        self.btnya.setDisabled(True)

    def run(self):

        self.wr = 0
        self.PIC = [QPixmap("2.png"), QPixmap("3.png"),
                    QPixmap("4.png"), QPixmap("5.png"),
                    QPixmap("6.png"), QPixmap("7.png"),
                    QPixmap("8.png"), QPixmap("9.png")]
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.png")
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        self.show()
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(True)
        self.btna.setEnabled(True)
        self.btnb.setEnabled(True)
        self.btnv.setEnabled(True)
        self.btng.setEnabled(True)
        self.btnd.setEnabled(True)
        self.btne.setEnabled(True)
        self.btne2.setEnabled(True)
        self.btnzh.setEnabled(True)
        self.btnz.setEnabled(True)
        self.btni.setEnabled(True)
        self.btny.setEnabled(True)
        self.btnk.setEnabled(True)
        self.btnl.setEnabled(True)
        self.btnm.setEnabled(True)
        self.btnn.setEnabled(True)
        self.btno.setEnabled(True)
        self.btnp.setEnabled(True)
        self.btnr.setEnabled(True)
        self.btns.setEnabled(True)
        self.btnt.setEnabled(True)
        self.btnu.setEnabled(True)
        self.btnf.setEnabled(True)
        self.btnh.setEnabled(True)
        self.btnc.setEnabled(True)
        self.btnch.setEnabled(True)
        self.btnsh.setEnabled(True)
        self.btnsch.setEnabled(True)
        self.btni2.setEnabled(True)
        self.btna2.setEnabled(True)
        self.btnyu.setEnabled(True)
        self.btnya.setEnabled(True)
        self.word = random.choice(open('словарь.txt', mode='rt',
                                  encoding='utf-8').read().split())
        self.label.setText('*' * len(self.word))

    def wrons(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap(self.PIC[self.wr])
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        self.show()
        if self.wr == 7:
            pass

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
