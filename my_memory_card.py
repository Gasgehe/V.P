from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication, QWidget, QRadioButton, 
QLabel, QGroupBox, QPushButton,
QVBoxLayout, QHBoxLayout, 
QButtonGroup
)
from random import shuffle, randint


# class Victorin():
#     def __init__(self, , , , , ):
#         self. = 
#         self. = 
#         self. =
#         self. = 
#         self. = 


# создание окна
app = QApplication([])
main_win = QWidget()

main_win.resize(500, 500)
main_win.setWindowTitle('Викторины')

#интерфейс
victorin = QLabel('Викторины')
victorin.setStyleSheet("font-size: 32px;")
btn_Victorin = QPushButton('Викторина по играм')
btn_Victorin2 = QPushButton('Викторина по фильмам')
btn_Victorin3 = QPushButton('Викторина по.....')

#Виджеты
menu_layout = QVBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()

menu_layout.addWidget(victorin, alignment=Qt.AlignCenter)
menu_layout.addWidget(btn_Victorin, alignment=Qt.AlignCenter)
menu_layout.addWidget(btn_Victorin2, alignment=Qt.AlignCenter)
menu_layout.addWidget(btn_Victorin3, alignment=Qt.AlignCenter)


# Викторина 1
question = QLabel('Вопрос')
next_btn = QPushButton('Ответить') 
ansgroupbox = QGroupBox('Варианты ответов')

btn1 = QRadioButton('Ответ1')
btn2 = QRadioButton('Ответ2')
btn3 = QRadioButton('Ответ3')
btn4 = QRadioButton('Ответ4')

ans1_layout = QHBoxLayout()
ans2_layout = QVBoxLayout()
ans3_layout = QVBoxLayout()
ans2_layout.addWidget(btn1)
ans2_layout.addWidget(btn2)
ans3_layout.addWidget(btn3)
ans3_layout.addWidget(btn4)
ans1_layout.addLayout(ans2_layout)
ans1_layout.addLayout(ans3_layout)
ansgroupbox.setLayout(ans1_layout)
V1 = QVBoxLayout()
V1.addWidget(question)
V1.addWidget(ansgroupbox)
V1.addWidget(next_btn)
main_win.setLayout(V1)

# main_win.setLayout(menu_layout)

#Функционал
def show_victorin1():
    pass



def show_victorin2():
    pass

def show_victorin2():
    pass

btn_Victorin.clicked.connect(show_victorin1)
main_win.show()
app.exec_()
