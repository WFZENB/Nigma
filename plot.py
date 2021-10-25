from PyQt5.QtGui import QFont
from pyqtgraph import PlotWidget, mkPen
from PyQt5.QtCore import Qt
import random as rnd


# цвтетовая схема
COLORS = {'Jasper':          (223, 58,  71),
          'Blueberry':       (68,  138, 255),
          'Dollar Bill':     (139, 195, 74),
          'Yellow':          (255, 255, 0),
          'Java':            (29,  233, 182),
          'Purple Plum':     (171, 71,  188),
          'Sasquatch Socks': (255, 64,  129),
          'Safety Orange':   (255, 154, 0)
         }

# альтернативная цветовая схема
# COLORS = {'Rosso Corsa':   (225, 0,   0),
#           'Red':           (255, 0,   0),
#           'Amber':         (255, 193, 0),
#           'Yellow':        (255, 255, 0),
#           'Mantis':        (110, 209, 66),
#           'Pantone Green': (0,   178, 71),
#           'Process Cyan':  (0,   178, 243),
#           'French Blue':   (0,   113, 196),
#           'Gulf Blue':     (0,   26,  98),
#           'Grape':         (129, 44,  164)
#          }


class Plot(PlotWidget):
    def __init__(self, parent=None, x_axis='Ось Х', y_axis='Ось Y'):
        super().__init__(parent=parent)

        self.setBackground((75, 78, 80))       # Цвет фона
        self.showGrid(x=True, y=True)          # Отображение сетки

        self.colors_pool = list(COLORS.keys()) # Список доступных цветов
        self.plot_pool   = {}                  # Учет объектов на плоскости

        # Отображение легенды
        self.legend = self.addLegend()
        self.legend.setPen((55, 58, 60))
        self.legend.setBrush((45, 48, 50, 200))

        self.set_axis_name(x_axis, y_axis)

        # Шрифт делений на осях
        font = QFont()
        font.setPointSize(11)
        self.getAxis("bottom").setTickFont(font)
        self.getAxis("left").setTickFont(font)

    def set_axis_name(self, x_axis, y_axis):
        # Шрифт и названия осей
        labelStyle = {'color': '#969696', 'font-size': '13pt'}
        self.setLabel('left', y_axis, **labelStyle)
        self.setLabel('bottom', x_axis, **labelStyle)

    # Добавление бесконечной линии
    def add_line(self, name, x=None, y=None, dotted=False):
        self.check_name(name)

        # Выставление параметров
        format_name  = f'<font size="4">{name}</font>'
        color_name, color = self.rnd_color()
        style = Qt.DotLine if dotted else None
        pen   = mkPen(color, width=3, style=style)

        if x and (y is None):
            # Добавление и отрисовка линии параллельной оси Y
            line = self.addLine(x=x, pen=pen, name=format_name)
            fake_line = self.plot([0], pen=pen, name=format_name)
            self.add_plot_to_pool(name, (line, fake_line), color_name)

        if y and (x is None):
            # Добавление и отрисовка линии параллельной оси X
            line = self.addLine(y=y, pen=pen, name=format_name)
            fake_line = self.plot([0], pen=pen, name=format_name)
            self.add_plot_to_pool(name, (line, fake_line), color_name)

    # Добавление грфика
    def add_chart(self, name, x, y, dotted=False):
        self.check_name(name)

        # Выставление параметров
        format_name  = f'<font size="4">{name}</font>'
        color_name, color = self.rnd_color()
        style = Qt.DotLine if dotted else None
        pen   = mkPen(color, width=3, style=style)

        # Отрисовка графика
        chart = self.plot(x, y, pen=pen, name=format_name)
        self.add_plot_to_pool(name, chart, color_name)

    # Добавление гистограммы
    def add_histogram(self, name, x, y):
        self.check_name(name)

        # Добавление избыточной точки
        x.append(x[len(x)-1]+1)

        # Выставление параметров
        format_name  = f'<font size="4">{name}</font>'
        color_name, color = self.rnd_color()

        # Отрисовка гистограммы
        histogram = self.plot(x, y, stepMode=True, fillLevel=0, brush=color, name=format_name)
        self.add_plot_to_pool(name, histogram, color_name)

    # Проверка на уникальность имени объекта
    def check_name(self, name):
        if name in self.plot_pool.keys():
            raise Exception(f'Имя \'{name}\' уже используется!')

    # Получение случайного цвета из палитры
    def rnd_color(self):
        # Ограничение на добавление графика
        if len(self.plot_pool) == 8:
            raise Exception('Невозможно добавить объект (достигнут максимум 8/8)!')

        # Выбор цвета и исключение его из набора
        i = rnd.randint(0, len(self.colors_pool) - 1)
        color_name = self.colors_pool.pop(i)
        return color_name, COLORS.get(color_name)

    # Добавление объекта в учет
    def add_plot_to_pool(self, name, plot, color):
        self.plot_pool[name] = (plot, color)

    # Удаление объекта
    def delete_plot(self, name):
        if name in self.plot_pool.keys():
            info  = self.plot_pool.pop(name)
            plot  = info[0]
            self.colors_pool.append(info[1])
            if isinstance(plot, tuple):
                self.removeItem(plot[0])
                self.legend.removeItem(plot[1])
            else:
                plot.clear()
                self.legend.removeItem(plot)

    # Удаление всех объектов
    def delete_all(self):
        self.clear()
        self.colors_pool = list(COLORS.keys())  # Сброс доступных цветов
        self.plot_pool   = {}                   # Сброс учета объектов

    # Метод для тестирования класса
    def test(self):
        self.add_histogram('name', [1, 2, 3, 5, 6], [5, 25, 3, 66, 50])
        self.add_chart('another_name', [1, 3, 4, 5, 6], [37, 33, 5, 1, 30])
        self.add_chart('line angle', [0, 8], [0, 60])
        self.add_chart('line -angle', [0, 8], [60, 0])
        self.add_line('y_line', y=30, dotted=True) # Пунктирная линия
        self.add_line('y_new_line', y=20, dotted=True)
        self.add_line('x_line', x=8)
        # self.delete_plot('x_line') # Удаление
        self.add_line('x_new_line', x=3)
        # self.add_line('x_new_line', x=2) # Тест ошибки (если добавляется больше 8 объектов)