from PyQt5 import QtCore, QtGui, QtWidgets

class LoadView:
    def __init__(self, root):
        self.lbl_font = QtGui.QFont() # Шрифт надписей
        self.btn_font = QtGui.QFont() # Шрифт кнопок

        self.centralWidget      = QtWidgets.QWidget(root)                   # Главный виджет
        self.centralLayout      = QtWidgets.QVBoxLayout(self.centralWidget) # Главный компоновщик

        self.horizontalLayout   = QtWidgets.QHBoxLayout()                   # Горизонтальный компоновщик
        self.label_init         = QtWidgets.QLabel()                        # Надпись приветствия
        self.button_load        = QtWidgets.QPushButton()                   # Кнопка загрузки файла

        self.status_bar         = QtWidgets.QStatusBar(root)                # Статусбар

        self.setupUi(root)

    def setupUi(self, root):
        # Выставление размеров шрифтов
        self.lbl_font.setPointSize(16)
        self.btn_font.setPointSize(14)

        # Определение размера окна и центрирование
        self.centralWidget.setMinimumSize(QtCore.QSize(1200, 850))
        self.centralLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Настройка надписи
        self.label_init.setFont(self.lbl_font)
        self.label_init.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.centralLayout.addWidget(self.label_init)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Expanding)
        self.centralLayout.addItem(spacerItem)

        # Настройка кнопки
        self.button_load.setMaximumSize(QtCore.QSize(250, 60))
        self.button_load.setFont(self.btn_font)
        self.horizontalLayout.addWidget(self.button_load)

        # Финальная компоновка
        self.centralLayout.addLayout(self.horizontalLayout)
        root.setCentralWidget(self.centralWidget)
        root.setStatusBar(self.status_bar)

        self.setTextUi()

    def setTextUi(self):
        # Выставление текста виджетам
        self.label_init.setText('Вас приветствует приложение анализа данных!\nПожалуйста, загрузите данные из файла (поддерживаемые форматы: .xlsx)')
        self.button_load.setText('Выбрать файл')