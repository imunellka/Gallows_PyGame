import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QApplication, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi('Виселица.ui', self)
        self.setWindowTitle('Виселица')
        self.btn1.clicked.connect(self.runbtn1)
        self.btn2.clicked.connect(self.runbtn2)
        self.btna.clicked.connect(self.runbtna)
        self.btnb.clicked.connect(self.runbtnb)
        self.btnv.clicked.connect(self.runbtnv)
        self.btng.clicked.connect(self.runbtng)
        self.btnd.clicked.connect(self.runbtnd)
        self.btne.clicked.connect(self.runbtne)
        self.btne2.clicked.connect(self.runbtne2)
        self.btnzh.clicked.connect(self.runbtnzh)
        self.btnz.clicked.connect(self.runbtnz)
        self.btni.clicked.connect(self.runbtni)
        self.btny.clicked.connect(self.runbtny)
        self.btnk.clicked.connect(self.runbtnk)
        self.btnl.clicked.connect(self.runbtnl)
        self.btnm.clicked.connect(self.runbtnm)
        self.btnn.clicked.connect(self.runbtnn)
        self.btno.clicked.connect(self.runbtno)
        self.btnp.clicked.connect(self.runbtnp)
        self.btnr.clicked.connect(self.runbtnr)
        self.btns.clicked.connect(self.runbtns)
        self.btnt.clicked.connect(self.runbtnt)
        self.btnu.clicked.connect(self.runbtnu)
        self.btnf.clicked.connect(self.runbtnf)
        self.btnh.clicked.connect(self.runbtnh)
        self.btnc.clicked.connect(self.runbtnc)
        self.btnch.clicked.connect(self.runbtnch)
        self.btnsh.clicked.connect(self.runbtnsh)
        self.btnsch.clicked.connect(self.runbtnsch)
        self.btni2.clicked.connect(self.runbtni2)
        self.btna2.clicked.connect(self.runbtna2)
        self.btnyu.clicked.connect(self.runbtnyu)
        self.btnya.clicked.connect(self.runbtnya)
        self.btnagain.clicked.connect(self.run)
        self.run()

    def runbtn1(self):

        if self.wr < 8:
            self.btn1.setDisabled(True)
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
        self.quit()

    def runbtn2(self):

        if self.wr < 8:
            self.btn2.setDisabled(True)
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
        self.quit()

    def runbtna(self):

        if self.wr < 8:
            self.btna.setDisabled(True)
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
        self.quit()

    def runbtnb(self):

        if self.wr < 8:
            self.btnb.setDisabled(True)
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
        self.quit()

    def runbtnv(self):

        if self.wr < 8:
            self.btnv.setDisabled(True)
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
        self.quit()

    def runbtng(self):

        if self.wr < 8:
            self.btng.setDisabled(True)
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
        self.quit()

    def runbtnd(self):

        if self.wr < 8:
            self.btnd.setDisabled(True)
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
        self.quit()

    def runbtne(self):

        if self.wr < 8:
            self.btne.setDisabled(True)
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
        self.quit()

    def runbtne2(self):

        if self.wr < 8:
            self.btne2.setDisabled(True)
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
        self.quit()

    def runbtnzh(self):

        if self.wr < 8:
            self.btnzh.setDisabled(True)
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
        self.quit()

    def runbtnz(self):

        if self.wr < 8:
            self.btnz.setDisabled(True)
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
        self.quit()

    def runbtni(self):

        if self.wr < 8:
            self.btni.setDisabled(True)
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
        self.quit()

    def runbtny(self):

        if self.wr < 8:
            self.btny.setDisabled(True)
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
        self.quit()

    def runbtnk(self):

        if self.wr < 8:
            self.btnk.setDisabled(True)
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
        self.quit()

    def runbtnl(self):

        if self.wr < 8:
            self.btnl.setDisabled(True)
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
        self.quit()

    def runbtnm(self):

        if self.wr < 8:
            self.btnm.setDisabled(True)
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
        self.quit()

    def runbtnn(self):

        if self.wr < 8:
            self.btnn.setDisabled(True)
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
        self.quit()

    def runbtno(self):

        if self.wr < 8:
            self.btno.setDisabled(True)
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
        self.quit()

    def runbtnp(self):

        if self.wr < 8:
            self.btnp.setDisabled(True)
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
        self.quit()

    def runbtnr(self):

        if self.wr < 8:
            self.btnr.setDisabled(True)
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
        self.quit()

    def runbtns(self):

        if self.wr < 8:
            self.btns.setDisabled(True)
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
        self.quit()

    def runbtnt(self):

        if self.wr < 8:
            self.btnt.setDisabled(True)
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
        self.quit()

    def runbtnu(self):

        if self.wr < 8:
            self.btnu.setDisabled(True)
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
        self.quit()

    def runbtnf(self):

        if self.wr < 8:
            self.btnf.setDisabled(True)
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
        self.quit()

    def runbtnh(self):

        if self.wr < 8:
            self.btnh.setDisabled(True)
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
        self.quit()

    def runbtnc(self):

        if self.wr < 8:
            self.btnc.setDisabled(True)
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
        self.quit()

    def runbtnch(self):

        if self.wr < 8:
            self.btnch.setDisabled(True)
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
        self.quit()

    def runbtnsh(self):

        if self.wr < 8:
            self.btnsh.setDisabled(True)
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
        self.quit()

    def runbtnsch(self):

        if self.wr < 8:
            self.btnsch.setDisabled(True)
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
        self.quit()

    def runbtni2(self):

        if self.wr < 8:
            self.btni2.setDisabled(True)
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
        self.quit()

    def runbtna2(self):

        if self.wr < 8:
            self.btna2.setDisabled(True)
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
        self.quit()

    def runbtnyu(self):

        if self.wr < 8:
            self.btnyu.setDisabled(True)
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
        self.quit()

    def runbtnya(self):

        if self.wr < 8:
            self.btnya.setDisabled(True)
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
        self.quit()

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
        self.show()

    def wrons(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap(self.PIC[self.wr - 1])
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        self.show()
        if self.wr == 8:
            reply = QMessageBox.question(self, 'ПОРАЖЕНИЕ',
                                         "Вы проиграли\n\
Загадано слово {}".format(self.word.upper()),
                                         QMessageBox.Retry | QMessageBox.Close,
                                         QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                self.run()
            else:
                sys.exit(app.exec_())

    def closeEvent(self, event):

        answer = QMessageBox.question(self, 'ВЫХОД',
                                      "Вы уверены, что хотите выйти?",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if answer == QMessageBox.No:
            event.ignore()
        else:
            event.accept()

    def quit(self):

        if "*" not in self.label.text():
            reply = QMessageBox.question(self, "ПОБЕДА",
                                         "Поздравляем! Вы выиграли!",
                                         QMessageBox.Retry | QMessageBox.Close,
                                         QMessageBox.Close)
            if reply == QMessageBox.Close:
                sys.exit(app.exec_())
            else:
                self.run()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
