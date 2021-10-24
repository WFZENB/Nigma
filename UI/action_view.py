from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy


class ActionView:
    def __init__(self, root, button_names):
        self.button_names = button_names

        # Определение количества рядов кнопок
        self.rows = len(button_names)
        if (self.rows % 2) == 1:
            self.rows += 1
        self.rows /= 2

        self.lbl_font = QtGui.QFont()  # Шрифт надписей
        self.btn_font = QtGui.QFont()  # Шрифт кнопок

        self.centralWidget    = QtWidgets.QWidget(root)                   # Главный виджет
        self.centralLayout    = QtWidgets.QVBoxLayout(self.centralWidget) # Главный компоновщик

        self.gridlayout       = QtWidgets.QGridLayout()                   # Сетка
        self.horizontalLayout = QtWidgets.QHBoxLayout()                   # Горизонтальный компоновщик

        self.label = QtWidgets.QLabel() # Надпись

        # Функциональные кнопки
        self.button_01 = QtWidgets.QPushButton()
        self.button_02 = QtWidgets.QPushButton()
        self.button_03 = QtWidgets.QPushButton()
        self.button_04 = QtWidgets.QPushButton()
        self.button_05 = QtWidgets.QPushButton()
        self.button_06 = QtWidgets.QPushButton()
        self.button_07 = QtWidgets.QPushButton()
        self.button_08 = QtWidgets.QPushButton()
        self.button_09 = QtWidgets.QPushButton()
        self.button_10 = QtWidgets.QPushButton()
        self.button_11 = QtWidgets.QPushButton()
        self.button_12 = QtWidgets.QPushButton()
        self.button_13 = QtWidgets.QPushButton()
        self.button_14 = QtWidgets.QPushButton()
        self.button_15 = QtWidgets.QPushButton()
        self.button_16 = QtWidgets.QPushButton()
        self.button_17 = QtWidgets.QPushButton()
        self.button_18 = QtWidgets.QPushButton()
        self.button_19 = QtWidgets.QPushButton()
        self.button_20 = QtWidgets.QPushButton()
        self.button_21 = QtWidgets.QPushButton()
        self.button_22 = QtWidgets.QPushButton()
        self.button_23 = QtWidgets.QPushButton()
        self.button_24 = QtWidgets.QPushButton()
        self.button_25 = QtWidgets.QPushButton()
        self.button_26 = QtWidgets.QPushButton()
        self.button_27 = QtWidgets.QPushButton()
        self.button_28 = QtWidgets.QPushButton()
        self.button_29 = QtWidgets.QPushButton()
        self.button_30 = QtWidgets.QPushButton()

        self.button_load = QtWidgets.QPushButton()  # Кнопка загрузки нового файла
        self.button_back = QtWidgets.QPushButton()  # Кнопка возврата на предыдущую страницу

        self.setupUi(root)

    def setupUi(self, root):
        # Выставление размеров шрифтов
        self.lbl_font.setPointSize(16)
        self.btn_font.setPointSize(13)

        # Определение размера окна и центрирование
        self.centralWidget.setMinimumSize(QtCore.QSize(1200, 850))
        self.gridlayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка надписи
        self.label.setFont(self.lbl_font)
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.centralLayout.addWidget(self.label)

        for i in range(len(self.button_names)):
            self.add_btn(i+1, self.button_names[i])

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка кнопки возврата к загрузке файла
        self.button_load.setMinimumSize(QtCore.QSize(340, 60))
        self.button_load.setFont(self.btn_font)
        self.horizontalLayout.addWidget(self.button_load)

        # Настройка кнопки возврата на пердыдущую страницу
        self.button_back.setMinimumSize(QtCore.QSize(340, 60))
        self.button_back.setFont(self.btn_font)
        self.horizontalLayout.addWidget(self.button_back)

        # Финальная компоновка
        self.centralLayout.addLayout(self.gridlayout)
        self.centralLayout.addLayout(self.horizontalLayout)
        root.setCentralWidget(self.centralWidget)

        self.setTextUi()

    def add_btn(self, n, name):
        x = (0 if n <= self.rows else 1)
        y = (n if n <= self.rows else n-self.rows)

        btn = eval('self.button_' + str(n).zfill(2))
        btn.setMinimumSize(QtCore.QSize(380, 60))
        btn.setFont(self.btn_font)
        btn.setText(name)
        self.gridlayout.addWidget(btn, y, x)

    def setTextUi(self):
        # Выставление текста виджетам
        self.label.setText('Выберите операцию:')
        self.button_load.setText("Загрузить новые данные")
        self.button_back.setText("Вернуться назад")