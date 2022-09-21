from PyQt5 import QtGui
from PyQt5.Qt import *
import sqlite3
import json
import sys
from create_exercise import *
import random
class my_window(QWidget):
    def __init__(self):
        super(my_window, self).__init__()
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        changesize(a0.size().width(),a0.size().height())

def changesize(a,b):
    mText.move((a-400)//2,100)
    But1.move((a-200)//2,50+b//3)
    But2.move((a - 200) // 2, 150 + b // 3)
    pic.resize(a,b)
    write_pad.resize(int(0.9*a),300)
    write_pad.move(int((0.1*a)/2),50)
    But3.move(write_pad.x()+(write_pad.width()//2)-(But3.width()//2),write_pad.y()+450)
    rb1.move(a//4-30,But3.y()+80)
    rb2.move(2*a // 4-30, But3.y() + 80)
    rb3.move(3*a // 4-30, But3.y() + 80)
    answer_pad.move(But3.x()-150,But3.y()-100)
    But4.move((a-But4.width())//2,b-100)
    exercise_display.resize(a//2+100,b//3)
    exercise_display.move(a//4-50,b//12)
    rb_a1.move(a // 5 - 30, But3.y() + 80)
    rb_a2.move(2 * a // 5 - 30, But3.y() + 80)
    rb_a3.move(3 * a // 5 - 30, But3.y() + 80)
    rb_a4.move(4 * a // 5 - 30, But3.y() + 80)
    rb_a5.move(4 * a // 5 +20, But3.y() + 80)
    rb_t.move(a//3,But3.y()+100)
    rb_f.move(2*a // 3, But3.y() + 100)
    ans_io.move((a-ans_io.width())//2,But3.y()+130)

app=QApplication(sys.argv)
window=my_window()
window.setStyleSheet("background-color: rgba(227,255,247,0.7);")
window.setWindowTitle("组卷考试评卷系统")
window.resize(800,800)
window.setMinimumSize(500,500)
mText=QLabel(window)
mText.setText("欢迎来到组卷考试评卷系统")
mText.move((window.x()-mText.width())//2,50)
mText.setStyleSheet("font-size: 30px;font-weight: bold;background-color: rgba(255,255,255,0);")
But1,But2=QPushButton(window),QPushButton(window)
But1.setStyleSheet("font-size: 20px;background-color: rgba(255,255,255,0.6);")
But2.setStyleSheet("font-size: 20px;background-color: rgba(255,255,255,0.6);")
But1.setText("向题库导入新题")
But1.adjustSize()
But1.resize(But1.width()+20,But1.height()+30)
But2.setText("出一套试卷给我")
But2.adjustSize()
But2.resize(But2.width()+20,But2.height()+30)
pic=QLabel(window)
pic.resize(window.width(),window.height())
pic.setStyleSheet("background-image: url('img_1.png');")
pic.lower()


#当点击加题后获取题面信息，然后输入至数据库当中
def add_task():
    print("start adding task to database")
    mText.setVisible(False)
    But1.setVisible(False)
    But2.setVisible(False)
    write_pad.setVisible(True)
    But3.setVisible(True)
    rb1.setVisible(True)
    rb2.setVisible(True)
    rb3.setVisible(True)
    answer_pad.setVisible(True)

def upload():
    global answer_type
    text1 = write_pad.toPlainText()
    write_pad.setText('')
    text2 = answer_pad.text()
    answer_pad.setText('')
    typ = answer_type
    insert_db(text1, typ, text2)

    rb1.click()
    answer_type=1
    mText.setVisible(True)
    But1.setVisible(True)
    But2.setVisible(True)
    write_pad.setVisible(False)
    But3.setVisible(False)
    rb1.setVisible(False)
    rb2.setVisible(False)
    rb3.setVisible(False)
    answer_pad.setVisible(False)
But1.clicked.connect(add_task)
write_pad=QTextEdit(window)
write_pad.resize(int(window.width()*0.9),300)
write_pad.setStyleSheet("background-color:white;")
write_pad.setPlaceholderText("在此填入题面")
answer_pad=QLineEdit(window)
answer_pad.setPlaceholderText("在此填入题面的答案(选择题填ABCD，判断填T/F)")
answer_pad.resize(400,30)
But3=QPushButton(window)
But3.setText("题面编辑完成")
But3.adjustSize()
group=QButtonGroup(window)
rb1,rb2,rb3=QRadioButton("是选择题",window),QRadioButton("是填空题",window),QRadioButton("是判断题",window)
group.addButton(rb1,1)
group.addButton(rb2,2)
group.addButton(rb3,3)
answer_type=1
def clc(x):
    global answer_type
    answer_type=group.id(x)
    print(answer_type)

group.buttonClicked.connect(clc)
write_pad.setVisible(False)
But3.setVisible(False)
rb1.setVisible(False)
rb2.setVisible(False)
rb3.setVisible(False)
answer_pad.setVisible(False)
But3.clicked.connect(upload)


#随机选题并且开始作答
exercise_display=QPlainTextEdit(window)
exercise_display.setReadOnly(True)
exercise_display.setStyleSheet("font-size: 24px;font-weight: bold;")
But4=QPushButton(window)
But4.setText("提交本题并开始下一题")
But4.adjustSize()
But4.resize(But4.width()+80,But4.height()+50)
group_ans=QButtonGroup()
rb_a1,rb_a2,rb_a3,rb_a4,rb_a5=QCheckBox("A",window),QCheckBox("B",window),QCheckBox("C",window),QCheckBox("D",window),QPushButton("选完了",window)
rb_t,rb_f=QRadioButton("对",window),QRadioButton("错",window)
group_ans.addButton(rb_t,1)
group_ans.addButton(rb_f,0)
ans_io=QLineEdit(window)
ans_io.setPlaceholderText("请输入你的答案")
exercise_display.setVisible(False)
But4.setVisible(False)
rb_a1.setVisible(False)
rb_a2.setVisible(False)
rb_a3.setVisible(False)
rb_a4.setVisible(False)
rb_a5.setVisible(False)
rb_t.setVisible(False)
rb_f.setVisible(False)
ans_io.setVisible(False)
rg=0
allp=0
exercise=[]
sc=0
pre_s=0
def solve_problems():
    global rg
    global allp
    global exercise
    global sc
    global pre_s
    print("start  solving problems")
    mText.setVisible(False)
    But1.setVisible(False)
    But2.setVisible(False)
    exercise_display.setVisible(True)
    But4.setVisible(True)
    nums=getinfo()
    choose=nums[0]
    fill=nums[1]
    decide=nums[2]
    db_exercise=get_exercises()
    exercise=[]
    exercise.extend(random.sample(db_exercise[0],random.randint(1,choose)))
    exercise.extend(random.sample(db_exercise[1],random.randint(1,fill)))
    exercise.extend(random.sample(db_exercise[2],random.randint(1,decide)))
    random.shuffle(exercise)
    rg=0
    allp= len(exercise)
    sc=0
    pre_s=100/allp
    But4.clicked.connect(dop)

def dop():
    global sc
    global pre_s
    global rg
    if rg>=allp:
        exercise_display.setPlainText("恭喜完成所有练习")
        exercise_display.insertPlainText("你的成绩是{}".format(int((sc+0.5)//1)))
    else:
        problem(exercise[rg])
        rg+=1


trueans=''
def problem(problem):
    global trueans
    # id ,type,info,answer
    trueans=problem[3]
    But4.setEnabled(False)
    if problem[1] == 1:
        rb_a1.setVisible(True)
        rb_a2.setVisible(True)
        rb_a3.setVisible(True)
        rb_a4.setVisible(True)
        rb_a5.setVisible(True)
        rb_a1.setEnabled(True)
        rb_a2.setEnabled(True)
        rb_a3.setEnabled(True)
        rb_a4.setEnabled(True)
        rb_a5.setEnabled(True)
    else:
        rb_a1.setVisible(False)
        rb_a2.setVisible(False)
        rb_a3.setVisible(False)
        rb_a4.setVisible(False)
        rb_a5.setVisible(False)
    if problem[1] == 2:
        ans_io.setVisible(True)
        ans_io.setText('')
        ans_io.setEnabled(True)
    else:
        ans_io.setVisible(False)
    if problem[1] == 3:
        rb_t.setVisible(True)
        rb_f.setVisible(True)
        group_ans.setExclusive(False)
        rb_t.setChecked(False)
        rb_f.setChecked(False)
        group_ans.setExclusive(True)
    else:
        rb_t.setVisible(False)
        rb_f.setVisible(False)
    exercise_display.setPlainText(problem[2])


def choose():
    global sc
    global pre_s
    global trueans
    But4.setEnabled(True)
    cor=True
    if rb_a1.isChecked() and 'A' not in trueans:
        cor=False
    if rb_a2.isChecked() and 'B' not in trueans:
        cor=False
    if rb_a3.isChecked() and 'C' not in trueans:
        cor=False
    if rb_a1.isChecked() and 'A' not in trueans:
        cor=False
    if cor:
        exercise_display.setPlainText("答对了")
        sc += pre_s
    else:
        exercise_display.setPlainText("答错了")
    rb_a1.setChecked(False)
    rb_a2.setChecked(False)
    rb_a3.setChecked(False)
    rb_a4.setChecked(False)
    rb_a1.setEnabled(False)
    rb_a2.setEnabled(False)
    rb_a3.setEnabled(False)
    rb_a4.setEnabled(False)
    rb_a5.setEnabled(False)
def judge_p(x):
    global trueans
    global sc
    global pre_s
    But4.setEnabled(True)
    ans=group_ans.id(x)
    if trueans=='T' and ans==1:
        exercise_display.setPlainText("答对了")
        sc+=pre_s
    elif trueans=='F' and ans==0:
        exercise_display.setPlainText("答对了")
    else:
        exercise_display.setPlainText("答错了")

def tk():
    global sc
    global pre_s
    global trueans
    if len(ans_io.text())== len(trueans) and ans_io.text()==trueans:
        exercise_display.setPlainText("答对了")
        sc += pre_s
        But4.setEnabled(True)
        ans_io.setEnabled(False)
    if len(ans_io.text())> len(trueans) or(len(ans_io.text())== len(trueans) and ans_io.text()!=trueans):
        exercise_display.setPlainText("答错了")
        But4.setEnabled(True)
        ans_io.setEnabled(False)


group_ans.buttonClicked.connect(judge_p)
rb_a5.clicked.connect(choose)
ans_io.textChanged.connect(tk)
But2.clicked.connect(solve_problems)
window.show()
sys.exit(app.exec_())
