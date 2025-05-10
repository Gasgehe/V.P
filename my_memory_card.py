#создай приложение для запоминания информации
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
Victorin = QLabel('Викторины')
r_group_box = QGroupBox('Выберите викторину')
btn_Victorin = QPushButton('Викторина по играм')
btn_Victorin2 = QPushButton('Викторина по фильмам')
btn_Victorin3 = QPushButton('Викторина по.....')

#Виджеты
# layout1 = QHBoxLayout()
# layout2 = QVBoxLayout()
# layout3 = QVBoxLayout()

# layout2.addWidget()
# layout2.addWidget()
# layout3.addWidget()

main_win.show()
app.exec_()
