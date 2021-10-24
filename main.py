from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from UI.view_manager import ViewManager
from sys import argv, exit
from plot import Plot # Импорт графика для тестового вывода


def main():
    # Инициализация окна и запуск приложения
    app = QApplication(argv)
    apply_stylesheet(app, theme='dark_teal.xml')  # Установка темы приложения
    vm = ViewManager() # Сохраняется в переменную чтобы экземпляр не удалился
    exit(app.exec_())


if __name__ == '__main__':
    main()
