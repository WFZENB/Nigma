from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy
from plot import Plot # Импорт графика для тестового вывода


class ResultView:
    def __init__(self, root):
        self.lbl_font = QtGui.QFont() # Шрифт надписей
        self.btn_font = QtGui.QFont() # Шрифт кнопок

        self.centralWidget = QtWidgets.QWidget(root)                    # Главный виджет
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)  # Главный компоновщик

        self.title        = QtWidgets.QLabel()       # Заголовок
        self.result_label = QtWidgets.QLabel()       # Результат
        self.plot         = Plot(self.centralWidget) # График

        self.setupUi(root)

    def setupUi(self, root):
        # Выставление размеров шрифтов
        self.lbl_font.setPointSize(16)
        self.btn_font.setPointSize(13)

        # Определение размера окна и центрирование
        self.centralWidget.setMinimumSize(QtCore.QSize(1200, 850))
        self.centralLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка заголовка
        self.title.setFont(self.lbl_font)
        self.title.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.centralLayout.addWidget(self.title)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка надписи с результатом
        self.result_label.setFont(self.lbl_font)
        self.result_label.setWordWrap(True)
        self.result_label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.centralLayout.addWidget(self.result_label)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Добавление графика
        self.centralLayout.addWidget(self.plot)

        # Финальная компоновка
        root.setCentralWidget(self.centralWidget)

        self.setTextUi()

    def setTextUi(self):
        # Выставление текста виджетам
        self.title.setText('Результат вычислений:')
        self.result_label.setText('<Вместо этого текста должен быть результат>')