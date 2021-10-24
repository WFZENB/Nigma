from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy


class ResultView:
    def __init__(self, root):
        self.lbl_font = QtGui.QFont() # Шрифт надписей
        self.btn_font = QtGui.QFont() # Шрифт кнопок

        self.centralWidget = QtWidgets.QWidget(root)  # Главный виджет
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)  # Главный компоновщик

        self.label = QtWidgets.QLabel()  # Надпись

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

        # Настройка надписи
        self.label.setFont(self.lbl_font)
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.centralLayout.addWidget(self.label)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Финальная компоновка
        root.setCentralWidget(self.centralWidget)

        self.setTextUi()

    def setTextUi(self):
        # Выставление текста виджетам
        self.label.setText('Результат вычислений:')