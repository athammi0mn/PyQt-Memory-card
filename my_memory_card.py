from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QLabel, QRadioButton, 
    QPushButton, QGroupBox,
    QVBoxLayout, QHBoxLayout,
    QButtonGroup
)
from random import shuffle
from random import randint

#bikin_window 
app = QApplication([])
window = QWidget()
window.resize(500,400)
window.setWindowTitle("Memo Card")

#widgets
#page_questions
lbquest = QLabel("ini pertanyaan")

rbtn1 = QRadioButton("ans1")
rbtn2 = QRadioButton("ans2")
rbtn3 = QRadioButton("ans3")
rbtn4 = QRadioButton("ans4")

btn = QPushButton("Answer")

rbtngroup = QGroupBox("Pilihan")

#page_result
ansgroup = QGroupBox("Jawaban")

lbres = QLabel("True/false")
lbcorrect = QLabel("correct ans")

#layouts
#h1
h1 = QHBoxLayout()
h1.addWidget(lbquest, alignment = Qt.AlignCenter)

#button_layouts
btnh1 = QHBoxLayout()
btnh1.addWidget(rbtn1, alignment = Qt.AlignCenter)
btnh1.addWidget(rbtn2, alignment = Qt.AlignCenter)

btnh2 = QHBoxLayout()
btnh2.addWidget(rbtn3, alignment = Qt.AlignCenter)
btnh2.addWidget(rbtn4, alignment = Qt.AlignCenter)

#btn_grouping
btns = QVBoxLayout()
btns.addLayout(btnh1)
btns.addLayout(btnh2)

rbtngroup.setLayout(btns)

#ans_lay
anslay = QVBoxLayout()
anslay.addWidget(lbres, alignment = Qt.AlignCenter)
anslay.addWidget(lbcorrect, alignment = Qt.AlignCenter)

ansgroup.setLayout(anslay)

#h2
h2 = QHBoxLayout()
h2.addWidget(rbtngroup)
h2.addWidget(ansgroup)
#dihide
ansgroup.hide()


#h3
h3 = QHBoxLayout()
h3.addStretch(1)
h3.addWidget(btn)
h3.addStretch(1)

#gabung_layouts
vmain = QVBoxLayout()
vmain.addLayout(h1)
vmain.addLayout(h2)
vmain.addLayout(h3)
window.setLayout(vmain)

#btn_grouping
rgroup = QButtonGroup()
rgroup.addButton(rbtn1)
rgroup.addButton(rbtn2)
rgroup.addButton(rbtn3)
rgroup.addButton(rbtn4)


ans = [rbtn1, rbtn2, rbtn3, rbtn4]

#class question

class soal():
    def __init__(self, question, rans, w1, w2, w3):
        self.question = question
        self.rans = rans
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

#Pertanyaan
quest1 = soal('Which of these songs is used as an opening for "April Showers Bring May Flowers"?', 'Bloom', 'NOSA', 'はじめまして', 'plot Twist')
quest2 = soal('Who is the toughest character from the show "Chiikawa"?', "Usagi", "Momonga", "Kurimanju","Chiikabu")
quest3 = soal('Which of these songs is NOT included in tws debut mini album "Sparkling Blue"?', 'hey! hey!', 'First Hooky', 'BFF', 'Unplugged Boy')
quest4 = soal("TWS's debut date is?", '1/22/24', '1/24/22', '7/22/24', '7/24/22')
quest5 = soal('Who of these "Chiikawa" characters is evil?', 'Momonga', 'Chimera', 'Chiikabu', 'Mimic')
quest6 = soal("Which of these is TWS's debut mini album?", 'Sparkling Blue', 'Try With Us', 'Play Hard', 'Last Bell')
quest7 = soal('Who of these "Chiikawa" characters is the strongest?', 'Rakko', 'Kurimanju', 'Hachiware', 'Kani')
quest8 = soal('Thank You.', 'Giant Fried Rice', 'Giant Caramel Pudding', 'Infinite Rice Cooker', 'Huh?')
quest9 = soal("In TWS's album, Play Hard, which of these songs is the main track?", 'Overdrive', 'Overthinking', 'Caffeine Rush', 'Head Shoulder Knees and Toes')
quest10 = soal('placeholder0', 'r', 'w', 'w', 'w')


listquest = []
listquest.append(quest1)
listquest.append(quest2)
listquest.append(quest3)
listquest.append(quest4)
listquest.append(quest5)
listquest.append(quest6)
listquest.append(quest7)
listquest.append(quest8)
listquest.append(quest9)
listquest.append(quest10)

corans = 0
totans = 0

#fungsi

def next_scene():
    if btn.text() == 'Answer':
        rbtngroup.hide()
        ansgroup.show()
        btn.setText('Next Question')
        checks()
        global totans
        totans += 1
        stats()
    elif btn.text() == 'Next Question':
        ind_rand = randint(0,len(listquest)-1)
        set_question(listquest[ind_rand])
        rgroup.setExclusive(False)
        rbtn1.setChecked(False)
        rbtn2.setChecked(False)
        rbtn3.setChecked(False)
        rbtn4.setChecked(False)
        rgroup.setExclusive(True)
        rbtngroup.show()
        ansgroup.hide()
        btn.setText('Answer')
def set_question(q):
    lbquest.setText(q.question)
    #pertanyaan_diacak
    shuffle(ans)
    #jawabannya
    ans[0].setText(q.rans)
    ans[1].setText(q.w1)
    ans[2].setText(q.w2)
    ans[3].setText(q.w3)
def checks():
    if ans[0].isChecked():
        lbres.setText('True')
        global corans
        corans += 1
    elif ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        lbres.setText('False')
def stats():
    global corans
    global totans
    print('Statistics')
    print('Right Answers:', corans)
    print('Wrong Answers:', totans - corans)
    print('Your Score:', round(corans/totans*100))
btn.clicked.connect(next_scene)

set_question(listquest[0])

#biar_muncul
window.show()
app.exec_()