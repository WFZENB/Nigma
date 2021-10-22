from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5 import QtWidgets, QtGui, QtCore


class HomeView(QWidget):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)

        self.central = QtWidgets.QWidget(self)

        self.gridlayout = QtWidgets.QGridLayout(self.central)  # макет для кнопок выбора групп действий
        self.gridlayout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.gridlayout1 = QtWidgets.QGridLayout(self.central)

        # Создание кнопки описательной статистики
        self.button_statistics = QtWidgets.QPushButton(self.central)
        self.button_statistics.setText("Описательная статистика")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_statistics.setFont(font)
        self.button_statistics.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_statistics, 0, 0)

        # Создание кнопки проверки статистических гипотез
        self.button_stat_hypothesis = QtWidgets.QPushButton(self.central)
        self.button_stat_hypothesis.setText("Проверка статистических гипотез")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_stat_hypothesis.setFont(font)
        self.button_stat_hypothesis.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_stat_hypothesis, 1, 0)

        # Создание кнопки дисперсионного анализа
        self.button_dispersion = QtWidgets.QPushButton(self.central)
        self.button_dispersion.setText("Дисперсионный анализ")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_dispersion.setFont(font)
        self.button_dispersion.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_dispersion, 2, 0)

        # Создание кнопки корреляционного анализа
        self.button_correlation = QtWidgets.QPushButton(self.central)
        self.button_correlation.setText("Корреляционный анализ")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_correlation.setFont(font)
        self.button_correlation.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_correlation, 3, 0)

        # Создание кнопки факторного анализа
        self.button_factor = QtWidgets.QPushButton(self.central)
        self.button_factor.setText("Факторный анализ")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_factor.setFont(font)
        self.button_factor.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_factor, 0, 1)

        # Создание кнопки распознования образов(кластерный анализ)
        self.button_cluster = QtWidgets.QPushButton(self.central)
        self.button_cluster.setText("Кластерный анализ")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_cluster.setFont(font)
        self.button_cluster.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_cluster, 1, 1)

        # Создание кнопки методов теории множеств
        self.button_set_theory = QtWidgets.QPushButton(self.central)
        self.button_set_theory.setText("Методы теории множеств")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_set_theory.setFont(font)
        self.button_set_theory.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_set_theory, 2, 1)

        # Создание кнопки аппроксимации зависимостей
        self.button_approximation = QtWidgets.QPushButton(self.central)
        self.button_approximation.setText("Аппроксимация зависимостей")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_approximation.setFont(font)
        self.button_approximation.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout.addWidget(self.button_approximation, 3, 1)

        # Создание кнопки возврата к загрузке файла
        self.button_back_main = QtWidgets.QPushButton(self.central)
        self.button_back_main.setText("Загрузить другой файл")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_back_main.setFont(font)
        self.button_back_main.setMinimumSize(QtCore.QSize(340, 60))
        self.gridlayout1.addWidget(self.button_back_main)


class Action(QWidget):                  # Создание окна для выбора конкретного действия
    def __init__(self, parent=None):
        super(Action, self).__init__(parent)

        self.button = QtWidgets.QPushButton("Результат", self)


class Result(QWidget):                  # Создание окна для вывод результата
    def __init__(self, parent=None):
        super(Result, self).__init__(parent)

        self.horizontal = QtWidgets.QHBoxLayout(self)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Рассчитать другое значение')
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button1.setFont(font)
        self.button1.setMinimumSize(QtCore.QSize(340, 60))
        self.horizontal.addWidget(self.button1)
        self.horizontal.addWidget(self.button1, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)


