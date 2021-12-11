from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
QHBoxLayout, QRadioButton, QMessageBox)
 
app = QApplication([])
 
# главное окно:
my_win = QWidget()
my_win.setWindowTitle('Crazy People')
my_win.move(100, 100)
my_win.resize(400, 300)


'''___________________Widgets___________________'''
qustion = QLabel('Вопрос')
rbt1 = QRadioButton('Ответ1')
rbt2 = QRadioButton('Ответ2')
rbt3 = QRadioButton('Ответ3')
rbt4 = QRadioButton('Ответ4')

'''___________________Layouts___________________'''
main_layout = QVBoxLayout()

h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()

h1_layout.addWidget(qustion, alignment=Qt.AlignCenter)
h2_layout.addWidget(rbt1, alignment=Qt.AlignCenter)
h2_layout.addWidget(rbt2, alignment=Qt.AlignCenter)
h3_layout.addWidget(rbt3, alignment=Qt.AlignCenter)
h3_layout.addWidget(rbt4, alignment=Qt.AlignCenter)

main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)

my_win.setLayout(main_layout)

my_win.show()
app.exec_()
 
