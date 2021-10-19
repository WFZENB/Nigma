from statistics import mode                             # Импортируем функцию мода


list_of_values = ("45", "4", "78", "-47", "-5", "-5")   # Пробный список


def mean(values):                                       # Среднее значение (все значения/на количество значений)
    value_sum = 0
    for i in range(len(values)):
        value_sum = value_sum + int(values[i])
    value_mean = (value_sum/len(values))
    return value_mean


def maximum(values):                                    # Нахождение максимума
    value_maximum = -10000000
    for i in range(len(values)):
        if int(values[i]) >= value_maximum:
            value_maximum = int(values[i])
    return value_maximum


def minimum(values):                                    # Нахождение минимума
    value_minimum = 10000000
    for i in range(len(values)):
        if int(values[i]) <= value_minimum:
            value_minimum = int(values[i])
    return value_minimum


def median(values):                                     # Нахождение медианы
    if len(values) % 2 == 0:
        value_median = len(values)/2
    else:
        value_median = ((len(values) / 2 - 1) + (len(values) / 2)) / 2
    return value_median


def search_mode(values):                                # Нахождение мода
    a = mode(values)
    return a


def search_range(values):                               # Нахождение размаха
    value_range = maximum(values) - minimum(values)
    return value_range


print(maximum(list_of_values), "~~",  minimum(list_of_values), "~~", mean(list_of_values))
print(median(list_of_values), "~~", search_mode(list_of_values), "~~", search_range(list_of_values))
print(search_mode(list_of_values))