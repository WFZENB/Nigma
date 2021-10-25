from PyQt5.QtWidgets import QMainWindow
from UI.load_view import LoadView
from UI.home_view import HomeView
from UI.action_view import ActionView
from UI.result_view import ResultView


class ViewManager(QMainWindow):
    def __init__(self):
        super(ViewManager, self).__init__()
        self.setWindowTitle('Analytics')
        self.move(350, 100)
        self.show_load()

    def show_load(self):
        load_view = LoadView(self)
        load_view.button_load.clicked.connect(self.show_dialog) # Бинд кнопки на вызов диалога
        load_view.button_load.setDefault(True)                  # Установка фокуса на кнопку
        self.show()

    def show_dialog(self):
        # TODO: диалог для выбора файла
        data_loaded = True

        if data_loaded:
            self.show_home() # Переход к станице выбор категории
        else:
            pass
            # TODO: диалог с ошибкой чтения файла

    def show_home(self):
        home_view = HomeView(self)
        home_view.button_load.clicked.connect(self.show_load) # Бинд кнопки на переход к странице загрузки

        # Бинд кнопок выбора категорий
        home_view.button_1.clicked.connect(lambda: self.specific_action(1))
        home_view.button_2.clicked.connect(lambda: self.specific_action(2))
        home_view.button_3.clicked.connect(lambda: self.specific_action(3))
        home_view.button_4.clicked.connect(lambda: self.specific_action(4))
        home_view.button_5.clicked.connect(lambda: self.specific_action(5))
        home_view.button_6.clicked.connect(lambda: self.specific_action(6))
        home_view.button_7.clicked.connect(lambda: self.specific_action(7))
        home_view.button_8.clicked.connect(lambda: self.specific_action(8))

        # Отключение неиспользуемых функций
        # TODO: удалять по мере необходимости
        home_view.button_2.setEnabled(False)
        home_view.button_3.setEnabled(False)
        home_view.button_4.setEnabled(False)
        home_view.button_5.setEnabled(False)
        home_view.button_6.setEnabled(False)
        home_view.button_7.setEnabled(False)
        home_view.button_8.setEnabled(False)

        self.show()

    def specific_action(self, action_num=0):
        # action_num - номер категории

        button_names = []     # Максимум 30 кнопок
        if action_num == 1:   # Описательная статистика
            button_names = ['Среденее значение', 'Стандартная ошибка', 'Доверительный интервал', 'Медиана', 'Минимум',
                            'Максимум', 'Размах']
        elif action_num == 2: # Проверка статистических гипотез
            button_names = []
        elif action_num == 3: # Дисперсионный анализ
            button_names = []
        elif action_num == 4: # Корреляционный анализ
            button_names = []
        elif action_num == 5: # Факторный анализ
            button_names = []
        elif action_num == 6: # Кластерный анализ
            button_names = []
        elif action_num == 7: # Методы теории множеств
            button_names = []
        elif action_num == 8: # Апроксимация зависимостей
            button_names = []

        action_view = ActionView(self, button_names)

        action_view.button_load.clicked.connect(self.show_load) # Бинд кнопки на переход к странице загрузки
        action_view.button_back.clicked.connect(self.show_home) # Бинд кнопки на переход к странице выбора категории

        # TODO: Бинд конкретных функциональных кнопок в соответствии с категорией
        if action_num == 1:
            action_view.button_01.clicked.connect(self.result)
        elif action_num == 2:
            pass
        elif action_num == 3:
            pass
        elif action_num == 4:
            pass
        elif action_num == 5:
            pass
        elif action_num == 6:
            pass
        elif action_num == 7:
            pass
        elif action_num == 8:
            pass

        self.show()

    def result(self):
        result_view = ResultView(self)

        # Зона тестирования вывода результата
        result_view.result_label.setText('Значение 1 = 12345.6789\nЗначение 2 = 12345.6789')

        # Зона тестирования граифика
        plot = result_view.plot
        plot.set_axis_name('Время', 'Величина')                           # Названия осей
        plot.test()                                                       # Тест виджета
        # plot.delete_all()                                                 # Очистка плоскости
        # plot.add_chart('some_name', [1, 3, 4, 5, 6], [37, 33, 5, 1, 30])  # Добавление графика

        self.show()