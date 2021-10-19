from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from qt_material import apply_stylesheet # Импорт библиотеки стилизации
from sys import argv, exit
from plot import Plot # Импорт графика для тестового вывода


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.lbl_font = QFont() # Шрифт надписей
        self.btn_font = QFont() # Шрифт кнопок

        self.centralwidget      = QtWidgets.QWidget(MainWindow)             # Главный виджет
        self.gridLayout         = QtWidgets.QGridLayout(self.centralwidget) # Главный компоновщик

        self.verticalLayout     = QtWidgets.QVBoxLayout()                   # Вертикальный компоновщик
        self.horizontalLayout   = QtWidgets.QHBoxLayout()                   # Горизонтальный компоновщик
        self.label_init         = QtWidgets.QLabel(self.centralwidget)      # Надпись приветствия
        self.button_load        = QtWidgets.QPushButton(self.centralwidget) # Кнопка загрузки файла

        self.status_bar         = QtWidgets.QStatusBar(MainWindow)          # Статусбар

        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        # Выставление размеров шрифтов
        self.lbl_font.setPointSize(16)
        self.btn_font.setPointSize(14)

        # Определение размера окна и центрирование
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 600))
        self.gridLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Настройка надписи
        self.label_init.setMinimumSize(QtCore.QSize(300, 60))
        self.label_init.setFont(self.lbl_font)
        self.label_init.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.label_init)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # Настройка кнопки
        self.button_load.setMinimumSize(QtCore.QSize(250, 60))
        self.button_load.setMaximumSize(QtCore.QSize(250, 60))
        self.button_load.setFont(self.btn_font)
        self.horizontalLayout.addWidget(self.button_load)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Зона тестирования граифика
        # self.plot_widget = Plot(self.centralwidget, 'Время (с)', 'Размер (м)') # Создание виджета
        # self.verticalLayout.addWidget(self.plot_widget)                        # Добавление виджета
        #
        # self.plot_widget.test()       # Тест виджета
        # self.plot_widget.delete_all() # Очистка плоскости
        # self.plot_widget.add_chart('some_name', [1, 3, 4, 5, 6], [37, 33, 5, 1, 30]) # добавление графика

        # Финальная компоновка
        self.gridLayout.addLayout(self.verticalLayout, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStatusBar(self.status_bar)

        self.setTextUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setTextUi(self):
        # Выставление текста виджетам
        self.label_init.setText('Вас приветствует приложение анализа данных!\nПожалуйста, загрузите данные из файла')
        self.button_load.setText('Выбрать файл')


class Win(QMainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.ui = Ui_MainWindow(self)
        self.setWindowTitle('Analytics')
        self.init()

        self.ui.button_load.clicked.connect(self.show_dialog) # Бинд кнопки на вызов диалога

    def init(self):
        self.ui.button_load.setDefault(True)  # Установка фокуса на кнопку

    def show_dialog(self):
        print('Здесь должен быть вызов диалога')
        pass # Здесь нужно прописать загрузку данных через диалог


def main():
    # Инициализация окна и запуск приложения
    app = QApplication(argv)
    apply_stylesheet(app, theme='dark_teal.xml')  # Установка темы приложения
    win = Win()
    win.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
