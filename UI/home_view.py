from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy


class HomeView:
    def __init__(self, root):
        self.lbl_font = QtGui.QFont()  # Шрифт надписей
        self.btn_font = QtGui.QFont()  # Шрифт кнопок

        self.centralWidget    = QtWidgets.QWidget(root)                   # Главный виджет
        self.centralLayout    = QtWidgets.QVBoxLayout(self.centralWidget) # Главный компоновщик

        self.gridlayout       = QtWidgets.QGridLayout()                   # Сетка
        self.horizontalLayout = QtWidgets.QHBoxLayout()                   # Горизонтальный компоновщик

        self.label = QtWidgets.QLabel()  # Надпись

        self.button_1    = QtWidgets.QPushButton() # Кнопка описательной статистики
        self.button_2    = QtWidgets.QPushButton() # Кнопка проверки статистических гипотез
        self.button_3    = QtWidgets.QPushButton() # Кнопка дисперсионного анализа
        self.button_4    = QtWidgets.QPushButton() # Кнопка корреляционного анализа
        self.button_5    = QtWidgets.QPushButton() # Кнопка факторного анализа
        self.button_6    = QtWidgets.QPushButton() # Кнопка кластерного анализа
        self.button_7    = QtWidgets.QPushButton() # Кнопка методов теории множеств
        self.button_8    = QtWidgets.QPushButton() # Кнопка апроксимации зафисимостей
        self.button_load = QtWidgets.QPushButton() # Кнопка загрузки нового файла

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
        spacerItem = QtWidgets.QSpacerItem(0, 250, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка надписи
        self.label.setFont(self.lbl_font)
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.centralLayout.addWidget(self.label)

        # Настройка кнопки описательной статистики
        self.button_1.setMinimumSize(QtCore.QSize(380, 60))
        self.button_1.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_1, 0, 0)

        # Настройка кнопки проверки статистических гипотез
        self.button_2.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_2, 1, 0)

        # Настройка кнопки дисперсионного анализа
        self.button_3.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_3, 2, 0)

        # Настройка кнопки корреляционного анализа
        self.button_4.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_4, 3, 0)

        # Настройка кнопки факторного анализа
        self.button_5.setMinimumSize(QtCore.QSize(380, 60))
        self.button_5.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_5, 0, 1)

        # Настройка кнопки распознования образов(кластерный анализ)
        self.button_6.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_6, 1, 1)

        # Настройка кнопки методов теории множеств
        self.button_7.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_7, 2, 1)

        # Настройка кнопки аппроксимации зависимостей
        self.button_8.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_8, 3, 1)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка кнопки возврата к загрузке файла
        self.button_load.setMinimumSize(QtCore.QSize(340, 60))
        self.button_load.setMaximumSize(QtCore.QSize(340, 60))
        self.button_load.setFont(self.btn_font)
        self.horizontalLayout.addWidget(self.button_load)

        # Финальная компоновка
        self.centralLayout.addLayout(self.gridlayout)
        self.centralLayout.addLayout(self.horizontalLayout)
        root.setCentralWidget(self.centralWidget)

        self.setTextUi()

    def setTextUi(self):
        # Выставление текста виджетам
        self.label.setText('Выберите категорию:')
        self.button_1.setText("Описательная статистика")
        self.button_2.setText("Проверка статистических гипотез")
        self.button_3.setText("Дисперсионный анализ")
        self.button_4.setText("Корреляционный анализ")
        self.button_5.setText("Факторный анализ")
        self.button_6.setText("Кластерный анализ")
        self.button_7.setText("Методы теории множеств")
        self.button_8.setText("Аппроксимация зависимостей")
        self.button_load.setText("Загрузить новые данные")