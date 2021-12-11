from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QRadioButton, 
    QButtonGroup)

app = QApplication([])
main_win = QWidget()
main_win.resize(400,300)

'''___________Виджеты___________'''
qustion_text = QLabel('Vopros')
group_button = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
answer_button = QPushButton('Ответить')

answer_group = QGroupBox('Правильный ответ:')
answer_text = QLabel('ETO OTVET')

ButtonGrp = QButtonGroup()
ButtonGrp.addButton(rbtn_1)
ButtonGrp.addButton(rbtn_2)
ButtonGrp.addButton(rbtn_3)
ButtonGrp.addButton(rbtn_4)

'''___________Лейаут___________'''

ans_grp_layout = QVBoxLayout()
ans_grp_layout.addWidget(answer_text, alignment = Qt.AlignCenter)

answer_group.setLayout(ans_grp_layout)

group_layout1 = QVBoxLayout()
group_layout2 = QVBoxLayout()
group_main_layout = QHBoxLayout()

group_layout1.addWidget(rbtn_1)
group_layout1.addWidget(rbtn_2)
group_layout2.addWidget(rbtn_3)
group_layout2.addWidget(rbtn_4)

group_main_layout.addLayout(group_layout1)
group_main_layout.addLayout(group_layout2)

group_button.setLayout(group_main_layout)

main_layout = QVBoxLayout()
main_layout.addWidget(qustion_text, alignment = Qt.AlignCenter)
main_layout.addWidget(answer_group, alignment = Qt.AlignCenter)
main_layout.addWidget(group_button, alignment = Qt.AlignCenter)
main_layout.addWidget(answer_button, alignment = Qt.AlignCenter)

main_win.setLayout(main_layout)
answer_group.hide()

'''___________Функции___________'''

def show_result():
    group_button.hide()
    answer_group.show()
    answer_button.setText('Следующий вопрос')

def show_question():
    answer_group.hide()
    group_button.show()
    ButtonGrp.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGrp.setExclusive(True)
    answer_button.setText('Ответить')

def show_click():
    if answer_button.text() == 'Ответить':
        show_result()
    else:
        show_question()

answer_button.clicked.connect(show_click)

main_win.show()
app.exec_()